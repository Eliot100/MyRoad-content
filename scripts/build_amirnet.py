"""Build adult/path_english_amirnet_01.json — full AMIRNET English road.

Expands the previous 60-minute starter into a full study road: vocabulary,
sentence completion, restatement, reading comprehension, review and mock stages.
All items are original (no NITE wording or official stems).

Official facts used here follow NITE pages and the 2026-11-11 fact check:
the 50–150 scale, a test of about 50 minutes, 7–8 sections, three current
question types, an adaptive format, a 35-day retake wait, and 7-year validity
are treated as confirmed. Item counts, per-section timing, and institutional
cutoffs (including any exemption threshold) are marked unverified.

The path field estimated_minutes is capped at 1200 by the MyRoad schema
(20 hours). Realistic mastery time is longer; see the PR description.

Run: python scripts/build_amirnet.py
"""
from __future__ import annotations

import json
from pathlib import Path

P = "am"


def mc(nid, typ, title, body, content, choices, correct, ok, why, method, hint, can_do,
       kind="understanding", review=None):
    n = {
        "id": f"{P}_{nid}",
        "type": typ,
        "kind": kind,
        "title": title,
        "body_he": body,
        "body_content": content,
        "choices": [],
        "correct": correct,
        "feedback_ok": ok,
        "feedback_try": why,
        "can_do": can_do,
        "worked_method": method,
        "hint": hint,
    }
    for cid, label, fb in choices:
        c = {"id": cid, "label": label}
        if fb:
            c["feedback"] = fb
        n["choices"].append(c)
    if review:
        n["review_topic_ids"] = review
    return n


def learn(nid, title, body, content, can_do):
    return {
        "id": f"{P}_{nid}",
        "type": "learn",
        "kind": "understanding",
        "title": title,
        "body_he": body,
        "body_content": content,
        "can_do": can_do,
    }


nodes: list[dict] = []
topics: list[dict] = []


def topic(tid, he, en, emoji, items, kind=None, review_ids=None):
    if kind or review_ids:
        stamped = []
        for n in items:
            n = dict(n)
            if kind:
                n["kind"] = kind
            if review_ids:
                n["review_topic_ids"] = list(review_ids)
            stamped.append(n)
        items = stamped
    topics.append({
        "id": tid,
        "titles": {"he": he, "en": en},
        "emoji": emoji,
        "node_ids": [n["id"] for n in items],
    })
    nodes.extend(items)


# ---------------------------------------------------------------------------
# 1. What AMIRNET is
# ---------------------------------------------------------------------------
topic("t_about", "מה זה אמירנט", "What AMIRNET is", "🧭", [
    learn(
        "about_learn",
        "אמירנט ולא פסיכומטרי",
        "מדצמבר 2026 אנגלית כבר לא חלק מהבחינה הפסיכומטרית. את רמת האנגלית לאקדמיה בודקים "
        "במבחן נפרד של מאל\"ו (NITE): אמירנט. זה מבחן ממוחשב ומסתגל, שאורך כ-50 דקות, עם "
        "שבעה עד שמונה פרקים. שלושת סוגי השאלות היום הם השלמת משפטים, "
        "ניסוח מחדש והבנת הנקרא. הציון בסולם 50–150, והוא שקול לפי מאל\"ו לציוני האנגלית "
        "הישנים (פסיכומטרי / אמיר / אמיר\"ם). כל מוסד קובע לבד מאיזה ציון יש פטור ואיך "
        "משבצים לרמה; ספי הפטור והשיבוץ לא מפורסמים ככלל אחיד של מאל\"ו (לא אומת כאן סף "
        "מספרי). מספר הפריטים בכל פרק וזמן מדויק לכל סוג שאלה גם הם לא אומתו. אפשר לגשת "
        "שוב אחרי המתנה של 35 יום, והציון תקף שבע שנים. ההרשמה נפרדת מהפסיכומטרי.",
        "AMIRNET: Sentence Completion, Restatement, Reading Comprehension. Scale 50–150. Official duration about 50 minutes. Item counts, per-section timing, and institutional cutoffs are unverified here.",
        "להבין מה אמירנט בודק ולמה הוא נפרד מהפסיכומטרי",
    ),
    mc(
        "about_types", "check", "שלושה סוגי שאלות",
        "איזה סוג שאלה לא מופיע היום באמירנט?",
        "AMIRNET question types today",
        [
            ("a", "Listening to a recorded lecture", None),
            ("b", "Sentence Completion", "השלמת משפטים היא אחד משלושת הסוגים של היום."),
            ("c", "Restatement", "ניסוח מחדש הוא אחד משלושת הסוגים של היום."),
            ("d", "Reading Comprehension", "הבנת הנקרא היא אחד משלושת הסוגים של היום."),
        ],
        "a",
        "נכון. האזנה עוד לא במבחן. מאל\"ו הודיעו שהיא תתווסף בשלבים מ-2027.",
        "היום יש שלושה סוגים: השלמת משפטים, ניסוח מחדש והבנת הנקרא. האזנה תתווסף רק בהמשך.",
        "כתבו את שלושת הסוגים של היום.\nבדקו כל תשובה מול הרשימה.\nמה שלא ברשימה הוא התשובה.",
        "שלושה סוגים מופיעים ברשימה של היום. אחד לא.",
        "לזהות את סוגי השאלות במבחן",
    ),
    mc(
        "about_rules", "check", "כללי ציון וניחוש",
        "מה נכון לפי כללי המבחן שאומתו?",
        "AMIRNET scoring rules",
        [
            ("a", "A blank answer is scored as wrong, so a guess is better than leaving it empty.", None),
            ("b", "Every university uses the same exemption cutoff of 134.", "סף הפטור נקבע בכל מוסד בנפרד, ולא אומת כאן ככלל אחיד של מאל\"ו."),
            ("c", "You may go back to any earlier section after you finish it.", "אפשר לחזור רק בתוך אותו פרק, לא לפרקים קודמים."),
            ("d", "The test has no time limit.", "המבחן כולו אורך כ-50 דקות."),
        ],
        "a",
        "נכון. תשובה חסרה נספרת כטעות, לכן עדיף לנחש מאשר להשאיר ריק.",
        "סף 134 הוא דוגמה מוסדית ולא כלל של מאל\"ו (לא אומת). אי אפשר לחזור לפרק קודם. יש מגבלת זמן.",
        "פסלו טענות על סף אחיד, על חזרה בין פרקים, ועל היעדר זמן.\nנשאר הכלל: תשובה חסרה = טעות.",
        "מה קורה אם לא עונים על שאלה?",
        "לדעת את כללי הניחוש והזמן",
    ),
])

# ---------------------------------------------------------------------------
# 2. Academic vocabulary
# ---------------------------------------------------------------------------
topic("t_vocab", "אוצר מילים אקדמי", "Academic vocabulary", "📚", [
    learn(
        "vocab_learn",
        "מילים בהקשר, לא ברשימה",
        "באמירנט אוצר המילים נבדק בעיקר בתוך משפט או קטע, לא ברשימת הגדרות. כדאי לבנות מאגר "
        "של מילים אקדמיות שכיחות (analyze, evidence, significant, method, obtain, establish, "
        "contribute, affect) ולתרגל אותן במשפט. שימו לב לחלק הדיבר: אותו שורש יכול להיות שם "
        "עצם או פועל (analysis / analyze, effect / affect). כשנתקלים במילה לא מוכרת, חפשו "
        "רמז במשפט: ניגוד, דוגמה, או הסבר אחרי פסיק או נקודה-פסיק. זמן הלימוד המומלץ לשלב "
        "הזה הוא הערכה בלבד: כמה שעות של חזרה מחודדת, לא נתון רשמי.",
        "analyze, evidence, significant, method, obtain, establish, contribute, affect / effect.",
        "לזהות מילה אקדמית לפי הקשר במשפט",
    ),
    mc("vocab_p1", "practice", "ראיה ולא ניחוש",
       "איזו מילה מתאימה ביותר למשפט?",
       "The claim is weak because the authors provide almost no ______ to support it.",
       [("a", "evidence", None),
        ("b", "decoration", "קישוט לא תומך בטענה."),
        ("c", "schedule", "לוח זמנים לא קשור לחיזוק טענה."),
        ("d", "audience", "קהל לא ממלא את החסר אחרי provide.")],
       "a", "נכון. evidence = ראיות. בלי ראיות הטענה חלשה.",
       "הטענה חלשה כי אין תמיכה. המילה שמסמנת תמיכה עובדתית היא evidence.",
       "שאלו: מה חסר כדי לתמוך בטענה?\nראיות.\nהתשובה: evidence.",
       "מה תומך בטענה במחקר?", "לבחור מילה אקדמית לפי הקשר"),
    mc("vocab_p2", "practice", "השפעה ולא תוצאה",
       "איזו מילה מתאימה ביותר למשפט?",
       "Lack of sleep can ______ a student's ability to concentrate in the morning.",
       [("a", "affect", None),
        ("b", "effect", "effect הוא בדרך כלל שם עצם. כאן דרוש פועל."),
        ("c", "accept", "לקבל לא מתאים ליכולת ריכוז."),
        ("d", "except", "מילת יוצא מן הכלל, לא פועל כאן.")],
       "a", "נכון. כאן דרוש פועל: affect = להשפיע. effect הוא בדרך כלל שם עצם.",
       "אחרי can בא פועל. Lack of sleep משפיע על היכולת. לכן affect, לא effect.",
       "בדקו את חלק הדיבר: אחרי can בא פועל.\neffect הוא שם עצם.\nהפועל הוא affect.",
       "איזה חלק דיבר חסר במשפט?", "להבחין בין affect ל-effect"),
    mc("vocab_p3", "practice", "לזהות גורמים",
       "איזו מילה מתאימה ביותר למשפט?",
       "The team tried to ______ the main factors behind the rise in prices.",
       [("a", "identify", None),
        ("b", "ignore", "להתעלם סותר את tried to, שמסמן מאמץ להבין."),
        ("c", "invent", "להמציא גורמים זה לא מטרת צוות מחקר."),
        ("d", "delay", "לדחות לא מתאים לגורמים מאחורי עלייה.")],
       "a", "נכון. identify = לזהות. הצוות ניסה לברר מה הגורמים.",
       "tried to + גורמים מאחורי תופעה = ניסיון לזהות אותם. התשובה identify.",
       "מה עושים ל-factors כדי להבין עליית מחירים?\nמזהים אותם.\nהתשובה: identify.",
       "מה המטרה של הצוות במשפט?", "לבחור פועל אקדמי שמתאים למטרה"),
    mc("vocab_p4", "practice", "סקירה מקיפה",
       "איזו מילה מתאימה ביותר למשפט?",
       "The chapter offers a ______ survey of recent work on memory, covering both laboratory and classroom studies.",
       [("a", "comprehensive", None),
        ("b", "narrow", "צר סותר את covering both..."),
        ("c", "temporary", "זמני לא מתאר היקף סקירה."),
        ("d", "silent", "לא קשור לסקירת מחקרים.")],
       "a", "נכון. comprehensive = מקיף, וזה מתאים לכיסוי של שני סוגי מחקרים.",
       "covering both מסביר שהסקירה רחבה. המילה היא comprehensive.",
       "מצאו את ההסבר אחרי הפסיק: שני סוגי מחקרים.\nזה היקף רחב.\nהתשובה: comprehensive.",
       "מה אומר החלק covering both...?", "להשלים תואר לפי היקף"),
    mc("vocab_p5", "practice", "לתרום ולא למנוע",
       "איזו מילה מתאימה ביותר למשפט?",
       "Regular practice can ______ to better performance on timed reading tasks.",
       [("a", "contribute", None),
        ("b", "prevent", "למנוע הצלחה סותר את better performance."),
        ("c", "refuse", "לסרב לא מתאים אחרי can ______ to."),
        ("d", "borrow", "לשאול לא מתאים לשיפור בביצוע.")],
       "a", "נכון. contribute to = לתרום ל. תרגול תורם לביצוע טוב יותר.",
       "המבנה can ______ to + שיפור דורש contribute. prevent היה הופך את הכיוון.",
       "שימו לב למילת היחס to אחרי החסר.\ncontribute to הוא צירוף קבוע.\nהתשובה: contribute.",
       "איזה פועל מגיע עם to במשמעות של תרומה?", "לזהות צירוף אקדמי contribute to"),
    mc("vocab_p6", "practice", "לבסס ממצא",
       "איזו מילה מתאימה ביותר למשפט?",
       "Further tests helped the lab ______ that the first result was not an accident.",
       [("a", "establish", None),
        ("b", "abandon", "לנטוש את הממצא סותר את further tests."),
        ("c", "conceal", "להסתיר לא מתאים למעבדה שבודקת שוב."),
        ("d", "postpone", "לדחות לא מסביר שהתוצאה אינה מקרית.")],
       "a", "נכון. establish = לבסס, לקבוע. בדיקות נוספות ביססו את התוצאה.",
       "בדיקות נוספות נועדו להראות שהתוצאה יציבה. הפועל הוא establish.",
       "מה עושות בדיקות נוספות לתוצאה ראשונה?\nמבססות אותה.\nהתשובה: establish.",
       "מה המטרה של further tests?", "לבחור פועל שמבסס תוצאה"),
    mc("vocab_chk", "check", "שיטה ולא ניחוש",
       "איזו מילה מתאימה ביותר למשפט?",
       "The paper describes a new ______ for measuring attention in young children.",
       [("a", "method", None),
        ("b", "melody", "לחן לא מודד קשב."),
        ("c", "furniture", "רהיטים לא מתאימים למדידה במאמר."),
        ("d", "holiday", "חג לא מתאר כלי מדידה.")],
       "a", "נכון. method = שיטה. המאמר מתאר שיטה חדשה למדידה.",
       "for measuring מסמן כלי או שיטת מדידה. המילה האקדמית היא method.",
       "החסר בא לפני for measuring.\nמה מתארים במאמר מדעי כדי למדוד?\nשיטה. התשובה: method.",
       "מה מתאר מאמר כשהוא מסביר איך מודדים?", "לבחור שם עצם אקדמי בהקשר מחקרי"),
])

