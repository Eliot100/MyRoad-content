---
status: planning
pathId: economics-bagrut-from-zero-adult
title: Economics (כלכלה) Bagrut from Zero — Adult
learner: מבוגר ישראלי שממלא 2 יח"ל בכלכלה כחלק ממקבץ מדעי החברה (או כמקצוע חיצוני).
start: אפס מושגים כלכליים.
target: 2 יח"ל כלכלה (בתוך מקבץ 5 יח"ל מדעי החברה). שאלון 063281 / 63281 לפי הטיוטה — לא אומת, ראו "Review notes".
originality: Sample items original. Do not copy MoE lists or existing MyRoad wording.
---

# כלכלה בגרות מאפס (מבוגר) (P16)

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.

## Learner, start, target
- **Learner**: מבוגר ישראלי שממלא 2 יח"ל בכלכלה כחלק ממקבץ מדעי החברה, או כמקצוע חיצוני.
- **Start**: אפס מושגים כלכליים.
- **Target**: 2 יח"ל כלכלה בתוך מקבץ 5 יח"ל מדעי החברה. לפי הטיוטה:
  - שאלון 063281 / 63281 (**unverified** by the bot).
  - מבנה: פרק א — 2 מתוך 4 שאלות × 27 נק'; פרק ב — 1 מתוך 2 × 24 נק' (ניתוח); פרק ג — 2 מתוך 6 × 11 נק' (**unverified**).
  - משך כ-2 שעות (**unverified**).
  - הבחינה החיצונית 70% מהציון (**unverified**).
- **Originality**: פריטי הדוגמה מקוריים.

## Public sources checked
Sources listed by the Grok draft; the bot did **not** re-open them in this run.
- [pop — מבנה הלימודים בכלכלה, חטיבה עליונה](https://pop.education.gov.il/learning-plans/economy/high-school/study-structure/)
- [pop — תוכנית הלימודים בכלכלה](https://pop.education.gov.il/tchumey_daat/social-sciences/high-school/pedagogy-of-social-sciences/economy-curriculum/)
- [pop — בחינות בגרות במדעי החברה](https://pop.education.gov.il/tchumey_daat/social-sciences/high-school/pedagogy-of-social-sciences/matriculation-exams/)

## Notes from the draft
- מינהל וכלכלה (מסלול מקצועי ישן יותר, שאלונים 839xxx) שונה: יותר ארגוני / ניהולי. הדרך הזו מיועדת לכלכלה במקבץ מדעי החברה, שלפי הטיוטה נפוצה יותר בהשלמת בגרות למבוגרים (**unverified**).
- מקבץ מלא דורש גם מקצוע שני ועבודת חקר (הערכה פנימית). לא מכוסה כאן.
- הטיוטה מציינת שלא נמצאו קודים חדשים מאומתים למינהל וכלכלה בדף הנוכחי.

## Stages (estimate hours; label as estimate)

### Stage 1: יסודות ומודל בסיסי (estimate 25–30h)
- **Goal**: מחסור, בחירה, עקומת תמורה, ביקוש והיצע.
- **Target level**: הסבר מילולי + שרטוט עקומות.
- **Topics/tiles**:
  - understanding: מחסור, בחירה ומחיר אלטרנטיבי, עקומת התמורה (גבול אפשרויות הייצור), תזוזות.
  - understanding: ביקוש והיצע, שיווי משקל, שינויים.
  - review: קריאת גרפים פשוטים.
- **Finish criteria**: 5 שאלות פתוחות מקוריות ב-75% ומעלה.
- **Level-up**: L1 = הגדרות; L2 = שרטוט + הסבר; L3 = ניתוח שינוי מדיניות.

### Stage 2: כשלי שוק, אי-שוויון ומאקרו (estimate 25–30h)
- **Goal**: כשלי שוק, אי-שוויון, מושגי מאקרו, תקציב, גלובליזציה.
- **Target level**: ניתוח אירוע ישראלי קצר.
- **Topics/tiles**:
  - understanding: כשלי שוק והתערבות ממשלתית, אי-שוויון ועוני, הון אנושי.
  - understanding: תוצר, אינפלציה, אבטלה, תקציב המדינה, גלובליזציה.
  - review: שילוב עקומות עם מדיניות.
- **Finish criteria**: סימולציה חלקית (פרק א + ב) ב-70% ומעלה.
- **Level-up**: L1 = מושגים; L2 = דוגמאות ישראליות; L3 = השוואת מדיניות.

### Stage 3: אינטגרציה ובחינה (estimate 15–20h)
- **Goal**: שליטה במבנה השאלון (063281 לפי הטיוטה) + נושאי בחירה בסיסיים.
- **Target level**: מעבר 60% בסימולציה מלאה.
- **Topics/tiles**:
  - understanding: שילוב בין נושאים, ניתוח מקרה (the draft's word here was garbled; "case analysis" is the bot's reading).
  - review: כל נושאי החובה.
- **Finish criteria**: 2 סימולציות מלאות.
- **Level-up**: L1 = תשובות קצרות; L2 = תשובות מלאות; L3 = תשובות עם קישור לתיאוריה.

## Finish criteria (road)
סימולציה מלאה ב-60% ומעלה, עם כיסוי של כל נושאי החובה.

## Level-up rules (3 levels per stage)
- עלייה אחרי 80%; חזרה לרמה קודמת אם פחות מ-60%.

## Metrics events needed
- `stage_start`, `tile_complete`, `essay_score`, `sim_exam_score`, `level_up`, `road_finish`.

## Schema gaps
- אין שדה למקבץ 5 יח"ל.
- אין הבחנה אוטומטית בין הערכה חיצונית לפנימית.
- אין מודל לעבודת חקר.

## 3 ORIGINAL sample items
1. הסבר מדוע עקומת התמורה קעורה כלפי הראשית. תן דוגמה ישראלית (חינוך מול תשתיות).
2. מחירי הדירות עלו. שרטט את השינוי בשוק הדירות (ביקוש / היצע) והסבר את השפעת מס הרכישה.
3. מהו כשל שוק של השפעה חיצונית שלילית? תן דוגמה של זיהום והצע התערבות ממשלתית אחת.

## Review notes (bot review, 2026-11-11)
- **Source**: SuperGrok Expert draft (chat bdc5a8ed, 2026-11-11), cleaned and split into files by a bot. The bot did not re-check the MoE pages in this run.
- **Unverified**:
  - Questionnaire code 063281 / 63281. The draft marks it verified on the social-sciences exams page, but the bot did not confirm it.
  - The paper structure (chapters, points), the ~2 h duration and the 70% external weight.
  - Whether adult externals take this paper the same way as school students.
  - All hour figures are estimates.
- **Originality check**: sample items are original (Grok-written, not copied from MoE).
