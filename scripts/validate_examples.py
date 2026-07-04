from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    (
        "Cognitive Cycle Record",
        ROOT / "schemas" / "cognitive-cycle-record.schema.json",
        ROOT / "examples" / "cognitive-cycle-record.example.yaml",
    ),
    (
        "Cognitive Organ Interface",
        ROOT / "schemas" / "cognitive-organ-interface.schema.json",
        ROOT
        / "examples"
        / "cognitive-organ-interface.structural-core.example.yaml",
    ),
    (
        "Cognitive Routing Plan",
        ROOT / "schemas" / "cognitive-routing-plan.schema.json",
        ROOT
        / "examples"
        / "cognitive-routing-plan.deep-structure.example.yaml",
    ),
    (
        "Cognitive Feedback Record",
        ROOT / "schemas" / "cognitive-feedback-record.schema.json",
        ROOT
        / "examples"
        / "cognitive-feedback-record.example.yaml",
    ),
    (
        "Cognitive Continuity Trace",
        ROOT / "schemas" / "cognitive-continuity-trace.schema.json",
        ROOT
        / "examples"
        / "cognitive-continuity-trace.example.yaml",
    ),
]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError(
            f"{path} must contain a JSON object at the root."
        )

    return data


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError(
            f"{path} must contain a YAML mapping at the root."
        )

    return data


def validate_target(
    title: str,
    schema_path: Path,
    example_path: Path,
) -> bool:
    print(f"[validate] {title}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

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
            location = ".".join(
                str(part) for part in error.absolute_path
            )
            location = location or "<root>"

            print(
                f"Error: {location}: {error.message}"
            )

        return False

    print(f"[ok] {example_path.name} is valid")
    return True


def main() -> int:
    all_valid = True

    for title, schema_path, example_path in VALIDATION_TARGETS:
        try:
            valid = validate_target(
                title,
                schema_path,
                example_path,
            )
        except Exception as exc:
            print(f"Error: validation failed: {exc}")
            valid = False

        all_valid = all_valid and valid

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())