# ---------------------------------------------------------------------------
# 3–5. Sentence completion
# ---------------------------------------------------------------------------
topic("t_sc_basic", "השלמת משפטים: בסיס", "Sentence completion: basics", "🧩", [
    learn(
        "sc1_learn",
        "קודם המשפט, אחר כך התשובות",
        "בהשלמת משפטים מופיע משפט עם חסר, וארבע אפשרויות. קראו קודם את כל המשפט ונחשו מילה "
        "משלכם, ורק אחר כך הסתכלו על התשובות. ברמה הבסיסית מחפשים התאמה פשוטה של משמעות: "
        "מילת סיבה ממשיכה כיוון, מילת ניגוד הופכת כיוון, ונקודה-פסיק או שני משפטים קרובים "
        "לעיתים מסבירים זה את זה. פסלו מילה שמתאימה רק לחלק מהמשפט. זמן ממוצע לשאלה במבחן "
        "לא אומת כאן; בתרגול עבדו בלי לחץ בהתחלה, ואחר כך קצבו את עצמכם.",
        "although = contrast · because / so = cause · ; = explanation",
        "למצוא רמז במשפט לפני שבוחרים מילה",
    ),
    mc("sc1_p1", "practice", "תוצאות שחוזרות",
       "בחרו את המילה שמשלימה את המשפט.",
       "The researchers' findings were ______; further experiments produced almost identical results.",
       [("a", "reproducible", None),
        ("b", "contradictory", "סותרות לא מתאים: הניסויים הבאים נתנו אותן תוצאות."),
        ("c", "speculative", "השערה בלבד לא מתאים לתוצאות שחזרו."),
        ("d", "forgotten", "שכוחות לא מסבירות תוצאות זהות בניסוי הבא.")],
       "a", "נכון. reproducible = אפשר לחזור עליהן ולקבל אותו דבר.",
       "החלק אחרי ה-; מסביר: ניסויים נוספים נתנו כמעט אותן תוצאות. לכן reproducible.",
       "מצאו את ההסבר אחרי ה-;.\nהוא אומר שהתוצאות חזרו.\nהתשובה: reproducible.",
       "מה קרה בניסויים הנוספים?", "להשלים מילה לפי הסבר במשפט"),
    mc("sc1_p2", "practice", "מילת ניגוד",
       "בחרו את המילה שמשלימה את המשפט.",
       "Although the bridge looked ______, engineers found serious cracks inside it.",
       [("a", "solid", None),
        ("b", "damaged", "although מסמנת ניגוד. אם הגשר נראה פגוע, אין ניגוד לסדקים."),
        ("c", "fragile", "fragile בכיוון של הסדקים, ו-although דורשת כיוון הפוך."),
        ("d", "unfinished", "לא גמור לא מנוגד לסדקים בפנים.")],
       "a", "נכון. although מסמנת ניגוד: נראה יציב, אבל היו סדקים.",
       "although הופכת כיוון. בחלק השני יש סדקים, לכן בראשון הגשר נראה solid.",
       "סמנו את although = ניגוד.\nהחלק השני: סדקים.\nההפך: נראה יציב. התשובה: solid.",
       "although מסמנת ניגוד בין שני חלקי המשפט.", "להשתמש במילת ניגוד כדי לבחור מילה"),
    mc("sc1_p3", "practice", "דחייה זמנית",
       "בחרו את המילה שמשלימה את המשפט.",
       "Due to technical problems, the conference was ______ until next month.",
       [("a", "postponed", None),
        ("b", "canceled permanently", "until next month מראה שזו דחייה, לא ביטול סופי."),
        ("c", "expanded", "הרחבה לא נובעת מתקלות טכניות."),
        ("d", "completed", "הושלמה סותר את until next month.")],
       "a", "נכון. postponed = נדחה. until next month מציין דחייה זמנית.",
       "Due to מסביר סיבה, ו-until next month אומר שהאירוע יקרה מאוחר יותר. לכן postponed.",
       "סמנו until next month.\nזה דחייה, לא ביטול.\nהתשובה: postponed.",
       "מה אומר until next month?", "להשלים לפי רמז של זמן"),
    mc("sc1_p4", "practice", "להגיש דוח",
       "בחרו את המילה שמשלימה את המשפט.",
       "Students who join the program must ______ a short report at the end of the term.",
       [("a", "submit", None),
        ("b", "receive", "לקבל דוח לא מתאים לחובת הסטודנטים."),
        ("c", "ignore", "להתעלם סותר את must."),
        ("d", "postpone forever", "לדחות לעד סותר את at the end of the term.")],
       "a", "נכון. submit = להגיש. זו דרישה בסוף הסמסטר.",
       "must + דוח בסוף התקופה = חובה להגיש. הפועל הוא submit.",
       "מי חייב לעשות משהו לדוח?\nהסטודנטים.\nהם מגישים אותו. התשובה: submit.",
       "מה עושים עם דוח בסוף קורס?", "להשלים פועל שמתאים לחובה"),
    mc("sc1_p5", "practice", "תור ארוך",
       "בחרו את המילה שמשלימה את המשפט.",
       "The museum's new exhibit was so ______ that visitors waited in line for hours.",
       [("a", "popular", None),
        ("b", "obscure", "אם התערוכה לא מוכרת, לא היו תורים."),
        ("c", "brief", "קצרה לא מסבירה המתנה של שעות."),
        ("d", "empty", "ריקה סותרת תורים ארוכים.")],
       "a", "נכון. so ... that מחבר סיבה לתוצאה: פופולרית, ולכן התורים.",
       "התוצאה אחרי that היא המתנה ארוכה. הסיבה שמתאימה: popular.",
       "מצאו את התוצאה אחרי that.\nמה גורם לתורים? תערוכה מבוקשת.\nהתשובה: popular.",
       "so ... that: מה גרם לתורים?", "להשלים לפי תוצאה במשפט"),
    mc("sc1_chk", "check", "מילת סיבה",
       "בחרו את המילה שמשלימה את המשפט.",
       "Because the instructions were so ______, almost every student completed the task without help.",
       [("a", "clear", None),
        ("b", "vague", "אם ההוראות לא ברורות, היו צריכים עזרה."),
        ("c", "lengthy", "ארוכות לא מסבירות הצלחה בלי עזרה."),
        ("d", "hidden", "מוסתרות סותרות הצלחה עצמאית.")],
       "a", "נכון. because מחברת סיבה ותוצאה: הוראות ברורות, ולכן הצליחו לבד.",
       "התוצאה: כמעט כולם הצליחו בלי עזרה. הסיבה המתאימה: ההוראות היו clear.",
       "מצאו את התוצאה: הצליחו בלי עזרה.\nמה גורם לזה? הוראות ברורות.\nהתשובה: clear.",
       "because: החלק הראשון הוא הסיבה לחלק השני.", "להשתמש במילת סיבה כדי לבחור מילה"),
])

topic("t_sc_mid", "השלמת משפטים: רמזים דקדוקיים", "Sentence completion: grammar cues", "🔤", [
    learn(
        "sc2_learn",
        "דקדוק ומשמעות יחד",
        "בשלב הזה המשפטים ארוכים יותר. בדקו גם משמעות וגם התאמה דקדוקית: יחיד או רבים, "
        "זמן הפועל, ומילת יחס קבועה (contribute to, succeed in, prevent from). מילה נרדפת "
        "שלא מתאימה למבנה היא מלכודת. קראו פעמיים: פעם למשמעות הכללית, ופעם לבדיקת התאמה "
        "מדויקת. מילות קישור כמו however, despite, due to, as a result הן רמזים חזקים.",
        "contribute to · succeed in · prevent from · however / despite = contrast",
        "לבדוק גם משמעות וגם התאמה דקדוקית",
    ),
    mc("sc2_p1", "practice", "למרות הכישלון",
       "בחרו את המילה שמשלימה את המשפט.",
       "Although the first trial failed, the researchers ______ useful data on the new material.",
       [("a", "obtained", None),
        ("b", "discarded", "לזרוק נתונים סותר את although, שמכין משהו חיובי אחרי כישלון."),
        ("c", "invented", "להמציא נתונים אינו מה שעושים אחרי ניסוי."),
        ("d", "avoided", "להימנע מנתונים לא מתאים.")],
       "a", "נכון. obtained = השיגו. למרות הכישלון, הושגו נתונים שימושיים.",
       "although מכין ניגוד לכישלון: בכל זאת הושג משהו. הפועל הוא obtained.",
       "סמנו although.\nאחרי כישלון מגיע רווח בלתי צפוי.\nהתשובה: obtained.",
       "מה אפשר עדיין להשיג אחרי ניסוי שנכשל?", "להשלים לפי ניגוד במשפט"),
    mc("sc2_p2", "practice", "לפגוע בריכוז",
       "בחרו את המילה שמשלימה את המשפט.",
       "High levels of stress can ______ a person's ability to concentrate for long periods.",
       [("a", "impair", None),
        ("b", "improve", "לשפר ריכוז סותר את High levels of stress."),
        ("c", "ignore", "הלחץ לא מתעלם מהיכולת; הוא פועל עליה."),
        ("d", "celebrate", "לא מתאים ליכולת ריכוז.")],
       "a", "נכון. impair = לפגוע. לחץ גבוה פוגע ביכולת להתרכז.",
       "לחץ גבוה + יכולת ריכוז = פגיעה. הפועל האקדמי הוא impair.",
       "שאלו מה לחץ עושה ליכולת ריכוז.\nהוא מחליש אותה.\nהתשובה: impair.",
       "מה הקשר בין לחץ לריכוז במשפט?", "לבחור פועל שמתאים לתוצאה שלילית"),
    mc("sc2_p3", "practice", "לסכם במילים שלהם",
       "בחרו את המילה שמשלימה את המשפט.",
       "The lecturer asked the students to ______ the main points in their own words.",
       [("a", "summarize", None),
        ("b", "memorize exactly", "in their own words סותר שינון מדויק."),
        ("c", "ignore", "להתעלם סותר את asked."),
        ("d", "translate into numbers", "לא מתאים ל-main points במילים.")],
       "a", "נכון. summarize = לסכם. in their own words מחזק את זה.",
       "in their own words = ניסוח עצמי של הרעיונות המרכזיים. הפועל הוא summarize.",
       "סמנו in their own words.\nזה סיכום, לא שינון.\nהתשובה: summarize.",
       "מה דורש in their own words?", "להשלים לפי צירוף במשפט"),
    mc("sc2_p4", "practice", "קשר חזק בנתונים",
       "בחרו את המילה שמשלימה את המשפט.",
       "The data ______ that there is a strong link between daily walking and lower blood pressure.",
       [("a", "suggest", None),
        ("b", "deny", "להכחיש סותר strong link."),
        ("c", "hide", "להסתיר לא מתאים לנתונים שמוצגים."),
        ("d", "prevent", "למנוע לא מתאים למבנה that there is.")],
       "a", "נכון. suggest = מצביעים על. הנתונים מצביעים על קשר.",
       "The data ______ that... דורש פועל כמו suggest או show. מבין האפשרויות: suggest.",
       "בדקו מה הנתונים עושים למשפט that...\nהם מצביעים על קשר.\nהתשובה: suggest.",
       "איזה פועל מתאים לפני that במשפט על נתונים?", "להשלים פועל שמתאים לנתונים"),
    mc("sc2_p5", "practice", "לשקול הצעה",
       "בחרו את המילה שמשלימה את המשפט.",
       "The committee will ______ the proposal only after a further discussion next week.",
       [("a", "consider", None),
        ("b", "reject immediately", "immediately סותר only after a further discussion."),
        ("c", "ignore completely", "דיון נוסף לא מתאים להתעלמות."),
        ("d", "destroy", "לא מתאים לוועדה אקדמית שדנה בהצעה.")],
       "a", "נכון. consider = לשקול. הדיון הנוסף מכין שקילה, לא דחייה מיידית.",
       "only after a further discussion אומר שההחלטה עוד לא סופית. הפועל הוא consider.",
       "סמנו only after.\nעוד יהיה דיון, אז אין החלטה סופית עכשיו.\nהתשובה: consider.",
       "מה קורה אחרי דיון נוסף?", "להשלים לפי רמז של רצף"),
    mc("sc2_chk", "check", "תזוזה של מדיניות",
       "בחרו את המילה שמשלימה את המשפט.",
       "The new policy is expected to ______ significant changes in how grants are awarded.",
       [("a", "produce", None),
        ("b", "prevent", "למנוע שינויים סותר expected to ______ significant changes."),
        ("c", "ignore", "מדיניות לא מתעלמת משינויים שהיא עצמה יוצרת."),
        ("d", "delay only the past", "לא מובן ולא מתאים לשינויים עתידיים.")],
       "a", "נכון. produce changes = לחולל שינויים. זה הצירוף שמתאים ל-expected to.",
       "expected to + changes: המדיניות צפויה לחולל שינויים. produce מתאים, prevent הופך כיוון.",
       "שאלו מה מדיניות חדשה עושה לשינויים.\nהיא יוצרת אותם.\nהתשובה: produce.",
       "איזה פועל מתאים עם changes?", "לבחור צירוף מדויק עם changes"),
])

