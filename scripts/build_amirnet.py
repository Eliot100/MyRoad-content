"""Build adult/path_english_amirnet_01.json (AMIRNET English placement road, starter).

Follows planning/amirnet-english-placement.md. All items are original (no NITE wording).
Run: python scripts/build_amirnet.py
"""
import json, sys
from pathlib import Path

P = "am"

def mc(nid, typ, title, body, content, choices, correct, ok, why, method, hint, can_do, kind="understanding", review=None):
    n = {"id": f"{P}_{nid}", "type": typ, "kind": kind, "title": title, "body_he": body,
         "body_content": content, "choices": [], "correct": correct, "feedback_ok": ok,
         "feedback_try": why, "can_do": can_do, "worked_method": method, "hint": hint}
    for cid, label, fb in choices:
        c = {"id": cid, "label": label}
        if fb:
            c["feedback"] = fb
        n["choices"].append(c)
    if review:
        n["review_topic_ids"] = review
    return n

def learn(nid, title, body, content, can_do):
    return {"id": f"{P}_{nid}", "type": "learn", "kind": "understanding", "title": title,
            "body_he": body, "body_content": content, "can_do": can_do}

nodes, topics = [], []

def topic(tid, he, en, emoji, items):
    topics.append({"id": tid, "titles": {"he": he, "en": en}, "emoji": emoji, "node_ids": [n["id"] for n in items]})
    nodes.extend(items)

topic("t_about", "מה זה אמירנט", "What AMIRNET is", "🧭", [
    learn("about_learn", "אמירנט ולא פסיכומטרי",
          "מדצמבר 2026 אנגלית כבר לא חלק מהבחינה הפסיכומטרית. את רמת האנגלית לאקדמיה בודקים במבחן נפרד של מאל\"ו (NITE): אמירנט. "
          "זה מבחן ממוחשב ומסתגל, בערך 50 דקות, עם שלושה סוגי שאלות: השלמת משפטים, ניסוח מחדש והבנת הנקרא. "
          "הציון בסולם 50–150. כל מוסד קובע לבד מאיזה ציון יש פטור ואיך משבצים לרמה. ההרשמה נפרדת מהפסיכומטרי.",
          "AMIRNET: Sentence Completion, Restatement, Reading Comprehension.",
          "להבין מה אמירנט בודק ולמה הוא נפרד מהפסיכומטרי"),
    mc("about_chk", "check", "שלושה סוגי שאלות", "איזה סוג שאלה לא מופיע היום באמירנט?", "AMIRNET question types",
       [("a", "Listening to a recorded lecture", None),
        ("b", "Sentence Completion", "השלמת משפטים היא אחד משלושת הסוגים של היום."),
        ("c", "Restatement", "ניסוח מחדש הוא אחד משלושת הסוגים של היום.")],
       "a", "נכון. האזנה עוד לא במבחן. מאל\"ו הודיעו שהיא תתווסף בשלבים מ-2027.",
       "היום יש שלושה סוגים: השלמת משפטים, ניסוח מחדש והבנת הנקרא. האזנה תתווסף רק בהמשך, לכן התשובה Listening.",
       "כתבו את שלושת הסוגים של היום: השלמת משפטים, ניסוח מחדש, הבנת הנקרא.\nבדקו כל תשובה מול הרשימה.\nמה שלא ברשימה הוא התשובה: Listening.",
       "שני סוגים מהתשובות מופיעים ברשימת שלושת הסוגים.", "לזהות את סוגי השאלות במבחן"),
])

