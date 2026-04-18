"""Upload files to archive.org with optional metadata."""

from __future__ import annotations

import json
import logging
import os
import time
from glob import glob
from pathlib import Path

import internetarchive

REQUIRED_INPUTS = ["access-key", "secret-key", "identifier", "files"]
SUPPORTED_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
BOOLEAN_TRUE_VALUES = {"1", "true", "yes", "on"}
BOOLEAN_FALSE_VALUES = {"0", "false", "no", "off"}
BOOLEAN_METADATA_FIELDS = {"adaptive_ocr", "betterpdf"}
INTEGER_METADATA_FIELDS = {"fixed-ppi", "ppi", "year"}
FLOAT_METADATA_FIELDS = {"size"}
ENUM_METADATA_ALLOWED_VALUES = {
    "closed_captioning": {"yes", "no"},
    "color": {"color", "black and white"},
    "page-progression": {"lr", "rl"},
    "sound": {"sound", "silent"},
}

METADATA_FIELDS = [
    "adaptive_ocr",
    "aspect_ratio",
    "betterpdf",
    "bookreader-defaults",
    "bwocr",
    "call_number",
    "ccnum",
    "closed_captioning",
    "color",
    "condition",
    "condition-visual",
    "contributor",
    "coverage",
    "creator",
    "creator-alt-script",
    "date",
    "description",
    "external-identifier",
    "fixed-ppi",
    "isbn",
    "issn",
    "lccn",
    "language",
    "licenseurl",
    "notes",
    "oclc-id",
    "openlibrary",
    "openlibrary_author",
    "openlibrary_edition",
    "openlibrary_subject",
    "openlibrary_work",
    "page-progression",
    "possible-copyright-status",
    "ppi",
    "publisher",
    "related-external-id",
    "rights",
    "scandate",
    "scanner",
    "size",
    "sound",
    "source",
    "sponsor",
    "subject",
    "title",
    "title-alt-script",
    "volume",
    "year",
]

CSV_METADATA_FIELDS = {
    "subject",
    "creator",
    "contributor",
    "coverage",
    "external-identifier",
    "openlibrary_author",
    "openlibrary_subject",
    "related-external-id",
    "isbn",
    "issn",
    "lccn",
    "oclc-id",
    "language",
}


def _configure_logging() -> logging.Logger:
    level = os.getenv("IA_LOG_LEVEL", "INFO").upper()
    logging.basicConfig(
        level=getattr(logging, level, logging.INFO),
        format="%(asctime)s %(levelname)s %(message)s",
    )
    return logging.getLogger("internet-archive-upload")


def _validate_log_level() -> None:
    raw_level = _normalize_string(os.getenv("IA_LOG_LEVEL", "INFO"))
    if not raw_level:
        return

    normalized_level = raw_level.upper()
    if normalized_level not in SUPPORTED_LOG_LEVELS:
        supported = ", ".join(sorted(SUPPORTED_LOG_LEVELS))
        raise ValueError(f"Invalid log level '{raw_level}'. Supported values: {supported}")


def _normalize_enum_metadata(field: str, value: str) -> str:
    allowed_values = ENUM_METADATA_ALLOWED_VALUES[field]
    normalized = value.strip().lower()
    if normalized not in allowed_values:
        supported = ", ".join(sorted(allowed_values))
        raise ValueError(f"Invalid value for '{field}': '{value}'. Supported values: {supported}")
    return normalized


def _normalize_boolean_metadata(field: str, value: str) -> str:
    normalized = value.strip().lower()
    if normalized in BOOLEAN_TRUE_VALUES:
        return "true"
    if normalized in BOOLEAN_FALSE_VALUES:
        return "false"
    raise ValueError(
        f"Invalid value for '{field}': '{value}'. "
        "Supported boolean values: true/false, yes/no, 1/0, on/off"
    )


def _normalize_integer_metadata(field: str, value: str) -> str:
    try:
        integer_value = int(value.strip())
    except ValueError as exc:
        raise ValueError(f"Invalid integer for '{field}': '{value}'") from exc
    return str(integer_value)


def _normalize_float_metadata(field: str, value: str) -> str:
    try:
        float_value = float(value.strip())
    except ValueError as exc:
        raise ValueError(f"Invalid float for '{field}': '{value}'") from exc
    return str(float_value)