topic("t_sc_adv", "השלמת משפטים: רמה גבוהה", "Sentence completion: advanced", "🎯", [
    learn(
        "sc3_learn",
        "מילים קרובות ומלכודות",
        "כאן מופיעות מילים אקדמיות קרובות במשמעות (undermine / weaken, subsequent / later, "
        "feasible / practical). חפשו את הרמז המרכזי: תוצאה, סיבה, ניגוד או תנאי, ואז בדקו "
        "איזו אפשרות מתאימה לו במדויק. שללו קודם מילים שנשמעות \"חכמות\" אך לא מתאימות "
        "להקשר, ומילים דומות בכתב (affect/effect, imply/infer). אם שני מועמדים נראים טוב, "
        "בדקו מילת יחס וחלק דיבר. זמן ממוצע לשאלה במבחן לא אומת.",
        "undermine · subsequent · feasible · imply / infer · affect / effect",
        "לבחור בין מילים קרובות לפי רמז מדויק",
    ),
    mc("sc3_p1", "practice", "לערער מסקנה",
       "בחרו את המילה שמשלימה את המשפט.",
       "Subsequent analysis ______ the first conclusion that the treatment had no effect.",
       [("a", "undermined", None),
        ("b", "confirmed without any further test", "without any further test סותר subsequent analysis."),
        ("c", "ignored", "ניתוח המשך לא מתעלם ממסקנה; הוא בוחן אותה."),
        ("d", "delayed permanently", "לא מתאים למסקנה שנבחנת מחדש.")],
       "a", "נכון. undermined = ערער. ניתוח מאוחר יותר ערער את המסקנה הראשונה.",
       "Subsequent analysis מול first conclusion מכין שינוי או ערעור. undermined מתאים.",
       "סמנו Subsequent מול first.\nיש בדיקה מאוחרת של מסקנה מוקדמת.\nהתשובה: undermined.",
       "מה ניתוח מאוחר יכול לעשות למסקנה ראשונה?", "להשלים פועל של ערעור"),
    mc("sc3_p2", "practice", "מעשי בתנאים אמיתיים",
       "בחרו את המילה שמשלימה את המשפט.",
       "Few of the proposed solutions proved ______ under real-world conditions.",
       [("a", "feasible", None),
        ("b", "decorative", "קישוטי לא קשור לתנאי אמת."),
        ("c", "imaginary", "דמיוני סותר proved under real-world conditions."),
        ("d", "silent", "לא מתאים לפתרונות.")],
       "a", "נכון. feasible = ישים, מעשי. מעט פתרונות עמדו במבחן המציאות.",
       "under real-world conditions בוחן ישימות. המילה היא feasible.",
       "סמנו real-world conditions.\nהשאלה היא אם הפתרון ישים.\nהתשובה: feasible.",
       "מה בודקים בתנאי אמת?", "להשלים תואר של ישימות"),
    mc("sc3_p3", "practice", "מגבלות שיטה",
       "בחרו את המילה שמשלימה את המשפט.",
       "The comprehensive review ______ several methodological limitations in earlier studies.",
       [("a", "identified", None),
        ("b", "concealed", "סקירה מקיפה לא מסתירה מגבלות; היא חושפת אותן."),
        ("c", "invented", "מגבלות מתודולוגיות מזוהות, לא מומצאות."),
        ("d", "celebrated", "לא מתאים למגבלות.")],
       "a", "נכון. identified = זיהתה. הסקירה מצאה מגבלות בשיטות של מחקרים קודמים.",
       "review + limitations: סקירה מציינת מגבלות. הפועל הוא identified.",
       "מה סקירה עושה למגבלות במחקרים קודמים?\nמזהה אותן.\nהתשובה: identified.",
       "מה תפקיד סקירה מקיפה?", "להשלים פועל בסקירת מחקר"),
    mc("sc3_p4", "practice", "לחקור השפעות",
       "בחרו את המילה שמשלימה את המשפט.",
       "Scientists continue to ______ how warmer winters affect the migration of local birds.",
       [("a", "investigate", None),
        ("b", "ignore", "continue to ignore סותר את רוח המשפט המחקרי."),
        ("c", "deny", "להכחיש את האופן שבו זה משפיע לא מתאים ל-how."),
        ("d", "postpone the past", "צירוף לא הגיוני.")],
       "a", "נכון. investigate = לחקור. הם ממשיכים לבדוק את ההשפעה.",
       "Scientists continue to + how... = המשך חקירה. הפועל הוא investigate.",
       "מי ממשיך לעשות משהו, ועל מה?\nמדענים, על השפעת החורפים.\nהתשובה: investigate.",
       "מה מדענים ממשיכים לעשות?", "להשלים פועל מחקרי"),
    mc("sc3_p5", "practice", "להרחיב הבנה",
       "בחרו את המילה שמשלימה את המשפט.",
       "The discovery of the new species has ______ our understanding of the forest's food web.",
       [("a", "expanded", None),
        ("b", "reduced", "גילוי מין חדש לא מצמצם הבנה."),
        ("c", "erased", "לא מוחק הבנה."),
        ("d", "hidden", "גילוי חושף, לא מסתיר.")],
       "a", "נכון. expanded = הרחיב. גילוי חדש מרחיב את ההבנה.",
       "discovery of a new species + understanding = הרחבה. expanded מתאים.",
       "מה גילוי חדש עושה להבנה?\nמרחיב אותה.\nהתשובה: expanded.",
       "איזה כיוון מתאים לגילוי חדש?", "להשלים פועל לפי כיוון חיובי"),
    mc("sc3_chk", "check", "לבהיר קשר",
       "בחרו את המילה שמשלימה את המשפט.",
       "The next set of studies aims to ______ the relationship between diet and sleep quality.",
       [("a", "clarify", None),
        ("b", "hide", "מחקרים לא שואפים להסתיר קשר."),
        ("c", "ignore", "aims to ignore לא הגיוני כמטרת מחקר."),
        ("d", "complicate without cause", "לסבך בלי סיבה אינו מטרה.")],
       "a", "נכון. clarify = להבהיר. המחקרים הבאים שואפים להבהיר את הקשר.",
       "aims to + relationship: המטרה היא להבהיר את הקשר. clarify מתאים.",
       "מה מטרת מחקרי המשך לגבי relationship?\nלהבהיר אותו.\nהתשובה: clarify.",
       "מה עושים לקשר שעדיין לא ברור לגמרי?", "לבחור פועל שמתאים למטרת מחקר"),
])

# ---------------------------------------------------------------------------
# 6–8. Restatement
# ---------------------------------------------------------------------------
topic("t_rest_basic", "ניסוח מחדש: בסיס", "Restatement: basics", "🔁", [
    learn(
        "rest1_learn",
        "אותה משמעות בדיוק",
        "בניסוח מחדש מופיע משפט מקורי וארבעה ניסוחים. בחרו את המשפט ששומר את כל המידע "
        "החשוב, בלי להוסיף ובלי להחסיר. בדקו שלושה דברים: מי עושה מה, מה הכיוון (חיובי "
        "או שלילי), ומילים של כמות או הגבלה כמו only, not, all, some, few. תשובה שנשמעת "
        "דומה אבל משנה כמות, זמן או כיוון היא מלכודת. ברמה הבסיסית השינויים פשוטים: "
        "פעיל וסביל, או מילה נרדפת. נסחו לעצמכם את הרעיון בעברית, ואז השוו.",
        "Same meaning: who, direction, only / not / all / some / few.",
        "לבדוק שתשובה שומרת את כל המשמעות",
    ),
    mc("rest1_p1", "practice", "מעטים סיימו",
       "איזה משפט אומר את אותו הדבר?",
       "Few students completed the assignment before the deadline.",
       [("a", "Almost none of the students finished before the deadline.", None),
        ("b", "Most students finished on time.", "few זה מעטים, לא רוב."),
        ("c", "All students finished early.", "all הפוך מ-few."),
        ("d", "The deadline was canceled.", "מידע חדש, לא במקור.")],
       "a", "נכון. few = מעטים מאוד, כמעט אף אחד לא סיים לפני המועד.",
       "few הוא כמות קטנה מאוד. Almost none שומר את זה. Most ו-All הופכים את הכמות.",
       "סמנו few.\nמעטים = כמעט אף אחד.\nהתשובה: Almost none of the students finished before the deadline.",
       "מה המשמעות של few?", "לשמור כמות בניסוח מחדש"),
    mc("rest1_p2", "practice", "נדחה בגלל מחלה",
       "איזה משפט אומר את אותו הדבר?",
       "The lecture was postponed because the professor was ill.",
       [("a", "The lecture took place later due to the professor's illness.", None),
        ("b", "The professor canceled the lecture permanently.", "postponed זה דחייה, לא ביטול סופי."),
        ("c", "Students preferred a different lecturer.", "מידע שלא מופיע במקור."),
        ("d", "The lecture was shorter than planned.", "המקור לא מדבר על אורך.")],
       "a", "נכון. postponed = נדחה, והסיבה היא מחלת המרצה.",
       "שני חלקים: דחייה, וסיבה. רק המשפט על took place later שומר את שניהם.",
       "פרקו לשניים: נדחה; בגלל מחלה.\nפסלו ביטול סופי ומידע חדש.\nנשארה דחייה בגלל מחלה.",
       "מה ההבדל בין postponed ל-canceled?", "לשמור סיבה וזמן בניסוח מחדש"),
    mc("rest1_p3", "practice", "לא כולם הסכימו",
       "איזה משפט אומר את אותו הדבר?",
       "Not all of the participants agreed with the final decision.",
       [("a", "Some participants disagreed with the decision.", None),
        ("b", "None of the participants agreed.", "not all זה לא כולם, לא אף אחד."),
        ("c", "Everyone agreed completely.", "הפוך מהמקור."),
        ("d", "Only one person disagreed.", "המקור לא קובע מספר מדויק.")],
       "a", "נכון. not all = לא כולם, כלומר חלק לא הסכימו.",
       "not all לא שווה none ולא שווה everyone. Some ... disagreed שומר את המשמעות.",
       "סמנו not all.\nזה אומר שחלק לא הסכימו.\nהתשובה: Some participants disagreed with the decision.",
       "מה ההבדל בין not all ל-none?", "לשמור שלילה חלקית בניסוח מחדש"),
    mc("rest1_p4", "practice", "למרות האורך",
       "איזה משפט אומר את אותו הדבר?",
       "Although the book is long, many students finished it in one week.",
       [("a", "Despite its length, many students completed the book in a week.", None),
        ("b", "The book was short, so students finished quickly.", "המקור אומר שהספר ארוך."),
        ("c", "No student managed to finish the book.", "סותר many students finished."),
        ("d", "The book took most students a month to read.", "חודש לא מופיע במקור.")],
       "a", "נכון. although = despite: למרות האורך, רבים סיימו בתוך שבוע.",
       "יש ניגוד בין אורך לבין סיום מהיר של רבים. Despite its length שומר את הניגוד ואת הזמן.",
       "שמרו שלושה דברים: הספר ארוך; רבים סיימו; בתוך שבוע.\nרק תשובה אחת שומרת את שלושתם.",
       "מה although מוסיף למשפט?", "לשמור ניגוד בניסוח מחדש"),
    mc("rest1_p5", "practice", "כמעט כולם תמכו",
       "איזה משפט אומר את אותו הדבר?",
       "Nearly all of the survey respondents supported the new policy.",
       [("a", "Almost everyone who answered the survey was in favor.", None),
        ("b", "Very few people supported the policy.", "הפוך מ-nearly all."),
        ("c", "Half of the respondents opposed it.", "מחצית לא מופיעה במקור."),
        ("d", "No one answered the survey.", "סותר את קיום המשיבים.")],
       "a", "נכון. nearly all = almost everyone, ו-supported = in favor.",
       "כמעט כל המשיבים תמכו. Almost everyone ... in favor שומר כמות וכיוון.",
       "סמנו nearly all ו-supported.\nכמעט כולם היו בעד.\nהתשובה: Almost everyone who answered the survey was in favor.",
       "מה המשמעות של nearly all?", "לשמור כמות גבוהה בניסוח מחדש"),
    mc("rest1_chk", "check", "עלויות ומורל",
       "איזה משפט אומר את אותו הדבר?",
       "Although the new policy reduced costs, it also lowered employee satisfaction.",
       [("a", "The policy cut expenses but damaged morale.", None),
        ("b", "Costs fell and satisfaction rose.", "במקור שביעות הרצון ירדה, לא עלתה."),
        ("c", "Satisfaction improved once costs were controlled.", "הכיוון של שביעות הרצון הפוך."),
        ("d", "The policy had no effect on workers.", "סותר lowered employee satisfaction.")],
       "a", "נכון. שני החלקים נשמרו: העלויות ירדו, ושביעות הרצון ירדה.",
       "יש שני חלקים הפוכים בכיוון הכלכלי והאנושי: חיסכון, ופגיעה במורל. רק cut expenses but damaged morale שומר את שניהם.",
       "פרקו לשניים: עלויות ירדו; שביעות רצון ירדה.\nבדקו כל תשובה מול שני החלקים.",
       "מה קרה לשביעות הרצון במקור?", "לבחור ניסוח ששומר שני חלקים"),
])

