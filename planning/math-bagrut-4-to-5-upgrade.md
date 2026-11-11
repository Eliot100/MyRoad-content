---
status: planning
pathId: math-bagrut-4-to-5-upgrade-adult
title: מתמטיקה — שדרוג מ־4 ל־5 יח"ל (Math 4-to-5 unit upgrade) — Adult
learner: Adult who passed (or is ready for) 4-unit math and wants 5-unit bagrut for academic admission.
start: Solid 4-unit level (right-triangle trig, circle and line analytic geometry, polynomial/rational/root/exp-log calculus, sequences, probability with statistics).
target: 5 יח"ל readiness for questionnaires 35571 + 35572 (new curriculum). Delta only — full 5-unit road is in math-bagrut5-from-zero.md.
originality: All sample items original. Do not copy MoE exam items or existing MyRoad math content.
---

# Math 4-to-5 unit upgrade (adults) — delta outline

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.
> **Delta only.** Learner, staging logic, level rules and schema gaps for 5 units are in [math-bagrut5-from-zero.md](./math-bagrut5-from-zero.md); this file lists only what a 4-unit graduate is missing and how to route them through the existing `adult/path_math_bagrut5_*` roads (PR #45 JSON on main). No new path ids proposed.

## 1. Learner, start, target

| Field | Definition |
|-------|------------|
| Learner | Adult with a 4-unit math bagrut (or 4-unit-level skills) needing 5 units, e.g. for a university admission threshold. |
| Start | 4-unit content per the MoE 4-unit curriculum (section 2). Assumed fluent in algebra and basic calculus. |
| Target | 5 יח"ל: questionnaires **35571** and **35572**. Learning readiness only — no grade promise. |
| Content originality | Original items only. |

## 2. Verified public sources (MoE)

Checked with `curl` + `pdftotext` on 2026-11-10 (Asia/Jerusalem):

| Source | URL | Status | What we take from it |
|--------|-----|--------|----------------------|
| MoE 4-unit curriculum, grades 10–12 (dated February 2015) | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/matematika/mat_4u.pdf | 200 (PDF) | Three content areas: geometry (Euclidean, analytic, trig), change (one-variable calculus), uncertainty (classical probability + extended statistics). Hours table 120/year: geometry+trig 40/30/30, statistics+probability 30/45/–, algebra+analysis 50/45/70 (grade 11 adds arithmetic and geometric sequences; grade 12 adds exponential/log equations, growth/decay). Trig is **right-triangle** based; grade 12 adds **space** geometry/trig (volumes, surface areas). Calculus: grade 10 polynomials only; grade 11 rational functions, intuitive limit, asymptotes, **square-root functions (linear inside only for integrals)**; grade 12 exp/log calculus. Explicit note: **trigonometric functions are excluded from 4-unit analysis**. Probability "as a tool only": **no combinatorics, no binomial coefficients**; includes conditional probability, normal distribution, statistical inference (confidence interval, hypothesis tests). |
| Bagrut paper 35571, summer תשפ"ו 2026 moed ב | https://meyda.education.gov.il/sheeloney_bagrut/2026/8/HEB/35571.pdf | 200 (PDF) | "תוכנית חדשה". Four chapters, 8 questions: 1 short questions (answer 2 of 4 sub-items); 2 **induction, sequences and probability**; 3 **plane geometry and trigonometry**; 4 **calculus of polynomial, root, rational and trigonometric functions**. Answer **5 questions, 22 pts each**, max 100. Non-graphing calculator + attached formula sheets. Duration on this paper: **4 hours 20 minutes**. Short-question samples include an induction proof and a sequence-in-a-triangle item. |
| 35572 topics | from [math-bagrut5-from-zero.md](./math-bagrut5-from-zero.md) §2 (MoE new-curriculum page, checked 2026-11-07) | — (not re-checked) | Analytic geometry and vectors (incl. space trig), complex numbers, exp/log calculus. |

**Settled (fact check 2026-11-11):** **3 h 45 min is the regular 35571 duration** (MoE web page and the summer תשפ"ו moed א paper, 5 × 20 pts) ([source](https://meyda.education.gov.il/sheeloney_bagrut/2026/6/HEB/35571.pdf)). The moed ב paper's **4 h 20 min with 5 × 22 pts (max 100)** is a special-sitting variant. Use 3:45 as the default simulation timer and label 4:20 as a special variant.

**Unverified / TODO**

- The 4-unit PDF is a **2015** document (grade 10 detailed; grades 11–12 "not final"). The current 4-unit exam may follow a newer program. **TODO:** read the current 4-unit pages before trusting the "already known" column.
- 4-unit questionnaire codes (new curriculum): **35471 + 35472** ([source](https://pop.education.gov.il/tchumey_daat/matmatika/chativa-elyona/teaching-mathematics/new-curriculum/)).
- Exact 5-unit probability scope (combinatorics? binomial?) and root-function scope were not read from the 5-unit curriculum PDFs. **TODO.**
- 35572 paper was not opened in this pass.
- Whether adults can sit only 35571/35572 after a 4-unit certificate (upgrade rules, grade replacement) — **TODO** with אגף הבחינות.
- All hours are **estimates**.

## 3. Delta map (what 4 → 5 adds)

| Topic | 4 units (per 2015 PDF) | 5 units (35571 / 35572) | Delta | Existing road to reuse |
|-------|------------------------|--------------------------|-------|------------------------|
| Induction | not listed | 35571 ch. 2 + short items | **New** | `path_math_bagrut5_04_sequences` |
| Sequences | arithmetic + geometric | with induction, mixed problems | **Deepen** | `path_math_bagrut5_04_sequences` |
| Probability | tool only; no combinatorics/binomial | 35571 ch. 2 | **Deepen** (scope TODO) | `path_math_bagrut5_05_probability` |
| Statistics / inference | yes | not in 35571/35572 topic lists | **Skip** | — |
| Plane geometry + trig | right-triangle trig; circle geometry | 35571 ch. 3 (plane geometry and trigonometry) | **Deepen**: general-triangle trig, proofs | `path_math_bagrut5_02_geometry`, `path_math_bagrut5_03_trig` |
| Trig functions in calculus | **explicitly excluded** | 35571 ch. 4 | **New** | `path_math_bagrut5_06_functions`, `_07_extrema`, `_08_integrals` |
| Root / rational calculus | yes (root: linear inside for integrals) | yes | **Light review + harder** | `_06_functions`, `_07_extrema`, `_08_integrals` |
| Analytic geometry | points, line, circle | with vectors (35572) | **Deepen** | `path_math_bagrut5_09_analytic` |
| Vectors (plane/space), space trig | space trig for volumes only | 35572 | **New** (vectors) | `path_math_bagrut5_10_vectors` |
| Complex numbers | not listed | 35572 | **New** | `path_math_bagrut5_11_complex` |
| Exp / log calculus | yes (grade 12) | 35572 | **Review at 5-unit depth** | `path_math_bagrut5_12_exp_log` |
| Exam format | — | 5 of 8, 22 pts each; long proofs | **New** | `path_math_bagrut5_13_exam` |

## 4. Stages (delta road)

Level concept: same **3 levels per stage** as the from-zero outline (L1 single idea, L2 multi-step, L3 exam synthesis).

| Stage | Hebrew label | Goal | Reuses | Est. hours (estimate) |
|-------|--------------|------|--------|------------------------|
| 0 | אבחון 4→5 | Placement on the delta topics only | `_00_placement` (filtered) | 1–2 |
| 1 | אינדוקציה וסדרות | Induction proofs; sequence problems at 5-unit depth | `_04_sequences` | 10–16 |
| 2 | הסתברות 5 יח"ל | Close the probability gap | `_05_probability` | 8–14 |
| 3 | גאומטריה וטריגו במישור | General-triangle trig; geometry proofs | `_02_geometry`, `_03_trig` | 14–22 |
| 4 | חדו"א של פונקציות טריגונומטריות | Derivatives, extrema, integrals of trig functions | `_06_functions`, `_07_extrema`, `_08_integrals` | 14–22 |
| 5 | וקטורים ומרחב | Vectors in plane/space; with analytic geometry | `_09_analytic`, `_10_vectors` | 14–22 |
| 6 | מספרים מרוכבים | Complex numbers | `_11_complex` | 8–14 |
| 7 | מעריכיות ולוגריתמים בעומק 5 | Review exp/log calculus at 5-unit depth | `_12_exp_log` | 4–8 |
| 8 | סימולציה | 35571 + 35572 timed sims | `_13_exam` | 10–16 |

**Tiles:** reuse tiles inside the listed roads; mark 4-unit-known tiles as "place-out eligible" (pass L2 check → skip). New tiles needed only where the delta says **New** and the road lacks them (audit TODO).

**Finish criteria (road):** Stage 8 checks at threshold on both questionnaire mixes; Stages 1–6 ≥ L2; no delta topic at level 0. Statistics tiles from 4 units do not count.

## 5. Level-up, weekly progress, metrics

Same rules as [math-bagrut5-from-zero.md](./math-bagrut5-from-zero.md) §6–§7. Additions:

| Metric | Proposal | Events needed |
|--------|----------|---------------|
| Delta coverage | delta topics ≥ L2 / all delta topics | `tile_level` |
| Place-out rate | tiles skipped by placement / tiles offered | placement events |
| Weekly progress vs goal | minutes + delta tiles levelled vs weekly goal (road screen); goals met/missed per week (metrics screen) | `session_start`, `session_end`, `tile_complete`, `level_change` |

## 6. Modes

- **Writing:** full worked solutions typed or photographed (proof steps are graded on the exam).
- **Recording:** learner explains an induction step aloud; checks reasoning, not just the answer.
- **Listening on:** narrated worked examples; **listening off:** text and formulas only.
- **Game:** "derivative sprint" for trig derivatives; "vector tug" (add/scale vectors to hit a target point); complex-plane rotation puzzles.

## 7. Schema gaps

Same as the from-zero outline §8, plus: a **place-out flag** per tile driven by a filtered placement, and a **delta-road wrapper** that sequences tiles from several existing roads without copying them.

## 8. ORIGINAL sample items (planning only)

1. **Induction (L2):** Prove for every natural \(n\): \(5^n - 1\) is divisible by 4.
2. **Trig calculus (L2):** Find the extreme points of \(f(x)=x+2\cos x\) on \([0,\pi]\).
3. **General triangle (L2):** In triangle \(PQR\), \(PQ=7\), \(PR=5\), \(\angle P=60^\circ\). Find \(QR\).
4. **Vectors (L1):** \(\vec a=(1,2,2)\). Find \(|\vec a|\) and a unit vector in its direction.
5. **Complex (L2):** Write \(z=-2+2i\) in trigonometric form and compute \(z^4\).
6. **Probability (L2):** A box holds 4 red and 3 blue cards; draw 3 without replacement. Find P(exactly 2 red).

## 9. Next steps

1. Audit the existing `path_math_bagrut5_*` roads for the **New** rows (induction, trig calculus, vectors, complex) and list missing tiles.
2. Confirm current 4-unit program and adult upgrade rules.
3. Default 35571 timer = 3 h 45 min (settled, see section 2); 4 h 20 min only as a labeled special-sitting variant.
4. Design the filtered placement with the format owner.
