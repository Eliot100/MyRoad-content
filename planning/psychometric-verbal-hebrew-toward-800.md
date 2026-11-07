# Psychometric verbal (Hebrew) toward ~800 — road outline

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.

## 1. Learner, start, target

| Field | Definition |
|-------|------------|
| Learner | Adult preparing for the Israeli Psychometric Entrance Test (PET / פסיכומטרי), focusing on **Verbal Reasoning in Hebrew** (חשיבה מילולית) |
| Start | Functional Hebrew reader/writer who can follow news-level prose but struggles with academic register, analogies, dense inference, and timed essay structure |
| Target | Strong verbal-domain performance that **supports** a general PET score near the top of the published scale (**200–800**). Verbal alone cannot “guarantee 800” — quantitative also weighs in. Goal framing: **verbal toward 800-capable profile** |
| Content originality | All sample stems and practice prompts in this doc are **original**. Do **not** copy NITE practice-test items, MoE lists, or existing MyRoad English bagrut content into future JSON. |

Hebrew labels: חשיבה מילולית · מטלת כתיבה · אנלוגיות · הבנה והסקה · הבנת הנקרא · פסיכומטרי.

Companion planning doc: [psychometric-quant-toward-800.md](./psychometric-quant-toward-800.md).

## 2. Verified public sources (NITE)

Checked with `curl` (HTTP 200) on 2026-11-07 (Asia/Jerusalem):

| Source | URL | Status | What we take from it |
|--------|-----|--------|----------------------|
| NITE — Two-domain PET format (EN) | https://www.nite.org.il/two-domain-psychometric-entrance-test/format/?lang=en | 200 | From **December 2026 onwards**, paper-and-pencil PET has **six sections** in Verbal or Quantitative; **first section** is Verbal **writing task** (**30 min Hebrew** / **35 min other languages**); remaining five MC sections typically **20 minutes** each (may differ by version); of five MC sections, **two per domain** are scored (one MC section unscored); Verbal MC types named on page: **Analogies**, **Critical Reading and Inference**, **Text Comprehension** |
| NITE — Score calculation (EN) | https://www.nite.org.il/two-domain-psychometric-entrance-test/scores/calculation/?lang=en | 200 | Domain scores **50–150**; general scores **200–800**; writing task weighted **25%** of the verbal domain score; two-domain general score weights verbal and quantitative **equally**; verbal-oriented general score gives verbal **triple** the weight of quantitative |
| NITE verbal examples PDF (EN) | https://www.nite.org.il/files/psych/new_psych/verbal-eng.pdf | 200 | Confirms verbal skills description; writing task = essay on given topic; writing **25%** of Verbal Reasoning; academic-writing expectations; analogies / critical reading & inference (incl. sentence completions) / text comprehension described with worked-style guidance |

**Hebrew PDF check:** `https://www.nite.org.il/files/psych/new_psych/verbal.pdf` returned **404** on 2026-11-07 — do not cite it. Prefer the live format/scores pages + the EN examples PDF above.

### Format notes (do not blur)

- **Two-domain PET (Dec 2026 onwards):** Verbal + Quantitative; general score 200–800.
- **Writing time:** Format page says **30 min for Hebrew**, **35 min for other languages**. The EN verbal PDF sample instructions still show “35 minutes” and a **≥25 lines** essay rule — treat the PDF as a **guide/examples** document that may lag the two-domain Hebrew timing; **reconcile against the live format page + Hebrew examinee materials** before shipping timed sims. Mark exact line-count / timebox for Hebrew two-domain sims as **verify-before-implement**.
- **Unverified here:** exact MC question counts per verbal section for every language/version; exact raw→scaled conversion tables; any “X correct = 800” claim. Do **not** invent those.
- **About “800”:** top of NITE’s published general score scale. No percentile or admission cutoff verified in this pass.

## 3. Stages (שלבים)

