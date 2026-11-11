---
status: planning
pathId: tanakh-bagrut-from-zero-adult
title: Tanakh / Bible (תנ"ך) Bagrut from Zero — Adult
learner: Adult Israeli learners with no formal Tanakh bagrut knowledge who need the compulsory 2-unit bagrut for a full certificate.
start: Basic Hebrew reading; little or no structured Bible study.
target: 2-unit תנ"ך ממלכתי bagrut (external exam; questionnaire code for adult externals unverified, see "Review notes").
originality: Sample items original. Do not copy MoE lists or existing MyRoad wording.
---

# Tanakh / Bible (תנ"ך) Bagrut from Zero (Adult)

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.

## Learner, start, target
- **Learner**: Adult finishing a full bagrut certificate.
- **Start**: Basic Hebrew reading; little or no structured Bible study.
- **Target**: 2-unit Tanakh (state track). The road covers the core narrative, historiography and thematic clusters of the public curriculum. School-assessment parts are noted where relevant; how adult externals are examined is **unverified**.
- **Originality**: Sample items are original.

## Public sources checked
- MoE content specification (high school): [https://pop.education.gov.il/learning-plans/bible/high-school/content/](https://pop.education.gov.il/learning-plans/bible/high-school/content/) (HTTP 200, 2026-11-11). Clusters: עלילות ראשית (creation stories, 15%, school assessment), patriarchs + Joseph (35%), formation of the nation / Exodus (35%), second school-assessment part (15%).
- Flexible bagrut program page: [https://pop.education.gov.il/tchumey_daat/tanach_mamlachti/chativa-elyona/pedagogy-state-bible-junior-high/flexible-program/](https://pop.education.gov.il/tchumey_daat/tanach_mamlachti/chativa-elyona/pedagogy-state-bible-junior-high/flexible-program/) (HTTP 200). New track: 35% external + 35% two controlled tasks + 30% alternative assessment.
- MoE circular for תשפ"ז (dated 01/07/26): [KOLEL2027.PDF](https://meyda.education.gov.il/files/Mazkirut_Pedagogit/tanach/tanach2027/KOLEL2027.PDF) (read 2026-11-11; see "Review notes").
- Related: [https://pop.education.gov.il/tchumey_daat/tanach_mamlachti/chativa-elyona/pedagogy-state-bible-junior-high/curriculum/](https://pop.education.gov.il/tchumey_daat/tanach_mamlachti/chativa-elyona/pedagogy-state-bible-junior-high/curriculum/)
- **Unverified / gaps**: the questionnaire code and format for adult externals (אקסטרניים), and the full chapter lists beyond the public summary. No codes were invented.

## Stages (estimate hours; label as estimate)

### Stage 1: Foundations and creation narratives (estimate 25–35h)
- **Goal**: Read and discuss the core Genesis creation and early-humanity stories; basic skills (locate, summarize, compare).
- **Target level**: Entry.
- **Topics/tiles**: Genesis 1–4, 9, 11 (selected); main ideas (the human in the image of God, responsibility, harmony vs. disorder). Kind: understanding.
- **Finish criteria**: Accurately summarize one creation narrative and identify 2 central ideas; locate verses in a provided text.

### Stage 2: Patriarchs and Joseph (estimate 30–40h)
- **Goal**: Analyze selected Abraham / Isaac / Jacob and Joseph stories (choice, family, divine plan).
- **Target level**: Intermediate.
- **Topics/tiles**: Selected chapters (Grok's draft list, unverified against the תשפ"ז מיקוד: Abraham 12, 15, 16, 18, 21–23; Isaac/Jacob 24, 27–29; Joseph 37–42, 44–45). Themes: barrenness, dreams, sibling rivalry, forgiveness. Kind: understanding + review.
- **Finish criteria**: Compare two characters on one theme (e.g. choice vs. plan); answer 3 open questions on provided excerpts.

### Stage 3: Formation of the nation (estimate 30–40h)
- **Goal**: Core Exodus selection plus thematic cross-cuts (leadership, belonging/foreignness), and one elective topic (נושא בחירה).
- **Target level**: Bagrut level.
- **Topics/tiles**: Selected Exodus chapters (Grok's draft: 2–3, 14, 19–20, 32–34; the תשפ"ז מיקוד appears to list 1–3, 12, 14, 19, 20, so 32–34 is **unverified**); leadership, covenant. Kind: understanding + practice.
- **Finish criteria**: Analyze one leadership episode and link it to an earlier theme; write a short comparison.

### Stage 4: Integrated review and mock (estimate 15–20h)
- **Goal**: Timed practice on mixed clusters, including an unseen passage (קטע להבנה ולניתוח).
- **Finish criteria**: Complete a full-style mock with ≥70% on content and skills sections (self-scored).

## Level-up rules (3 levels per stage)
- Level 1: Recognition / summary of a provided text.
- Level 2: Analysis of a theme or character in known chapters.
- Level 3: Transfer / comparison to a new but related excerpt.
- Advance on consistent Level 2 mastery.
- Spacing: review tiles every 4–7 days; mixed thematic retrieval at the end of each stage.

## Metrics events needed
- `tile_completed`, `stage_completed`, `mock_score`, `theme_identified`, `comparison_produced`.

## Schema gaps
- Scoring of open-ended analysis and comparison is not fully supported in the current schema. Flag for Content.
- No oral component assumed for adult externals.

## 3 ORIGINAL sample items
1. **Understanding**: קרא קטע מבראשית א' (בריאת האדם). מה הרעיון המרכזי לגבי מעמד האדם? (a) האדם דומה לבעלי חיים (b) האדם נברא בצלם אלוהים ויש לו אחריות (c) האדם נברא אחרון כי הוא חשוב פחות.
2. **Analysis**: בסיפור העקידה (בראשית כ"ב), איזה מתח מרכזי עולה בין ציווי אלוהי לבין קשר אב-בן? (accept a reasoned answer that names the conflict of values).
3. **Comparison**: השווה בין תגובת יוסף לאחיו בפרק מ"ה לבין תגובה אפשרית של דמות אחרת מסיפורי האבות לסיטואציית משבר משפחתי.

## Review notes (bot review, 2026-11-11)

- **Source**: SuperGrok Expert draft (chat f76ced5b, 2026-11-10), split and checked by a bot.
- **Confirmed** from MoE KOLEL2027.PDF (תשפ"ז circular): two tracks. Regular track (מתווה רגיל): one 70% external exam, questionnaire **1261** (four chapters: Genesis 48 pts, Exodus 24, elective topic 16, unseen passage 12), plus 2 × 15% school assessment (1263). Flexible track (מתווה גמיש): 35% external exam (1215 or 1225 depending on the topic split; 1214/1224 for new immigrants), 35% two controlled tasks (1211/1212 or 1221/1222), 30% school assessment. These are **school** codes.
- **Confirmed**: the Genesis focus (1, 2, 3, 4, 9, 11:1–9) matches Grok's Stage 1 list. The 15/35/35/15 cluster split matches the regular-track study plan.
- **Unverified**: the questionnaire code and exam format for adult externals (the circular does not name an externals' paper; do not assume 1261); the patriarch/Joseph and Exodus chapter lists (reconcile with the KOLEL2027 מיקוד table, which is hard to read in text form); all hour figures are estimates.
- **Originality check**: sample items are original (Grok-written, not copied from MoE).
