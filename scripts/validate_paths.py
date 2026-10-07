"""Validate every path JSON in this repo against the schema on MyRoad main.

The schema is not copied here: CI installs `myroad-core` straight from
`Eliot100/MyRoad` main, so the platform's loader is the single source of truth.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from pydantic import ValidationError

from myroad_core.content.locale_rules import validate_locale_consistency
from myroad_core.content.schema import validate_content_path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    files = sorted(p for p in ROOT.rglob("*.json") if ".git" not in p.parts)
    if not files:
        print("No path JSON files found.")
        return 1

    errors: list[str] = []
    seen_ids: dict[str, Path] = {}
    for fp in files:
        rel = fp.relative_to(ROOT)
        try:
            data = json.loads(fp.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{rel}: invalid JSON: {exc}")
            continue
        try:
            path = validate_content_path(data)
        except (ValidationError, ValueError) as exc:
            errors.append(f"{rel}: schema error:\n{exc}")
            continue
        if path.id in seen_ids:
            errors.append(f"{rel}: duplicate path id {path.id!r} (also in {seen_ids[path.id]})")
        else:
            seen_ids[path.id] = rel
        for msg in validate_locale_consistency(path):
            errors.append(f"{rel}: locale: {msg}")

    for e in errors:
        print(f"::error::{e}" if "\n" not in e else e)
    print(f"Checked {len(files)} files, {len(errors)} problem(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
