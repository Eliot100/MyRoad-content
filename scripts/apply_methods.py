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
MARK = "\nהסבר: "  # old layout: method appended to body_he
PREFIX = "הסבר: "
HYPHEN = re.compile(r"(?<=[\u0590-\u05FF])[-\u05BE](?=\S)")  # also maqaf
LONG_DASH = re.compile(r"\s*[\u2014\u2013]\s*")  # long dashes become a comma


def load(name: str, folder: str = "methods", attr: str = "M") -> dict | None:
    fp = ROOT / "scripts" / folder / f"{name}.py"
    if not fp.is_file():
        return None
    spec = importlib.util.spec_from_file_location(f"{folder}_{name}", fp)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, attr)


def apply_doc(d: dict, name: str | None = None) -> list[str]:
    """Apply scripts/methods/<name>.py (and scripts/hints/<name>.py when present) to one path doc
    in place. Returns base step ids with no row (or with a wrong choice that has no feedback).
    A variant step (variant_of) uses its own row, or else the row of its base.

    worked_method: the method, shown by the app under its own "how to solve" label (no prefix).
    body_he: the question only. feedback_try: the worked answer.
    hint: a nudge before answering. choices[].feedback: why that wrong choice is wrong."""
    name = name or d["id"].removeprefix("path_")
    table = load(name)
    hints = load(name, "hints", "H") or {}
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
        base = n.get("variant_of") or ""
        row = table.get(nid) or table.get(base)
        if not row:
            if not base:
                missing.append(nid)
            continue
        method, why = row
        n["body_he"] = n["body_he"].split(MARK)[0]
        n["worked_method"] = method.removeprefix(PREFIX)
        n["feedback_try"] = why
        if hints:
            h = hints.get(nid) or hints.get(base)
            if not h:
                missing.append(f"{nid} (hint)")
                continue
            n["hint"], per_choice = h
            ok = n.get("correct")
            ok = set(ok) if isinstance(ok, list) else {ok}
            for c in n.get("choices") or []:
                if c["id"] in ok:
                    c.pop("feedback", None)
                elif c["id"] in per_choice:
                    c["feedback"] = per_choice[c["id"]]
                else:
                    missing.append(f"{nid}.{c['id']} (feedback)")
    return missing


def main() -> int:
    bad = 0
    for arg in sys.argv[1:]:
        fp = ROOT / arg
        d = json.loads(fp.read_text(encoding="utf-8"))
        for n in d["nodes"]:
            n.pop("media_hint", None)  # not shown by the app
        missing = apply_doc(d, fp.stem.removeprefix("path_")) if load(fp.stem.removeprefix("path_")) else []
        fp.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(arg, "missing:", missing)
        bad += bool(missing)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
