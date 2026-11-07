# YAEL Hebrew from zero — road outline

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.

## 1. Learner, start, target

| Field | Definition |
|-------|------------|
| Learner | Adult needing **Hebrew proficiency for Israeli higher education** (often after PET, or as a standalone requirement): olim, Arabic- or English-dominant speakers, returnees |
| Start | Near-zero to low intermediate Hebrew: can decode letters / basic phrases, or spoken survival Hebrew without academic reading/writing |
| Target | NITE **YAEL** (Hebrew Proficiency Test / בחינת יע״ל) readiness — and awareness of **YAELNET** (computerized variant) where the learner’s administration uses it |
| Content originality | All sample prompts below are **original**. Do not copy NITE YAEL items or MoE vocabulary lists. Do not reuse MyRoad English bagrut passage text. |

Hebrew labels: יע״ל · יעלנט · השלמת משפטים · ניסוח מחדש · הבנת הנקרא · מטלת כתיבה.

### Why YAEL (not CS bagrut5) as the third planning subject

Verified on 2026-11-07 (Asia/Jerusalem):

- **YAEL:** multiple NITE pages returned **HTTP 200** with concrete format, scoring, and examinee guidance (see §2).
- **CS 5-unit bagrut:** MoE deep links under guessed `computer-science` / `madey_hamachshev` paths **redirected to the MoE pop home** without usable curriculum body in this pass; `edu.gov.il` CS page returned **403**. Sources were too weak to outline a responsible MoE-aligned CS road without inventing figures.

Therefore this batch ships **YAEL**; CS bagrut5 remains a future research item once stable MoE CS curriculum URLs are confirmed.

## 2. Verified public sources (NITE)

Checked with `curl` (HTTP 200) on 2026-11-07 (Asia/Jerusalem):

| Source | URL | Status | What we take from it |
|--------|-----|--------|----------------------|
| NITE — YAEL format (EN) | https://www.nite.org.il/other-tests/yael/format/?lang=en | 200 | **Four sections**: three MC + one writing. Each of first three MC sections: **22 questions**, **20 minutes**, types **Sentence Completions**, **Restatements**, **Reading Comprehension** (vocab, grammar, syntax, reading). Same types grouped; ascending difficulty except RC (text order). Writing: **15 minutes**, essay on topic; well organized + correct Hebrew. Two of three MC sections scored; one unscored for quality control — treat all seriously. Format may change with advance notice on NITE site |
| NITE — YAEL scores (EN) | https://www.nite.org.il/other-tests/yael/scores/calculation/?lang=en | 200 | MC raw = number correct → scaled **50–150**; essay scored by **two** raters on **content, structure, richness of language, correctness of language** → scaled **50–150**; general YAEL = weighted average with MC **2/3** and essay **1/3**; final scale **50–150** |
| NITE — YAEL about | https://www.nite.org.il/other-tests/yael/about-the-test/?lang=en | 200 | ~1.5 hours; points to format page |
| NITE — Following the PET / during YAEL | https://www.nite.org.il/other-tests/yael/following-the-pet/?lang=en | 200 | Booklet+answer sheet logistics; essay **12–15 lines**; pencil; draft page not scored; copy assignment into allocated box |
| NITE — YAEL hub | https://www.nite.org.il/other-tests/yael/?lang=en | 200 | Entry hub (redirect target for several legacy paths) |
| NITE — YAELNET hub | https://www.nite.org.il/other-tests/yaelnet/?lang=en | 200 | Computerized Hebrew proficiency sibling — learners may sit YAELNET instead of paper YAEL; **reconcile section counts/timings from YAELNET-specific pages before building computer-sim modes** (do not assume paper YAEL numbers apply unchanged) |

**Unverified / do not invent:** university-specific minimum YAEL cutoffs; percentile tables; any claim that a given MyRoad accuracy maps to a 50–150 score; exact YAELNET MC section count/time without a dedicated YAELNET format citation in the implementation pass.

Third-party prep sites (e.g. commercial YAEL courses) were **not** used as authoritative structure sources.

## 3. Stages (שלבים)

3 levels per stage. Hours are **estimates only**.

| Stage | Focus | Goal | Est. hours (estimate) |
|-------|-------|------|------------------------|
| 0 | Script, sound–letter, survival | Decode print; basic present-tense needs | 20–40 |
| 1 | Core morphology & high-frequency vocab | Gender/number agreement; everyday→school lexicon | 25–45 |
| 2 | Sentence building & prepositions | Accurate simple/compound sentences | 20–35 |
| 3 | Sentence completions (YAEL type) | Grammar+vocab under 4-option distractors | 15–25 |
| 4 | Restatements (YAEL type) | Preserve meaning across syntactic paraphrase | 15–25 |
| 5 | Reading comprehension | Short→medium academic-lite texts + questions | 20–35 |
| 6 | Writing task (12–15 lines) | On-topic, organized, correct Hebrew under 15 min | 15–25 |
| 7 | Mixed timed YAEL sections | Full paper-YAEL-style simulations | 12–20 |
| 8 | Admin coaching | Unscored section, YAEL vs YAELNET, score axes 50–150 | 2–4 |

**Road finish criteria:** Stage 7 checks at threshold on completions, restatements, and RC mixes; Stage 6 writing meets length + rubric floor; Stage 8 checklist done. Language: “YAEL-ready practice profile,” not “you will score X.”

