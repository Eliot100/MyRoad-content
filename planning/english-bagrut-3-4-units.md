---
status: planning
pathId: english-bagrut-3-4-units-adult
title: English Bagrut 3 and 4 Units — Adult Lighter Road
learner: Adult Israeli learners starting from basic English (about A2 or lower) who want a lighter bagrut path than the existing 5-unit English roads.
start: Basic reading and listening; limited formal secondary English.
target: English bagrut 3 units (Modules A + B + C) or 4 units (Modules C + D + E). Module C is shared.
originality: Sample items original. Do not copy MoE lists or existing MyRoad wording.
---

# English Bagrut 3 and 4 Units (Adult, lighter road)

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.

> Scope note: this is **bagrut** English. It is unrelated to the 2026-11-10 decision that moved English off the psychometric road onto AMIRNET (see [amirnet-english-placement.md](./amirnet-english-placement.md)).

## Learner, start, target
- **Learner**: Adult who needs English for a full bagrut certificate and prefers a lighter path than the 5-unit roads.
- **Start**: Basic reading and listening.
- **Target**: 3 units (Modules A + B + C, CEFR exit about A2) or 4 units (Modules C + D + E, about B1). Module C is shared, so a learner can start on 3 units and extend to 4. Focus on reading, short writing and vocabulary; the oral part is noted but its weight and format for adult externals are **unverified**.
- **Originality**: Sample items are original.

## Public sources checked
- MoE English portal: [https://pop.education.gov.il/tchumey_daat/english/](https://pop.education.gov.il/tchumey_daat/english/) (HTTP 200, 2026-11-11).
- MoE exam tracks list, winter תשפ"ו: [TrecksEnglishWin2026.pdf](https://meyda.education.gov.il/files/Exams/TrecksEnglishWin2026.pdf) (read 2026-11-11). Module codes: A **016381**, B **016384**, C **016382**, D **016484**, E **016471** (F 016584, G 016582).
- MoE מיקוד 2024 for English: [english.pdf](https://meyda.education.gov.il/files/portal_talmidim/mikud/2024/english.pdf) (read 2026-11-11). Marks 16384 (Module B) and 16484 (Module D) as "לנבחנים אקסטרניים בלבד"; lists the Module C opinion-writing topics and the Module E vocabulary Band lists.
- Secondary (commercial prep sites, not official): the 3-unit = A + B + C and 4-unit = C + D + E split, module weights 27/26/27 + oral 20, and word counts. Treat as secondary.
- **Unverified / gaps**: oral exam weight and format for adult externals; current (2026/27) מיקוד; exact word counts. No codes were invented.

## Stages (estimate hours; label as estimate)

### Stage 1: Foundations for 3 units — Modules A and B (estimate 30–40h)
- **Goal**: Short informational and personal texts, interview-style listening, core vocabulary and grammar.
- **Target level**: 3-unit readiness.
- **Topics/tiles**: present simple/continuous, basic connectors; Module A is reading comprehension; Module B for externals is a written reading paper (016384). Kind: understanding.
- **Finish criteria**: Answer 5 comprehension questions on a 150-word original text with ≥80% accuracy; complete a short listening task.

### Stage 2: Module C — reading + short opinion writing (estimate 25–35h)
- **Goal**: Longer reading plus a short opinion paragraph (shared by 3 and 4 units).
- **Target level**: Bridge.
- **Topics/tiles**: medium-length reading (secondary sources: up to about 300 words); opinion writing on the MoE topic list (secondary sources: 70–90 words). Kind: understanding + practice.
- **Finish criteria**: Write a coherent opinion paragraph (original prompt) with a clear main idea and 2 supports; self-score ≥70% on the criteria.

### Stage 3: 4-unit extension — Modules D and E (estimate 25–35h)
- **Goal**: More complex reading; for externals, Module D (016484) is reading + a written response (opinion and/or description related to the text); Module E (016471) is reading + vocabulary from the Band lists.
- **Target level**: 4 units.
- **Topics/tiles**: Kind: understanding + review; Band vocabulary drills with spacing.
- **Finish criteria**: Analyze an extended original text and write a 100-word response; reach ≥80% on a Band-list vocabulary set.

### Stage 4: Review and mock — choose 3 or 4 units (estimate 15–20h)
- **Goal**: Timed module-by-module practice.
- **Finish criteria**: Complete the chosen mock set with ≥70% (self-scored).

## Level-up rules (3 levels per stage)
- Level 1: Basic comprehension of short texts.
- Level 2: Accurate answers plus simple production.
- Level 3: Fluent production under time with fewer language errors.
- Advance on consistent Level 2.
- Spacing: vocabulary and grammar review every 3–5 days; mixed skill retrieval.

## Metrics events needed
- `tile_completed`, `stage_completed`, `mock_score`, `writing_produced`, `listening_accuracy`.

## Schema gaps
- Speaking/oral transcript scoring and a full writing rubric are not fully in the schema (partial support via the existing transcript check). Flag for Content.
- Listening audio generation is a separate need.

## 3 ORIGINAL sample items
1. **Reading (Module A/B style)**: Read: "Many people in Tel Aviv ride bicycles to work because the city added new bike lanes. The lanes make the trip safer and faster." What is the main reason people ride bikes? (a) They like exercise (b) New lanes make it safer and faster (c) Cars are expensive.
2. **Writing (Module C style)**: Write 60–80 words: Do you prefer studying alone or with a friend? Give two reasons.
3. **Analysis (Module D/E style)**: Read a short original paragraph about a student who moved to a new city. What challenge did she face and how did she solve it? Support your answer with details from the text.

## Review notes (bot review, 2026-11-11)

- **Source**: SuperGrok Expert draft (chat f76ced5b, 2026-11-10), split and checked by a bot.
- **Confirmed** (official MoE PDFs): module codes A 016381, B 016384, C 016382, D 016484, E 016471; 16384 and 16484 are written papers for externals only (school students do the B/D literature modules in school).
- **Corrected**: Grok described Stage 3 as "longer writing, literary elements if required". Per the 2024 מיקוד, Module E is reading + vocabulary (Band lists) and the externals' Module D is reading + a written response. Stage 3 now says that.
- **Unverified**: oral exam (BOOST/COBE) weight and whether/how adult externals take it; module weights 27/26/27/20 (secondary sources only); word counts; the 2026/27 מיקוד; all hour figures are estimates.
- **Originality check**: sample items are original (Grok-written, not copied from MoE).
