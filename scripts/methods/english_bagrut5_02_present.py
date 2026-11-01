"""Methods and worked wrong answer explanations. Keyed by node id."""
S = "הסבר: בהווה רגיל, אחרי he, she, it מוסיפים s לפועל. אחרי I, you, we, they לא מוסיפים. למשל she reads, they read."
THERE = "הסבר: There is לדבר אחד, There are ליותר מאחד. למשל There is a cup, There are two cups."
DO = "הסבר: שאלה בהווה פותחים בDo עם I, you, we, they, ובDoes עם he, she, it. הפועל נשאר בלי s."
M = {
    "pr_t_simple_p1": (S, "במשפט יש He, לכן מוסיפים s: He drinks coffee."),
    "pr_t_simple_p2": (S, "במשפט יש They, לכן בלי s: They start early."),
    "pr_t_there_p1": (THERE, "a book הוא ספר אחד, לכן There is a book."),
    "pr_t_there_p2": (THERE, "two books הם שני ספרים, לכן There are two books."),
    "pr_t_q_p1": (DO, "במשפט יש you, לכן Do: Do you work here?"),
    "pr_t_q_p2": (DO, "במשפט יש she, לכן Does, והפועל live בלי s: Does she live here?"),
    "pr_rev1_q": (S, "במשפט יש She, לכן מוסיפים s: She works at home."),
    "pr_t_day_idea": ("הסבר: קוראים את המשפט הראשון. לרוב הוא אומר על מה כל הקטע.",
                      "המשפט הראשון: Maya works at home. כל השאר מתאר את יום העבודה שלה בבית."),
    "pr_t_day_detail": ("הסבר: מחפשים בקטע את המילה starts ואת השעה שאחריה.",
                        "כתוב She starts at eight, כלומר בשמונה. at four היא השעה שבה היא עוצרת."),
    "pr_t_neg_p1": ("הסבר: שלילה בהווה: does not עם he, she, it, וdo not עם I, you, we, they. הפועל בלי s.",
                    "במשפט יש She, לכן does not: She does not like coffee."),
    "pr_t_neg_p2": ("הסבר: שלילה בהווה: do not עם I, you, we, they, וdoes not עם he, she, it.",
                    "במשפט יש They, לכן do not: They do not live here."),
    "pr_t_freq_p1": ("הסבר: מילים כמו always, never באות לפני פועל רגיל. למשל I always read.",
                     "walks הוא פועל רגיל, לכן always בא לפניו: She always walks."),
    "pr_t_freq_p2": ("הסבר: עם am, is, are מילים כמו never באות אחריהם. למשל She is always happy.",
                     "עם he בא is, וnever בא אחריו: He is never late."),
    "pr_rev2_q": (THERE, "two books הם יותר מאחד, לכן There are two books."),
    "pr_final_check": ("הסבר: בשאלה עם there מחליפים סדר: Is there לדבר אחד, Are there ליותר מאחד.",
                       "a book הוא ספר אחד, לכן Is there a book on the desk?"),
}
