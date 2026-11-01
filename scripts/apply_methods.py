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
HYPHEN = re.compile(r"(?<=[\u0590-\u05FF])-(?=\S)")  # "מ-150" -> "מ 150" (no dashes rule)


def load(name: str) -> dict:
    fp = ROOT / "scripts" / "methods" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, fp)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.M


def main() -> int:
    for arg in sys.argv[1:]:
        fp = ROOT / arg
        table = load(fp.stem.removeprefix("path_"))
        d = json.loads(fp.read_text(encoding="utf-8"))
        missing = []
        for n in d["nodes"]:
            for k in ("body_he", "feedback_ok", "feedback_try", "title"):
                if n.get(k):
                    n[k] = HYPHEN.sub(" ", n[k])
            if n["type"] not in ("practice", "check"):
                continue
            row = table.get(n["id"])
            if not row:
                missing.append(n["id"])
                continue
            method, why = row
            q = n["body_he"].split(MARK)[0]
            n["body_he"] = q + "\n" + method
            n["feedback_try"] = why
        fp.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(arg, "missing:", missing)
    return 0


if __name__ == "__main__":
    sys.exit(main())
