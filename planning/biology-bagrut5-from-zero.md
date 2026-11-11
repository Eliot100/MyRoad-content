# Biology 5-unit bagrut from zero — road outline

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.

## 1. Learner, start, target

| Field | Definition |
|-------|------------|
| Learner | Adult (MyRoad v1 audience). Content later in Hebrew; UI languages he/en/ar. |
| Start | Near zero formal biology. Assumes general knowledge and enough Hebrew (or supported UI language) to read short explanations. |
| Target | Readiness for Israel MoE **Biology 5 יח"ל** specialist track: the three core theoretical topics plus scientific-thinking skills for the written paper. Wet lab and the full bio-heker (research) assignment stay school-based; this road builds transferable reasoning, not a fake lab certificate. |
| Content originality | Sample items are **original**. Do not copy exam items. |

Proposed future path family (JSON later, never here): `biology_bagrut5`.

## 2. Verified public sources

Checked with `curl -I -L` on 2026-11-08 (Asia/Jerusalem):

| Source | URL | HTTP | What we take from it |
|--------|-----|------|----------------------|
| Specialist 5 יח"ל curriculum | https://pop.education.gov.il/tchumey_daat/biologya/chativa-elyona/biology-pedagogy/curriculum-specialize/ | 200 | Theoretical program built on **three core topics**: (1) the human body with emphasis on homeostasis, (2) the cell — structure and activity, (3) ecology. **One** deepening topic is chosen from: gene-expression control and genetic engineering; comparative physiology; bacteria and viruses in the human body. The page also describes a practical side: lab work and a research assignment (bio-heker), with published weights of theoretical **55%**, lab **15%**, and alternative/research assessment **30%**. |
| Curriculum hub | https://pop.education.gov.il/tchumey_daat/biologya/chativa-elyona/biology-pedagogy/curriculum/ | 200 | Index pointing at the specialist 5-unit track. |
| Non-specialist intro (not this road) | https://pop.education.gov.il/tchumey_daat/biologya/chativa-elyona/biology-pedagogy/curriculum-not-specialize/ | 200 | “Introduction to biology” / מבוא — **not** the 5-unit specialist path. Do not mix the two. |
| Final project notes | https://pop.education.gov.il/tchumey_daat/biologya/chativa-elyona/biology-pedagogy/thesis/ | 200 | Separate final-project (עבודת גמר) track. Out of scope for the default from-zero road. |

**Slug warning:** `…/tchumey_daat/biology/…` (English spelling) redirected to the pedagogical-space homepage on 2026-11-08. The live subject slug is **`biologya`**. An earlier note that the curriculum page “occasionally 404s” referred to the wrong slug.

**Not invented:** fine-grained syllabus tables inside the 2015 curriculum PDF linked from the specialist page (not fully parsed here); year-specific mikud. **Questionnaire codes (gap filled):** theory paper **43381** (4 chapters, 32/35/18/15 pts, 3.5 h on the summer 2026 alternate sitting) ([source](https://meyda.education.gov.il/sheeloney_bagrut/2026/6/HEB/43381.pdf)); practical lab exam **43386** (3 h) ([source](https://meyda.education.gov.il/sheeloney_bagrut/2026/6/HEB/43386.pdf)). Externals' codes are not confirmed.

**Unverified / deferred:** which deepening topic an adult external examinee must take; how much of the 30% research/lab component can be completed outside a school (fact check 2026-11-11: unverified); recommended classroom hours per subtopic.

## 3. Stages (שלבים)

Hours are **unverified estimates**. 3 levels per stage, as in other planning docs.

| Stage | Hebrew label | Goal | Target level | Est. hours (estimate) |
|-------|--------------|------|--------------|----------------------|
| 0 | הצבה | Placement + biology language (organism / cell / ecosystem) | Place into Stage 1 | 2–4 |
| 1 | התא | Cell structure and activity: organelles, membrane transport, respiration basics, DNA/RNA overview, mitosis/meiosis intro — only as the official core list requires | L2 | 40–60 |
| 2 | גוף האדם והומאוסטזיס | Major systems and feedback that maintain internal stability | L2; L3 on integration | 60–90 |
| 3 | אקולוגיה | Ecosystems, energy flow, cycles, populations, human impact | L2–L3 | 30–50 |
| 4 | נושא העמקה (בחירה) | Overview of **one** official deepening topic (do not invent a fourth option) | L2 awareness to L3 if sources allow | 16–30 |
| 5 | חקר ונתונים (מודעות) | Graphs, simple experimental design, research-text interpretation. Not a substitute for bio-heker or the lab exam. | L2–L3 reasoning | 20–40 |
| 6 | סימולציית בגרות | Mixed theoretical questions across the three core topics | L3 under time | 30–50 |

**Total estimate:** about 200–320 hours including one deepening overview (180–290 without it). Estimates only.

## 4. Topics / tiles (משבצות)

Understanding then review for: cell organelles and membrane processes; cellular energy (respiration) at curriculum depth; each major human system named in the official core; homeostasis and feedback; ecology principles and human impact; data interpretation and experimental design; one official deepening topic (chosen later, not here).

Do not add extra “popular science” chapters (evolution-as-a-full-stage, biochemistry survey, etc.) until they appear on the official specialist list.

## 5. Finish criteria

- Explain a body process at both cell and organism levels.
- Describe a homeostasis example with a feedback loop.
- Interpret a simple ecological graph or data set.
- Answer multi-part theoretical questions in the style of the external paper (original items only).
- End-check proposal: ≥80% at the stage’s target level; no review topic stuck at level 0.

## 6. Level-up and spacing

L1 identify structures/functions; L2 explain process and regulation; L3 apply to a novel scenario or data. Recycle systems and core ideas on the product’s default spacing. A fail streak drops or holds a level.

## 7. Metrics

Same event family as other planning roads: `session_start` / `session_end`, `tile_complete`, `level_change`, `answer_submit` (topic-tagged), `check_attempt`. Derived: weekly progress vs goal, stage mastery, accuracy by topic, exam-sim readiness. Honest zeros until real answers exist.

## 8. Schema gaps

1. Multi-part items with a shared stimulus (text, graph, or diagram).
2. Diagram labeling (organelle, organ-system, food-web) — interaction type may be missing.
3. Lab/research awareness tiles vs scored checks. The app cannot replace MoE lab or bio-heker logistics.
4. How (or whether) a learner picks the official deepening topic — product decision.
5. Subject tag `biology` and series ids.
6. Parse the full 2015 (updated 2017) curriculum PDF before JSON.

## 9. Original sample items (not for JSON yet)

1. Describe how the body maintains blood glucose using a negative-feedback example, and name the hormones you are using in the explanation.
2. Why does a plant cell have a cell wall and a large vacuole while a typical animal cell does not? Link each structure to a function.
3. A rabbit population would double every month with unlimited resources. What limits growth in a real ecosystem? Name two factors and explain each in one sentence.

## 10. Next steps (when leaving planning)

1. Download and reconcile the official full specialist curriculum PDF.
2. Confirm externals' questionnaire codes (school codes 43381 / 43386 found, see section 2) and mikud on the live MoE pages.
3. Decide how deepening-topic choice is represented in the product.
4. Author JSON under `adult/` (never under `planning/`).
