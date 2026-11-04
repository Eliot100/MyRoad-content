"""Full worked solutions (worked_method) per step: rule, apply to this item, the answer. Keyed by node id."""
W = {
    "pr_t_simple_p1": "בהווה רגיל מוסיפים s לפועל אחרי he, she, it. למשל Dan cooks.\nבמשפט יש He, לכן drink מקבל s.\nהתשובה: drinks.",
    "pr_t_simple_p2": "אחרי I, you, we, they הפועל נשאר בלי s. למשל we cook.\nבמשפט יש They, לכן start בלי s.\nהתשובה: start.",
    "pr_t_there_p1": "There is לדבר אחד, There are לכמה דברים. למשל There is a lamp.\na book הוא ספר אחד.\nהתשובה: is.",
    "pr_t_there_p2": "There is לדבר אחד, There are לכמה דברים. למשל There are three chairs.\ntwo books הם יותר מספר אחד.\nהתשובה: are.",
    "pr_t_q_p1": "שאלה בהווה פותחת ב Do עם I, you, we, they. למשל Do we need milk?\nבשאלה יש you.\nלכן Do: Do you work here?",
    "pr_t_q_p2": "שאלה בהווה פותחת ב Does עם he, she, it, והפועל נשאר בלי s.\nבשאלה יש she, לכן Does, ו live נשאר כמו שהוא.\nהתשובה: Does she live here?",
    "pr_rev1_q": "חזרו על הכלל: אחרי he, she, it הפועל בהווה מקבל s.\nבמשפט יש She, לכן work נהיה works.\nהתשובה: works.",
    "pr_t_day_idea": "כדי למצוא על מה הקטע, קראו את המשפט הראשון ובדקו שהשאר מתאים לו.\nהמשפט הראשון אומר שמאיה עובדת מהבית, וכל השאר מתאר את היום הזה.\nהתשובה: She works at home.",
    "pr_t_day_detail": "חפשו בקטע את הפועל מהשאלה וקראו מה בא אחריו.\nאחרי starts כתוב at eight. at four היא שעת הסיום.\nהתשובה: at eight.",
    "pr_t_neg_p1": "שלילה בהווה עם he, she, it היא does not, והפועל נשאר בלי s. למשל Tom does not swim.\nבמשפט יש She.\nהתשובה: does not.",
    "pr_t_neg_p2": "שלילה בהווה עם I, you, we, they: do not. למשל We do not swim.\nבמשפט יש They. are not work אינו אנגלית תקינה.\nהתשובה: do not.",
    "pr_t_freq_p1": "מילים כמו always באות לפני פועל רגיל. למשל Ben always sings.\nהפועל כאן הוא walks, לכן always לפניו.\nהתשובה: She always walks.",
    "pr_t_freq_p2": "עם am, is, are מילים כמו never באות אחרי הפועל. למשל We are never bored.\nעם He בא is, ו never אחריו.\nהתשובה: is never.",
    "pr_rev2_q": "חזרו על הכלל: There are כשיש יותר מדבר אחד.\nבמשפט כתוב two books, שני ספרים.\nהתשובה: are.",
    "pr_final_check": "בשאלה עם there מקדימים את is או are. Is there לדבר אחד, Are there לכמה.\na book הוא ספר אחד.\nהתשובה: Is.",
}
