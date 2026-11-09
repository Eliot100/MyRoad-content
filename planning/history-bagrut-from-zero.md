---
status: planning
pathId: history-bagrut-from-zero-adult
title: History Bagrut from Zero — Adult (Israeli / general)
learner: Adult Israeli learners completing bagrut.
start: Near zero formal high-school history.
target: Standard bagrut history (typically 2–3 units; 70% external on core topics).
originality: Original sample items only.
---

# History Bagrut from Zero (Adult)

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.

## Learner, start, target
- **Learner**: Adult finishing bagrut certificate in Israel.
- **Start**: Minimal prior structured knowledge of modern Israeli/general history.
- **Target**: Bagrut history covering mandatory core (WWII, Holocaust, rise of State of Israel, selected modern topics). Exact unit count varies by track; outline follows public high-school structure descriptions.
- **Originality**: Sample items original.

## Public sources checked
- MoE history introduction: [https://pop.education.gov.il/learning-plans/history/high-school/introduction/](https://pop.education.gov.il/learning-plans/history/high-school/introduction/) (partial retrieval)
- Related pages on pop.education.gov.il for high-school history structure (70% mandatory base for bagrut, 30% school choice).
- **Unverified / gap**: Full current official syllabus PDF with exact topic list, hour counts, and questionnaire symbols not successfully extracted as complete public document returning full detail in this run. Outline uses only publicly described core themes (antisemitism, WWII, totalitarianism, Holocaust, from Yishuv to State of Israel). Thin stages; Content must verify against latest MoE materials before building.

## Stages (estimate hours; label as estimate)

### Stage 1: Chronological & Conceptual Foundations (estimate 10–15h)
- **Goal**: Basic timeline skills, primary/secondary sources idea, cause-effect.
- **Topics/tiles**:
  - Understanding: How historians use sources; simple timeline of 20th century Europe/Middle East.
  - Review: Order 5 key events.
- **Finish criteria**: Place 6 events on rough timeline; identify one cause-effect pair.

### Stage 2: Rise of Totalitarianism & WWII Europe (estimate 18–25h)
- **Goal**: Understand conditions leading to WWII and totalitarian regimes.
- **Topics/tiles**:
  - Understanding: Economic/political crises of 1920s–30s; key features of Nazi/Soviet systems (high level).
  - Review: Match regime feature to description.
- **Finish criteria**: Explain 2 factors that enabled rise of Nazi regime; outline main theaters of WWII.

### Stage 3: Holocaust & Antisemitism (estimate 15–22h)
- **Goal**: Core knowledge of antisemitism escalation and Holocaust events (as required in bagrut).
- **Topics/tiles**:
  - Understanding: Stages from discrimination to genocide; key locations/events at high level.
  - Review: Identify primary source type.
- **Finish criteria**: Summarize sequence of major stages; answer one “explain the significance” item.

### Stage 4: From Yishuv to State of Israel (estimate 18–25h)
- **Goal**: Zionist movement basics, British Mandate, 1948 war, early state challenges.
- **Topics/tiles**:
  - Understanding: Key milestones 1880s–1950s; immigration waves; independence war.
  - Review: Timeline of 1947–49.
- **Finish criteria**: Describe 3 major events leading to 1948; identify one internal/external challenge of early state.

### Stage 5: Synthesis & Exam Practice (estimate 12–18h)
- **Goal**: Connect themes; practice bagrut-style questions (source analysis, explanation).
- **Topics/tiles**: Review + original short source items.
- **Finish criteria**: Complete mixed set of 8 original items covering prior stages.

## Level-up rules (3 levels per stage)
- Level 1: Recall / place on timeline.
- Level 2: Explain cause or significance.
- Level 3: Analyze short original source or compare two events.
- Spacing: Spaced review of timeline tiles every stage; heavy review of Holocaust and 1948 after Stage 4.

## Metrics events needed
- `stage_started`, `tile_completed`, `level_up`, `source_item_correct`, `stage_finished`, `practice_set_score`.

## Schema gaps
- None proposed. Existing understanding/review/practice tiles sufficient. Source analysis may need future item type (list separately if required later).

## 3 ORIGINAL sample items
1. **Timeline**: Place in order: Declaration of Independence, UN partition plan, end of British Mandate.  
2. **Cause**: Give one economic or political reason why extremist movements gained support in Europe in the 1930s.  
3. **Short source**: “The new state faced both military threats and the need to absorb large numbers of immigrants.” What challenge does this sentence highlight? Explain in one sentence.

## Review notes (bot review, 2026-11-09)

- **Thin sources.** Only the MoE history introduction page was confirmed (HTTP 200, 2026-11-09). The "70% mandatory / 30% school choice" split, the "2–3 units" target, questionnaire codes and the exact core-topic list are **unverified**. Reconcile them with the current MoE history syllabus and the external-examinee (אקסטרני) exam pattern before any content JSON.
- **Unverified:** all stage hour figures are estimates.
- **Possible schema gap:** source-analysis items may need an item type of their own later. This is noted only and not proposed here.
- **Originality check:** sample items grepped against MyRoad-content and MyRoad (no matches).
