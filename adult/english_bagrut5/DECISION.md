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

## Update 1.11.2026: placement routing as data (issue #19)
Every road 01 to 08 carries placement_route {from_placement: path_english_bagrut5_00_placement, band_min = band_max = road index}. This copies core: placement_band gives 1 (needs practice or 4+ mistakes), 3 (1 to 3 mistakes), 5 (none), and SERIES[band] is the road. route_by_band on these files gives 1 -> 01, 3 -> 03, 5 -> 05, same as SERIES.
Options: A (chosen) one band per road index, matches SERIES exactly, future bands need no content change. B ranges (01: 1 to 2, 03: 3 to 4, 05: 5 to 8): same result today, hides 02, 04, 06 to 08. C only 01, 03, 05: fewest fields, roads without a route look unroutable.
00 t_end text no longer maps topics to roads (that was screen text only and disagreed with the band rule); it says the app opens the right road.
Known limits: schema has no route_path_id or first tile field, so the app starts at the road's first step. Core placement_api still uses SERIES for this placement id, not placement_route; the data is ready when Dev switches.
