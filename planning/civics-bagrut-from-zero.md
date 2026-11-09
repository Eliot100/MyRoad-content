---
status: planning
pathId: civics-bagrut-from-zero-adult
title: אזרחות (Civics) Bagrut from Zero — Adult
learner: Adult Israeli learners completing bagrut certificate (often required for full certification).
start: Near zero prior formal civics knowledge.
target: 2-unit civics bagrut (questionnaire codes — see "Review notes" below); strong foundation for optional 5-unit enrichment.
originality: All sample items original. No copy of MoE lists or existing MyRoad content.
---

# Civics / Citizenship (אזרחות) Bagrut from Zero (Adult)

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.

## Learner, start, target
- **Learner**: Adult in Israel finishing bagrut (common requirement for full certificate).
- **Start**: Zero / minimal formal knowledge of Israeli political system, rights, democracy principles.
- **Target**: 2-unit bagrut external exam + school performance task (per current MoE flexible pathway). Optional path toward 5-unit.
- **Originality note**: Sample items below are original sentences. Do not copy MoE concept lists or textbook wording.

## Public sources checked
- MoE pedagogical portal: [https://pop.education.gov.il/tchumey_daat/citizenship/citizenship-high-school/citizenship-pedagogy/curriculum](https://pop.education.gov.il/tchumey_daat/citizenship/citizenship-high-school/citizenship-pedagogy/curriculum) (HTTP 200)
- Bagrut exams page: [https://pop.education.gov.il/tchumey_daat/citizenship/citizenship-high-school/citizenship-pedagogy/bagrut-exam/](https://pop.education.gov.il/tchumey_daat/citizenship/citizenship-high-school/citizenship-pedagogy/bagrut-exam/) (HTTP 200)
- Circular PDF: [https://meyda.education.gov.il/files/Mazkirut_Pedagogit/ezrachut/mafmartashpav.pdf](https://meyda.education.gov.il/files/Mazkirut_Pedagogit/ezrachut/mafmartashpav.pdf) (retrieved)
- **Unverified / gap**: Full detailed topic list and exact hour allocations for current 2-unit external exam not fully extracted from public PDFs in this run. Outline thinned to high-level stages matching public descriptions (core principles, authorities, rights, Jewish-democratic state, clusters).

## Stages (estimate hours; label as estimate)

### Stage 1: Foundations — What is Citizenship & the State (estimate 12–18h)
- **Goal**: Understand citizen/state concepts, basic rights/duties, why civics matters.
- **Target level**: Recognition of core terms.
- **Topics/tiles**:
  - Understanding: Definition of citizen (legal status, belonging, participation); state characteristics.
  - Review: Simple identification of rights vs duties.
- **Finish criteria**: Can explain in own words 3 aspects of citizenship; identify 4 basic rights in short original scenarios.

### Stage 2: Democratic Principles (estimate 15–22h)
- **Goal**: Master core democratic values and mechanisms.
- **Topics/tiles**:
  - Understanding: Rule of law, majority rule + minority rights, separation of powers, limited government, tolerance/pluralism.
  - Review: Apply principle to short original case.
- **Finish criteria**: Match principle to original scenario; explain one tension (e.g., majority vs rights).

### Stage 3: Israeli Political System & Authorities (estimate 18–25h)
- **Goal**: Know structure of Knesset, government, courts, elections basics.
- **Topics/tiles**:
  - Understanding: Roles of legislative, executive, judicial; election principles.
  - Review: Map authority to function.
- **Finish criteria**: Describe primary role of each branch; identify who does what in original short description.

### Stage 4: Jewish & Democratic State + Clusters (estimate 12–18h)
- **Goal**: Navigate Israel as Jewish and democratic; touch one cluster (e.g., parties/elections or local authorities).
- **Topics/tiles**:
  - Understanding: Declaration of Independence principles, basic laws concept, selected cluster.
  - Review: Compare/contrast two positions on an issue.
- **Finish criteria**: Summarize 2–3 key features of Jewish-democratic framing; answer one cluster-style question.

### Stage 5: Exam Skills & Performance Task Prep (estimate 10–15h)
- **Goal**: Practice “ציין / הצג / הסבר” style and short argument.
- **Topics/tiles**: Review of all prior + original item practice.
- **Finish criteria**: Complete 5 original mixed items with correct structure.

## Level-up rules (3 levels per stage)
- Level 1: Recognition / definition.
- Level 2: Application to short original scenario.
- Level 3: Explanation / short argument linking concept to text or case.
- Spacing: Review prior stage tiles every 3–4 new tiles; spaced repetition on core terms.

## Metrics events needed
- `stage_started`, `tile_completed` (understanding/review), `level_up`, `item_correct`/`item_incorrect`, `stage_finished`, `exam_practice_score`.

## Schema gaps
- No specific gaps listed here. Do not invent schema changes. Content later maps to existing tile types (understanding, review, practice).

## 3 ORIGINAL sample items (early topics)
1. **Fill in the blank**: “In a democracy the government must follow the ______ even when a majority wants a different outcome.” (options: law / majority / party / media)  
2. **Application**: A local group wants to ban a public speech because they disagree with the speaker. Which democratic principle is most directly challenged? Explain in one sentence.  
3. **Short restatement**: “Citizens have both rights and duties.” Restate the main idea in different words.

## Review notes (bot review, 2026-11-09)

Checked against the MoE civics circular already cited above (`mafmartashpav.pdf`, HTTP 200, text extracted 2026-11-09):

- **Questionnaire codes (corrected).** The draft's `~34271` is the **old 70% outline**. For תשפ"ו the circular lists: grade-12 track 80% exam `34281` + 20% performance task `34283`; old outline 70% `34271`; new outline 35% / 35% / 30% with a 30% performance task `034263`. From תשפ"ז, exams have no מיקוד and no eased answer rules.
- **Adults / externals.** The circular says external examinees (אקסטרנים) and re-takers sit **two external exams**: `34281` (80%) plus `34282` (20%, no מיקוד). The school performance task does not apply to them. So Stage 5 for adult learners should prepare for `34282`, not a school task. Confirm with the exams department before building content.
- **Unverified:** all stage hour figures are estimates. Topic weights and the full core-topic and cluster list were not extracted from the official syllabus.
- **5 units:** the circular describes an optional הגבר (5-unit) extension. Out of scope for this outline.
- **Originality check:** sample items grepped against MyRoad-content and MyRoad (no matches).
