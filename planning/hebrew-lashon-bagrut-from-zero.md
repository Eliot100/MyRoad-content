---
status: planning
pathId: hebrew-lashon-bagrut-from-zero-adult
title: עברית — הבנה, הבעה ולשון (Hebrew lashon) Bagrut from Zero — Adult external examinee
learner: Adult Israeli learner (external examinee / נבחן אקסטרני or re-taker) completing the compulsory Hebrew bagrut.
start: Fluent everyday Hebrew speaker with no formal grammar (לשון) since school, or never sat the exam. Not a Hebrew-as-second-language road (see YAEL outline).
target: Readiness for the 70% external questionnaire 11281 (עברית: הבנה, הבעה ולשון) plus the written 30% questionnaire that externals sit instead of a school grade (11282 — unverified, see section 2).
originality: All sample items original. Do not copy MoE exam texts, articles, or existing MyRoad wording.
---

# Hebrew lashon (עברית: הבנה, הבעה ולשון) Bagrut from Zero (Adult)

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.
> Distinct from [yael-hebrew-from-zero.md](./yael-hebrew-from-zero.md) (Hebrew as an additional language for YAEL) and from [psychometric-verbal-hebrew-toward-800.md](./psychometric-verbal-hebrew-toward-800.md) (PET verbal).

## 1. Learner, start, target

| Field | Definition |
|-------|------------|
| Learner | Adult in Israel finishing a bagrut certificate as an external examinee or re-taker. Hebrew is their working language. |
| Start | Reads and writes everyday Hebrew. Weak or no formal knowledge of morphology (שורש, בניין, משקל), syntax terms, number grammar, or source-based academic writing. |
| Target | Readiness for questionnaire **11281** (the 70% external paper) and the external 30% paper. Learning readiness only, not a promised grade. |
| Content originality | Sample items are **original**. Reading passages for practice must be written for MyRoad or clearly licensed — never copied from exam articles. |

Hebrew glossary: מקצוע → סדרה → דרך → שלב → משבצת.

## 2. Verified public sources (MoE)

Checked with `curl` + `pdftotext` on 2026-11-10 (Asia/Jerusalem):

| Source | URL | Status | What we take from it |
|--------|-----|--------|----------------------|
| MoE curriculum, עברית (הבנה, הבעה ולשון) grades 7–12, תשס"ג 2003 | https://meyda.education.gov.il/files/Curriculum/hebrew-7-12.pdf | 200 (PDF) | Four chapters: א מערכת הצורות, ב אוצר המילים והמשמעים, ג תחביר, ד הבנה והבעה. Suggested time split: each of א/ב/ג **15–20%**, ד **40–50%**. Under the "meaningful learning" reform one system (תחביר **or** צורות) is taught in depth for the 70% part and the other in reduced scope for the 30% part. Chapter ד includes text typology, reading, writing processes, summary, argument writing, writing from sources, Bible/Chazal texts, and oral texts. |
| Bagrut paper 11281, winter תשפ"ו 2026 | https://meyda.education.gov.il/sheeloney_bagrut/2026/1/HEB/11281.pdf | 200 (PDF) | Duration **3 hours**. Part 1 הבנה והבעה **50 pts**; Part 2 לשון **50 pts**: פרק א שם המספר ואותיות השימוש, then **choose one** of פרק ב תחביר / פרק ג מערכת הצורות. Allowed aid: דף עזר (נספח 2). Articles in נספח 1. Writing task: a **סקירה** (review) of **100–200 words** from named articles, with accepted quoting (דרכי מסירה) and bibliography (25 pts). Part 2: פרק א (numbers + prefixes) is **compulsory, 10 pts**; the chosen פרק ב or ג is **40 pts** (answer 4 of 5 questions, 10 pts each). |
| Bagrut paper 11281, summer תשפ"ו 2026 (moed 6) | https://meyda.education.gov.il/sheeloney_bagrut/2026/6/HEB/11281.pdf | 200 (PDF) | Same structure (3 hours, 50/50, review task 100–200 words, 25 pts). |
| Bagrut paper 11281, summer תשפ"ו 2026 moed ב (moed 8) | https://meyda.education.gov.il/sheeloney_bagrut/2026/8/HEB/11281.pdf | 200 (PDF) | Marked "בבחינה במועד זה יש הנחיות מיוחדות": **3.5 hours**, Part 1 **44 pts** (review task 22 pts), Part 2 **56 pts** (4 questions × 14 pts). Treat as a special-sitting variant, not the default. |
| MoE Hebrew מפמ"ר circular תשפ"ד | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/Ivrit/hozermafmaralyesodi2023_2024.pdf | 200 (PDF) | Questionnaire code table: **11281** 70% general; **11282** הבנה והבעה 30% (written); **11283** school 30% report code; **11271** lashon-only paper for מיזם הכתיבה schools; adapted/olim codes (11241, 11284, 11272 …). Re-takers sit without a school (מגן) grade. |

