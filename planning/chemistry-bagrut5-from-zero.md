# Chemistry 5-unit bagrut from zero — road outline

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.

## 1. Learner, start, target

| Field | Definition |
|-------|------------|
| Learner | Adult (MyRoad v1 audience). Content later in Hebrew with technical terms; UI languages he/en/ar. |
| Start | Near zero formal chemistry. Assumes arithmetic and basic algebra, plus enough Hebrew (or supported UI language) to read short explanations. No assumed high-school chemistry. |
| Target | Readiness for Israel MoE **Chemistry 5 יח"ל**. School students: 70% = written 037381/037387 (55%) + inquiry lab 037388/037376 (15%), plus 30% internal. **Adult externals** have no internal part and sit three external papers: **037381 (55%) + 037382 (15%) + 037282 (30%)** ([source](https://pop.education.gov.il/tchumey_daat/chemistry/high-school/pedagogy/matriculation-exams/)). This is learning readiness, not a promised bagrut grade. |
| Content originality | Sample items in this doc are **original**. Do not copy exam items. Future practice items must be original or clearly licensed. |

Hebrew glossary (approved MyRoad terms): מקצוע → סדרה → דרך → שלב → משבצת.

Proposed future path family (JSON later, never here): `chemistry_bagrut5`.

## 2. Verified public sources

Checked with `curl -I -L` (HTTP 200) on 2026-11-08 (Asia/Jerusalem):

| Source | URL | What we take from it |
|--------|-----|----------------------|
| MoE pedagogical space — Chemistry curriculum | https://pop.education.gov.il/tchumey_daat/chemistry/high-school/pedagogy/curriculum/ | 5 יח"ל program (from תשע"ה): modular core + extension; **70% external / 30% internal**. External (70%) topics named on the page: bonding and structure; stoichiometry; redox; acids and bases; food chemistry — vitamins, minerals, fatty acids and triglycerides **only**; energetics and dynamics 1 — energy in chemical reactions and reaction rate **only**; inquiry lab — part 2 **only**. |
| MoE — Bagrut exams (Chemistry) | https://pop.education.gov.il/tchumey_daat/chemistry/high-school/pedagogy/matriculation-exams/ | Repeats the 70/30 split and the same named external topics. Describes the written external paper (multiple-choice + unseen article + choice of open questions) and lists questionnaire codes including **037381** (written) / **037387** (computerized alternative), plus lab/mini-research and school-assessment codes. External/resit examinees have a separate three-questionnaire pattern listed on that page. |
| MoE free prep course | https://pop.education.gov.il/sherutey-tiksuv-bachinuch/students-online-courses/preparatory-courses-matriculation/chemistry/ | Free 5 יח"ל prep emphasizing structure/bonding, acids–bases, redox, and energy; open to adults completing chemistry bagrut. |
| MoE curriculum PDF (filename as published) | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/Chimya/curiculum-050526.pdf | HTTP 200 PDF linked from the pedagogical space (filename spelled `curiculum-…`). Fine-grained topic tables were **not** fully parsed in this planning pass — reconcile before any content JSON. |

**Not invented:** classroom hour tables, formula-sheet contents, and year-specific mikud trims. Treat the stage list below as a scaffold aligned to the **named** external 70% blocks.

**Unverified / deferred:** exact recommended hours per subtopic; whether a given adult external examinee must take a particular lab code; full 30% choice-module menu and lab protocols (school-specific). Buffers and other acids–bases subtopics must be taken from the official PDF, not assumed.

## 3. Stages (שלבים)

Hours below are **unverified estimates**, not MoE figures. Product rule: **3 levels per stage** (L1 recall/one-step, L2 multi-step / two representations, L3 novel context or data interpretation).