topic("t_complete", "השלמת משפטים", "Sentence completion", "🧩", [
    learn("comp_learn", "רמזים בתוך המשפט",
          "בהשלמת משפט מחפשים רמז: מילת ניגוד (although, but) הופכת כיוון. מילת סיבה (because, so) ממשיכה את אותו כיוון. "
          "קראו את כל המשפט לפני שמסתכלים על התשובות, ונחשו מילה משלכם.",
          "although = ניגוד · because = סיבה · ; = הסבר", "למצוא רמז במשפט לפני שבוחרים מילה"),
    mc("comp_p1", "practice", "תוצאות שחוזרות", "בחרו את המילה שמשלימה את המשפט.",
       "The researchers' findings were ______; further experiments produced almost identical results.",
       [("a", "reproducible", None),
        ("b", "contradictory", "סותרות לא מתאים: הניסויים הבאים נתנו אותן תוצאות."),
        ("c", "speculative", "השערה בלבד לא מתאים לתוצאות שחזרו שוב.")],
       "a", "נכון. reproducible = אפשר לחזור עליהן ולקבל אותו דבר.",
       "החלק אחרי ה-; מסביר: ניסויים נוספים נתנו כמעט אותן תוצאות. לכן reproducible.",
       "מצאו את ההסבר אחרי ה-;.\nהוא אומר שהתוצאות חזרו שוב.\nהמילה שמתאימה לתוצאות שחוזרות: reproducible.",
       "מה קרה בניסויים הנוספים?", "להשלים מילה לפי הסבר במשפט"),
    mc("comp_p2", "practice", "מילת ניגוד", "בחרו את המילה שמשלימה את המשפט.",
       "Although the bridge looked ______, engineers found serious cracks inside it.",
       [("a", "solid", None),
        ("b", "damaged", "although מסמנת ניגוד. אם הגשר נראה פגוע, אין ניגוד לסדקים."),
        ("c", "fragile", "fragile בכיוון של הסדקים, ו-although דורשת כיוון הפוך.")],
       "a", "נכון. although מסמנת ניגוד: נראה יציב, אבל היו סדקים.",
       "although אומרת שהחלק הראשון הפוך לשני. בשני יש סדקים, לכן בראשון הגשר נראה solid.",
       "סמנו את מילת הקישור: although = ניגוד.\nהחלק השני: סדקים רציניים.\nההפך מזה: נראה יציב. התשובה: solid.",
       "although מסמנת ניגוד בין שני חלקי המשפט.", "להשתמש במילת ניגוד כדי לבחור מילה"),
    mc("comp_chk", "check", "מילת סיבה", "בחרו את המילה שמשלימה את המשפט.",
       "Because the instructions were so ______, almost every student completed the task without help.",
       [("a", "clear", None),
        ("b", "vague", "אם ההוראות לא ברורות, תלמידים היו צריכים עזרה."),
        ("c", "lengthy", "ארוכות לא מסבירות למה הצליחו בלי עזרה.")],
       "a", "נכון. because מחברת סיבה ותוצאה: הוראות ברורות, ולכן הצליחו לבד.",
       "התוצאה: כמעט כולם הצליחו בלי עזרה. הסיבה שמתאימה: ההוראות היו clear.",
       "מצאו את התוצאה: הצליחו בלי עזרה.\nשאלו: מה גורם לזה?\nהוראות ברורות. התשובה: clear.",
       "because: החלק הראשון הוא הסיבה לחלק השני.", "להשתמש במילת סיבה כדי לבחור מילה"),
])