**Unverified / TODO**

- **Externals' exact pair.** The תשפ"ד code table appears to route "נבחני משנה ואקסטרניים" to written paper **11282** in place of the school code 11283, but the PDF table text is garbled after extraction. **TODO:** confirm in the current (תשפ"ו/תשפ"ז) Hebrew circular or with אגף הבחינות before building exam-sim content for 11282.
- Content scope (מפרט תכנים) of 11282 and which grammar topics are in the reduced 30% scope were **not** read in this pass.
- The 2003 curriculum is the framework document; the exam focus (מיקוד) per year may narrow topics. **TODO:** read the current מיקוד.
- All hour figures below are **estimates**, not MoE figures.

## 3. Stages (שלבים)

Level concept: **3 levels per stage** — L1 recognise/name, L2 apply in a new sentence or short text, L3 exam-style (explain, transform, justify).

| Stage | Hebrew label | Goal | Target level (end) | Est. hours (estimate) |
|-------|--------------|------|--------------------|------------------------|
| 0 | אבחון | Placement: reading, short writing sample, grammar baseline | Place into Stage 1 or 2 | 1–2 |
| 1 | קריאה והבנה | Text types, main idea, structure, connectives, writer's stance | L2 | 12–18 |
| 2 | כתיבה מן המקורות | סיכום, סקירה, טיעון; quoting rules and bibliography | L2–L3 | 16–24 |
| 3 | שם המספר ואותיות השימוש | Number grammar (gender, construct, ordinal), prefixes ו/ה/ב/כ/ל/מ/ש | L2 | 8–12 |
| 4A | תחביר (track A) | Parts of speech, sentence parts, sentence types, transformations | L2–L3 | 18–28 |
| 4B | מערכת הצורות (track B) | Root and pattern, בניינים, גזרות, משקלים, linear formation | L2–L3 | 18–28 |
| 5 | אוצר מילים ומשמעים | Register, connotation, polysemy, idioms — inside reading tasks | L2 | 6–10 |
| 6 | סימולציה | Timed 11281-style papers (plus 11282 when confirmed) | L3 under time | 10–16 |

**Track choice:** the learner picks **one** of 4A/4B, matching the exam's "choose one chapter" rule. The other track is optional enrichment, and may be needed for the 30% paper (TODO above).

**Finish criteria (road):** Stage 6 checks at threshold on two full timed papers; Stages 1–3, 5 and the chosen track ≥ target level.

## 4. Topics / tiles per stage

Kinds: `learn` (understanding, one-time), `practice` (review, returns), `check`.

### Stage 1 — Reading
- learn: text types (מידעי, טיעוני, סקירה); thesis vs support; connectives as logic markers
- practice: "what is the function of this paragraph?"; match connective to relation (ניגוד, סיבה, תוצאה)
- check: one original 400-word article, 6 items

### Stage 2 — Writing from sources
- learn: summary rules; review (סקירה) structure; direct vs indirect quoting (דרכי מסירה); in-text source mention + bibliography line
- practice: rewrite a quotation as indirect speech; merge two source sentences into one review sentence; trim a draft to 100–200 words
- check: original 2-article pack → a 100–200 word review, rubric-scored (content, organisation, language, source use)

### Stage 3 — Numbers and prefixes
- learn: number–noun gender agreement; construct forms (שלושת, שלוש־עשרה); ordinals; spelling prefixes with ה הידיעה
- practice: write numbers in words inside sentences (dates, money, quantities)
- check: 10 mixed items

### Stage 4A — Syntax
- learn: parts of speech; subject/predicate/copula; objects, adverbials, attributes, apposition; simple / compound / complex sentences; "חלקים כוללים"
- practice: tag underlined words; convert compound ↔ complex; identify the clause's role
- check: 4 questions in exam layout, 10 pts each