3 levels per stage (L1 foundational accuracy → L2 mixed / denser prose → L3 full section pace with hard items). Hours are **estimates only** (not NITE figures).

| Stage | Focus | Goal | Est. hours (estimate) |
|-------|-------|------|------------------------|
| 0 | Placement + academic-Hebrew habits | Diagnose gaps; introduce PET verbal map | 2–4 |
| 1 | Academic vocabulary & morphology | Precise word meaning; roots/patterns useful for analogies | 10–16 |
| 2 | Analogies | Define precise semantic relations; avoid near-miss traps | 10–16 |
| 3 | Sentence logic / completions | Logical connectors; consistent completion under distractors | 8–14 |
| 4 | Critical reading & inference (short) | Arguments, assumptions, valid vs invalid conclusions | 10–16 |
| 5 | Text comprehension (long) | Structure, detail, inference, author stance | 12–20 |
| 6 | Academic writing task | Plan → draft ≥ required length; content + language rubrics | 12–20 |
| 7 | Mixed timed verbal sections | Full verbal-section simulations | 12–20 |
| 8 | Score-profile coaching | How verbal interacts with general 200–800 scales; writing 25% reminder | 3–6 |

**Road finish criteria:** Stage 7 end-checks meet threshold (see §5) on analogy-heavy, inference-heavy, and comprehension-heavy mixes; Stage 6 writing checklist passes human/product rubric at L2+; Stage 8 checklist completed. Language: “verbal ready to support a top-scale general score,” not “you will score 800.”

## 4. Topics / tiles (משבצות) per stage

Kinds: `learn` (**understanding**), `practice` (**review**), `check`, later worked-method / listen / write / game modes.

### Stage 0 — Map & habits
- What NITE verbal measures (reasoning + academic expression)
- Unscored-section reminder — treat every section seriously
- Pacing: mark vs grind; reading instructions inside the clock
- Sample habit check: “According to NITE’s two-domain format page, is the writing task part of Verbal or a third domain?”

### Stage 1 — Academic vocabulary (early topic — original samples)
Understanding + review tiles on precise synonyms, register, and root families **without** copying NITE lists.

**3 original Hebrew/bilingual practice prompts (planning only):**
1. בחר/י את המילה הקרובה ביותר במשמעות ל־«דקדקני» בהקשר אקדמי: (א) קפדני (ב) ממהר (ג) סתמי (ד) רועש — נמק/י מדוע שלוש האחרות נדחות.
2. Complete in Hebrew with the most precise academic connector: «הטענה אינה נשענת על נתונים; _____, אין לקבלה כמסקנה.» Options style: לפיכך / למרות זאת / למשל / כביכול — justify in one bilingual sentence.
3. Root awareness (original): «כתוב/י משפט אקדמי קצר עם השורש כ־ת־ב במשמעות של חיבור טקסט (לא העתקה), והחלף/י למילה נרדפת ברמת רישום גבוהה.»

### Stage 2 — Analogies (early topic — original samples)
- Relation types: part–whole, cause–effect, degree, function, contrast (teach as **strategies**, not a closed MoE/NITE taxonomy copy)
- Precision over loose association

**3 original prompts:**
1. נמל : דבש :: עץ : ? — הצע/י זוג יחס מדויק בעברית (למשל «תפוח» אם היחס הוא מקור→תוצר), ואז בנה/י מסיח קרוב־אבל־שגוי.
2. Bilingual stem: `LIBRARY : BOOK :: ARCHIVE : ?` — answer in Hebrew with the relation stated explicitly («מקום שמירה → פריט מאוחסן»).
3. «רמזור : תנועה :: … : מחלוקת» — בחר/י השלמה לוגית מקורית והסבר/י מדוע «שופט» חזק יותר מ־«רחוב».

### Stage 3 — Sentence completions / logic
- Connectors: cause, concession, contrast, exemplification
- Consistency across multiple blanks

