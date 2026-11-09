---
status: planning
pathId: psychometric-english-toward-800
title: Psychometric English (toward strong contribution / AMIRNET equivalent) — Adult
learner: Adult Israeli preparing for higher education.
start: Intermediate English (post bagrut5 or equivalent); distinct from existing MyRoad English bagrut5 roads 00–08.
target: High English domain / AMIRNET score that supports overall strong psychometric-related outcomes (user target ~800 general; note English is now separate).
originality: All sample items original. Do not copy NITE or existing MyRoad English wording.
---

# Psychometric English Section / AMIRNET toward Strong Score (Adult)

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.

## Learner, start, target
- **Learner**: Adult in Israel targeting higher education; needs strong English proficiency score.
- **Start**: After or parallel to English bagrut5; focuses on academic-style sentence completion, restatement, reading.
- **Target**: High performance on English domain (pre-Dec 2026) or AMIRNET (post-Dec 2026). User goal framed as strong contribution toward general ~800-range outcomes. English is being separated from PET as of Winter 2026; AMIRNET becomes the placement test.
- **Originality note**: Samples below are fully original. No copying of NITE examples or MyRoad English content.

## Public sources checked
- NITE format (legacy English domain): [https://www.nite.org.il/psychometric-entrance-test/format-5/?lang=en](https://www.nite.org.il/psychometric-entrance-test/format-5/?lang=en)
- Two-domain PET change & English separation: [https://www.nite.org.il/two-domain-psychometric-test/general-information/?lang=en](https://www.nite.org.il/two-domain-psychometric-test/general-information/?lang=en), [https://www.nite.org.il/news/notice-15022026/?lang=en](https://www.nite.org.il/news/notice-15022026/?lang=en)
- AMIRNET structure (sentence completion, restatement, reading comprehension; experimental listening/grammar later): NITE AMIRNET tips and format pages (HTTP 200).
- **Unverified / gap**: Exact current scoring tables, item counts that guarantee a specific contribution to an 800 general score, and full AMIRNET experimental weighting not invented. Outline focuses on the three core question types that remain stable.

## Stages (estimate hours; label as estimate)

### Stage 1: Sentence Completion — Vocabulary & Context (estimate 15–22h)
- **Goal**: Fast accurate completion using academic vocabulary and collocations.
- **Topics/tiles**:
  - Understanding: Common academic words, word families, context clues.
  - Review: Timed original completions.
- **Finish criteria**: 80%+ on 20 original sentence-completion items.

### Stage 2: Restatement — Precise Meaning (estimate 12–18h)
- **Goal**: Identify which restatement preserves the exact meaning.
- **Topics/tiles**:
  - Understanding: Paraphrase techniques, negation, modifiers.
  - Review: Compare original sentence to four options.
- **Finish criteria**: Correctly choose restatement on 15 original items.

### Stage 3: Reading Comprehension — Short Academic Texts (estimate 20–28h)
- **Goal**: Answer main-idea, detail, inference, vocabulary-in-context questions under time.
- **Topics/tiles**:
  - Understanding: Passage structure, question types.
  - Review: Full short passages (original).
- **Finish criteria**: Complete 4 original passages (5 questions each) with ≥75% accuracy.

### Stage 4: Mixed Timed Practice & Strategy (estimate 12–18h)
- **Goal**: Simulate section timing and mixed types.
- **Topics/tiles**: Review of all + strategy (skip, eliminate).
- **Finish criteria**: Full mixed set under approximate time constraints.

### Stage 5: High-Level Polish (estimate 10–15h)
- **Goal**: Harder items, trap recognition, consistency.
- **Topics/tiles**: Review + difficult original items.
- **Finish criteria**: Consistent high accuracy on harder mixed set.

## Level-up rules (3 levels per stage)
- Level 1: Untimed accuracy on basic items.
- Level 2: Timed with moderate difficulty.
- Level 3: Timed hard items + explanation of wrong choices.
- Spacing: Daily short review of prior-stage vocabulary/restatement; longer passages spaced.

## Metrics events needed
- `stage_started`, `tile_completed`, `item_correct`/`item_incorrect` (by type), `timed_set_score`, `level_up`, `stage_finished`.

## Schema gaps
- None proposed. Existing practice and review tiles cover the three question types. Timed mixed sets can use current mechanisms.

## 3 ORIGINAL sample items
1. **Sentence completion**: “The researchers’ findings were ______; further experiments produced almost identical results.” (options: preliminary / reproducible / contradictory / speculative)  
2. **Restatement**: “Although the new policy reduced costs, it also lowered employee satisfaction.” Which restatement is closest?  
   a) Costs fell and satisfaction rose.  
   b) The policy cut expenses but damaged morale.  
   c) Employees preferred the old policy because it cost more.  
   d) Satisfaction improved once costs were controlled.  
3. **Reading (short original)**:  
   “A small coastal town began measuring water quality after residents reported unusual algae. Early tests showed elevated nutrient levels near the river mouth. Officials later discovered that a nearby farm had changed its fertilizer schedule. Within two seasons the algae decreased.”  
   Question: What most directly explains the drop in algae? (options: new measurement tools / change in farm practice / increased tourism / colder weather)

## Review notes (bot review, 2026-11-09)

- **Target framing needs Eliot's call.** NITE's notice (https://www.nite.org.il/news/notice-081026/?lang=en, plus the two-domain FAQ) says that from the **winter (December) 2026** sitting the PET has only Verbal (50%) and Quantitative (50%). English is tested **only** in the separate computerized AMIRNET, which institutions use for English placement or exemption. So from Dec 2026 English does **not** feed the PET general (~800) score. This road should target AMIRNET placement/exemption, and the "toward 800" filename and title are kept only for continuity with the draft.
- **Unverified:** AMIRNET score scale, exemption thresholds, item counts and timing are not stated here. The cited `notice-15022026` and `format-5` URLs timed out from the review box and were not confirmed. The CHE rationale (adding listening, writing and speaking) suggests a later schema gap for listening/writing/speaking items, which is not proposed here.
- **Unverified:** all stage hour figures and percentage finish thresholds are planning estimates.
- **Originality check:** sample items grepped against MyRoad-content and MyRoad (no matches).
