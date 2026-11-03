"""Worked examples shown as learn steps after a topic's learn step, before its practice.
Keyed by topic id: list of (title, body_he, body_content)."""
E = {
    "t_simple": [
        ("דוגמה: he עם s", "זה הרגל. אחרי he מוסיפים s לפועל. He reads every day.", "He reads every day."),
        ("דוגמה: we בלי s", "אחרי I, you, we, they לא מוסיפים s. We cook at home.", "We cook at home."),
        ("דוגמה: טעות: שם של אדם", "טעות נפוצה: Dana walk to work. Dana היא she, לכן מוסיפים s. נכון: Dana walks to work.", "Dana walks to work."),
    ],
    "t_there": [
        ("דוגמה: there is", "יש כוס אחת. לכן there is. There is a cup on the table.", "There is a cup on the table."),
        ("דוגמה: there are", "יש שלושה כיסאות. לכן there are. There are three chairs in the room.", "There are three chairs in the room."),
        ("דוגמה: טעות: is עם רבים", "טעות נפוצה: There is two cats. יש שני חתולים, וזה רבים. נכון: There are two cats.", "There are two cats."),
    ],
    "t_q": [
        ("דוגמה: Do they", "שאלה על they. Do בהתחלה, והפועל בלי s. Do they eat here?", "Do they eat here?"),
        ("דוגמה: Does he", "שאלה על he. Does בהתחלה, והפועל בלי s. Does he drive to work?", "Does he drive to work?"),
        ("דוגמה: טעות: Do עם she", "טעות נפוצה: Do she like tea? עם he, she, it שואלים Does. נכון: Does she like tea?", "Does she like tea?"),
    ],
    "t_day": [
        ("דוגמה: מה היא עושה בבוקר", "שאלה: What does Maya do after eight? קראו את המשפט שבא אחרי She starts at eight. התשובה: She drinks water and opens her mail.", "She drinks water and opens her mail."),
        ("דוגמה: לאן היא הולכת", "שאלה: Where does Maya walk at four? המשפט האחרון עונה: She stops at four and walks to the park. התשובה: to the park.", "She stops at four and walks to the park."),
        ("דוגמה: טעות: מילה אחת בלי הקשר", "טעות נפוצה: רואים client וחושבים שמאיה מדברת עם לקוח כל יום. בקטע כתוב Some days. לכן רק בחלק מהימים.", "Some days she talks to a client."),
    ],
    "t_neg": [
        ("דוגמה: does not", "שלילה על he. does not, והפועל בלי s. He does not eat meat.", "He does not eat meat."),
        ("דוגמה: do not", "שלילה על we. do not, והפועל בלי s. We do not drive to work.", "We do not drive to work."),
        ("דוגמה: טעות: s אחרי does not", "טעות נפוצה: She does not drinks tea. ה s כבר נמצאת ב does. נכון: She does not drink tea.", "She does not drink tea."),
    ],
    "t_freq": [
        ("דוגמה: always לפני הפועל", "always בא לפני הפועל העיקרי. Dan always eats at noon.", "Dan always eats at noon."),
        ("דוגמה: never אחרי are", "never בא אחרי am, is, are. They are never at home on Sunday.", "They are never at home on Sunday."),
        ("דוגמה: טעות: always אחרי הפועל", "טעות נפוצה: We drink always tea. always בא לפני הפועל. נכון: We always drink tea.", "We always drink tea."),
    ],
}