topic("t_restate", "ניסוח מחדש", "Restatement", "🔁", [
    learn("rest_learn", "אותה משמעות בדיוק",
          "בניסוח מחדש מחפשים משפט שאומר בדיוק את אותו הדבר. בודקים שלושה דברים: מי עושה מה, מה הכיוון (חיובי או שלילי), ומילים כמו only, not, all, some. "
          "תשובה שמוסיפה מידע או מחסירה חלק היא לא נכונה, גם אם היא נשמעת דומה.",
          "Same meaning: who, direction, only/not/all/some.", "לבדוק שתשובה שומרת את כל המשמעות"),
    mc("rest_p1", "practice", "חיסכון ומורל", "איזה משפט אומר את אותו הדבר?",
       "Although the new policy reduced costs, it also lowered employee satisfaction.",
       [("a", "The policy cut expenses but damaged morale.", None),
        ("b", "Costs fell and satisfaction rose.", "במקור שביעות הרצון ירדה, לא עלתה."),
        ("c", "Satisfaction improved once costs were controlled.", "הכיוון הפוך: במקור שביעות הרצון ירדה.")],
       "a", "נכון. שני החלקים נשמרו: העלויות ירדו, ושביעות הרצון ירדה.",
       "במקור יש שני חלקים: עלויות ירדו, ושביעות רצון ירדה. רק The policy cut expenses but damaged morale שומרת את שניהם.",
       "פרקו את המקור לשני חלקים: עלויות ירדו; שביעות רצון ירדה.\nבדקו כל תשובה מול שני החלקים.\nרק אחת שומרת את שניהם: The policy cut expenses but damaged morale.",
       "בדקו מה קרה לשביעות הרצון במקור.", "לבחור ניסוח ששומר שני חלקים"),
    mc("rest_chk", "check", "רק חלק", "איזה משפט אומר את אותו הדבר?",
       "Only a few of the volunteers had any previous experience.",
       [("a", "Most of the volunteers were new to this kind of work.", None),
        ("b", "None of the volunteers had experience.", "במקור היו כמה עם ניסיון, לא אף אחד."),
        ("c", "The volunteers were all experienced.", "only a few אומר שרובם בלי ניסיון.")],
       "a", "נכון. only a few עם ניסיון = רובם חדשים.",
       "only a few = מעטים. אז רוב המתנדבים בלי ניסיון, וזה Most of the volunteers were new to this kind of work.",
       "סמנו את המילה only a few.\nמעטים עם ניסיון אומר שרובם בלי ניסיון.\nהתשובה: Most of the volunteers were new to this kind of work.",
       "שימו לב ל-only a few: כמה זה?", "לשמור כמות (only, all, none) בניסוח מחדש"),
])

topic("t_read", "הבנת הנקרא", "Reading comprehension", "📖", [
    learn("read_learn", "קטע קצר, שאלה אחת",
          "קראו קודם את השאלה, אחר כך את הקטע. בשאלת סיבה חפשו מה השתנה לפני התוצאה. התשובה חייבת להופיע בקטע או לנבוע ממנו ישירות.",
          "Question first, then the passage.", "לקרוא קטע מתוך השאלה"),
    mc("read_p1", "practice", "האצות בעיר החוף", "מה מסביר הכי ישירות את הירידה באצות?",
       "A small coastal town began measuring water quality after residents reported unusual algae. Early tests showed elevated nutrient levels near the river mouth. Officials later discovered that a nearby farm had changed its fertilizer schedule. Within two seasons the algae decreased.",
       [("a", "a change in farm practice", None),
        ("b", "new measurement tools", "המדידות רק מצאו את הבעיה, לא פתרו אותה."),
        ("c", "colder weather", "מזג אוויר לא מוזכר בקטע.")],
       "a", "נכון. החווה שינתה את הדישון, ואחרי שתי עונות האצות ירדו.",
       "בקטע, מה שהשתנה לפני הירידה הוא לוח הדישון של החווה. לכן a change in farm practice.",
       "חפשו בקטע מה השתנה.\nהדבר היחיד שהשתנה הוא הדישון בחווה.\nאחריו האצות ירדו. התשובה: a change in farm practice.",
       "מה גילו הפקידים בסוף?", "למצוא סיבה בקטע קצר"),
    mc("read_chk", "check", "רעיון מרכזי", "מה הרעיון המרכזי של הקטע?",
       "Many people believe that multitasking saves time. However, studies of office workers suggest that switching between tasks often increases the total time needed and raises the number of errors. Focusing on one task at a time may therefore be more efficient.",
       [("a", "Doing one task at a time may work better than multitasking.", None),
        ("b", "Office workers make more errors than other workers.", "הקטע לא משווה בין עובדי משרד לעובדים אחרים."),
        ("c", "Multitasking saves time for most people.", "זו האמונה שהקטע מערער, לא המסקנה שלו.")],
       "a", "נכון. However מסמן את הטענה של הכותב, והמשפט האחרון מסכם אותה.",
       "אחרי However באה הטענה של הכותב, והמשפט האחרון מסכם: להתמקד במשימה אחת יעיל יותר.",
       "מצאו את However: אחריה בא מה שהכותב חושב.\nהמשפט האחרון מסכם את זה.\nהתשובה: Doing one task at a time may work better than multitasking.",
       "מה בא אחרי However?", "למצוא רעיון מרכזי בקטע"),
])

