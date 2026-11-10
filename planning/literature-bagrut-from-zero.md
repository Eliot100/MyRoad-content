---
status: planning
pathId: literature-bagrut-from-zero-adult
title: ספרות (Literature) Bagrut from Zero — Adult
learner: Adult Israeli learner completing the compulsory 2-unit literature bagrut (state track, ממלכתי).
start: Reads Hebrew fiction for pleasure at most; no formal literary analysis since school.
target: Readiness for the 2-unit external literature exam (old outline, 70% external). Questionnaire codes for adult externals are unverified (see section 2).
originality: All sample items and micro-texts original. Never reproduce set poems or stories; link to licensed editions instead.
---

# Literature (ספרות) Bagrut from Zero (Adult)

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.
> Distinct from the English road `adult/path_english_bagrut5_07_literature_oral.json` (English literature for the English bagrut).

## 1. Learner, start, target

| Field | Definition |
|-------|------------|
| Learner | Adult in Israel finishing bagrut; Hebrew reader. |
| Start | No literary terms (דובר, מבנה, דימוי, נקודת תצפית); has not read the set works. |
| Target | 2 יח"ל literature, external written exam covering the four genres. The optional 5-unit extension (הגבר) is out of scope. Learning readiness, not a grade promise. |
| Content originality | Set works are copyrighted in many cases. MyRoad must **not** copy them; tiles point to the licensed edition named by MoE and ask original questions. |

Hebrew glossary: מקצוע → סדרה → דרך → שלב → משבצת.

## 2. Verified public sources (MoE)

Checked with `curl` + `pdftotext` on 2026-11-10 (Asia/Jerusalem):

| Source | URL | Status | What we take from it |
|--------|-----|--------|----------------------|
| Literature curriculum, upper secondary, from תשע"ה (file `02sifrutmm2017`) | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/sifrut/02sifrutmm2017.pdf | 200 (PDF) | Base program = **2 יח"ל**, split **70% external / 30% school**. External part covers four chapters: **שירה, סיפור קצר, רומן/נובלה, דרמה**. Summary table: short stories — 2 Agnon, 1 first-half-20th-c, 1 second-half, 2 translated (36 h); 1 novel or novella (15–20 h) + 4–6 reading books; drama — one play (a Sophocles or Shakespeare tragedy, or one modern play) + basics of drama and tragedy (18 h); total **113 h external, 49 h school**. Poetry in this 2017 version: 13 poems (medieval, Bialik, first half of the 20th c). 5-unit extension adds units 3–5 (world literature epic/fiction/drama/poetry, etc.). |
| מפמ"ר literature circular תשפ"ו (dated 2 July 2025) | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/sifrut/chozer_mafmar_2026.pdf | 200 (PDF) | **Old outline:** 70% external + 30% alternative assessment. **New outline:** 35% external + two controlled tasks 35% + 30% alternative assessment; the 35% exam has cluster 1 (short story, novel/novella) and cluster 2 (drama, poetry). **New poetry program only** from winter תשפ"ו in both outlines: 10 clusters of 16 poems in pairs; MoE names two clusters (currently **ב or ז**), the teacher picks one and teaches one poem per pair = **8 poems**, spanning medieval, Bialik, 20th–21st c and translated poetry. From winter תשפ"ו an **unseen-text question** appears in both the poetry and short-story chapters. תשפ"ו keeps the reduced scope (מיקוד) of תשפ"ה; **from תשפ"ז: no מיקוד and no eased answer rules.** Works in focus until summer תשפ"ו: Truman Capote "חג מולד אחד" (short story) and Orwell's "1984" (novel). Adapted 70% exam (codes 8281, 8284): answer 3 questions — one from novel/novella or drama (40 pts) and two from poetry/short story (30 pts each). |

**Unverified / TODO**

- **Adult external examinees.** The circular addresses schools; it does not state which outline or questionnaire an אקסטרני sits. Assumption for planning: externals take the **old-outline 70% external exam** (no school tasks). **TODO:** confirm with אגף הבחינות.
- **Questionnaire codes.** The circular says "סמלי שאלונים – בקישור"; the linked list was not read. Codes 8281 / 8284 are cited only for the adapted exam. The regular exam's code and answer rules (חוקי המענה) are **TODO**.
- **Poem list.** The 2017 13-poem structure is **superseded** by the new poetry program; the cluster ב / ז poem lists were not extracted. **TODO** before content.
- The work lists (רשימות היצירות) are behind download-only links and were not read.
- All hour figures below are **estimates** adapted for adults, not MoE figures.

## 3. Stages (שלבים)

Level concept: **3 levels per stage** — L1 identify a device or fact, L2 explain its effect in a passage, L3 write an exam-style argued answer with evidence.

| Stage | Hebrew label | Goal | Target level (end) | Est. hours (estimate) |
|-------|--------------|------|--------------------|------------------------|
| 0 | אבחון | Reading baseline + one short written response | Place | 1 |
| 1 | כלי קריאה | Core terms: speaker/narrator, point of view, imagery, structure, conflict, theme | L2 | 8–12 |
| 2 | שירה | Poetry: 8 poems from the chosen cluster + unseen-poem skills | L3 | 20–30 |
| 3 | סיפור קצר | Short stories (Agnon + others) + unseen-story skills | L3 | 20–30 |
| 4 | רומן ונובלה | One novel or novella in depth | L3 | 14–20 |
| 5 | דרמה | One play + drama and tragedy basics | L3 | 14–20 |
| 6 | כתיבת תשובה | Answer structure: claim → quote → explanation; comparison answers | L3 | 6–10 |
| 7 | סימולציה | Timed full papers under the confirmed answer rules | L3 under time | 8–12 |

