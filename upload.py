import logging
import os

import internetarchive
from retry import retry


def main():
    """Upload the provided files to archive.org with optional metadata."""
    # Get env variables
    access_key = os.getenv("access-key")
    secret_key = os.getenv("secret-key")
    identifier = os.getenv("identifier")
    files = os.getenv("files")

    # Metadata fields (add more as needed)
    metadata_fields = [
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
    # Cache environment variables
    env_vars = {field: os.getenv(field) for field in metadata_fields}

    metadata = {}
    for field, value in env_vars.items():
        if value:
            # For list fields (subject, creator, contributor, coverage, openlibrary_author, openlibrary_subject, related-external-id, isbn, issn, lccn, oclc-id, language), split on comma
            if field in [
                "subject",
                "creator",
                "contributor",
                "coverage",
                "openlibrary_author",
                "openlibrary_subject",
                "related-external-id",
                "isbn",
                "issn",
                "lccn",
                "oclc-id",
                "language",
            ]:
                metadata[field] = [v.strip() for v in value.split(",") if v.strip()]
            else:
                metadata[field] = value

    # Set the logger
    logging.basicConfig(level="DEBUG", format="%(asctime)s - %(name)s - %(message)s")
    logger = logging.getLogger(__name__)

    logger.debug(f"Uploading {files} with metadata: {metadata}")
    kwargs = dict(
        access_key=access_key,
        secret_key=secret_key,
        verbose=True,
        files=files,
        metadata=metadata if metadata else None,
    )
    # Remove None metadata to avoid passing empty dict
    if not metadata:
        kwargs.pop("metadata")
    try:
        _upload(identifier, **kwargs)
    except Exception as e:
        logger.error(f"Upload failed after retries: {e}")
        raise


@retry(tries=10, delay=30, backoff=2)
def _upload(identifier: str, **kwargs):
    try:
        internetarchive.upload(identifier, **kwargs)
    except Exception as e:
        logging.error(f"Error during upload: {e}")
        raise


if __name__ == "__main__":
    main()
