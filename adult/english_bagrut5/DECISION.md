# DECISION: weakest English road after the placement audit

Context: audit of roads 00..08 against the placement test (00). Rule from the design: the first road with two mistakes in its topic in 00 is the gap.

| Option | What | Effect |
|---|---|---|
| A | Add a t_accuracy probe to 00, rewrite 04 | 04 becomes reachable, duplicates gone |
| B | Deepen 01 only | 01 richer, 04 stays unreachable |
| C | Only rewrite the 00 result text | Honest text, 04 still never a gap |

Decision: A. 04 had no placement probe (never a gap), the "saw yesterday" item appeared 4 times, COND repeated the word order item, 2 items per topic, and no check passage.

Changes:
- 00: new topic t_accuracy (2 items) routes to 04; result text lists every topic to road mapping (letters and am is are to 01); blurb no longer says four areas; English text no longer says band or station.
- 04: 3 items per content topic, zero article, adjective order, if + present, since, an hour; new review items; final check on the library passage.
- All roads: practice title תרגול, סיום דרך, topic בדיקה, 01 blurb; no hyphen in Hebrew text; 01 c_t item no longer allows cot or cut.

Verified: validate_paths.py 0 problems; MyRoad core pytest green with CONTENT_DIR; routing check 8 of 8 topics map to existing roads; dash and glossary scans 0.

Known limits: routing lives only in screen text; the two mistakes threshold is still open in glossary 09; 00 still has 1 to 4 items per topic.

How to switch: edit scripts/build_english_bagrut5.py (placement() or the 04 teach block) and run it; JSON is generated.

Schema gaps: no field mapping a placement topic to a road id; no mistake threshold field; no free text answer for essays.
