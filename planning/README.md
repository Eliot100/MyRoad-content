# Planning area (MyRoad-content)

**status: planning**

This folder holds **docs-only** learning-road outlines and research notes.
It is **not** publishable learner content.

## Safety (critical)

- The MyRoad platform content loader discovers learner paths by recursively
  collecting `*.json` under the content tree (`default_content_dir` +
  `_find_json_files` / `root.rglob("*.json")` in
  `packages/core/src/myroad_core/content/loader.py`).
- **Never put path JSON in this folder.** Only Markdown (and maybe `.txt`).
- Today the loader only loads `*.json`, so Markdown here is safe and will not
  appear as learner paths. Keep it that way.
- Every planning doc must state `status: planning` clearly at the top.
- Do not put secrets, credentials, or personal learner data here.

## How to use

1. Research with the `learning-content-research` skill steps (learner, sources,
   stages, tiles, finish criteria, level-up, metrics, schema gaps).
2. Keep outlines in Markdown under `planning/`.
3. Update `planning/INDEX.md` when adding or changing an idea.
4. When an outline is ready to become real content, create path JSON under the
   normal content trees (`adult/`, etc.) in a separate content PR — never by
   dropping JSON into `planning/`.
5. Hand schema gaps to the format owner; do not invent schema fields in JSON.

## Current ideas

See [INDEX.md](./INDEX.md).

Batch 2026-11-07 added: psychometric verbal (Hebrew), math 5-unit from zero
(adults; planning only — distinct from `path_math_zero_to_equation` /
`path_math_bagrut_3_units` and from content PR #45 JSON), and YAEL Hebrew from
zero (chosen over CS bagrut5 for stronger verified public sources).

Batch 2026-11-08 added: chemistry 5-unit from zero, biology 5-unit from zero,
and computer-science theoretical-path bagrut from zero (after MoE pages
returned HTTP 200; CS unit 5 vs unit 3 options are distinguished in the outline).

Batch 2026-11-09 added: civics bagrut from zero, history bagrut from zero,
and psychometric English / AMIRNET (English leaves the PET score from the
December 2026 sitting; see the review notes in the outline).

## Bot note

Docs-only planning. Bot: maria. No path JSON in this PR.
