# DECISION: Arabic 5 units, batch 1 (31.10.2026, MyRoad Content)

## Context
Issue #15. Design: Option C (Arabic script from day one, MSA backbone, spoken thread in every stage). Batch 1 = road 00 (placement, with a from zero exit) and road 01 stages 0 to 2. Schema on MyRoad main has no variant_of, exam_required, audio_url, or arabic SubjectId (checked 31.10.2026).

## Options for variants
| Option | Pros | Cons | Score | Cost to switch |
|---|---|---|---|---|
| A (chosen) sibling nodes, id suffix __a1w0 / __a0w0 / __a1w1 / __a0w1, title tag | valid today, one script, mechanical move to variant_of | learner sees each tile up to 4 times in a row until the player picks one variant | 8 | low: add variant_of in the script |
| B only base tiles, variants later | short roads | breaks #161 rule | 4 | medium |
| C separate path per variant | clean per path | 4x files, routing unclear | 5 | high |

## Decision
A. Valid against main now, every tile has its variants, and base id = id before "__" maps to variant_of when the field merges.

Variant rules: audio = speak_text (TTS); no audio = no speak_text, Hebrew transliteration in body_he; writing = write by hand on paper, then choose; no writing = choose only. speak tiles have audio and no audio only. Celebrate has one version. No exam only tiles in this batch.

## Other choices
- subject general, content_locale ar (no arabic subject yet).
- 01 has no prerequisite so a learner who answers "from zero" in 00 opens it directly.
- English title of 01 avoids the word "zero" (core test test_route_existing_step_offers_adult_math_paths matches on it).
- Spoken Arabic uses Levantine forms (شو، كيفك، منيح) as in the ministry question bank (see sources.md).

## Verified
- python scripts/validate_paths.py: 23 files, 0 problems.
- MyRoad core pytest with CONTENT_DIR: 547 passed.
- Dash scan next to Hebrew, glossary scan, empty body_content scan: 0.

## Known limits
Routing from 00 to roads lives in screen text only (no route_path_id). Writing variant is self checked. Roads 02 to 09 not built.

## How to switch
Edit scripts/build_arabic_bagrut5.py (VARIANTS, tile()) and rerun; JSON is generated.
