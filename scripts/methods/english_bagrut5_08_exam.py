"""Methods and worked wrong answer explanations. Keyed by node id."""
FIND = "הסבר: מחפשים בקטע את המילים מהשאלה, קוראים את המשפט שלהן ובוחרים תשובה שכתובה שם."
ESSAY = "הסבר: חיבור דעה בנוי כך: פתיחה עם דעה, סיבה מהקטע, ומשפט סיום."
SPELL = "הסבר: בתשובת קריאה בודקים אם הבנת. כתיב לבד לא מוריד שם נקודות. בחיבור הדיוק כן נספר."
WORD = "הסבר: קוראים את המשפט שסביב המילה ובודקים איזה פירוש מתאים לו."
M = {
    "ex_t_mix_idea": ("הסבר: הרעיון המרכזי מחבר את כל הקטע: מה טוב ומה רע בשינוי.",
                      "המועצה מרוצה כי שכר הדירה משולם, אבל הקונים המבוגרים מפסיקים לבוא. לכן Moving the market helps the rent and hurts the buyers."),
    "ex_t_mix_vocab": (WORD, "at a higher price פירושו במחיר גבוה יותר, כלומר it costs more."),
    "ex_t_write_shape": (ESSAY, "Opinion, one reason from the text, and a closing sentence הם שלושת החלקים של חיבור."),
    "ex_t_write_chk": (SPELL, "בתשובת קריאה כתיב לבד לא מוריד את נקודות הקריאה. לכן התשובה הראשונה."),
    "ex_rev1_q": (ESSAY, "דעה, סיבה ומשפט סיום: Opinion, a reason, a closing sentence."),
    "ex_t_read2_p1": ("הסבר: מסיקים רק ממה שכתוב בקטע, בלי להוסיף דברים שאין בו.",
                      "כתוב שהסדנאות החינמיות בלי חובה נסגרו תוך שנה. לכן A room with no duty did not last."),
    "ex_t_read2_p2": ("הסבר: המשפט האחרון בקטע מסכם לרוב את הטענה.",
                      "the room stays when someone besides the learner pays attention: החדר נשאר כשמישהו שם לב. זו המטרה."),
    "ex_t_write2_p1": (SPELL, "הדיוק נספר בחיבור. בתשובת קריאה קצרה הכתיב לבד לא מוריד."),
    "ex_t_write2_p2": ("הסבר: הטווח כולל את שני הקצוות. 120 עד 140 פירושו כל מספר מ120 ועד 140.",
                       "140 הוא הקצה העליון של הטווח, לכן החיבור בתוך הטווח."),
    "ex_t_last_p1": ("הסבר: משפט סיום אומר את הדעה וסיבה קצרה במשפט שלם.",
                     "I would keep the stall, because the buyers know the fruit הוא משפט שלם עם דעה וסיבה."),
    "ex_t_last_chk": ("הסבר: הדרך האחרונה היא מבחן חוזר: היא מערבבת את מה שלמדנו ואין בה נושא חדש.",
                      "הדרך הזו מערבבת קריאה, כתיבה ודיבור ולא מלמדת נושא חדש. האותיות היו בדרך הראשונה."),
    "ex_rev2_q": (WORD, "higher price פירושו מחיר גבוה יותר: it costs more."),
    "ex_final_check": (SPELL, "בתשובת קריאה כתיב לבד לא מוריד נקודות. לכן Spelling alone does not remove the reading points."),
}