topic("t_rest_complex", "ניסוח מחדש: מבנים מורכבים", "Restatement: complex syntax", "⛓️", [
    learn(
        "rest2_learn",
        "משפטי זיקה וסדר סיבה",
        "המשפטים כוללים משפטי זיקה, תנאי ומילות קישור מורכבות. זהו קודם מה הנושא, ומה "
        "היחס בין החלקים: סיבה, תוצאה, ניגוד או תנאי. סמנו במקור מילות מפתח של כמות, זמן "
        "ושלילה, וודאו שהן מופיעות בניסוח הנכון. שללו תשובות שמוסיפות מידע, שהופכות סיבה "
        "לתוצאה, או שמשנות את התנאי (if) לעובדה שכבר התקיימה. recommended זה לא אותו דבר "
        "כמו required.",
        "cause vs effect · if = condition, not a fact · recommended ≠ required",
        "לשמור יחסים לוגיים בניסוח מחדש",
    ),
    mc("rest2_p1", "practice", "רק אחרי חזרה",
       "איזה משפט אומר את אותו הדבר?",
       "The results were published only after the experiment had been repeated.",
       [("a", "Publication occurred after the experiment was done again.", None),
        ("b", "The experiment was repeated after publication.", "הסדר הפוך."),
        ("c", "The results were never published.", "סותר published."),
        ("d", "The experiment failed and was not repeated.", "סותר had been repeated.")],
       "a", "נכון. only after = רק אחרי שהניסוי חזר, ואז פורסמו התוצאות.",
       "הסדר: קודם חזרה על הניסוי, אחר כך פרסום. Publication occurred after... שומר את הסדר.",
       "סמנו only after.\nקודם חזרה, אחר כך פרסום.\nפסלו תשובות עם סדר הפוך.",
       "מה קדם למה במקור?", "לשמור סדר זמנים בניסוח מחדש"),
    mc("rest2_p2", "practice", "המלצה ולא חובה",
       "איזה משפט אומר את אותו הדבר?",
       "The professor recommended that students review the material before the exam.",
       [("a", "The professor suggested reviewing the material in advance.", None),
        ("b", "Students were required to review.", "recommended זה המלצה, לא חובה."),
        ("c", "Reviewing was unnecessary.", "סותר recommended."),
        ("d", "The exam covered only new material.", "מידע חדש.")],
       "a", "נכון. recommended = suggested, לא required.",
       "שמרו את החוזק של הפעולה: המלצה. suggested ... in advance שומר גם את הזמן before the exam.",
       "סמנו recommended.\nזו המלצה, לא חובה.\nהתשובה עם suggested.",
       "מה ההבדל בין recommended ל-required?", "לא להחליף המלצה בחובה"),
    mc("rest2_p3", "practice", "קיצוץ תקציב",
       "איזה משפט אומר את אותו הדבר?",
       "Due to budget cuts, several research projects were canceled.",
       [("a", "Some projects stopped because of reduced funding.", None),
        ("b", "Extra funding allowed more projects.", "הפוך מהמקור."),
        ("c", "All projects continued as planned.", "סותר were canceled."),
        ("d", "The budget increased significantly.", "סותר budget cuts.")],
       "a", "נכון. due to budget cuts = בגלל קיצוץ, וכמה פרויקטים הופסקו.",
       "סיבה: קיצוץ. תוצאה: כמה פרויקטים בוטלו. Some projects stopped because of reduced funding שומר את שניהם.",
       "שמרו סיבה ותוצאה.\nקיצוץ, ולכן חלק מהפרויקטים נעצרו.\nפסלו תשובות על תוספת תקציב.",
       "מה גרם לביטול הפרויקטים?", "לשמור סיבה ותוצאה"),
    mc("rest2_p4", "practice", "תנאי למימון",
       "איזה משפט אומר את אותו הדבר?",
       "The museum will open its new wing next year if funding is secured.",
       [("a", "Opening next year depends on obtaining funding.", None),
        ("b", "The wing is already open.", "סותר will open next year."),
        ("c", "Funding has already been secured.", "if אומר שהמימון עדיין לא בטוח."),
        ("d", "The museum will close permanently.", "מידע הפוך.")],
       "a", "נכון. if funding is secured = הפתיחה תלויה בהשגת מימון.",
       "זה תנאי, לא עובדה שכבר התקיימה. depends on obtaining funding שומר את התנאי ואת העיתוי.",
       "סמנו if.\nזו תלות, לא עובדה.\nהתשובה: Opening next year depends on obtaining funding.",
       "מה if עושה למשפט?", "לא להפוך תנאי לעובדה"),
    mc("rest2_p5", "practice", "נוכחות וציון",
       "איזה משפט אומר את אותו הדבר?",
       "Students who attended all classes performed better on the final exam.",
       [("a", "Regular attendance was linked to higher exam performance.", None),
        ("b", "Attendance had no relation to exam scores.", "סותר performed better."),
        ("c", "Students who missed classes scored higher.", "הפוך מהמקור."),
        ("d", "The final exam was canceled.", "מידע חדש.")],
       "a", "נכון. מי שהגיע לכל השיעורים השיג תוצאה טובה יותר במבחן.",
       "יש קשר בין נוכחות מלאה לבין הישג גבוה יותר. linked to higher exam performance שומר את הקשר בלי להוסיף סיבתיות חזקה מדי, וזה עדיין נאמן למקור.",
       "שמרו את הקשר: נוכחות מלאה, וציונים גבוהים יותר.\nפסלו היעדר קשר או כיוון הפוך.",
       "מי קיבל תוצאה טובה יותר?", "לשמור קשר בין שני חלקים"),
    mc("rest2_chk", "check", "הסיבה עדיין לא ידועה",
       "איזה משפט אומר את אותו הדבר?",
       "Researchers have not yet determined the exact cause of the phenomenon.",
       [("a", "The precise cause remains unknown.", None),
        ("b", "The cause is already known.", "סותר have not yet determined."),
        ("c", "The phenomenon does not exist.", "המקור מניח שהתופעה קיימת."),
        ("d", "All researchers agree on the cause.", "סותר את העובדה שהסיבה לא נקבעה.")],
       "a", "נכון. have not yet determined = עדיין לא נקבעה הסיבה המדויקת.",
       "not yet = עדיין לא. The precise cause remains unknown שומר את זה בלי להוסיף מידע.",
       "סמנו not yet.\nהסיבה המדויקת עוד לא ידועה.\nהתשובה: The precise cause remains unknown.",
       "מה אומר not yet determined?", "לשמור שלילה של ידיעה"),
])

topic("t_rest_nuance", "ניסוח מחדש: הבדלים עדינים", "Restatement: nuance and traps", "🔍", [
    learn(
        "rest3_learn",
        "almost, only, not all",
        "ברמה הזו המלכודות דקות: almost / nearly, only, rarely, not all מול none. משפט "
        "שמכיל את אותן מילים בסדר אחר עלול לשנות את המשמעות. בדקו במיוחד כמות, טווח "
        "ושלילה. אם תשובה מוסיפה both / only / always שלא היו במקור, פסלו אותה. תרגלו "
        "שלילה שיטתית של שלוש התשובות לפני שאתם בוחרים.",
        "not all ≠ none · almost ≠ exactly · do not add only / always / both",
        "לזהות הבדל עדין בכמות או בשלילה",
    ),
    mc("rest3_p1", "practice", "גם וגם",
       "איזה משפט אומר את אותו הדבר?",
       "The article argues that technology can both help and harm learning.",
       [("a", "The article claims technology has positive and negative effects on learning.", None),
        ("b", "Technology only helps learning.", "only מוחק את harm."),
        ("c", "Technology has no impact.", "סותר help and harm."),
        ("d", "Learning improves only with technology.", "מוסיף only ומוחק את הנזק.")],
       "a", "נכון. both help and harm = גם יתרון וגם חיסרון.",
       "יש שני כיוונים. positive and negative effects שומר את שניהם. תשובות עם only מוחקות חלק.",
       "סמנו both ... and.\nיש שני צדדים.\nפסלו תשובות שמשאירות רק צד אחד.",
       "מה both מוסיף למקור?", "לא למחוק אחד משני חלקים"),
    mc("rest3_p2", "practice", "חינם לנרשמים",
       "איזה משפט אומר את אותו הדבר?",
       "The workshop was free for all registered students.",
       [("a", "Registered students paid nothing to attend.", None),
        ("b", "Only some students could attend for free.", "all registered, לא only some."),
        ("c", "Registration was expensive.", "המקור לא אומר כמה עולה הרישום, רק שהסדנה חינם לנרשמים."),
        ("d", "The workshop was canceled.", "מידע חדש.")],
       "a", "נכון. free for all registered = הנרשמים לא שילמו על ההשתתפות.",
       "מי מקבל חינם? כל הסטודנטים שנרשמו. paid nothing to attend שומר את זה בלי להוסיף טענה על מחיר הרישום.",
       "סמנו free ו-all registered.\nהנרשמים לא שילמו על הסדנה.\nהתשובה: Registered students paid nothing to attend.",
       "למי הסדנה הייתה חינם?", "לשמור מי מקבל את ההטבה"),
    mc("rest3_p3", "practice", "מגמת התחממות",
       "איזה משפט אומר את אותו הדבר?",
       "Climate data collected over decades show a clear warming trend.",
       [("a", "Long-term data indicate rising temperatures.", None),
        ("b", "Temperatures have remained stable.", "סותר warming trend."),
        ("c", "Data are insufficient to show any trend.", "סותר show a clear ... trend."),
        ("d", "Cooling has been observed.", "הפוך מ-warming.")],
       "a", "נכון. over decades = long-term, ו-warming trend = rising temperatures.",
       "יש נתונים ארוכי טווח ומגמת עלייה. Long-term data indicate rising temperatures שומר את שניהם.",
       "שמרו טווח ומגמה.\nעשרות שנים, והתחממות.\nפסלו יציבות או התקררות.",
       "מה מראים הנתונים לאורך זמן?", "לשמור מגמה בניסוח מחדש"),
    mc("rest3_p4", "practice", "עלייה הדרגתית",
       "איזה משפט אומר את אותו הדבר?",
       "The data indicate a gradual increase rather than a sudden change.",
       [("a", "The data show a slow rise instead of an abrupt one.", None),
        ("b", "There was a sudden dramatic shift.", "סותר rather than a sudden change."),
        ("c", "No change occurred.", "סותר gradual increase."),
        ("d", "The data are incomplete.", "מידע חדש.")],
       "a", "נכון. gradual = slow, rather than a sudden change = instead of an abrupt one.",
       "יש ניגוד בין עלייה איטית לבין שינוי פתאומי. slow rise instead of an abrupt one שומר את הניגוד.",
       "סמנו gradual ו-rather than sudden.\nעלייה איטית, לא קפיצה.\nהתשובה: The data show a slow rise instead of an abrupt one.",
       "מה rather than שולל?", "לשמור ניגוד בין הדרגתי לפתאומי"),
    mc("rest3_p5", "practice", "נרשמו אבל לא הגיעו",
       "איזה משפט אומר את אותו הדבר?",
       "Not every student who registered actually attended.",
       [("a", "Some registered students did not attend.", None),
        ("b", "All registered students attended.", "הפוך מ-not every."),
        ("c", "Registration was closed.", "מידע חדש."),
        ("d", "Attendance was mandatory for all.", "לא נאמר במקור.")],
       "a", "נכון. not every ... attended = חלק מהנרשמים לא הגיעו.",
       "not every שווה some did not. זה לא אומר שאף אחד לא הגיע, וגם לא שכולם הגיעו.",
       "סמנו not every.\nחלק מהנרשמים לא הגיעו.\nהתשובה: Some registered students did not attend.",
       "מה not every אומר על הנוכחות?", "לשמור שלילה חלקית"),
    mc("rest3_chk", "check", "מעט פתרונות ישימים",
       "איזה משפט אומר את אותו הדבר?",
       "Few of the proposed solutions proved feasible under real-world conditions.",
       [("a", "Only a small number of the proposed solutions were practical in actual conditions.", None),
        ("b", "Most solutions worked well in practice.", "הפוך מ-few."),
        ("c", "All solutions were feasible.", "סותר few."),
        ("d", "Feasibility was never tested.", "סותר proved ... under real-world conditions.")],
       "a", "נכון. few = מספר קטן, ו-feasible = practical in actual conditions.",
       "שמרו כמות קטנה וישימות בתנאי אמת. Only a small number ... practical in actual conditions שומר את שניהם.",
       "סמנו few ו-feasible.\nמעטים היו מעשיים במציאות.\nפסלו most ו-all.",
       "כמה פתרונות עמדו במבחן המציאות?", "לשמור few בישימות"),
])

