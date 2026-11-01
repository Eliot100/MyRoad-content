#!/usr/bin/env python3
"""Add a short method (in body_he, after the question) and a specific wrong answer explanation
(feedback_try) to practice and check steps, from scripts/methods/<file>.py. Idempotent.

Usage: python scripts/apply_methods.py adult/path_math_zero_to_equation.json
"""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARK = "\nהסבר: "
HYPHEN = re.compile(r"(?<=[\u0590-\u05FF])[-\u05BE](?=\S)")  # also maqaf
LONG_DASH = re.compile(r"\s*[\u2014\u2013]\s*")  # long dashes become a comma


def load(name: str) -> dict:
    fp = ROOT / "scripts" / "methods" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, fp)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.M


def apply_doc(d: dict, name: str | None = None) -> list[str]:
    """Apply scripts/methods/<name>.py to one path doc in place. Returns base step ids with no row.
    A variant step (variant_of) uses its own row, or else the row of its base."""
    table = load(name or d["id"].removeprefix("path_"))
    missing = []
    step = 0
    for n in d["nodes"]:
        if n["type"] not in ("practice", "check"):
            continue
        for k in ("body_he", "feedback_ok", "feedback_try", "title"):
            if n.get(k):
                n[k] = LONG_DASH.sub(", ", HYPHEN.sub(" ", n[k]))
        step += 1
        nid = n.get("id") or f"#{step}"  # some grade3 nodes have no id: key "#n" = n-th practice/check step
        row = table.get(nid) or table.get(n.get("variant_of") or "")
        if not row:
            if not n.get("variant_of"):
                missing.append(nid)
            continue
        method, why = row
        q = n["body_he"].split(MARK)[0]
        n["body_he"] = q + "\n" + method
        n["feedback_try"] = why
    return missing


def main() -> int:
    for arg in sys.argv[1:]:
        fp = ROOT / arg
        d = json.loads(fp.read_text(encoding="utf-8"))
        missing = apply_doc(d, fp.stem.removeprefix("path_"))
        fp.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(arg, "missing:", missing)
    return 0


if __name__ == "__main__":
    sys.exit(main())
