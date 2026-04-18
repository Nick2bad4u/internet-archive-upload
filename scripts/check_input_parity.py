"""Verify action.yml inputs stay in sync with upload.py constants."""

from __future__ import annotations

import ast
import json
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
ACTION_PATH = REPO_ROOT / "action.yml"
UPLOAD_PATH = REPO_ROOT / "upload.py"
ACTION_ONLY_INPUTS = {"log-level"}


def _extract_list_constant(module: ast.Module, name: str) -> list[str]:
    for node in module.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    if isinstance(node.value, (ast.List, ast.Tuple)):
                        values: list[str] = []
                        for elt in node.value.elts:
                            if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                                values.append(elt.value)
                            else:
                                raise ValueError(f"{name} contains non-string element")
                        return values
    raise ValueError(f"Could not find constant: {name}")


def main() -> int:
    action = yaml.safe_load(ACTION_PATH.read_text(encoding="utf-8"))
    action_inputs = set((action.get("inputs") or {}).keys())

    module = ast.parse(UPLOAD_PATH.read_text(encoding="utf-8"))
    required_inputs = _extract_list_constant(module, "REQUIRED_INPUTS")
    metadata_fields = _extract_list_constant(module, "METADATA_FIELDS")

    handled_inputs = set(required_inputs + metadata_fields)

    missing_in_upload = sorted((action_inputs - handled_inputs) - ACTION_ONLY_INPUTS)
    action_only_present = sorted(action_inputs & ACTION_ONLY_INPUTS)
    extra_in_upload = sorted(handled_inputs - action_inputs)

    required_expected = {"access-key", "secret-key", "identifier", "files"}
    required_mismatch = set(required_inputs) ^ required_expected

    report = {
        "action_input_count": len(action_inputs),
        "handled_input_count": len(handled_inputs),
        "missing_in_upload": missing_in_upload,
        "extra_in_upload": extra_in_upload,
        "action_only_inputs": action_only_present,
        "required_inputs": required_inputs,
    }
    print(json.dumps(report, indent=2, sort_keys=True))

    if missing_in_upload or extra_in_upload:
        print("\n❌ Input parity check failed.")
        return 1

    if required_mismatch:
        print(
            "\n❌ Required inputs changed unexpectedly. "
            f"Expected {sorted(required_expected)}, got {required_inputs}"
        )
        return 1

    print("\n✅ Input parity check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
