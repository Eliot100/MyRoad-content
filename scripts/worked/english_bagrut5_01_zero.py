"""Full worked solutions (worked_method) per step: rule, apply to this item, the answer. Keyed by node id."""
W = {
    "z_t_letters_p1": "אמרו את המילה לאט והקשיבו לצליל הראשון. למשל ten נפתחת ב t.\nבמילה sun שומעים s, u, n.\nהתשובה: s.",
    "z_t_letters_p2": "אמרו את המילה לאט והקשיבו לצליל האחרון. למשל cup נגמרת ב p.\nבמילה map שומעים m, a, p.\nהתשובה: p.",
    "z_t_be_p1": "מצאו מי במשפט. I תמיד הולך עם am.\nבמשפט הזה מדבר I.\nלכן am: I am tired.",
    "z_t_be_p2": "מצאו מי במשפט. he או she הולכים עם is.\nבמשפט הזה יש She.\nלכן is: She is at home.",
    "z_t_not_p1": "בשלילה כותבים not מיד אחרי am, is, are.\nעם They בא are, ואחריו not.\nהתשובה: are not.",
    "z_t_not_p2": "בשלילה עם I כותבים am ואחריו not, בלי do.\nבמשפט יש I, לכן am not.\nהתשובה: I am not hungry.",
    "z_rev1_q": "חזרו על הכלל: I עם am, he או she עם is, you, we, they עם are.\nמי שבמשפט הוא I.\nהתשובה: am.",
    "z_t_you_p1": "we פירושו אנחנו, ו we הולך תמיד עם are.\nבמשפט יש We.\nלכן are: We are students.",
    "z_t_you_p2": "they פירושו הם, ו they הולך תמיד עם are.\nבמשפט יש They.\nלכן are: They are at school.",
    "z_t_word_p1": "קראו את האותיות לפי הסדר וחברו את הצלילים. למשל b, e, d נותן bed.\nכאן s, u, n יחד נותנים sun. bus נפתחת ב b, ו son כתובה עם o.\nהתשובה: sun.",
    "z_t_word_p2": "נסו כל אות במקום החסר ובדקו איזו מילה מתאימה לרמז.\nחיה קטנה שאומרת מיאו היא cat. עם o יוצא cot, ועם u יוצא cut.\nהתשובה: a.",
    "z_t_sent_p1": "בכל משפט שלם יש מי שעושה ויש פועל. למשל He is tall.\nב Am here חסר מי, וב I here חסר פועל.\nהתשובה: I am here.",
    "z_t_sent_p2": "לפני am צריך את I, ו I נכתבת תמיד באות גדולה.\ni קטנה אינה נכונה, ו am כבר כתוב במשפט.\nהתשובה: I.",
    "z_rev2_q": "חזרו על הכלל: you הולך תמיד עם are, גם כשמדברים אל אדם אחד.\nבמשפט יש You.\nהתשובה: are.",
    "z_final_check": "בשלילה הפועל נשאר כמו במשפט רגיל, ו not בא אחריו.\nעם They בא are, ואחריו כבר כתוב not.\nהתשובה: are.",
}
