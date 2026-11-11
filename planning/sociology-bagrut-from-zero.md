---
status: planning
pathId: sociology-bagrut-from-zero-adult
title: Sociology (סוציולוגיה) Bagrut from Zero — Adult
learner: מבוגר ישראלי שממלא 2 יח"ל בסוציולוגיה כחלק ממקבץ מדעי החברה.
start: אפס מושגים סוציולוגיים.
target: 2 יח"ל סוציולוגיה, תוכנית חדשה (תשפ"ג לפי הטיוטה). שאלון 065261 / 65261 לפי הטיוטה — לא אומת, ראו "Review notes".
originality: Sample items original. Do not copy MoE lists or existing MyRoad wording.
---

# סוציולוגיה בגרות מאפס (מבוגר) (P17)

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.

## Learner, start, target
- **Learner**: מבוגר ישראלי שממלא 2 יח"ל בסוציולוגיה כחלק ממקבץ מדעי החברה.
- **Start**: אפס מושגים סוציולוגיים.
- **Target**: 2 יח"ל סוציולוגיה. לפי הטיוטה:
  - שאלון חיצוני 065261 / 65261 (**unverified** by the bot).
  - מבנה: חלק א — 1 מתוך 2 × 12 נק'; חלק ב — 4 סעיפים × 11 נק'; חלק ג — 4 סעיפים × 11 נק' (**unverified**).
  - תוכנית חדשה (תשפ"ג) (**unverified**).
  - הבחינה החיצונית 70% מהציון (**unverified**).
  - שאלון פנימי 065273 (**unverified**).
- **Originality**: פריטי הדוגמה מקוריים.

## Public sources checked
Sources listed by the Grok draft; the bot did **not** re-open them in this run.
- [pop — תוכנית הלימודים בסוציולוגיה](https://pop.education.gov.il/tchumey_daat/social-sciences/high-school/sociology-pedagogy/sociology-curriculum/)
- [pop — בחינות בגרות בסוציולוגיה](https://pop.education.gov.il/tchumey_daat/social-sciences/high-school/sociology-pedagogy/matriculation-exams/)
- [pop — תוכנית לימודים בסוציולוגיה, חטיבה עליונה (מבנה ועקרונות)](https://pop.education.gov.il/learning-plans/sociology/high-school/)

## Notes from the draft
- חלק ממקבץ 5 יח"ל מדעי החברה (יחד עם כלכלה / פסיכולוגיה / מדע המדינה + עבודת חקר). ראו גם [economics-bagrut-from-zero.md](./economics-bagrut-from-zero.md).
- נושאים: תרבות נעורים וצריכה, חיים משפחתיים, עולם העבודה וארגונים, גלובליזציה.

## Stages (estimate hours; label as estimate)

### Stage 1: תרבות וזהות (estimate 20–25h)
- **Goal**: תרבות נעורים, צריכה, זהות, גופמן, אתנוצנטריות.
- **Target level**: הסבר מושג + דוגמה ישראלית.
- **Topics/tiles**:
  - understanding: תרבות, זהות, הצגת העצמי (גופמן), אתנוצנטריות ויחסיות תרבותית.
  - understanding: תרבות צריכה, פנאי, רשתות חברתיות.
  - review: מושגי יסוד בסוציולוגיה.
- **Finish criteria**: 4 שאלות קצרות ב-75% ומעלה.
- **Level-up**: L1 = הגדרות; L2 = דוגמאות; L3 = השוואת גישות.

### Stage 2: משפחה, עבודה וגלובליזציה (estimate 25–30h)
- **Goal**: משפחה, ארגונים, גלובליזציה, אי-שוויון.
- **Target level**: ניתוח תופעה בעזרת 2 תיאוריות.
- **Topics/tiles**:
  - understanding: דפוסי משפחה, תיאוריות (פונקציונליסטית, פמיניסטית), ביורוקרטיה, תרבות ארגונית.
  - understanding: גלובליזציה, הגירה, שעתוק וניעות חברתית.
  - review: קישור בין הנושאים.
- **Finish criteria**: סימולציה חלקית (חלק א + ב) ב-70% ומעלה.
- **Level-up**: L1 = מושגים; L2 = יישום על מקרה; L3 = השוואה תיאורטית.

### Stage 3: אינטגרציה ובחינה (estimate 15–20h)
- **Goal**: שליטה במבנה השאלון (065261 לפי הטיוטה).
- **Target level**: מעבר 60% בסימולציה.
- **Topics/tiles**:
  - understanding: שאלות אינטגרטיביות, ניתוח מאמר / טקסט.
  - review: כל ארבעת הנושאים.
- **Finish criteria**: 2 סימולציות מלאות.
- **Level-up**: L1 = תשובות קצרות; L2 = תשובות מלאות; L3 = תשובות עם קישור למושגים מרובים.

## Finish criteria (road)
סימולציה מלאה ב-60% ומעלה, עם שימוש נכון במושגים.

## Level-up rules (3 levels per stage)
- עלייה אחרי 80%; חזרה לרמה קודמת אם פחות מ-60%.

## Metrics events needed
- `stage_start`, `tile_complete`, `concept_score`, `sim_exam_score`, `level_up`, `road_finish`.

## Schema gaps
- אין שדה למקבץ 5 יח"ל.
- אין הבחנה אוטומטית בין הערכה חיצונית לפנימית.
- אין מודל לעבודת חקר.

## 3 ORIGINAL sample items
1. הסבר את המושג "הצגת העצמי" של גופמן. תן דוגמה מהשימוש ברשת חברתית.
2. השווה בין משפחה מסורתית למשפחה פוסט-מודרנית לפי שני מאפיינים. תן דוגמה ישראלית.
3. מהי גלובליזציה? הסבר שני מאפיינים (דחיסת זמן-מרחב, תלות הדדית) ותן דוגמה אחת מעולם העבודה.

## Review notes (bot review, 2026-11-11)
- **Source**: SuperGrok Expert draft (chat bdc5a8ed, 2026-11-11), cleaned and split into files by a bot. The bot did not re-check the MoE pages in this run.
- **Unverified**:
  - External questionnaire code 065261 / 65261 and internal code 065273. The draft marks them verified on the MoE exams page, but the bot did not confirm them.
  - The paper structure (parts, points), the new-program year (תשפ"ג) and the 70% external weight.
  - Whether adult externals take this paper the same way as school students.
  - All hour figures are estimates.
- **Originality check**: sample items are original (Grok-written, not copied from MoE).
