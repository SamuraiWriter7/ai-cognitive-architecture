from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]

SCHEMA_PATH = ROOT / "schemas" / "cognitive-cycle-record.schema.json"
EXAMPLE_PATH = ROOT / "examples" / "cognitive-cycle-record.example.yaml"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping at the root.")

    return data


def main() -> int:
    print("[validate] Cognitive Cycle Record")
    print(f"  schema : {SCHEMA_PATH.relative_to(ROOT)}")
    print(f"  example: {EXAMPLE_PATH.relative_to(ROOT)}")

    schema = load_json(SCHEMA_PATH)
    example = load_yaml(EXAMPLE_PATH)

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    )

    errors = sorted(
        validator.iter_errors(example),
        key=lambda error: list(error.absolute_path),
    )

    if errors:
        for error in errors:
            location = ".".join(str(part) for part in error.absolute_path)
            location = location or "<root>"
            print(f"Error: {location}: {error.message}")

        return 1

    print(f"[ok] {EXAMPLE_PATH.name} is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