# ---------------------------------------------------------------------------
# 9–11. Reading comprehension
# ---------------------------------------------------------------------------
PASS_A = (
    "Many universities now offer online courses alongside traditional classroom instruction. "
    "Research indicates that students who combine both formats often achieve similar or better "
    "results than those who study only in person. However, success in online components requires "
    "strong time-management skills. Students who regularly check the course platform and complete "
    "assignments on schedule tend to perform well. In contrast, those who postpone work until the "
    "last minute frequently struggle."
)
PASS_B = (
    "Renewable energy sources such as solar and wind power have become more affordable in recent "
    "years. As a result, many countries have increased their investment in these technologies. "
    "One challenge, however, is that solar and wind energy depend on weather conditions. To "
    "address this, researchers are developing better storage systems that can hold electricity "
    "for use when the sun is not shining or the wind is not blowing. These improvements are "
    "expected to support further growth in renewable energy."
)
PASS_C = (
    "Sleep researchers have long studied the relationship between sleep duration and academic "
    "performance. Recent studies suggest that students who sleep seven to nine hours per night "
    "generally perform better on exams than those who sleep less. In addition, consistent sleep "
    "schedules appear more beneficial than irregular ones, even when total hours are similar. "
    "Universities have begun to educate students about these findings, encouraging them to "
    "prioritize sleep during exam periods."
)
PASS_D = (
    "Public libraries in several cities have started lending simple scientific kits, such as "
    "soil-testing tools and small weather sensors, for a period of two weeks. Staff members "
    "report that families often borrow a kit after attending a weekend workshop at the library. "
    "The goal is not to replace school laboratories, but to let children try a short investigation "
    "at home and then talk about the results in a follow-up session. Early surveys show that "
    "children who complete both the home task and the follow-up session remember the key idea "
    "longer than children who only watch a demonstration."
)
PASS_E = (
    "A coastal research group mapped how pedestrians move through a renovated port area. They "
    "found that benches facing the water were used mainly in the late afternoon, while shaded "
    "paths farther inland attracted visitors at midday. Shop owners had expected most people to "
    "stay near the new cafes all day. The map suggests a simpler pattern: visitors follow comfort, "
    "not the location of food, when the weather is hot. The group recommends adding shade on the "
    "waterfront if the city wants more even use of the area throughout the day."
)

topic("t_read_main", "הבנת הנקרא: רעיון ופרטים", "Reading: main idea and details", "📖", [
    learn(
        "read1_learn",
        "שאלה תחילה, אחר כך הקטע",
        "קטעי האמירנט הם בדרך כלל קצרים ועוסקים בנושא אקדמי כללי. אורך מדויק ומספר שאלות "
        "לכל קטע לא אומתו כאן, וגם לא הזמן המדויק לפרק קריאה. בתרגול קראו קודם את השאלה, "
        "ואחר כך את הקטע, וחפשו את המשפט הרלוונטי. בשאלת רעיון מרכזי היזהרו מפרט נכון שהוא "
        "משני, וממשפט שמופיע אבל לא עונה על מה שנשאל. התשובה חייבת להישען על הכתוב.",
        "Question first, then the passage. Main idea vs a true but secondary detail.",
        "למצוא רעיון מרכזי ופרט מפורש",
    ),
    mc("read1_p1", "practice", "רעיון מרכזי: למידה משולבת",
       "מה הרעיון המרכזי של הקטע?",
       PASS_A,
       [("a", "Combining online and classroom learning can work well when students manage their time.", None),
        ("b", "Online courses are always better than classroom courses.", "always לא נאמר, והקטע מדבר על שילוב ועל ניהול זמן."),
        ("c", "Most students fail online courses.", "לא נאמר."),
        ("d", "Universities should stop offering online courses.", "הפוך מהכיוון של הקטע.")],
       "a", "נכון. הקטע מציג שילוב יעיל, בתנאי שיש ניהול זמן.",
       "המשפטים הראשונים מציגים את השילוב, ו-However מוסיף את תנאי ניהול הזמן. זה הרעיון המרכזי.",
       "קראו את המשפט השני ואת However.\nיש תועלת לשילוב, אם מנהלים זמן.\nפסלו always וטענות קיצוניות.",
       "מה מוסיף However לרעיון הכללי?", "למצוא רעיון מרכזי בקטע"),
    mc("read1_p2", "practice", "פרט: מי מצליח",
       "לפי הקטע, אילו סטודנטים נוטים להצליח בחלק המקוון?",
       PASS_A,
       [("a", "Those who check the platform regularly and meet deadlines.", None),
        ("b", "Those who never check the platform.", "הפוך מהכתוב."),
        ("c", "Those who postpone assignments.", "הקטע אומר שהם מתקשים."),
        ("d", "Those who study only in person.", "השאלה על החלק המקוון.")],
       "a", "נכון. זה פרט מפורש: בדיקה סדירה ועמידה בלוחות זמנים.",
       "חפשו את המשפט על regularly check ו-on schedule. הוא עונה ישירות על השאלה.",
       "אל תסכמו מהזיכרון.\nחזרו למשפט על מי שמצליח.\nהתשובה שם במפורש.",
       "איזה משפט מתאר את מי שמצליח?", "לאתר פרט מפורש בקטע"),
    mc("read1_p3", "practice", "פרט: מחיר נמוך יותר",
       "לפי הקטע, מה גרם למדינות להגדיל את ההשקעה באנרגיה מתחדשת?",
       PASS_B,
       [("a", "These sources have become more affordable.", None),
        ("b", "Storage systems are already perfect.", "הקטע אומר שיש אתגר, והאחסון עדיין בפיתוח."),
        ("c", "Weather is always reliable.", "הפוך: התלות במזג האוויר היא האתגר."),
        ("d", "Investment has decreased.", "סותר increased their investment.")],
       "a", "נכון. more affordable מוביל, as a result, להגדלת ההשקעה.",
       "As a result מחבר את המחיר הנמוך יותר להשקעה הגדולה יותר. זה פרט מפורש.",
       "סמנו As a result.\nמה בא לפניו? המחיר נעשה נגיש יותר.\nזו הסיבה להשקעה.",
       "מה מחבר As a result בין שני משפטים?", "לאתר סיבה מפורשת"),
    mc("read1_p4", "practice", "פרט: אתגר מזג האוויר",
       "איזה אתגר הקטע מציין לגבי אנרגיית שמש ורוח?",
       PASS_B,
       [("a", "They depend on weather conditions.", None),
        ("b", "Countries have no interest in them.", "סותר את ההשקעה הגדלה."),
        ("c", "They produce too much electricity at all times.", "לא נאמר."),
        ("d", "They have become more expensive.", "סותר more affordable.")],
       "a", "נכון. One challenge, however... depend on weather conditions.",
       "However מסמן את האתגר: תלות במזג האוויר. זה משפט מפורש.",
       "חפשו את המילה challenge.\nהמשפט שאחריה הוא התשובה.",
       "איפה מופיעה המילה challenge?", "לאתר אתגר מפורש בקטע"),
    mc("read1_p5", "practice", "פרט: שעות שינה",
       "לפי הקטע, מה נמצא לגבי סטודנטים שישנים שבע עד תשע שעות?",
       PASS_C,
       [("a", "They generally perform better on exams than those who sleep less.", None),
        ("b", "They usually perform worse on exams.", "הפוך מהכתוב."),
        ("c", "They have irregular schedules.", "הקטע לא אומר את זה על הקבוצה הזו."),
        ("d", "They ignore university advice.", "לא נאמר.")],
       "a", "נכון. זה ממצא מפורש במשפט השני של הקטע.",
       "חפשו seven to nine hours. המשפט הזה משווה אותם למי שישן פחות, והתוצאה טובה יותר.",
       "אל תוסיפו מידע.\nחזרו למשפט עם seven to nine.\nהתשובה שם.",
       "מה המשפט השני אומר על הציונים?", "לאתר ממצא מפורש"),
    mc("read1_chk", "check", "רעיון מרכזי: שינה",
       "מה מטרת הקטע בעיקר?",
       PASS_C,
       [("a", "To present findings about sleep and academic performance.", None),
        ("b", "To criticize university policies.", "אין ביקורת על מדיניות."),
        ("c", "To recommend specific study techniques.", "הקטע לא מלמד שיטות למידה, אלא שינה."),
        ("d", "To compare different universities.", "אין השוואה בין מוסדות.")],
       "a", "נכון. הקטע מציג ממצאים על שינה והישגים, ומוסיף שמוסדות מתחילים להעביר את המסר.",
       "רוב המשפטים הם ממצאי מחקר על שינה וציונים. המשפט האחרון רק מראה שימוש בממצאים, לא מחליף את המטרה.",
       "שאלו במה רוב הקטע עוסק.\nשינה והישגים בבחינות.\nפסלו ביקורת, שיטות למידה והשוואת מוסדות.",
       "על מה רוב המשפטים בקטע?", "להבחין בין מטרה לפרט"),
])