## 4. Topics / tiles per stage

Kinds: `learn` (understanding), `practice` (review), `check`; later listen / speak / write / game modes (MyRoad product already aims at multi-mode practice).

### Stage 0 — From zero script
- Print letters; niqqud optional fade-out; RTL habits
- Survival phrases → read simple notices
- Sample: “Match printed letter כ to its name; then read כֶּלֶב with and without vowels.”

### Stage 1 — Morphology & vocab (early topic — original samples)

**3 original Hebrew/bilingual practice prompts:**
1. השלם/י: «הסטודנטית כותבת את ה____.» (א) דו״ח (ב) דו״חות (ג) לדווח (ד) מדווח — נמק/י התאמת מין ומספר.
2. Bilingual: Pick the best Hebrew for “The library closes at eight.” — «הספרייה נסגרת בשמונה» vs near-miss word-order/gender errors; explain in English why gender on the verb matters.
3. Root family (original): מן השורש ל־מ־ד, כתוב/י שני משפטים: אחד על «תלמיד», ואחד על «למידה» בהקשר אוניברסיטאי קצר.

### Stage 2 — Sentence building (early topic — original samples)

**3 original prompts:**
1. סדר/י מחדש לעברית תקינה: «אתמול / בשוק / קניתי / ירקות / טריים» — ואז החלף/י לזמן הווה.
2. Preposition precision: «אני גרה ___ תל אביב אבל לומדת ___ האוניברסיטה.» (ב / בְ / ל / מ) — choose and justify.
3. Bilingual transformation: English “Because it rained, the trip was canceled.” → original Hebrew sentence with «משום ש…» (not a copied exam sentence).

### Stage 3 — Sentence completions (YAEL type)
- Verb conjugation, prepositions, connectors, agreement under distractors
- Ascending difficulty within sets (NITE pattern)

### Stage 4 — Restatements
- Same meaning, different syntax; reject subtle meaning shifts

### Stage 5 — Reading comprehension
- Original short texts (campus life, civic info, popular science — **original**)
- Local detail, pronoun reference, main idea, inference

### Stage 6 — Writing
- 12–15 lines (paper YAEL examinee guidance); 15 minutes
- Rubric practice on NITE’s four published axes: content, structure, richness, correctness
- Copy-prompt-into-box habit; pencil/draft discipline for paper sim; typed mode for YAELNET-oriented practice (**flag which mode**)

### Stage 7 — Mixed timed
- 22Q / 20 min section sims (paper YAEL numbers from format page)
- Error taxonomy: morphology / preposition / paraphrase drift / RC misread / writing off-topic

### Stage 8 — Coaching
- MC 2/3 + essay 1/3 weighting (NITE)
- Unscored MC section exists
- When to prefer YAELNET logistics — send learner to NITE YAELNET pages (do not invent differences)

## 5. Finish criteria per stage

- Stage check ≥ **80%** at target level; no review topic at level 0.
- Stages 3–5: core ≥ L2 before leaving.
- Stage 6: two timed essays in 12–15 line band, on-topic, rubric floor met.
- Stage 7: ≥ threshold on two mixed timed sections (or 2 of last 3).
- Never convert MyRoad % into a claimed YAEL 50–150 score.

## 6. Level-up rules (3 levels / stage)

| Level | Meaning | Up | Down |
|-------|---------|----|------|
| L1 | Slow, scaffolded Hebrew; glosses allowed | Spaced successes | Fail streak / dormancy |
| L2 | Standard YAEL-like items; light time | Mixed sets sustained | Fail mixed |
| L3 | Full section pace; harder RC + writing clock | L2 + timed check | Miss timed → L2 |

Spacing: product defaults; interleave reading and writing weekly so productive skills do not lag recognition.

## 7. Metrics

| Metric | Proposal | Events needed |
|--------|----------|---------------|
| Weekly progress vs goal | minutes / tiles leveled | session + `level_change` |
| Accuracy by YAEL skill tag | completions / restatements / RC | `answer_submit` |
| Writing rubric subscores | 4 axes | `writing_attempt` |
| Timed-section comfort | Stage 7 trend | `check_attempt` |
| Script fluency (early) | optional letter/decoding checks | placement / Stage 0 events |

Honest empty state until real answers exist.

## 8. Schema gaps (format owner)

1. **RTL Hebrew-first** authoring UX with optional bilingual gloss that does not leak on check tiles.
2. **Writing task** node: line guide (12–15), 15-minute timer, prompt-copy checkbox for paper-sim fidelity.
3. **Rubric capture** for four NITE axes (not a fake official score).
4. **Restatement** item layout (stem sentence + 4 paraphrases) with long-string RTL MC.
5. **Passage + question group** sharing one text.
6. **YAEL vs YAELNET mode** flag (timers/UI differ — confirm before implementing).
7. Explicit `level` on tiles; subject `yael_hebrew`.
8. Speech/listen modes for Stages 0–2 (product multi-mode learning) without claiming they are scored YAEL sections.

## 9. Next steps

1. Confirm YAELNET format deltas from NITE YAELNET-specific documentation.
2. Decide path id series, e.g. `path_yael_he_00_…`.
3. Build original item generators for completions/restatements; store exemplars in DB.
4. Author JSON under `adult/` only after schema agreement — **never** under `planning/`.
