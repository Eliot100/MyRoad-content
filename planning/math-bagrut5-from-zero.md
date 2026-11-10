# Math 5-unit bagrut from zero (adults) — road outline

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.
> Distinct from existing adult paths `path_math_zero_to_equation` and `path_math_bagrut_3_units`.
> Open content PR #45 (`feat/math-bagrut5`) already authors **path JSON** for a 5-unit chain — this file is the **planning/research scaffold** (sources, adult-from-zero staging, schema gaps). Do not conflict with or duplicate that JSON here.

## 1. Learner, start, target

| Field | Definition |
|-------|------------|
| Learner | Adult in Israel (he/en/ar UI later) returning to math after a long gap; may hold an old 3-unit bagrut or none |
| Start | Near zero for high-school math: arithmetic and one-variable equations shaky-to-OK; **no** assumed fluency with functions, trig, or calculus |
| Target | Israel MoE **Mathematics 5 יח"ל** bagrut readiness under the **new curriculum** exam structure (questionnaires **35571** and **35572** as published on MoE pedagogical pages). Learning readiness goal — not a guaranteed MoE grade |
| Content originality | Sample stems in this doc are **original**. Do not copy MoE exam items. Future practice must be original or clearly licensed. |

Hebrew glossary: מקצוע → סדרה → דרך → שלב → משבצת.

### How this differs from existing / in-flight content