topic("t_read_infer", "הבנת הנקרא: מילה בהקשר והסקה", "Reading: vocabulary and inference", "💡", [
    learn(
        "read2_learn",
        "רק מה שהטקסט תומך בו",
        "יש שאלות על משמעות מילה בהקשר של הקטע, לא בהגדרת מילון כללית, ויש שאלות הסקה. "
        "הסקה מותרת רק אם היא נובעת ישירות מהכתוב. אל תסתמכו על ידע כללי שמחוץ לקטע. "
        "מילות קישור כמו however, therefore, for example, in contrast עוזרות לראות כיוון. "
        "אם תשובה הולכת מעבר למה שכתוב, פסלו אותה גם אם היא נשמעת סבירה בחיים.",
        "Context meaning ≠ dictionary meaning. Infer only what the text supports.",
        "להסיק מסקנה ולפרש מילה לפי הקטע",
    ),
    mc("read2_p1", "practice", "משמעות struggle",
       "המילה struggle במשפט האחרון של הקטע קרובה ביותר במשמעות ל:",
       PASS_A,
       [("a", "have difficulty", None),
        ("b", "succeed easily", "זה ההפך, בניגוד ל-perform well במשפט הקודם."),
        ("c", "enjoy", "לא מתאים לניגוד In contrast."),
        ("d", "ignore the course", "לא נאמר שהם מתעלמים, אלא שקשה להם.")],
       "a", "נכון. struggle = להתקשות, בניגוד למי שמבצע היטב.",
       "In contrast מציב את struggle מול perform well. לכן זו קושי, לא הצלחה.",
       "סמנו In contrast.\nלפניו: מצליחים. אחריו: struggle.\nההפך מהצלחה הוא קושי.",
       "למה In contrast מופיע לפני struggle?", "לפרש מילה לפי ניגוד בקטע"),
    mc("read2_p2", "practice", "הסקה על דחיינים",
       "מה אפשר להסיק על סטודנטים שדוחים את העבודה לרגע האחרון?",
       PASS_A,
       [("a", "They are likely to face challenges in the online part of the course.", None),
        ("b", "They always get higher grades.", "הפוך מהכתוב."),
        ("c", "They prefer traditional classes only.", "הקטע לא אומר מה הם מעדיפים."),
        ("d", "They never use the platform.", "לא נאמר never.")],
       "a", "נכון. frequently struggle מאפשר להסיק שצפויים להם קשיים, בלי להחמיר ל-always או never.",
       "ההסקה נשענת על המשפט האחרון. תשובות עם always או never חורגות מהכתוב, וגם העדפת כיתה רגילה לא מופיעה.",
       "חזרו למשפט על postpone.\nמה נאמר? frequently struggle.\nבחרו ניסוח זהיר, בלי always.",
       "איזו מילת כמות מופיעה עם struggle?", "להסיק בלי להחמיר את הכתוב"),
    mc("read2_p3", "practice", "תפקיד as a result",
       "הביטוי as a result בקטע על אנרגיה מתחדשת מציג:",
       PASS_B,
       [("a", "a consequence", None),
        ("b", "a cause", "הסיבה באה לפני הביטוי, לא אחריו."),
        ("c", "an unrelated idea", "יש קשר ברור."),
        ("d", "a contradiction", "contradiction היה however, לא as a result.")],
       "a", "נכון. as a result = כתוצאה מכך, כלומר תוצאה.",
       "לפני הביטוי: המחיר נעשה נגיש. אחריו: ההשקעה גדלה. זה קשר של תוצאה.",
       "שאלו מה בא אחרי as a result.\nזו התוצאה.\nהתשובה: a consequence.",
       "מה בדרך כלל בא אחרי as a result?", "לזהות תפקיד של מילת קישור"),
    mc("read2_p4", "practice", "הסקה על אחסון",
       "מה אפשר להסיק מהמשפט האחרון בקטע על אנרגיה מתחדשת?",
       PASS_B,
       [("a", "Improvements in storage may support continued expansion of renewables.", None),
        ("b", "Growth in renewable energy is unlikely.", "סותר expected to support further growth."),
        ("c", "Weather will no longer matter at all.", "הקטע לא מבטיח שהתלות תיעלם לגמרי."),
        ("d", "Investment will stop.", "סותר further growth.")],
       "a", "נכון. expected to support further growth תומך בהסקה זהירה על המשך התרחבות.",
       "ההסקה נשארת קרובה לכתוב: may support. תשובות מוחלטות כמו no longer matter at all חורגות.",
       "קראו את המשפט האחרון.\nexpected to support further growth.\nבחרו ניסוח זהיר עם may.",
       "מה בדיוק נאמר על ההשפעה של האחסון?", "להסיק בזהירות מהמשפט האחרון"),
    mc("read2_p5", "practice", "הסקה על אוניברסיטאות",
       "מה אפשר להסיק מהמשפט האחרון בקטע על שינה?",
       PASS_C,
       [("a", "Universities believe sleep advice may help students around exams.", None),
        ("b", "Students already sleep enough.", "אם כך, לא היה צורך לעודד אותם."),
        ("c", "The research is outdated.", "לא נאמר."),
        ("d", "Exams do not affect sleep.", "הקטע לא טוען את זה.")],
       "a", "נכון. העובדה שהמוסדות מעודדים שינה בתקופת מבחנים מרמזת שהם רואים בזה תועלת.",
       "encouraging them to prioritize sleep during exam periods תומך בהסקה שהמוסדות מאמינים שיש בזה ערך. זו הסקה, לא ציטוט מילה במילה, אבל היא צמודה לכתוב.",
       "שאלו למה מוסדות מעודדים שינה.\nכי הם חושבים שזה יכול לעזור.\nפסלו טענות שלא מופיעות.",
       "מה משתמע מכך שמוסדות מעודדים שינה?", "להסיק מטרה מפעולה בקטע"),
    mc("read2_chk", "check", "לוח שינה קבוע",
       "מה הקטע אומר על לוח שינה קבוע?",
       PASS_C,
       [("a", "It appears more helpful than an irregular schedule, even with similar total hours.", None),
        ("b", "It is less important than total hours.", "הפוך: גם כשהשעות דומות, הקביעות מועילה יותר."),
        ("c", "It has no effect.", "סותר more beneficial."),
        ("d", "It is impossible for students.", "לא נאמר.")],
       "a", "נכון. זה כמעט ניסוח מחדש של המשפט השלישי בקטע.",
       "even when total hours are similar הוא הרמז: הקביעות מוסיפה מעבר לסך השעות.",
       "חפשו consistent sleep schedules.\nקראו את כל המשפט, כולל even when.\nהתשובה שם.",
       "מה even when מוסיף להשוואה?", "לקרוא את כל המשפט, לא רק את תחילתו"),
])

topic("t_read_struct", "הבנת הנקרא: מבנה ומטרה", "Reading: structure and purpose", "🗺️", [
    learn(
        "read3_learn",
        "איך החלקים קשורים",
        "יש שאלות על תפקיד משפט או פסקה, על הקשר בין חלקים, או על מטרת הכותב. קראו את "
        "המשפט הראשון והאחרון כדי לקבל מפה, ושימו לב למילות מעבר. קטע עשוי לפתוח בממצא, "
        "להציג אתגר, ואז פתרון מוצע. תשובה נכונה חלקית אבל לא מדויקת לגבי המבנה היא מלכודת. "
        "גם כאן: אל תבלבלו בין עובדה לבין המלצה.",
        "Opening finding, contrast or challenge, then a proposed response. Fact ≠ recommendation.",
        "לזהות מבנה ומטרה בקטע",
    ),
    mc("read3_p1", "practice", "מטרת ההשאלה בספרייה",
       "מה המטרה של השאלת הערכות, לפי הקטע?",
       PASS_D,
       [("a", "To let children try a short investigation at home and discuss it later, not to replace school labs.", None),
        ("b", "To replace school laboratories completely.", "הקטע אומר במפורש שהמטרה אינה להחליף מעבדות בית ספר."),
        ("c", "To sell scientific tools to families.", "הכלים מושאלים, לא נמכרים."),
        ("d", "To cancel weekend workshops.", "הסדנאות הן נקודת הכניסה להשאלה, לא משהו שמבטלים.")],
       "a", "נכון. The goal is not to replace school laboratories, but to let children try a short investigation at home...",
       "משפט המטרה מנוסח במפורש: לא להחליף מעבדה, אלא ניסוי קצר בבית ושיחה אחריו.",
       "חפשו The goal.\nקראו את כל המשפט, כולל not to replace.\nזו התשובה.",
       "איפה הקטע מצהיר על מטרה?", "לאתר הצהרת מטרה"),
    mc("read3_p2", "practice", "פרט תומך במטרה",
       "מה מראות הסקרים המוקדמים בקטע על הספרייה?",
       PASS_D,
       [("a", "Children who do both the home task and the follow-up remember the key idea longer.", None),
        ("b", "Children who only watch a demonstration remember the most.", "הפוך מהכתוב."),
        ("c", "Families never borrow kits after workshops.", "סותר often borrow a kit after attending a weekend workshop."),
        ("d", "The kits are borrowed for a full school year.", "נאמר two weeks.")],
       "a", "נכון. זה הממצא בסוף הקטע, והוא תומך בערך של המסלול המלא.",
       "המשפט האחרון משווה בין מי שמשלים בית ומפגש לבין מי שרק צופה בהדגמה.",
       "קראו את המשפט האחרון.\nמי זוכר לאורך זמן יותר?\nמי שעושה גם בית וגם מפגש.",
       "מה משווה המשפט האחרון?", "לקשר ממצא למטרה של הקטע"),
    mc("read3_p3", "practice", "מבנה קטע הנמל",
       "איך הקטע על אזור הנמל מאורגן?",
       PASS_E,
       [("a", "It reports a study result, contrasts it with shop owners' expectation, and ends with a recommendation.", None),
        ("b", "It tells the history of the port from the nineteenth century.", "אין היסטוריה ארוכה."),
        ("c", "It lists cafe menus and prices.", "לא נאמר."),
        ("d", "It argues that food, not comfort, explains movement all day.", "הפוך מהמסקנה.")],
       "a", "נכון. יש ממצא, ציפייה שהופרכה, והמלצה בסוף.",
       "התחלה: מיפוי תנועה. אמצע: ציפיית החנוונים מול הדפוס בפועל. סוף: המלצה להוסיף צל.",
       "סמנו ממצא, ציפייה, והמלצה.\nזה סדר הקטע.\nפסלו היסטוריה או תפריטים.",
       "מה בא בסוף הקטע?", "לזהות סדר: ממצא, ניגוד, המלצה"),
    mc("read3_p4", "practice", "מסקנה מול ציפייה",
       "מה הכותבים מסיקים לגבי תנועת המבקרים בחום?",
       PASS_E,
       [("a", "Visitors follow comfort, not the location of food.", None),
        ("b", "Most people stay near the new cafes all day, as shop owners expected.", "זו הציפייה שהממצא מערער."),
        ("c", "Benches facing the water are used mainly at midday.", "נאמר late afternoon, והצל בפנים מושך בצהריים."),
        ("d", "The port should remove all benches.", "לא נאמר.")],
       "a", "נכון. The map suggests a simpler pattern: visitors follow comfort, not the location of food, when the weather is hot.",
       "המשפט עם suggests הוא המסקנה, והוא מנוגד לציפיית בעלי החנויות.",
       "חפשו suggests.\nשם המסקנה.\nאל תבלבלו אותה עם מה שבעלי החנויות ציפו.",
       "מה בעלי החנויות ציפו, ומה בפועל?", "להבחין בין ציפייה למסקנה"),
    mc("read3_chk", "check", "המלצה בסוף",
       "מה הקבוצה ממליצה לעיר?",
       PASS_E,
       [("a", "To add shade on the waterfront if it wants more even use throughout the day.", None),
        ("b", "To close the cafes at midday.", "לא נאמר."),
        ("c", "To remove the inland paths.", "לא נאמר."),
        ("d", "To stop mapping pedestrian movement.", "הפוך: המיפוי הוא הבסיס להמלצה.")],
       "a", "נכון. ההמלצה מפורשת במשפט האחרון: להוסיף צל בטיילת.",
       "recommends adding shade on the waterfront הוא משפט המלצה, לא תיאור מצב קיים.",
       "חפשו recommends.\nזו המלצה לעיר, עם תנאי: אם רוצים שימוש אחיד יותר במשך היום.",
       "איזה פועל מסמן המלצה בסוף?", "להבחין בין ממצא להמלצה"),
])

