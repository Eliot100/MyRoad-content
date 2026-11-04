"""Full worked solutions (worked_method) per step: rule, apply to this item, the answer. Keyed by node id."""
W = {
    "g_t_read_idea": "מצאו בקטע את המילים מהשאלה וקראו את המשפט שבו הן מופיעות.\nבקטע הסדנאות שנשארו גבו תשלום קטן וביקשו מכל חבר ללמד שעה. החדרים החינמיים בלי חובה נסגרו.\nהתשובה: Workshops with a fee and a duty.",
    "g_t_read_purpose": "שאלו מה הפסקה עושה לטענה: מוסיפה סיבה, דוגמה או תשובה למי שחולק.\nהמבקרים טוענים שעזרה מלמדת לחכות, והכותב עונה להם בעובדות.\nהתשובה: to answer the claim that help makes people wait.",
    "g_t_essay_open": "פתיחה של חיבור דעה היא משפט שלם שאומר את הדעה.\nBecause a fee ו Fee room open people אינם משפטים שלמים.\nהתשובה: In my opinion, a small fee keeps the room open.",
    "g_t_essay_org": "בפסקת גוף יש נימוק ודוגמה. הדוגמה לבד לא מסבירה למה הדעה נכונה.\nלפסקה יש סיפור אבל אין נקודה, לכן חסר המשפט שמחבר אותו לדעה. שם עיר או תאריך לא יעזרו.\nהתשובה: a reason that ties the story to the opinion.",
    "g_t_rubric_len": "במחוון האורך הוא רק חלק אחד מהציון, והתוכן נבדק בנפרד.\n70 מילים פחות מ 120, לכן יורדות נקודות אורך. התוכן עדיין יכול לקבל נקודות.\nהתשובה: It loses points for length and can still earn content points.",
    "g_t_rubric_chk": "נימוק עונה על השאלה למה ומוסיף מידע חדש. חזרה על אותה מילה אינה נימוק.\nA fee is a fee ו Because fee fee רק חוזרים. רק האפשרות הראשונה מסבירה מה התשלום נותן.\nהתשובה: A fee gives the city a reason to keep the lease.",
    "g_rev1_q": "חזרו לכלל: בדקו אם המשפט מסביר למה, או רק אומר שוב את אותו דבר.\nA fee gives a reason to keep the lease מוסיף סיבה. השניים האחרים ריקים.\nהתשובה: A fee gives a reason to keep the lease.",
    "g_t_body_p1": "סיבה בגוף החיבור היא משפט שלם עם מי, פועל ומידע ברור.\nDuty duty hour ו Because duty הם מילים בלי פועל.\nהתשובה: A duty means every member teaches one hour.",
    "g_t_body_p2": "המבנה של חיבור דעה: פתיחה, שתי סיבות עם דוגמה, ומשפט סיום.\nבטווח של 120 עד 140 מילים יש מקום בדיוק לשתי סיבות ואחריהן סיום.\nהתשובה: two reasons, then a closing sentence.",
    "g_t_close_p1": "משפט סיום מחזיר את הדעה במשפט שלם, ולרוב נפתח במילים כמו To sum up.\nרק האפשרות הראשונה היא משפט שלם שאומר שוב את הדעה.\nהתשובה: For these reasons, a small fee is worth keeping.",
    "g_t_close_p2": "סיום טוב חוזר על הדעה במילים חדשות. העתקה של הפתיחה לא מוסיפה דבר.\nכאן המשפט האחרון זהה לראשון, מילה במילה.\nהתשובה: It adds nothing new.",
    "g_t_words_p1": "הבינו את המילה ממי שמחזיק בה ומה עושים איתה במשפט.\nהעירייה מחזיקה ב lease של החדר, כלומר בזכות להשתמש בו.\nהתשובה: the right to use the room.",
    "g_t_words_p2": "חפשו מה בא אחרי המילה. מה שבא אחריה מסביר אותה.\nאחרי a duty בא to teach one hour, משהו שכל חבר חייב לעשות.\nהתשובה: something you must do.",
    "g_rev2_q": "חזרו לשיטה: מצאו בקטע את המילה lasted וקראו את המשפט שלה.\nשם כתוב שהסדנאות שנשארו גבו תשלום קטן וביקשו מכל חבר ללמד.\nהתשובה: Ones with a fee and a duty.",
    "g_final_check": "זכרו שבמחוון האורך והתוכן נבדקים בנפרד, ואף אחד מהם לא מאפס את השני.\nחיבור של 70 מילים קצר מהטווח ומפסיד נקודות אורך, אבל לא מקבל אפס.\nהתשובה: Length loses points. Content can still earn some.",
}
