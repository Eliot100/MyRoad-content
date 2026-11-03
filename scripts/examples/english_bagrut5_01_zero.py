"""Worked examples shown as learn steps after a topic's learn step, before its practice.
Keyed by topic id: list of (title, body_he, body_content)."""
E = {
    "t_letters": [
        ("דוגמה: שם וצליל", "לאות יש שם ויש צליל. השם של b הוא בי, והצליל שלה הוא ב, כמו בתחילת bed.", "b: bed, bag, bus"),
        ("דוגמה: צליל ראשון", "אומרים dog לאט: d, o, g. הצליל הראשון הוא d, לכן המילה נפתחת באות d.", "dog: d o g"),
        ("דוגמה: צליל אחרון", "אומרים cup לאט: c, u, p. הצליל האחרון הוא p, לכן המילה נגמרת באות p.", "cup: c u p"),
    ],
    "t_be": [
        ("דוגמה: I עם am", "המשפט מדבר על I. עם I תמיד אומרים am. לכן: I am a dad.", "I am a dad."),
        ("דוגמה: she עם is", "she פירושה היא. עם he, she, it אומרים is. לכן: She is ill.", "She is ill."),
        ("דוגמה: טעות עם he", "טעות נפוצה: He am sad. am הולך רק עם I. עם he אומרים is. נכון: He is sad.", "He is sad."),
    ],
    "t_not": [
        ("דוגמה: am not", "שמים not אחרי am. I am sad. בשלילה: I am not sad.", "I am not sad."),
        ("דוגמה: is not", "שמים not אחרי is. It is big. בשלילה: It is not big.", "It is not big."),
        ("דוגמה: טעות: do בשלילה", "טעות נפוצה: He do not is ill. לא מוסיפים do. שמים not אחרי is. נכון: He is not ill.", "He is not ill."),
    ],
    "t_you": [
        ("דוגמה: you עם are", "you פירושו אתה או את, וגם אתם או אתן. עם you תמיד אומרים are. You are kind.", "You are kind."),
        ("דוגמה: we עם are", "we פירושו אנחנו. עם we אומרים are. We are at home.", "We are at home."),
        ("דוגמה: טעות עם they", "טעות נפוצה: They is sad. they פירושו הם או הן, וזה רבים. עם they אומרים are. נכון: They are sad.", "They are sad."),
    ],
    "t_word": [
        ("דוגמה: מחברים צלילים", "קראו כל אות לפי הצליל שלה: h, a, t. חברו את הצלילים יחד. יוצאת המילה hat.", "h-a-t: hat"),
        ("דוגמה: מילה עם e", "קראו p, e, n לאט, ואז מהר יותר. יוצאת המילה pen.", "p-e-n: pen"),
        ("דוגמה: טעות: רק האות הראשונה", "טעות נפוצה: רואים b ומנחשים bus. קראו את כל האותיות: b, o, x. המילה היא box.", "b-o-x: box"),
    ],
    "t_sent": [
        ("דוגמה: משפט שלם", "He is a cook. יש מישהו: He. יש פועל: is. יש אות גדולה בהתחלה ונקודה בסוף.", "He is a cook."),
        ("דוגמה: אות גדולה ונקודה", "המשפט it is hot נפתח באות קטנה ואין בו נקודה. מתקנים: It is hot.", "It is hot."),
        ("דוגמה: טעות: חסר פועל", "טעות נפוצה: Dan sad. חסר הפועל. Dan הוא אדם אחד, לכן is. נכון: Dan is sad.", "Dan is sad."),
    ],
}
