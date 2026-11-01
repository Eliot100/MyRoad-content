"""Methods and worked wrong answer explanations. Keyed by node id."""
FIND = "הסבר: מחפשים בקטע את המילים מהשאלה, קוראים את המשפט שלהן ובוחרים תשובה שכתובה שם."
WORD = "הסבר: קוראים את המשפט שסביב המילה ובודקים איזה פירוש מתאים לו."
REF = "הסבר: מילה כמו it או she מחליפה שם שכבר הופיע. מחפשים את השם במשפט שלפניה."
M = {
    "e_t_read_idea": ("הסבר: הרעיון המרכזי מחבר את ההתחלה והסוף של הקטע, לא פרט אחד.",
                      "הקטע אומר שהאולם נקי אבל רחוק ויקר, והקונים המבוגרים מפסיקים לבוא. לכן: A cleaner market can lose the people it was for."),
    "e_t_read_purpose": ("הסבר: שואלים מה הכותב רוצה שנבין בסוף הקטע.",
                         "הקטע מראה מה הפסידו כשהשוק עבר לאולם: מחיר גבוה, מרחק מהאוטובוס, דוכנים ריקים. לכן to show a cost of moving the market."),
    "e_t_read_word": (WORD, "הכתבת ספרה stalls ריקים ותור בstall אחד שמוכר פירות. לכן אלה שולחנות שמוכרים בהם."),
    "e_t_vocab_p1": (WORD, "far from the bus פירושו רחוק מהאוטובוס, כלומר not close."),
    "e_t_vocab_p2": (WORD, "loose fruit בא מול plastic boxes, כלומר פרי שלא בתוך קופסה."),
    "e_t_ref_p1": (REF, "במשפט שלפני כתוב The hall is clean. לכן It is also far מדבר על the hall."),
    "e_t_ref_chk": (FIND, "כתוב The owner, Nira, refused the plastic boxes. מי שמסרבת היא Nira."),
    "e_rev1_q": (REF, "It בא אחרי The hall is clean, לכן הוא the hall."),
    "e_t_detail_p1": (FIND, "כתוב She counted empty stalls before nine, כלומר לפני תשע."),
    "e_t_detail_p2": (FIND, "כתוב It is also far from the bus, so older buyers stop coming. הסיבה היא המרחק מהאוטובוס."),
    "e_t_infer_p1": (FIND, "כתוב The council calls the hall a success because the rent is paid. לכן The rent is paid."),
    "e_t_infer_p2": ("הסבר: מחברים מה הדמות עושה ומה היא אומרת כדי להבין מה היא רוצה.",
                     "נירה מסרבת לקופסאות ואומרת שהלקוחות יודעים לבחור אפרסק. היא רוצה לקוחות שבוחרים את הפרי בעצמם."),
    "e_t_band_p1": (WORD, "a queue at the stall הוא תור של אנשים שמחכים ליד הדוכן."),
    "e_t_band_p2": (WORD, "She refused the boxes: היא אמרה לא לקופסאות. refused פירושו said no."),
    "e_rev2_q": (WORD, "stalls ריקים שמוכרים בהם פירות הם tables where people sell."),
    "e_final_check": ("הסבר: הנקודה של הכותב היא מה שכל הקטע מוביל אליו, בעיקר המשפטים האחרונים.",
                      "האולם נקי, אבל רחוק ויקר וקונים מפסיקים לבוא. לכן A clean hall can lose its buyers."),
}
