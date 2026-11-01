"""Methods and worked wrong answer explanations. Keyed by node id."""
FIND = "הסבר: מחפשים בקטע את המילים מהשאלה, קוראים את המשפט שלהן ובוחרים תשובה שכתובה שם."
ESSAY = "הסבר: חיבור דעה בנוי כך: פתיחה עם דעה, שתי סיבות עם דוגמה, ומשפט סיום. כל חלק הוא משפט שלם."
WORD = "הסבר: קוראים את המשפט שסביב המילה ובודקים איזה פירוש מתאים לו."
RUB = "הסבר: במחוון אורך הוא רק חלק אחד מהציון. חיבור קצר מדי מפסיד נקודות אורך, ותוכן טוב עדיין מקבל נקודות."
M = {
    "g_t_read_idea": (FIND, "כתוב שהסדנאות שנשארו גבו תשלום קטן וביקשו מכל חבר ללמד שעה. החינמיות בלי חובה נסגרו. לכן Workshops with a fee and a duty."),
    "g_t_read_purpose": ("הסבר: שואלים מה החלק הזה עושה לטענה של הכותב: מוסיף סיבה, דוגמה או תשובה למי שחולק.",
                         "המבקרים אומרים שעזרה מלמדת לחכות, והכותב עונה להם מהנתונים. לכן to answer the claim that help makes people wait."),
    "g_t_essay_open": (ESSAY, "In my opinion, a small fee keeps the room open הוא משפט שלם עם דעה. השאר אינם משפטים."),
    "g_t_essay_org": (ESSAY, "דוגמה לבד לא מוכיחה. צריך נימוק שמחבר את הסיפור לדעה."),
    "g_t_rubric_len": (RUB, "70 מילים קצר מהטווח, לכן יורדות נקודות אורך. התוכן עדיין נבדק ויכול לקבל נקודות."),
    "g_t_rubric_chk": ("הסבר: נימוק אומר למה, ומוסיף מידע חדש. חזרה על אותה מילה אינה נימוק.",
                       "A fee gives the city a reason to keep the lease אומר למה התשלום טוב. השניים האחרים רק חוזרים על fee."),
    "g_rev1_q": ("הסבר: נימוק אומר למה, ומוסיף מידע חדש. חזרה על אותה מילה אינה נימוק.",
                 "A fee gives a reason to keep the lease מסביר למה. A fee is a fee רק חוזר."),
    "g_t_body_p1": (ESSAY, "A duty means every member teaches one hour הוא משפט שלם שנותן סיבה ברורה."),
    "g_t_body_p2": (ESSAY, "בחיבור של 120 עד 140 מילים יש מקום לשתי סיבות ואחריהן משפט סיום."),
    "g_t_close_p1": ("הסבר: משפט סיום חוזר על הדעה במילים חדשות, למשל עם For these reasons.",
                     "For these reasons, a small fee is worth keeping סוגר את הדעה במשפט שלם."),
    "g_t_close_p2": ("הסבר: סיום טוב אומר את הדעה שוב במילים אחרות, לא מעתיק את הפתיחה.",
                     "משפט שמעתיק את הפתיחה מילה במילה לא מוסיף כלום, לכן הוא חלש."),
    "g_t_words_p1": (WORD, "a lease the city holds: העירייה מחזיקה בזכות להשתמש בחדר. lease הוא the right to use the room."),
    "g_t_words_p2": (WORD, "a duty to teach one hour: משהו שחייבים לעשות. duty הוא something you must do."),
    "g_rev2_q": (FIND, "כתוב The workshops that lasted charged a small fee and asked every member to teach. לכן Ones with a fee and a duty."),
    "g_final_check": (RUB, "70 מילים קצר מ120, לכן יורדות נקודות אורך, והתוכן עדיין יכול לקבל נקודות."),
}
