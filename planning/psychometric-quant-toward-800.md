# Psychometric quantitative toward ~800 — road outline

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.

## 1. Learner, start, target

| Field | Definition |
|-------|------------|
| Learner | Adult preparing for the Israeli Psychometric Entrance Test (PET / פסיכומטרי), focusing on **Quantitative Reasoning** |
| Start | Can do middle-school arithmetic; shaky on word problems, percentages, and geometry under time |
| Target | Strong quantitative domain performance that **supports** a general PET score near the top of the published scale (**200–800**). This road alone cannot “guarantee 800” — verbal (and, on older formats, English) also weigh in. Goal framing: **quant toward 800-capable profile** |
| Content originality | Sample items below are **original**. Do not copy NITE practice-test items into content. |

Hebrew labels: חשיבה כמותית · בעיות ושאלות · הבנת גרף/טבלה · פסיכומטרי.

## 2. Verified public sources (NITE)

Checked with `curl` (HTTP 200) on 2026-11-06 (Asia/Jerusalem):

| Source | URL | What we take from it |
|--------|-----|----------------------|
| NITE — Two-domain PET format (EN) | https://www.nite.org.il/two-domain-psychometric-entrance-test/format/?lang=en | From **December 2026 onwards**, paper-and-pencil PET has **six sections** in **Verbal** or **Quantitative** domains; first section is Verbal **writing task** (30 min Hebrew / 35 min other languages); remaining five MC sections typically **20 minutes** each (may differ by version); of five MC sections, **two per domain** are scored (one MC section is unscored for equating/quality); Quantitative tests number/math concepts and data in tables/graphs; knowledge comparable to **bagrut math minimum (3 units)** / roughly 9th–10th grade; formulas largely provided; **not** aimed at trig or calculus; question types: **Questions and Problems**, **Graph or Table Comprehension** |
| NITE — Score calculation (EN) | https://www.nite.org.il/two-domain-psychometric-entrance-test/scores/calculation/?lang=en | Domain scores on **50–150** scale; **general** scores on **200–800**; two-domain general score weights verbal and quantitative **equally**; quantitative-oriented general score gives quantitative **triple** the weight of verbal; verbal-oriented gives verbal triple quantitative |
| NITE quantitative examples PDF | https://www.nite.org.il/files/psych/new_psych/quantitive-eng.pdf | Confirms quant domain description and example structure (PDF reachable) |

**Topic list (from NITE format page, Quantitative Reasoning):** percentages; exponents and roots; properties of numbers; inequalities; factors; arithmetic with integers and fractions; equations; abbreviated multiplication formulas; coordinate systems; combinatorics; probability; averages; distance and work problems; plane figures (lines, triangles, quadrilaterals, polygons, circles); solids (boxes, cylinders, cones, prisms, pyramids).

**Explicitly out of scope per NITE:** trigonometry; differential/integral calculus; speed-of-calculation as the primary difficulty.

### Important format note (do not blur)

- **Two-domain PET (Dec 2026 onwards):** Verbal + Quantitative; general score 200–800 with the weightings above.
- **Older three-area materials** (Verbal, Quantitative, English) still exist on the web and in PDFs. Planning for new adult learners should **default to the two-domain structure** and treat English-as-third-area as legacy unless the learner sits an administration that still uses it.
- **Unverified here:** exact question counts per MC section for every language/version (NITE says counts/times may differ and will be published before administrations). Do not invent a fixed “20 questions” as a hard fact for all versions without a specific NITE citation for that version.

**About “800”:** 800 is the **top of NITE’s published general score scale**. This doc does **not** claim a percentile, admission cutoff, or required raw correct-count for 800 — those figures were **not** verified in this pass. Label any future cutoff claims with a dated NITE/university source or mark **unverified**.

## 3. Stages (שלבים)

3 levels per stage (L1 foundational timed accuracy → L2 mixed / multi-step → L3 full section pace with hard items). Hours are **estimates only**.

| Stage | Focus | Goal | Est. hours (estimate) |
|-------|-------|------|------------------------|
| 0 | Placement + calculator-free habits | Diagnose gaps; teach “formulas on sheet” mindset | 2–4 |
| 1 | Number properties & arithmetic fluency | Integers, fractions, factors, exponents/roots | 8–14 |
| 2 | Percent, ratio, proportion | Classic psych word-problem cores | 8–14 |
| 3 | Equations & inequalities | Translate text → equation; solve cleanly | 8–14 |
| 4 | Averages, work, distance | Rate problems without calc dependence | 8–14 |
| 5 | Plane geometry | Angles, triangles, polygons, circles | 10–16 |
| 6 | Solids & coordinate geometry | Boxes/cylinders/etc.; coordinate plane | 8–14 |
| 7 | Combinatorics & probability | Counting + basic probability literacy | 8–14 |
| 8 | Graphs & tables | Extract, compare, infer | 8–12 |
| 9 | Mixed timed sections | Full quant-section simulations | 12–20 |
| 10 | Score-profile coaching | How quant interacts with general 200–800 scales; pacing; review of error taxonomies | 3–6 |

**Road finish criteria:** Stage 9 end-checks meet threshold (see §5) on both Problems-heavy and Graph/Table-heavy mixes; Stage 10 checklist completed. Target language: “quant ready to support a top-scale general score,” not “you will score 800.”

## 4. Topics / tiles

Kinds: `learn` (understanding), `practice` (review), `check`, later worked-method / game modes.