| Stage | Hebrew label | Goal | Target level | Est. hours (estimate) |
|-------|--------------|------|--------------|----------------------|
| 0 | הצבה / שפה כימית | Placement + particle / symbol / macro language | Place into Stage 1 or light review | 2–4 |
| 1 | מבנה וקישור | Atomic structure, periodic trends, ionic/covalent bonding, states, pure vs mixture | L2 on core tiles | 40–60 |
| 2 | סטוכיומטריה | Balancing, mole, mass/volume relations, limiting reagent, concentration | L2; L3 intro on mixed calc | 50–70 |
| 3 | חמצון–חיזור וחומצות–בסיסים | Oxidation numbers, balancing redox; acids/bases as listed for the external 70% | L2–L3 | 40–60 |
| 4 | אנרגיה, קצב, וכימיית מזון (מוגבל) | Energy in reactions and rate factors **only**; vitamins/minerals + fatty acids/triglycerides **only** | L2–L3 | 30–50 |
| 5 | מעבדת חקר (מודעות) | Interpret data and simple inquiry (lab part 2 awareness). Wet lab stays school-based. | L2 reasoning | 20–40 |
| 6 | סימולציית בגרות | Timed mixed papers in the published external structure | L3 under time | 30–50 |

**Total estimate:** about 210–330 hours, depending on prior math. Label remains estimate.

## 4. Topics / tiles (משבצות)

- `learn` / understanding — one-time concept tile
- `practice` / review — returns with spacing
- `check` — stage end-check

Core tile families: bonding and structure (macro / micro / symbol) → review; stoichiometry calculations → heavy review; redox → review; acids/bases (only as the official list requires) → review; thermochemistry basics + rate factors → understanding then review; limited food chemistry → understanding; inquiry skills (variables, data interpretation) → understanding.

## 5. Finish criteria

- End-check proposal: ≥80% on original mixed items at the stage’s target level, with no review topic stuck at level 0.
- Explain a phenomenon at particle level and link it to a macroscopic observation.
- Solve multi-step stoichiometry and redox items (and acids–bases items that the official list actually includes).
- Stage 6: sit a mixed simulation matching the published external structure (MC + unseen-style literacy + open questions). Timebox TBD from official questionnaire instructions — do not invent duration here.

## 6. Level-up and spacing

Reuse MyRoad product defaults for intervals (do not hardcode days until the product owner confirms). L1 → L2 → L3 as in other planning docs: consecutive success raises a level; a fail streak or long dormancy drops or holds. Mix symbolic, numeric, and particle-level explanations so level-up is not memorization.

## 7. Metrics

| Metric | Formula (proposal) | Events needed |
|--------|--------------------|---------------|
| Weekly progress vs goal | minutes and/or tiles leveled vs weekly goal | `session_start`, `session_end`, `tile_complete`, `level_change` |
| Stage mastery | fraction of stage tiles at ≥ target level | `tile_level` |
| Accuracy by topic | correct / attempted per topic tag | `answer_submit` |
| Exam-sim readiness | Stage 6 check scores over last N attempts | `check_attempt` |

No fake baselines. Until real answers exist, UI shows honest zeros.

## 8. Schema gaps (do not change the format here)

1. Structured numeric + unit answers and multi-part items (shared stem).
2. Particle-diagram / model interaction (not in current English-path node shapes).
3. Formula-sheet mode (show vs hide allowed formulas).
4. Lab-checklist awareness tiles vs scored checks. The app cannot certify a wet lab.
5. Subject tag `chemistry` and bagrut5 series ids — confirm with the publish pipeline.
6. Reconcile the official curriculum PDF topic tables before authoring JSON.

## 9. Original sample items (not for JSON yet)

1. Explain why NaCl conducts electricity when molten but not as a solid, using particle-level language.
2. Calculate the mass of CO₂ produced when 5.0 g of carbon burns completely (show steps). Assume complete combustion to CO₂ only.
3. A solution has [H⁺] = 1×10⁻³ M. What is its pH, and is it acidic or basic? Why?

## 10. Next steps (when leaving planning)

1. Parse the official curriculum PDF topic tables and any formula sheet.
2. External/resit codes confirmed: **037381 + 037382 + 037282** (from summer תשע"ח on) ([source](https://pop.education.gov.il/tchumey_daat/chemistry/high-school/pedagogy/matriculation-exams/)); check the separate תשפ"ז focusing file for externals.
3. Decide one long path vs a series.
4. Author content JSON under `adult/` (never under `planning/`).