### Stage 4B — Morphology
- learn: root + pattern; seven בניינים and their meanings; common גזרות (חסרי פ"נ, נחי ל"י …); noun patterns; blends and acronyms
- practice: extract root and בניין from a bolded verb in context; build a noun in a given משקל
- check: 4 questions in exam layout

### Stage 5 — Vocabulary and meaning
- learn: register (משלב), connotation, metaphor vs literal, idioms from sources
- practice: replace a word with a higher-register synonym without changing meaning

### Stage 6 — Simulation
- Full timed papers built from original articles; 3 hours default; an optional 3.5-hour "special sitting" variant labelled as such
- Error log by chapter; formula-sheet discipline only with the official דף עזר (do not rewrite it)

## 5. Finish criteria per stage

- End-check ≥ **80%** at stage target level; no review topic stuck at level 0.
- Stage 2 writing: rubric ≥ 80% on two different source packs, word count within 100–200.
- Stage 4: the chosen track at L3 on two exam-layout checks.

## 6. Level-up rules (3 levels / stage)

| Level | Meaning | Up when | Down when |
|-------|---------|---------|-----------|
| L1 | Names the form or term | Spaced successes (product SRS) | Fail streak / long gap |
| L2 | Applies it in a new sentence or text | Harder pool sustained across 2 sessions | Fail L2 pool |
| L3 | Explains, transforms, and justifies as on the exam | L2 sustained + L3 check passed | Fail L3 → L2 practice |

Difficulty rises after sufficient progress: longer sentences, rarer גזרות, and source packs with conflicting claims. Use `*_l1/_l2/_l3` topic id suffixes (as in PR #45) rather than a new level field.

## 7. Weekly progress and metrics

| Metric | Proposal | Events needed |
|--------|----------|---------------|
| Weekly progress vs goal | minutes + tiles levelled vs the learner's weekly goal, on the road screen | `session_start`, `session_end`, `tile_complete`, `level_change` |
| Goals met / missed | per-week flag on the metrics screen | weekly rollup of the above |
| Accuracy by chapter | correct / attempted for numbers, syntax, morphology | `answer_submit` |
| Writing rubric trend | rubric score per criterion over time | `writing_submit`, `rubric_score` |
| Exam-sim readiness | Stage 6 scores by part | `check_attempt` |

Honest empty state until real answers exist.

## 8. Modes

- **Writing:** summaries and reviews typed in-app; word counter; rubric feedback.
- **Recording:** learner reads a paragraph aloud or explains a grammar choice orally (supports oral-text goals in chapter ד).
- **Listening on:** short audio passages (original) for main-idea items; TTS of grammar rules.
- **Listening off:** all items work silently with text only.
- **Game:** "root hunt" (find the shared root in 5 words against a timer); "number duel" (write the number in words fastest); connective matching cards.

## 9. Schema gaps (format owner)

1. Long-form writing item with word-count bounds and rubric scoring.
2. Source pack: 2–3 articles shared across several items.
3. Track selector (syntax vs morphology) inside one road.
4. Audio-response (recording) item type.
5. Tagging of underlined/bolded words inside a passage.

Do not invent schema fields here; hand these to the format owner.

## 10. ORIGINAL sample items (planning only)

1. **Numbers:** Write the number in words: "בטיול השתתפו (18) ________ מטיילות ו־(3) ________ מדריכים."
2. **Morphology:** In "המכונה **הופעלה** מחדש", give the root and the בניין, and write the same root in בניין פיעל, past tense, 3rd person feminine.
3. **Syntax:** Join into one complex sentence without changing the meaning: "הרכבת איחרה. העובדים הגיעו באיחור לישיבה."
4. **Writing from sources:** Turn into indirect speech with source mention: החוקרת אמרה: "רוב הקוראים מדלגים על ההערות."
5. **Reading:** In a paragraph that opens "אמנם קריאה דיגיטלית נוחה, אך…", what is the role of "אמנם … אך"?

## 11. Next steps

1. Confirm the externals' 30% paper (11282?) and its content scope in the current circular.
2. Read the current מיקוד and list the reduced-scope grammar topics.
3. Write an original article bank (10 packs) before any path JSON.
4. Hand schema gaps to the format owner.