def _normalize_string(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _parse_inputs() -> dict[str, str]:
    """Parse inputs from IA_INPUTS_JSON, with fallback to legacy env var names."""
    raw_json = os.getenv("IA_INPUTS_JSON", "").strip()
    if raw_json:
        try:
            payload = json.loads(raw_json)
        except json.JSONDecodeError as exc:
            raise ValueError("IA_INPUTS_JSON is not valid JSON") from exc

        if not isinstance(payload, dict):
            raise ValueError("IA_INPUTS_JSON must decode to an object")

        return {str(k): _normalize_string(v) for k, v in payload.items()}

    # Backward compatibility (legacy env strategy)
    return {
        "access-key": _normalize_string(os.getenv("access-key") or os.getenv("IA_ACCESS_KEY")),
        "secret-key": _normalize_string(os.getenv("secret-key") or os.getenv("IA_SECRET_KEY")),
        "identifier": _normalize_string(os.getenv("identifier") or os.getenv("IA_IDENTIFIER")),
        "files": _normalize_string(os.getenv("files") or os.getenv("IA_FILES")),
        **{field: _normalize_string(os.getenv(field)) for field in METADATA_FIELDS},
    }


def _validate_required_inputs(inputs: dict[str, str]) -> None:
    missing = [key for key in REQUIRED_INPUTS if not inputs.get(key)]
    if missing:
        raise ValueError(f"Missing required inputs: {', '.join(missing)}")


def _normalize_files(files_input: str) -> str | list[str]:
    """Support comma-separated file list while preserving single path/glob strings."""
    candidates = [p.strip() for p in files_input.split(",") if p.strip()]
    if not candidates:
        raise ValueError("Input 'files' is empty after trimming")
    if len(candidates) == 1:
        return candidates[0]
    return candidates


def _build_metadata(inputs: dict[str, str]) -> dict[str, object]:
    metadata: dict[str, object] = {}
    for field in METADATA_FIELDS:
        value = _normalize_string(inputs.get(field))
        if not value:
            continue
        if field in BOOLEAN_METADATA_FIELDS:
            value = _normalize_boolean_metadata(field, value)
        if field in INTEGER_METADATA_FIELDS:
            value = _normalize_integer_metadata(field, value)
        if field in FLOAT_METADATA_FIELDS:
            value = _normalize_float_metadata(field, value)
        if field in ENUM_METADATA_ALLOWED_VALUES:
            value = _normalize_enum_metadata(field, value)
        if field in CSV_METADATA_FIELDS:
            metadata[field] = [v.strip() for v in value.split(",") if v.strip()]
        else:
            metadata[field] = value
    return metadata


def _validate_file_targets(files: str | list[str]) -> None:
    targets = [files] if isinstance(files, str) else files
    for target in targets:
        if any(char in target for char in "*?[]"):
            if not glob(target):
                raise ValueError(f"File pattern matched no files: {target}")
            continue

        if not Path(target).exists():
            raise ValueError(f"File or directory does not exist: {target}")


def _upload_with_retry(
    identifier: str,
    *,
    access_key: str,
    secret_key: str,
    files: str | list[str],
    metadata: dict[str, object],
    logger: logging.Logger,
    max_attempts: int = 5,
    initial_delay_seconds: int = 5,
) -> None:
    kwargs: dict[str, object] = {
        "access_key": access_key,
        "secret_key": secret_key,
        "verbose": True,
        "files": files,
    }
    if metadata:
        kwargs["metadata"] = metadata

    delay = max(initial_delay_seconds, 1)
    for attempt in range(1, max_attempts + 1):
        try:
            internetarchive.upload(identifier, **kwargs)
            logger.info("Upload completed successfully")
            return
        except Exception:
            if attempt >= max_attempts:
                logger.exception("Upload failed after %d attempts", max_attempts)
                raise

            logger.warning(
                "Upload attempt %d/%d failed; retrying in %d seconds",
                attempt,
                max_attempts,
                delay,
            )
            time.sleep(delay)
            delay = min(delay * 2, 120)


def main() -> int:
    _validate_log_level()
    logger = _configure_logging()
    inputs = _parse_inputs()
    _validate_required_inputs(inputs)

    identifier = inputs["identifier"]
    files = _normalize_files(inputs["files"])
    _validate_file_targets(files)
    metadata = _build_metadata(inputs)

    logger.info(
        "Starting archive.org upload to identifier '%s' with %d metadata field(s)",
        identifier,
        len(metadata),
    )

    _upload_with_retry(
        identifier,
        access_key=inputs["access-key"],
        secret_key=inputs["secret-key"],
        files=files,
        metadata=metadata,
        logger=logger,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