| Asset | What it is | Relation to this outline |
|-------|------------|--------------------------|
| `adult/path_math_zero_to_equation.json` | Numbers → one-variable equation | **Prerequisite / feeder** — adults may complete it (or place out) before Stage 1 here |
| `adult/path_math_bagrut_3_units.json` | 3-unit **new program** clusters (society/science, plane/space, financial) | **Different target level** (3 יח"ל). Do not merge topics into 5-unit roads blindly |
| PR #45 `feat/math-bagrut5` | Actual 5-unit **path JSON** series (placement + topic roads + exam) | **Content implementation track**. This planning doc must stay Markdown-only and may inform later revisions; it must not add JSON or fight PR #45 file paths |

Proposed future path family (if separate from PR #45 naming): `math_bagrut5` series — coordinate with #45 ids before any new JSON.

## 2. Verified public sources (MoE)

Checked with `curl` (HTTP 200) on 2026-11-07 (Asia/Jerusalem):

| Source | URL | Status | What we take from it |
|--------|-----|--------|----------------------|
| MoE — New math curriculum (high school) | https://pop.education.gov.il/tchumey_daat/matmatika/chativa-elyona/teaching-mathematics/new-curriculum/ | 200 | New program entered schools תשפ"ד; **5 יח"ל** grade-10/11/12 curriculum PDF links listed; exam structure for **שאלון 35571** (weight **60%**, duration **3 hours 45 minutes**) and **שאלון 35572** (weight **40%**, duration **2.5 hours**) published on-page |
| MoE — Examination & evaluation | https://pop.education.gov.il/tchumey_daat/matmatika/chativa-elyona/teaching-mathematics/examination-evaluation/ | 200 | Bagrut info / formula sheets / focusing notes; adults (בוגרים) in תשפ"ו may still choose new vs old exam program — **product must ask which track** before exam-sim content |
| MoE — Free prep courses (Campus IL) | https://pop.education.gov.il/tchumey_daat/matmatika/chativa-elyona/teaching-mathematics/preparatory-courses-for-matriculation/ | 200 | Free digital prep for 3/4/5 units; explicitly mentions adults completing bagrut; Hebrew & Arabic offerings |
| MoE — Math high-school hub | https://pop.education.gov.il/tchumey_daat/matmatika/chativa-elyona/teaching-mathematics/ | 200 | Hub for curriculum / old structure / teaching notes |

### Exam topic scaffold (from MoE new-curriculum page text — reconcile with grade PDF packs before JSON)

**שאלון 35571 (60%):** short items; probability / sequences & induction; plane geometry & trigonometry; calculus (חדו״א). Regular structure: ch. 1 compulsory, answer 3 of 4; ch. 2 1 of 2; ch. 3 1 of 2; ch. 4 2 of 3; 20 pts each ([source](https://pop.education.gov.il/tchumey_daat/matmatika/chativa-elyona/teaching-mathematics/new-curriculum/)). Summer 2026 papers used eased rules: answer **2 of 4** short items, 5 questions total (moed א: at least one from ch. 1 or 2, one each from ch. 3 and 4) ([source](https://meyda.education.gov.il/sheeloney_bagrut/2026/6/HEB/35571.pdf)). Build simulation rules per exam year.

**שאלון 35572 (40%):** analytic geometry & vectors (incl. space trig); complex numbers; calculus of exponential & logarithmic functions.

**Not invented / deferred:** full fine-grained topic tables and hour allocations live in MoE **PDF** curriculum packs linked from the new-curriculum page. Those PDFs were **not** fully downloaded/parsed in this planning pass. Treat stage topic lists below as a **pedagogical scaffold aligned to the named exam blocks**, to be reconciled against official 5 יח"ל grade PDFs before shipping or revising content JSON.

**Unverified:** exact recommended classroom hours per subtopic; which optional items appear for every adult external examinee population; precise formula-sheet contents per language — mark **MoE PDF check** before shipping.

**Broken / weak URL note:** older guessed paths like `.../tchumey_daat/mathematics/...` redirected to the MoE pop home in earlier probes — prefer the **`matmatika`** URLs above (verified 200 with real curriculum content).

## 3. Stages (שלבים)

Each stage: goal, target capability, **estimated** hours (estimate only — not MoE figures).

Level concept: **3 levels per stage** — L1 recall/apply basic, L2 multi-step / mixed representations, L3 exam-like synthesis and error spotting.

| Stage | Hebrew label | Goal | Target level (end) | Est. hours (estimate) |
|-------|--------------|------|--------------------|------------------------|
| 0 | הצבה + גישור | Placement; bridge from zero-to-equation / 3-unit habits | Place into Stage 1 or light review | 3–6 |
| 1 | אלגברה ופונקציות יסוד | Algebra fluency; function concept | L2 | 16–28 |
| 2 | גאומטריה וטריגונומטריה במישור | Plane geometry + trig for 35571 | L2 | 16–28 |
| 3 | סדרות ואינדוקציה | Sequences & induction | L2 | 10–18 |
| 4 | הסתברות | Probability literacy for 35571 | L2 | 10–18 |
| 5 | חדו״א — יסודות | Limits intuition → derivative → applications | L2–L3 intro | 20–36 |
| 6 | חדו״א — אינטגרלים ויישומים | Integrals & exam-style applications | L2 | 14–24 |
| 7 | הנדסה אנליטית ווקטורים | Analytic geometry + vectors (→ 35572) | L2 | 16–28 |
| 8 | מספרים מרוכבים | Complex numbers | L2 | 8–14 |
| 9 | מעריכיות ולוגריתמים + חדו״א שלהן | Exp/log and their calculus (35572) | L2 | 12–20 |
| 10 | סימולציית 35571 / 35572 | Mixed exam sims under time | L3 under time | 14–24 |

**Finish criteria (road):** Stage 10 checks at threshold on both questionnaire-style mixes; core Stages 1–9 tiles ≥ stage target level. Readiness language only — no grade promise.

Adult bridge note: learners who only finished `path_math_zero_to_equation` need Stage 0–1 heavily; learners with strong 3-unit may place into Stage 2–3 after diagnostic — **do not** skip calculus/vectors/complex by assuming 3-unit ≡ 5-unit.

## 4. Topics / tiles per stage

Kinds: `learn` (understanding), `practice` (review), `check`; worked_method / can_do already used in MyRoad math content — keep consistency with PR #45 patterns when implementing.

### Stage 0 — Bridge
- Diagnostic across algebra, functions, geometry, basic trig
- Calculator / formula-sheet habits (official נוסחאון — do not invent allowed formulas)
- Sample: “Solve \(2x-5=11\). Then sketch \(y=2x-5\) and name slope/intercept.”

### Stage 1 — Algebra & functions
- Linear/quadratic; systems; inequalities
- Function notation; domain; transformations light
- Sample: “For \(f(x)=x^2-4x\), find vertex and intercepts.”

### Stage 2 — Plane geometry & trig
- Triangles, circle theorems as required by curriculum PDF (reconcile)
- Trig identities / equations / applications in plane
- Sample: “In right triangle with opposite 5 and hypotenuse 13, find \(\sin\) and the acute angle qualitatively.”

### Stage 3 — Sequences & induction
- Arithmetic/geometric sequences; induction proofs at 5-unit depth (reconcile PDF)
- Sample: “Prove by induction a simple sum formula (original coefficients).”

### Stage 4 — Probability
- Basic probability, conditional (as required), counting links
- Sample: “Two draws without replacement from an urn — compute a joint event.”

### Stage 5–6 — Calculus
- Derivative rules; tangent; extrema; word problems
- Integral as antiderivative / area (curriculum depth)
- Sample: “Find maxima of an original polynomial on an interval.”

### Stage 7 — Analytic geometry & vectors
- Lines, circles, conics as required; vectors in plane/space; space trig as listed for 35572
- Sample: “Given two points, write line equation; find a perpendicular vector.”

### Stage 8 — Complex numbers
- Form, operations, polar/trig form as required
- Sample: “Compute \((1+i)^2\) and locate on Argand diagram.”

### Stage 9 — Exp/log calculus
- Exp/log algebra; derivatives/integrals of these families per 35572
- Sample: “Differentiate \(\ln(3x+1)\) and interpret growth.”

### Stage 10 — Exam simulation
- Mixed 35571-style and 35572-style **original** multi-part items
- Timed sections using MoE-published durations as **practice timeboxes** (cite MoE page; do not invent)
- Error-log review; formula-sheet discipline

## 5. Finish criteria per stage

- End-check ≥ **80%** at stage target level; no review topic stuck at level 0.
- Understanding tiles completed once with micro-check.
- Review tiles reach minimum level (usually L1 to leave; L2 for core exam stages).
- Stage 10: separate checks aligned to 35571-heavy and 35572-heavy mixes.

## 6. Level-up rules (3 levels / stage)

| Level | Meaning | Up when | Down when |
|-------|---------|---------|-----------|
| L1 | Single-idea items; can state the idea | Spaced successes / product SRS | Fail streak / dormancy policy |
| L2 | Multi-step / graph+symbol / two representations | Harder pool sustained | Fail L2 pool |
| L3 | Exam-like synthesis, explain-a-mistake | Sustained L2 + L3 check | Fail L3 → L2 practice |

Spacing: product defaults; mix symbolic and numeric; require method (worked_method) so level-up ≠ memorizing answers. PR #45 already uses `*_l1/_l2/_l3` topic id suffixes — prefer that convention over inventing a new level schema field unless format owner adds one.

## 7. Metrics

| Metric | Proposal | Events needed |
|--------|----------|---------------|
| Weekly progress vs goal | minutes and/or tiles leveled vs weekly goal | `session_start`, `session_end`, `tile_complete`, `level_change` |
| Stage mastery | fraction of stage tiles ≥ target level | `tile_level` |
| Accuracy by topic | correct/attempted | `answer_submit` |
| Exam-sim readiness | Stage 10 check scores | `check_attempt` |
| Bridge flag | still dependent on zero-to-equation skills | placement events |

Honest empty state until real answers exist.

## 8. Schema gaps (format owner)

1. **Multi-part bagrut-style item** (א/ב/ג) with shared stem and partial credit policy.
2. **Symbolic / numeric+unit** answer types beyond MC (tolerance, exact fractions).
3. **Diagram** interaction (graphs, geometric figures) + accessibility text.
4. **Formula-sheet overlay** toggle (official נוסחאון reference, not a rewritten sheet).
5. **Track selector** for adults: new curriculum vs old exam program (תשפ"ו MoE note).
6. Explicit coordination with PR #45 id scheme (`path_math_bagrut5_*`) — avoid duplicate series names.
7. Generator + uniqueness checks (PR #45 already emphasizes no repeated questions) — keep as pipeline requirement.
8. Subject/group tags for 5-unit adult series in catalog locale rules.

## 9. Original sample micro-items (planning only)

1. “A taxi charges ₪12 plus ₪3.5 per km. Write cost as \(C(d)\) and find cost for 8 km.”
2. “Differentiate \(f(x)=3x^4-2x\); find \(f'(1)\).”
3. “Vector \(\vec{u}=\langle 2,0\rangle\), \(\vec{v}=\langle 0,3\rangle\). Compute \(\vec{u}+\vec{v}\) and its magnitude.”
4. “Solve \(2^x=8\) without a calculator; explain via powers of 2.”

## 10. Next steps

1. Reconcile stage topics against MoE 5 יח"ל grade-10/11/12 PDF packs.
2. Align with PR #45: either treat #45 as the implementation of this outline, or open a follow-up content PR only for gaps — **never** drop JSON into `planning/`.
3. Resolve adult new-vs-old exam track UX with product.
4. Hand schema gaps to format owner before expanding answer types.