topic("t_mixed", "תרגול מעורב", "Mixed practice", "⏱️", [
    learn("mix_learn", "כמו במבחן",
          "במבחן אין הפסקות, וחוזרים אחורה רק בתוך אותו פרק. תשובה חסרה נספרת כטעות, לכן עדיף לנחש מאשר להשאיר ריק. "
          "המבחן מסתגל, וכאן לא משחזרים את זה. כאן מתרגלים ערבוב של שלושת הסוגים.",
          "No blanks: a missing answer counts as wrong.", "לדעת את כללי הזמן והניחוש"),
    mc("mix_r1", "practice", "חזרה: השלמה", "בחרו את המילה שמשלימה את המשפט.",
       "The museum's new exhibit was so ______ that visitors waited in line for hours.",
       [("a", "popular", None),
        ("b", "obscure", "אם התערוכה לא מוכרת, לא היו תורים ארוכים."),
        ("c", "brief", "קצרה לא מסבירה למה חיכו שעות.")],
       "a", "נכון. so ... that: פופולרית, ולכן התורים.",
       "so ... that מחבר סיבה לתוצאה. התוצאה היא תורים ארוכים, לכן popular.",
       "מצאו את התוצאה אחרי that: חיכו שעות.\nמה גורם לזה? תערוכה מבוקשת.\nהתשובה: popular.",
       "so ... that: מה גרם לתורים?", "להשלים משפט בתרגול מעורב", kind="review", review=["t_complete"]),
    mc("mix_r2", "check", "חזרה: ניסוח מחדש", "איזה משפט אומר את אותו הדבר?",
       "The report was not published until the errors had been corrected.",
       [("a", "The report came out only after the errors were fixed.", None),
        ("b", "The report was published with several errors.", "במקור תיקנו את הטעויות לפני הפרסום."),
        ("c", "The errors were found after the report came out.", "הסדר הפוך: התיקון היה לפני הפרסום.")],
       "a", "נכון. not ... until = רק אחרי.",
       "not ... until אומר שהפרסום בא רק אחרי התיקון. זה The report came out only after the errors were fixed.",
       "סמנו not ... until: זה אומר רק אחרי.\nקודם תיקון, אחר כך פרסום.\nהתשובה: The report came out only after the errors were fixed.",
       "not ... until: מה קרה קודם?", "לשמור סדר זמנים בניסוח מחדש", kind="review", review=["t_restate"]),
    {"id": f"{P}_celebrate", "type": "celebrate", "kind": "understanding", "title": "סיום דרך",
     "body_he": "סיימתם את דרך הפתיחה לאמירנט. בדקו באתר של המוסד שלכם איזה ציון צריך לפטור או לשיבוץ.",
     "body_content": "AMIRNET starter road done.", "can_do": "לגשת לתרגול אמירנט עם שלושת סוגי השאלות"},
])

path = {
    "id": "path_english_amirnet_01",
    "titles": {"he": "אמירנט: אנגלית לפטור והשמה", "en": "AMIRNET: English placement", "ar": "أميرنت: الإنجليزية للتصنيف والإعفاء"},
    "blurbs": {
        "he": "דרך פתיחה לאמירנט: השלמת משפטים, ניסוח מחדש והבנת הנקרא. מדצמבר 2026 אנגלית לא בפסיכומטרי.",
        "en": "A starter road for AMIRNET: sentence completion, restatement, and reading. From December 2026 English is not part of the psychometric test.",
        "ar": "مسار بداية لأميرنت: إكمال الجمل وإعادة الصياغة والقراءة.",
    },
    "subject": "english",
    "group_ids": ["adult", "amirnet"],
    "emoji": "🎓",
    "explain_locale": "he",
    "content_locale": "en",
    "estimated_minutes": 60,
    "prerequisite_path_ids": [],
    "score": {"group_id": "amirnet_150", "part_id": "english", "weight": 1},
    "topics": topics,
    "nodes": nodes,
}

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
out = ROOT / "adult" / "path_english_amirnet_01.json"
out.write_text(json.dumps(path, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(out, len(nodes), "nodes")