### Stage 0
- What NITE quant measures (reasoning > arithmetic speed)
- Using the formula page; when not to over-compute
- Pacing: skip/mark vs grind
- Sample: “Which skill is primary on PET quant per NITE: rapid long division, or choosing a correct quantitative model?”

### Stage 1 — Numbers
- Divisibility, primes, GCD/LCM intuition
- Negative numbers; absolute value
- Exponents/roots identities used in psych items
- Sample: “If \(n\) is even, is \(n^2\) always divisible by 4? Explain with an example.”

### Stage 2 — Percent & ratio
- Percent change; successive percents
- Part–whole; mixtures (basic)
- Sample: “A price rises 20% then falls 20%. Is the final price equal to the start? Show with 100.”

### Stage 3 — Equations
- Linear equations; systems light
- Inequalities on a number line
- Abbreviated multiplication patterns as shortcuts
- Sample: “Solve for \(x\): \(3(x-2)=2x+5\).”

### Stage 4 — Rates
- Distance = rate × time variants
- Work problems (combined rates)
- Average pitfalls (average of averages)
- Sample: “A and B paint a fence in 6 h together; A alone would take 10 h. How long would B alone take?”

### Stage 5 — Plane geometry
- Angle chasing; triangle inequality qualitative
- Area/perimeter; similar triangles
- Circle: circumference/area; inscribed angle ideas as needed for psych (keep within NITE topic list)
- Sample: “A rectangle’s length doubles and width halves. What happens to area?”

### Stage 6 — Solids & coordinates
- Volume/surface of listed solids (formulas on sheet)
- Midpoint, slope, distance on plane
- Sample: “A cylinder and a box have the same height and the same base area. How do volumes compare?”

### Stage 7 — Counting & probability
- Basic counting (with/without order) — keep elementary
- Probability of simple events; independence intuition
- Sample: “A bag has 3 red and 2 blue. Probability of red then blue without replacement?”

### Stage 8 — Graphs & tables
- Read value; compare categories; percent of total from table
- Infer trend; spot misleading scale (reasoning, not rant)
- Sample original mini-table: monthly bus riders for three lines — ask which line grew most in absolute riders vs percent.

### Stage 9 — Mixed timed
- Section-length mixes; include easy→hard ordering practice (NITE notes ascending difficulty within type)
- Error log: translation error vs algebra slip vs misread graph

### Stage 10 — Profile coaching
- Explain equal vs quant-oriented general score weighting using NITE’s published rules only
- Choose practice emphasis based on learner’s verbal vs quant balance (product may later suggest)
- Reminder: unscored section exists — treat every section seriously (NITE guidance)

## 5. Finish criteria per stage

- Stage check ≥ **80%** at the stage’s target level; no review topic left at level 0.
- Stages 1–8: leave with core tiles ≥ L2; optional stretch at L3.
- Stage 9: ≥ threshold on **two** timed mixed checks in a row (or 2 of last 3 — product choice).
- Never gate on an invented “raw score = 800” conversion.

## 6. Level-up (3 levels / stage)

| Level | Quant meaning | Up | Down |
|-------|---------------|----|------|
| L1 | Untimed or gentle time; single-skill items | Spaced successes | Fail streak / dormancy policy |
| L2 | Standard item difficulty; light time pressure | Sustained L1 + mixed sets | Fail mixed set |
| L3 | Hard items + full section pace | L2 stable + timed check | Miss timed check → L2 drill |

Drop a level on conceptual confusion (wrong model), not only on arithmetic slips — tag error types in events.

## 7. Metrics

| Metric | Proposal | Events |
|--------|----------|--------|
| Weekly progress vs goal | minutes and/or tiles leveled vs weekly goal | session + level_change |
| Accuracy by topic tag | correct/attempted | answer_submit |
| Median time per item (by stage) | latency percentiles | answer_submit.latency_ms |
| Timed-section projected comfort | Stage 9 check trend | check_attempt |
| Domain balance note | qualitative flag if verbal neglected | optional separate verbal road later |

Honest empty state until real answers exist.

## 8. Schema gaps (format owner)

1. **Strict timer per section** with pause rules for practice vs sim.
2. **Figure/table stem** asset type (accessible text alternative required).
3. **Formula-sheet overlay** toggle.
4. **Answer types:** MC (4 options, NITE-style), numeric, and “which quantity larger” comparison if used in some materials — confirm which appear in **current** two-domain quant (NITE format page emphasizes Problems + Graph/Table; older guides also mention Quantitative Comparisons — treat Comparisons as **verify-before-implement**).
5. **Error taxonomy** field on attempts (translation / setup / calc / misread).
6. **Score explainer** content blocks citing NITE weightings (not a live score converter pretending official equating).
7. Explicit `level` on tiles; subject `psychometric_quant`.

## 9. Original sample stems (planning only)

1. “A shop discounts a ₪80 item by 15%. What is the sale price?”
2. “Train A travels 120 km in 2 h. Train B is 25% faster. How long does B need for 120 km?”
3. “In a table of four cities’ rainfall, which city has the median value?”
4. “A square’s side increases by 10%. By what percent does its area increase?”

## 10. Next steps

1. Confirm question-type mix for the exact administration year (two-domain) from NITE updates.
2. Decide path id series, e.g. `path_psych_quant_01_…`.
3. Build generators for original MC distractors; store exemplars in DB per product decision.
4. Author JSON under `adult/` only after schema gaps are agreed — never under `planning/`.