# ---------------------------------------------------------------------------
# 12–13. Mixed review (kind=review)
# ---------------------------------------------------------------------------
topic(
    "t_mix_sc_rest",
    "חזרה משולבת: השלמת משפט וניסוח מחדש",
    "Mixed review: sentence completion and restatement",
    "🔁",
    [
        learn(
            "mix1_learn",
            "אותם כלים, משפטים חדשים",
            "כאן מתרגלים יחד השלמת משפט וניסוח מחדש, בלי פריטים שכבר הופיעו. בחרו לפי "
            "הקשר דקדוקי וסמנטי, ושמרו על אותה טענה בניסוח מחדש. אין כאן דרישת קדם "
            "לדרך אחרת, אבל החזרה נשענת על הנושאים שכבר עברתם בדרך הזו.",
            "New items only. Same claim on restatement; grammar plus meaning on completion.",
            "לחבר השלמת משפט וניסוח מחדש",
        ),
        mc("mix1_p1", "practice", "חזרה: despite",
           "בחרו את המילה שמשלימה את המשפט.",
           "____ the cost, they decided to repair the building.",
           [("a", "Despite", None),
            ("b", "Because", "because מצריך משפט או that, ולא מתאים ל-the cost כניגוד."),
            ("c", "Although", "although מצריך משפט, לא צירוף שמני לבד."),
            ("d", "Therefore", "therefore לא פותח ניגוד לפני עלות.")],
           "a", "נכון. despite + צירוף שמני: despite the cost.",
           "אחרי הרווח בא the cost, צירוף שמני. despite מתאים, although לא.",
           "בדקו מה בא אחרי הרווח.\nצירוף שמני: despite.\nפסלו although בלי משפט.",
           "despite או although לפני the cost?", "ליישם despite מול although"),
        mc("mix1_p2", "practice", "חזרה: unless",
           "בחרו את המילה שמשלימה את המשפט.",
           "The experiment will fail ____ the temperature is kept stable.",
           [("a", "unless", None),
            ("b", "if", "if ישנה את הטענה: ייכשל אם השומרים על יציבות, וזה הפוך."),
            ("c", "because", "because נותן סיבה, לא תנאי שלילי."),
            ("d", "so", "so לא מתאים כאן.")],
           "a", "נכון. unless = אם לא: ייכשל אם לא ישמרו על טמפרטורה יציבה.",
           "unless שומר על תנאי שלילי. if לבדו הופך את הקשר.",
           "שאלו מתי הניסוי ייכשל.\nרק אם לא שומרים על יציבות.\nunless.",
           "מה unless מוסיף ל-if?", "ליישם unless בתנאי שלילי"),
        mc("mix1_p3", "practice", "חזרה: ניסוח hardly",
           "בחרו את המשפט הקרוב ביותר במשמעות למשפט הזה.",
           "The committee hardly discussed the proposal.",
           [("a", "The committee barely discussed the proposal.", None),
            ("b", "The committee discussed the proposal at length.", "הפוך מ-hardly."),
            ("c", "The committee approved the proposal.", "לא נאמר."),
            ("d", "The committee rejected the proposal immediately.", "חורג מהכתוב.")],
           "a", "נכון. hardly ≈ barely, כמעט לא דנו.",
           "hardly מצמצם את היקף הדיון. at length הוא ההפך, ואישור או דחייה לא מופיעים.",
           "תרגמו hardly: כמעט לא.\nחפשו מילה שקולה, כמו barely.\nפסלו הרחבה או פעולה אחרת.",
           "למה barely מתאים ל-hardly?", "לשמור על אותה מידה בניסוח מחדש"),
        mc("mix1_p4", "practice", "חזרה: in contrast",
           "בחרו את המילה שמשלימה את המשפט.",
           "Rural clinics have few specialists. ____, city hospitals have many.",
           [("a", "In contrast", None),
            ("b", "Similarly", "אין דמיון, יש ניגוד."),
            ("c", "Therefore", "אין כאן קשר של תוצאה, רק השוואה מנוגדת."),
            ("d", "For example", "המשפט השני אינו דוגמה לראשון.")],
           "a", "נכון. few מול many הוא ניגוד: in contrast.",
           "המספרים הפוכים. similarly שגוי, therefore מוסיף סיבתיות שאין במשפטים.",
           "סמנו few ו-many.\nזה ניגוד.\nin contrast.",
           "איזו מילת קישור מתאימה ל-few מול many?", "לבחור מילת ניגוד בחזרה"),
        mc("mix1_p5", "practice", "חזרה: ניסוח prior to",
           "בחרו את המשפט הקרוב ביותר במשמעות למשפט הזה.",
           "The results were published prior to the conference.",
           [("a", "The results were published before the conference.", None),
            ("b", "The results were published after the conference.", "prior to = before, לא after."),
            ("c", "The results were published during the conference.", "לא אותו זמן."),
            ("d", "The results were never published.", "סותר published.")],
           "a", "נכון. prior to = before.",
           "זה ניסוח מילה במילה כמעט: החלפת prior to ב-before בלי לשנות זמן.",
           "תרגמו prior to.\nלפני.\nפסלו after ו-during.",
           "מה פירוש prior to?", "לנסח מחדש ביטוי זמן"),
        mc("mix1_p6", "practice", "חזרה: would have",
           "בחרו את המילה שמשלימה את המשפט.",
           "If the samples had been labeled, the error ____ avoided.",
           [("a", "would have been", None),
            ("b", "will be", "זה לא מותנה בעבר."),
            ("c", "was", "חסר המבנה המותנה."),
            ("d", "has been", "לא מבנה של if + past perfect.")],
           "a", "נכון. if + past perfect → would have been.",
           "had been labeled קובע מותנה בעבר. will be ו-was לא מתאימים למבנה.",
           "סמנו had been.\nזה מותנה בעבר.\nwould have been.",
           "איזה מבנה בא אחרי if + past perfect?", "ליישם מותנה בעבר בחזרה"),
        mc("mix1_chk", "check", "חזרה: ניסוח no sooner",
           "בחרו את המשפט הקרוב ביותר במשמעות למשפט הזה.",
           "No sooner had the lecture ended than the questions began.",
           [("a", "The questions began immediately after the lecture ended.", None),
            ("b", "The questions began long after the lecture ended.", "סותר immediately."),
            ("c", "The questions began before the lecture ended.", "הפוך."),
            ("d", "There were no questions after the lecture.", "סותר began.")],
           "a", "נכון. no sooner... than = מיד אחרי.",
           "המבנה הזה מציין רצף מיידי, לא עיכוב ולא היפוך סדר.",
           "תרגמו no sooner... than.\nמיד אחרי.\nפסלו long after ו-before.",
           "מה no sooner... than אומר על סדר הזמנים?", "לנסח מחדש מבנה רצף"),
    ],
    kind="review",
    review_ids=["t_sc_basic", "t_sc_mid", "t_sc_adv", "t_rest_basic", "t_rest_complex", "t_rest_nuance"],
)

topic(
    "t_mix_rc",
    "חזרה משולבת: קריאה ממוקדת",
    "Mixed review: focused reading",
    "📚",
    [
        learn(
            "mix2_learn",
            "זמן לקטע, בלי שעון רשמי מאומת",
            "תרגלו קטע מלא עם כמה שאלות ברצף. במבחן הרשמי יש מגבלת זמן לכל פרק, אבל "
            "חלוקת הדקות המדויקת לשאלות קריאה לא אומתה כאן, לכן אין כאן שעון רשמי. "
            "עבדו בקצב יציב: שאלה, חזרה למשפט הרלוונטי, בחירה, ומעבר הלאה. אל תישארו "
            "על פריט אחד יותר מדי.",
            "A passage with several questions in a row. Official per-question timing is unverified here.",
            "לענות על כמה שאלות מאותו קטע ברצף",
        ),
        mc("mix2_p1", "practice", "רעיון: ערכות מדע",
           "מה הרעיון המרכזי של הקטע?",
           PASS_D,
           [("a", "Libraries lend science kits so children can investigate at home and discuss the results, not to replace school labs.", None),
            ("b", "School laboratories are closing in several cities.", "לא נאמר."),
            ("c", "Workshops have replaced home tasks.", "הקטע מחבר סדנה, משימה בבית, ומפגש המשך."),
            ("d", "Children remember demonstrations better than home tasks.", "הפוך מהסקר בסוף.")],
           "a", "נכון. המטרה והמבנה של התכנית הם הרעיון המרכזי.",
           "הקטע פותח בהשאלה, מבהיר שזו לא תחליף למעבדה, ומסיים בממצא שתומך במסלול המלא.",
           "חפשו The goal.\nזה לב הקטע.\nשלבו את ה-not to replace.",
           "איזה משפט ממקד את מטרת התכנית?", "למצוא רעיון מרכזי בחזרה על קריאה"),
        mc("mix2_p2", "practice", "פרט: משך השאלה",
           "לכמה זמן מושאלות הערכות?",
           PASS_D,
           [("a", "Two weeks", None),
            ("b", "Two days", "נאמר two weeks."),
            ("c", "A full school year", "ארוך מדי ביחס לכתוב."),
            ("d", "The text does not say.", "נאמר במפורש two weeks.")],
           "a", "נכון. for a period of two weeks.",
           "פרט מספרי מפורש בפתיחה. אין צורך להסיק.",
           "חפשו מספר וזמן.\ntwo weeks.\nזו התשובה.",
           "איפה מופיע משך ההשאלה?", "לאתר פרט מספרי"),
        mc("mix2_p3", "practice", "הסקה: למה סדנה",
           "מה אפשר להסיק על הסדנאות בסוף השבוע?",
           PASS_D,
           [("a", "They often lead families to borrow a kit afterward.", None),
            ("b", "They are required before any child may enter the library.", "חורג מהכתוב."),
            ("c", "They have replaced the follow-up sessions.", "המפגש המשך נשאר חלק מהתכנית."),
            ("d", "Staff members want to cancel them.", "לא נאמר.")],
           "a", "נכון. Staff members report that families often borrow a kit after attending a weekend workshop.",
           "often borrow... after attending הוא בסיס להסקה זהירה, לא לחובה או לביטול.",
           "קראו את המשפט על workshop.\noften + after.\nזה הקשר, בלי להחמיר ל-required.",
           "מה קורה לעיתים קרובות אחרי הסדנה?", "להסיק בזהירות מ-often"),
        mc("mix2_p4", "practice", "רעיון: נמל",
           "מה הרעיון המרכזי של הקטע על אזור הנמל?",
           PASS_E,
           [("a", "Visitor movement follows comfort in hot weather, unlike what shop owners expected, so shade on the waterfront may spread use more evenly.", None),
            ("b", "The cafes are empty all day.", "לא נאמר."),
            ("c", "Benches are never used.", "יש שימוש, בעיקר אחר הצהריים."),
            ("d", "The renovation failed and should be reversed.", "הקטע לא קורא לבטל את השיפוץ.")],
           "a", "נכון. זה מחבר ממצא, ניגוד לציפייה, והמלצה.",
           "הרעיון המרכזי אינו רק פרט על ספסלים, אלא הדפוס הכללי וההשלכה לעיר.",
           "חברו שלושה חלקים: ממצא, ציפייה, המלצה.\nזה הרעיון.\nאל תישארו רק אצל הספסלים.",
           "מה מחבר את סוף הקטע לפתיחתו?", "לנסח רעיון מרכזי מקטע מובנה"),
        mc("mix2_chk", "check", "פרט: מתי ספסלים",
           "מתי בעיקר משתמשים בספסלים הפונים למים?",
           PASS_E,
           [("a", "In the late afternoon", None),
            ("b", "At midday", "בצהריים מושכים השבילים המוצלים בפנים."),
            ("c", "Only at night", "לא נאמר."),
            ("d", "The text does not say.", "נאמר late afternoon.")],
           "a", "נכון. benches facing the water were used mainly in the late afternoon.",
           "זו הבחנה מפורשת מול shaded paths... at midday. קל להפוך ביניהם אם קוראים מהר.",
           "סמנו benches ו-shaded paths.\nלכל אחד זמן שונה.\nהשאלה על הספסלים: late afternoon.",
           "מה הזמן שמצוין ליד benches facing the water?", "לא לערבב בין שני פרטי זמן"),
    ],
    kind="review",
    review_ids=["t_read_main", "t_read_infer", "t_read_struct"],
)

# ---------------------------------------------------------------------------
# 14. Mixed simulation + celebrate
# ---------------------------------------------------------------------------
PASS_F = (
    "City planners in a mid-sized town proposed turning a rarely used railway corridor into a "
    "tree-lined walking path. Supporters argued that the path would give residents a safe route "
    "away from busy streets and would encourage short trips on foot. Opponents claimed that the "
    "project would cost too much and that the land should be reserved for a future road. A "
    "follow-up survey found that most residents who lived within a ten-minute walk of the corridor "
    "supported the path, while support was weaker among people who usually commute by car from "
    "farther neighborhoods. The planning committee postponed a final decision until a detailed "
    "budget could be published."
)