### Stage 4 — Critical reading & inference
- Short argument paragraphs (original); identify assumption, strengthen/weaken, valid conclusion
- Distinguish fact vs opinion; contend with opposing view (aligns with NITE writing/critical framing)

### Stage 5 — Text comprehension
- Longer original passages (science / history / social science style — **original prose**, not exam copies)
- Detail, structure, inference, vocabulary-in-context

### Stage 6 — Writing task
- Academic register; thesis + support; paragraphing; avoid personal/emotional rant
- Practice to **≥ required line count** once Hebrew two-domain rules are confirmed
- Rubric practice mirroring NITE’s published axes (content & language; writing **25%** of verbal domain) — do not invent rater score cutoffs

### Stage 7 — Mixed timed
- Section-length mixes; ascending difficulty within type (per NITE note)
- Error log: vocab vs relation vs inference vs misread stem

### Stage 8 — Profile coaching
- Equal vs verbal-oriented general score weightings using **only** NITE’s published rules
- Reminder: writing is 25% of verbal domain — skipping essay practice caps the domain

## 5. Finish criteria per stage

- Stage check ≥ **80%** at the stage’s target level; no review topic left at level 0.
- Stages 1–5: leave with core tiles ≥ L2; stretch at L3.
- Stage 6: two timed essays meeting length + rubric floor (product-defined; not an invented NITE raw score).
- Stage 7: ≥ threshold on **two** timed mixed checks in a row (or 2 of last 3 — product choice).
- Never gate on an invented “raw score = 800” conversion.

## 6. Level-up rules (3 levels / stage)

| Level | Verbal meaning | Up | Down |
|-------|----------------|----|------|
| L1 | Untimed/gentle; single-skill items | Spaced successes | Fail streak / dormancy policy |
| L2 | Standard density; light time pressure | Sustained L1 + mixed sets | Fail mixed set |
| L3 | Hard items + full section pace; essay under clock | L2 stable + timed check | Miss timed check → L2 drill |

Tag error types: vocabulary, relation-definition, logic/inference, comprehension misread, writing structure, writing language.

Spacing: reuse MyRoad product defaults; mix short MC with periodic writing so level-up is not pure recognition.

## 7. Metrics

| Metric | Proposal | Events needed |
|--------|----------|---------------|
| Weekly progress vs goal | minutes and/or tiles leveled vs weekly goal | `session_start`, `session_end`, `level_change` |
| Accuracy by topic tag | correct/attempted | `answer_submit` + topic_id |
| Median time per item | latency percentiles | `answer_submit.latency_ms` |
| Writing rubric subscores | content / language (product rubric aligned to NITE axes) | `writing_attempt` |
| Timed-section comfort | Stage 7 check trend | `check_attempt` |
| Domain balance note | flag if quant neglected | optional link to quant road |

Honest empty state until real answers exist.

## 8. Schema gaps (format owner — do not invent schema)

1. **Timed writing** node with line-count / word-count constraints and draft scratch area.
2. **Rubric scoring** UI (two axes: content, language) — human and/or model-assisted; not a fake official NITE score.
3. **Analogy stem** layout (A:B :: C:? ) with RTL-safe Hebrew.
4. **Long passage** asset with accessibility text; multi-question group sharing one stem.
5. **Strict section timer** with unscored-section coaching copy.
6. Explicit `level` on tiles; subject tag `psychometric_verbal`.
7. Error taxonomy field on attempts.
8. Score explainer content blocks citing NITE weightings (not a live official equating converter).

## 9. Next steps (when leaving planning)

1. Confirm Hebrew two-domain writing **time + minimum length** from current NITE Hebrew examinee materials (PDF vs format-page reconciliation).
2. Decide path id series, e.g. `path_psych_verbal_he_01_…`.
3. Build generators for original analogy/inference distractors; store exemplars in DB per product decision.
4. Author JSON under `adult/` only after schema gaps are agreed — **never** under `planning/`.