**Finish criteria (road):** two timed simulations at threshold; every genre stage ≥ L3 on its end check, including one **unseen** text each for poetry and short story.

## 4. Topics / tiles per stage

Kinds: `learn` (understanding), `practice` (review), `check`.

### Stage 1 — Reading tools
- learn: speaker vs poet; narrator types; figurative language (simile, metaphor, personification); rhythm and line breaks; plot, conflict, turning point
- practice: label a device in an original micro-text and state its effect in one sentence

### Stage 2 — Poetry
- learn: per poem — context (period), speaker, structure, key images, theme; per period — medieval conventions, Bialik, 20th–21st c, translated
- practice: "two poems in a pair" comparison tiles; unseen original poem drills
- check: one set-poem question + one unseen-poem question

### Stage 3 — Short story
- learn: per story — characters, narrator, time/space, symbol, ending
- practice: evidence hunt (find the line that supports a claim); unseen original story drills
- check: one set-story question + one unseen-story question

### Stage 4 — Novel / novella
- learn: plot map, character arcs, narrative technique, central ideas
- practice: chapter-recall cards; "trace a motif across three chapters"
- check: one 40-point-style essay (rules TODO)

### Stage 5 — Drama
- learn: exposition, conflict, climax, tragic hero, chorus/dialogue functions
- practice: scene-function questions; character motivation
- check: one essay-style question

### Stage 6 — Answer writing
- learn: claim–quote–explain paragraph; comparison frame; time budgeting per question
- practice: rewrite a weak paragraph into a strong one

### Stage 7 — Simulation
- Full timed papers; questions original; the set works referenced by title only

## 5. Finish criteria per stage

- End check ≥ **80%** of rubric at L3; no review topic at level 0.
- Each set work: recall tiles ≥ L2 (characters, events, key quotes **as references**, not copied text).
- Unseen-text checks passed on two different original texts per genre (poetry, short story).

## 6. Level-up rules (3 levels / stage)

| Level | Meaning | Up when | Down when |
|-------|---------|---------|-----------|
| L1 | Names device / recalls fact | Spaced successes | Fail streak / long gap |
| L2 | Explains effect in context | 2 sessions sustained on L2 pool | Fail L2 pool |
| L3 | Argued answer with evidence, rubric ≥ 80% | L3 check passed | Rubric < 60% twice → L2 practice |

Difficulty rises with longer passages, comparison questions, and unseen texts. Use `*_l1/_l2/_l3` suffixes.

## 7. Weekly progress and metrics

| Metric | Proposal | Events needed |
|--------|----------|---------------|
| Weekly progress vs goal | minutes + works covered + tiles levelled, on the road screen | `session_start`, `session_end`, `tile_complete`, `level_change` |
| Goals met / missed | per-week flag on the metrics screen | weekly rollup |
| Rubric trend | score per criterion (claim, evidence, explanation, language) | `writing_submit`, `rubric_score` |
| Coverage | set works with recall ≥ L2 / total | `tile_level` |
| Unseen-text readiness | unseen check scores | `check_attempt` |

## 8. Modes

- **Writing:** typed paragraph and essay answers with rubric feedback.
- **Recording:** learner explains a poem or scene aloud (2 minutes), then compares with a model outline.
- **Listening on:** narrated original micro-texts; audio summaries of plot (original wording).
- **Listening off:** all tasks available as text only.
- **Game:** "device detective" (spot the device in 5 lines against a timer); "who said it?" character cards built from original paraphrases; motif bingo for the novel.

## 9. Schema gaps (format owner)

1. Rubric-scored essay item (criteria + weights).
2. Reference-only tile for copyrighted works (title, edition, pages, no text body).
3. Unseen-text item with a long original passage shared across sub-questions.
4. Cluster selector (poetry cluster ב vs ז) at road start.
5. Audio-response item type.

## 10. ORIGINAL sample items (planning only)

Micro-texts below were written for this doc.

1. **Imagery (L1):** "העיר נרדמה על כתפי הגשם." Name the device and explain in one sentence what it suggests about the city.
2. **Speaker (L2):** In the original lines "אני אוסף את הבוקר בכפות ידיי / והוא נשפך לי בין האצבעות", what does the speaker feel about time? Support with one word from the lines.
3. **Narrator (L2):** Rewrite "ראיתי את אבי עומד ליד החלון" in a third-person narrator, and state one thing the reader loses.
4. **Drama (L2):** Why might a playwright open with a minor servant's dialogue before the main hero appears? Give two functions.
5. **Answer writing (L3):** Claim: "הסוף הפתוח מחזק את משמעות הסיפור." Write a claim–evidence–explanation paragraph about any short story you studied (evidence by reference, not long quotation).

## 11. Next steps

1. Confirm external-examinee outline, questionnaire code and answer rules with אגף הבחינות.
2. Extract the cluster ב and ז poem lists and the short-story / novel / drama work lists.
3. Check licensing for each set work; plan reference-only tiles.
4. Hand schema gaps to the format owner.
