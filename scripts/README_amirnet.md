# AMIRNET full practice road

Source for `adult/path_english_amirnet_01.json`.

This is a full practice road, not a 60-minute starter. Eliot asked for a longer road
because people need much more than an hour to learn and master the material.

## Size

- 15 topics: 14 study or review stages plus a closing celebrate topic
- Original scored multiple-choice items only (4 choices), plus teaching and celebrate steps
- `estimated_minutes` is 1200, the schema maximum (20 hours)
- Realistic study time is longer, on the order of 45 to 50 hours, including rereading,
  reviewing misses, and repeating mixed practice. That longer estimate cannot be stored
  in `estimated_minutes` because the schema caps the field at 1200.

## Stage list

1. `t_about` — What AMIRNET is (confirmed: 50–150 scale, about 50 minutes; unverified: item counts, per-section timing, institutional cutoffs)
2. `t_vocab` — Academic vocabulary in context
3. `t_sc_basic` — Sentence completion: connectors and clause type
4. `t_sc_mid` — Sentence completion: contrast, condition, result
5. `t_sc_adv` — Sentence completion: academic phrasing and tense
6. `t_rest_basic` — Restatement: same claim, simple paraphrases
7. `t_rest_complex` — Restatement: connectors and structure
8. `t_rest_nuance` — Restatement: quantity, negation, tone
9. `t_read_main` — Reading: main idea and details
10. `t_read_infer` — Reading: vocabulary in context and inference
11. `t_read_struct` — Reading: structure and purpose
12. `t_mix_sc_rest` — Mixed review of sentence completion and restatement
13. `t_mix_rc` — Mixed review of reading (several questions on a passage)
14. `t_sim` — Mixed exam-style simulation
15. `t_end` — Celebrate

There is no placement test in this road (that comes later) and no prerequisite path.

## Facts

Confirmed, from the content fact-check: official scale 50–150; official duration about
50 minutes; retake and validity rules as recorded there.

Unverified here, and marked in the teaching text: exact item counts, official per-section
timing, and any institutional exemption cutoff (for example a 134-style threshold).

Do not treat this road as a score predictor.

## Rebuild

```bash
python3 scripts/build_amirnet.py
```

Writes `adult/path_english_amirnet_01.json`.
