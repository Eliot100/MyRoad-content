"""Methods and worked wrong answer explanations. Keyed by node id."""
PAST = "הסבר: מילת הזמן קובעת. yesterday היא עבר. פועל רגיל בעבר מקבל ed, למשל walked, ויש פעלים שמשתנים, למשל go נהיה went."
FUT = "הסבר: tomorrow היא עתיד. כותבים will ואחריו הפועל בלי שינוי. למשל will go."
TEXT = "הסבר: מחפשים בקטע את המילים מהשאלה ובוחרים תשובה שכתובה שם, לא ניחוש."
M = {
    "tm_t_past_p1": (PAST, "Yesterday היא עבר. send בעבר הוא sent: Yesterday he sent the letter."),
    "tm_t_past_p2": ("הסבר: שלילה בעבר: did not ואחריו הפועל בלי שינוי. למשל I did not see.",
                     "זה עבר, לכן did: She did not go."),
    "tm_t_fut_p1": (FUT, "Tomorrow היא מחר, לכן will leave: Tomorrow I will leave early."),
    "tm_t_fut_p2": ("הסבר: לתוכנית קרובה שכבר סגורה משתמשים בam, is, are ופועל עם ing. למשל I am meeting her at six.",
                    "זו תוכנית קבועה לשבע. עם We בא are, ואחריו catching: We are catching the bus at seven."),
    "tm_t_story_idea": ("הסבר: הרעיון המרכזי מסכם את כל הסיפור: מה קרה בהתחלה ומה בסוף.",
                        "בהתחלה אישה זרה נותנת לג'ונה חצי תפוז. בבוקר הוא משאיר שקית תפוזים. כלומר הוא מחזיר טובה."),
    "tm_t_story_infer": ("הסבר: בשאלת למה מחברים פרטים מהקטע לסיבה שהגיונית לפיהם.",
                         "ג'ונה לא יודע את שם האישה, אבל רוצה להחזיר טובה. לכן מספיק for the bus. אין בקטע שהוא לא יודע לכתוב."),
    "tm_rev1_q": (PAST, "Yesterday היא עבר. walk בעבר הוא walked: Yesterday he walked home."),
    "tm_t_irreg_p1": (PAST, "go משתנה בעבר לwent: Yesterday she went home. אין מילה goed."),
    "tm_t_irreg_p2": ("הסבר: יש פעלים שמשתנים בעבר. see נהיה saw. seen בא רק אחרי have.",
                      "see בעבר הוא saw: I saw the note."),
    "tm_t_ago_p1": ("הסבר: ago בא אחרי משך זמן ומשמעו לפני. למשל three years ago.",
                    "two days ago פירושו לפני יומיים: I met him two days ago."),
    "tm_t_ago_p2": ("הסבר: will הוא עתיד, לכן מילת הזמן צריכה להיות על משהו שעוד יקרה.",
                    "I will call הוא עתיד, לכן Tomorrow: Tomorrow I will call."),
    "tm_t_who_p1": (TEXT, "כתוב Jonah missed the last bus and waited. מי שחיכה הוא Jonah."),
    "tm_t_who_p2": (TEXT, "כתוב waited under the pharmacy light, כלומר מתחת לאור של בית המרקחת."),
    "tm_rev2_q": (FUT, "Tomorrow היא מחר, לכן will leave: Tomorrow we will leave early."),
    "tm_final_check": (FUT, "Tomorrow היא מחר, לכן will leave: Tomorrow we will leave early."),
}
