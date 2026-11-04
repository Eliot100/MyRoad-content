"""Full worked solutions (worked_method) per step: rule, apply to this item, the answer. Keyed by node id."""
W = {
    "plc_t_letters_p1": "אמרו את המילה לאט, צליל אחרי צליל. למשל lamp: l, a, m, p.\nבמילה cat שומעים c, a, t. הצליל הראשון הוא c.\nהתשובה: c.",
    "plc_t_letters_chk": "אמרו את המילה לאט והקשיבו לצליל שבסוף. למשל fox נגמרת ב x.\nבמילה dog שומעים d, o, g. הצליל האחרון הוא g.\nהתשובה: g.",
    "plc_t_be_p1": "התאימו את הפועל למי שבמשפט: I עם am, he או she עם is, you, we, they עם are.\nבמשפט הזה מי שמדבר הוא I.\nלכן am: I am a student.",
    "plc_t_be_chk": "התאימו את הפועל למי שבמשפט: I עם am, he או she עם is, you, we, they עם are.\nבמשפט הזה יש You.\nלכן are: You are ready.",
    "plc_t_present_p1": "בהווה רגיל מוסיפים s לפועל אחרי he, she, it. למשל Tom plays.\nבמשפט יש He, וזה פעולה שחוזרת כל יום.\nלכן works: He works every day.",
    "plc_t_present_chk": "שאלה בהווה פותחת ב Do עם I, you, we, they, וב Does עם he, she, it.\nבשאלה הזו יש you.\nלכן Do: Do you live here?",
    "plc_t_time_p1": "חפשו את מילת הזמן. yesterday היא עבר, ופועל רגיל מקבל ed. למשל play נהיה played.\nopen הוא פועל רגיל, לכן מוסיפים ed.\nהתשובה: opened.",
    "plc_t_time_chk": "חפשו את מילת הזמן. tomorrow היא עתיד: will ואחריו הפועל בלי שינוי. למשל will eat.\nכאן הפועל הוא leave.\nהתשובה: will leave.",
    "plc_t_accuracy_p1": "בפעם הראשונה כותבים a או an. כשהדבר כבר הוזכר כותבים the.\nהכלב הופיע כבר במשפט הראשון, a dog.\nלכן בפעם השנייה: The.",
    "plc_t_accuracy_chk": "זמן שכבר נגמר, כמו last week, הולך עם עבר רגיל בלי have.\nבמשפט יש last week, לכן צריך את lost.\nהתשובה: I lost my key last week.",
    "plc_t_read_idea": "שאלו מה קרה בכל הקטע מההתחלה ועד הסוף, ולא פרט אחד.\nבקטע תלמידים פנו לעירייה, והספרייה נשארה פתוחה עד הערב.\nהתשובה: Students kept a library open in the evening.",
    "plc_t_read_detail": "מצאו בקטע את השם מהשאלה וקראו מה כתוב מיד אחריו.\nליד מר כהן כתוב שהוא מקשיב ושואל שאלה אחת.\nהתשובה: He listens and asks one question.",
    "plc_t_read_infer": "בשאלת למה מצאו בקטע את המשפט שנותן סיבה.\nהקטע מספר שבערבי לימודים מלא, ובשישי שקט. נעילה וחוסר ספרים לא מופיעים.\nהתשובה: The text says school nights are full and Fridays are quiet.",
    "plc_t_read_word": "קראו את המשפט שסביב המילה ובדקו איזה פירוש מתאים לו.\nה neighbours הביאו ספרים, כלומר אנשים מהסביבה.\nהתשובה: people who live nearby.",
    "plc_t_write_p1": "משפט שלם צריך מי שעושה, פועל ורעיון שנגמר.\nBecause the library ו Should stay חסרים. רק באפשרות הראשונה יש I, think ורעיון שלם.\nהתשובה: I think the library should stay open.",
    "plc_t_write_chk": "פתיחה טובה אומרת את הדעה במשפט שלם וברור.\nבדקו כל אפשרות: רק אחת היא משפט עם דעה, השתיים האחרות הן מילים בלי סדר.\nהתשובה: In my opinion, evening hours help students.",
}