topic("t_sim", "סימולציה מעורבת לקראת המבחן", "Mixed exam-style simulation", "🎯", [
    learn(
        "sim_learn",
        "פריטים מעורבים, בלי הבטחת ציון",
        "השלב הזה מחקה את הגיוון שבמבחן: אוצר מילים, השלמת משפט, ניסוח מחדש וקריאה בזה אחר זה. "
        "המבנה המדויק של הפרקים, מספר השאלות בכל פרק וחלוקת הזמן הרשמית לא אומתו כאן, וגם לא "
        "סף פטור של מוסד כלשהו. זו סימולציה לתרגול, לא חיזוי ציון. עבדו ברצף, בלי לחזור אחורה "
        "אחרי בחירה, כמו במבחן.",
        "Mixed items in exam-like sequence. Official section timing, item counts, and institutional cutoffs are unverified. This does not predict a score.",
        "לתרגל רצף מעורב לקראת המבחן",
    ),
    mc("sim_p1", "practice", "סימולציה: insufficient",
       "בחרו את המילה שמשלימה את המשפט.",
       "The evidence was ____ to support such a strong conclusion.",
       [("a", "insufficient", None),
        ("b", "abundant", "abundant = בשפע, והמשפט מצריך חסר."),
        ("c", "irrelevant only because it was long", "לא מתאים דקדוקית או לטענה."),
        ("d", "celebrated", "לא מתאים להקשר של ראיה ומסקנה.")],
       "a", "נכון. insufficient = לא מספיק לתמוך במסקנה חזקה.",
       "such a strong conclusion דורש מילה שמצמצמת את כוח הראיה. abundant הפוך.",
       "שאלו אם הראיה מספיקה.\nהכיוון: לא.\ninsufficient.",
       "איזו מילה מתאימה לראיה חלשה מול מסקנה חזקה?", "אוצר מילים בסימולציה"),
    mc("sim_p2", "practice", "סימולציה: although",
       "בחרו את המילה שמשלימה את המשפט.",
       "____ the method is simple, it produces reliable results.",
       [("a", "Although", None),
        ("b", "Because", "because מוחק את הניגוד בין פשטות לאמינות."),
        ("c", "Despite", "despite מצריך צירוף שמני, לא משפט."),
        ("d", "Therefore", "therefore לא פותח ניגוד כאן.")],
       "a", "נכון. although + משפט: הפשטות לא מונעת תוצאות אמינות.",
       "אחרי הרווח בא משפט שלם. although מתאים, despite לא.",
       "בדקו מה אחרי הרווח.\nמשפט: although.\nפסלו despite.",
       "although או despite לפני the method is simple?", "השלמת משפט בסימולציה"),
    mc("sim_p3", "practice", "סימולציה: ניסוח postpone",
       "בחרו את המשפט הקרוב ביותר במשמעות למשפט הזה.",
       "The committee postponed a final decision until a detailed budget could be published.",
       [("a", "The committee delayed its final decision until a detailed budget was available.", None),
        ("b", "The committee made a final decision before any budget was published.", "הפוך מ-postponed until."),
        ("c", "The committee rejected the project immediately.", "לא נאמר."),
        ("d", "The committee published the budget and then voted at once.", "סותר את הדחייה עד לפרסום התקציב.")],
       "a", "נכון. postponed... until ≈ delayed... until.",
       "נשמרים שני חלקים: הדחייה, והתנאי של תקציב מפורט. אישור או דחייה מיידית חורגים.",
       "שמרו על postponed ועל until.\nזו דחייה עד תנאי.\nפסלו החלטה מוקדמת.",
       "מה נשמר כשמחליפים postpone ב-delay?", "ניסוח מחדש בסימולציה"),
    mc("sim_p4", "practice", "סימולציה: רעיון שביל",
       "מה הרעיון המרכזי של הקטע?",
       PASS_F,
       [("a", "A proposal to turn a railway corridor into a walking path has mixed support and is waiting for a published budget.", None),
        ("b", "The town has already opened the walking path.", "ההחלטה נדחתה, התכנית עוד לא אושרה."),
        ("c", "Everyone in the town opposes the path.", "יש תומכים, בעיקר ליד המסדרון."),
        ("d", "The land has already been used for a new road.", "זו רק העמדה של המתנגדים, לא מצב קיים.")],
       "a", "נכון. הקטע מציג הצעה, נימוקים לשני הצדדים, ממצא מסקר, ודחיית החלטה.",
       "הרעיון המרכזי מחבר את כל החלקים, לא רק את עמדת התומכים או המתנגדים.",
       "סכמו ארבעה חלקים: הצעה, ויכוח, סקר, דחייה.\nזו התמונה המלאה.\nפסלו already opened.",
       "האם התקבלה החלטה סופית בקטע?", "רעיון מרכזי בסימולציה"),
    mc("sim_p5", "practice", "סימולציה: פרט סקר",
       "לפי הסקר, היכן התמיכה בשביל הייתה חזקה יותר?",
       PASS_F,
       [("a", "Among residents who lived within a ten-minute walk of the corridor.", None),
        ("b", "Among people who usually commute by car from farther neighborhoods.", "שם התמיכה הייתה חלשה יותר."),
        ("c", "Only among shop owners.", "לא נאמר."),
        ("d", "The survey did not distinguish between groups.", "הקטע מבחין במפורש בין שתי קבוצות.")],
       "a", "נכון. most residents who lived within a ten-minute walk... supported the path.",
       "יש ניגוד מפורש בין מי שגר קרוב לבין נוסעי הרכב משכונות רחוקות יותר.",
       "חפשו follow-up survey.\nשתי קבוצות.\nהתמיכה חזקה יותר אצל הגרים במרחק הליכה.",
       "אילו שתי קבוצות הסקר משווה?", "פרט מפורש בסימולציה"),
    mc("sim_p6", "practice", "סימולציה: הסקה",
       "מה אפשר להסיק מהמשפט האחרון?",
       PASS_F,
       [("a", "The committee wanted more budget information before deciding.", None),
        ("b", "The committee had already approved the path.", "postponed a final decision סותר אישור."),
        ("c", "A detailed budget had already been published.", "until a detailed budget could be published אומר שטרם פורסם."),
        ("d", "The survey results were ignored.", "לא נאמר; נאמר רק שההחלטה נדחתה עד לתקציב.")],
       "a", "נכון. דחייה עד לפרסום תקציב מפורט משמעה שחסר מידע תקציבי להחלטה.",
       "זו הסקה צמודה ל-postponed... until. תשובות על אישור או על תקציב שכבר פורסם סותרות את הכתוב.",
       "קראו postponed until.\nמה חסר? תקציב מפורט.\nזו ההסקה.",
       "מה התנאי שעומד בפני ההחלטה הסופית?", "הסקה זהירה בסימולציה"),
    mc("sim_p7", "practice", "סימולציה: ניסוח weaker support",
       "בחרו את המשפט הקרוב ביותר במשמעות למשפט הזה.",
       "Support was weaker among people who usually commute by car from farther neighborhoods.",
       [("a", "People who typically drive in from more distant neighborhoods were less likely to support the path.", None),
        ("b", "People who typically drive in from more distant neighborhoods were the strongest supporters.", "הפוך מ-weaker."),
        ("c", "No one from farther neighborhoods had an opinion.", "חורג מהכתוב."),
        ("d", "Car commuters refused to answer the survey.", "לא נאמר.")],
       "a", "נכון. weaker support ≈ less likely to support, עם אותה קבוצה.",
       "נשמרים הקבוצה והכיוון: תמיכה חלשה יותר, לא היעדר דעה ולא תמיכה חזקה.",
       "שמרו על weaker ועל אותה קבוצה.\nless likely to support.\nפסלו strongest.",
       "איך מנסחים weaker support בלי להפוך את הכיוון?", "ניסוח מחדש בסימולציה"),
    mc("sim_chk", "check", "סימולציה: provided that",
       "בחרו את המילה שמשלימה את המשפט.",
       "The path can be built ____ the budget is approved.",
       [("a", "provided that", None),
        ("b", "unless", "unless הופך את התנאי: ייננה אם התקציב לא יאושר."),
        ("c", "despite", "despite לא מתאים כאן דקדוקית או לוגית."),
        ("d", "in contrast", "אין כאן ניגוד בין שני משפטים עצמאיים.")],
       "a", "נכון. provided that = בתנאי ש, והתקציב הוא תנאי חיובי לבנייה.",
       "unless הופך את התנאי. despite ו-in contrast לא מתאימים למבנה.",
       "שאלו מתי אפשר לבנות.\nאם התקציב יאושר.\nprovided that, לא unless.",
       "provided that או unless לפני the budget is approved?", "השלמת תנאי בסימולציה"),
])


topic("t_end", "סיימתם את דרך האמירנט", "You finished the AMIRNET road", "🎉", [
    {
        "id": "am_end_celebrate",
        "type": "celebrate",
        "kind": "understanding",
        "title": "כל הכבוד",
        "body_he": (
            "סיימתם דרך תרגול מלא באמירנט: מבנה המבחן, אוצר מילים, השלמת משפט, ניסוח מחדש, "
            "הבנת הנקרא, חזרה וסימולציה מעורבת. אין כאן מבדק רמה ואין דרישת קדם. הציון "
            "הרשמי הוא על סולם 50 עד 150, ומשך המבחן הוא כ-50 דקות; ספי פטור של מוסדות, "
            "מספר השאלות המדויק בכל פרק וחלוקת הזמן הפנימית לא אומתו כאן. אפשר לחזור "
            "לשלבים חלשים ולתרגל שוב לפני מועד הבחינה."
        ),
        "body_content": (
            "You finished a full AMIRNET practice road: test structure, vocabulary, sentence "
            "completion, restatement, reading, review, and a mixed simulation. There is no "
            "placement test here and no prerequisite. The official scale is 50 to 150, and "
            "the test lasts about 50 minutes. Institutional cutoffs, exact item counts, and "
            "internal timing are unverified here. Revisit weaker stages before your exam date."
        ),
        "can_do": "לחזור לשלבים חלשים ולהמשיך להתכונן לאמירנט",
    }
])

# ---------------------------------------------------------------------------
# Path
# ---------------------------------------------------------------------------
PATH = {
    "id": "path_english_amirnet_01",
    "titles": {
        "he": "אמירנט: הכנה לציון 150",
        "en": "AMIRNET: toward a 150 score",
        "ar": "أميرنت: نحو علامة 150",
    },
    "blurbs": {
        "he": (
            "דרך תרגול מלאה לאמירנט: אוצר מילים, השלמת משפט, ניסוח מחדש והבנת הנקרא, "
            "עם חזרה וסימולציה. בלי דרישת קדם. מבדק רמה יתווסף בהמשך. שדה הזמן במערכת "
            "מוגבל ל-20 שעות; היקף הלימוד המומלץ ארוך יותר ומופיע בתיאור הדרך."
        ),
        "en": (
            "A full AMIRNET practice road: vocabulary, sentence completion, restatement, and "
            "reading, with review and a mixed simulation. No prerequisite. A placement test "
            "will come later. The system's time field is capped at 20 hours; the recommended "
            "study load is longer and is described with the road."
        ),
        "ar": (
            "طريق تمرين كامل لامتحان الأميرنت: مفردات، إكمال جمل، إعادة صياغة وفهم المقروء، "
            "مع مراجعة ومحاكاة. دون متطلبات سابقة. اختبار تحديد المستوى سيُضاف لاحقا. "
            "حقل الوقت في النظام محدود بـ 20 ساعة؛ عبء الدراسة الموصى به أطول ويظهر في وصف الطريق."
        ),
    },
    "emoji": "📝",
    "subject": "english",
    "group_ids": ["adult", "amirnet"],
    "content_locale": "en",
    "explain_locale": "he",
    "estimated_minutes": 1200,
    "score": {"group_id": "amirnet_150", "part_id": "english", "weight": 1},
    "topics": topics,
    "nodes": nodes,
    "prerequisite_path_ids": [],
}

README = """# AMIRNET full practice road

Source for `adult/path_english_amirnet_01.json`.

This is a full practice road, not a 60-minute starter. Eliot asked for a longer road
because people need much more than an hour to learn and master the material.

## Size

- 15 topics: 14 study or review stages plus a closing celebrate topic
- Original scored multiple-choice items only (4 choices), plus teaching and celebrate steps
- `estimated_minutes` is 1200, the schema maximum (20 hours)
- Realistic study time is longer, on the order of 45 to 50 hours, including rereading,
  reviewing misses, and repeating mixed practice. That longer estimate cannot be stored
  in `estimated_minutes` because the schema caps the field at 1200.

## Stage list

1. `t_about` — What AMIRNET is (confirmed: 50–150 scale, about 50 minutes; unverified: item counts, per-section timing, institutional cutoffs)
2. `t_vocab` — Academic vocabulary in context
3. `t_sc_basic` — Sentence completion: connectors and clause type
4. `t_sc_mid` — Sentence completion: contrast, condition, result
5. `t_sc_adv` — Sentence completion: academic phrasing and tense
6. `t_rest_basic` — Restatement: same claim, simple paraphrases
7. `t_rest_complex` — Restatement: connectors and structure
8. `t_rest_nuance` — Restatement: quantity, negation, tone
9. `t_read_main` — Reading: main idea and details
10. `t_read_infer` — Reading: vocabulary in context and inference
11. `t_read_struct` — Reading: structure and purpose
12. `t_mix_sc_rest` — Mixed review of sentence completion and restatement
13. `t_mix_rc` — Mixed review of reading (several questions on a passage)
14. `t_sim` — Mixed exam-style simulation
15. `t_end` — Celebrate

There is no placement test in this road (that comes later) and no prerequisite path.

## Facts

Confirmed, from the content fact-check: official scale 50–150; official duration about
50 minutes; retake and validity rules as recorded there.

Unverified here, and marked in the teaching text: exact item counts, official per-section
timing, and any institutional exemption cutoff (for example a 134-style threshold).

Do not treat this road as a score predictor.

## Rebuild

```bash
python3 scripts/build_amirnet.py
```

Writes `adult/path_english_amirnet_01.json`.
"""


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    out = root / "adult" / "path_english_amirnet_01.json"
    out.write_text(json.dumps(PATH, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (root / "scripts" / "README_amirnet.md").write_text(README, encoding="utf-8")
    n_topics = len(PATH["topics"])
    n_steps = len(PATH["nodes"])
    n_mc = sum(1 for n in PATH["nodes"] if n.get("type") in {"practice", "check"})
    print(f"Wrote {out}")
    print(f"topics={n_topics} steps={n_steps} scored_items={n_mc} estimated_minutes={PATH['estimated_minutes']}")


if __name__ == "__main__":
    main()
