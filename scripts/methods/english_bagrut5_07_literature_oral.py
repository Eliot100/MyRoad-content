"""Methods and worked wrong answer explanations. Keyed by node id."""
FIND = "הסבר: מחפשים בסיפור את המשפט שעונה על השאלה ובוחרים תשובה שכתובה שם."
POEM = "הסבר: קוראים את השורה מילה במילה. בשיר הזה חפץ, המדרגה, פועל כמו אדם: זוכר, לא סולח, לא מספר."
TONE = "הסבר: הטון הוא איך השיר נשמע. בודקים את המילים: שקטות או צוחקות, רכות או קשות."
M = {
    "lit_t_story_change": ("הסבר: משווים את ההתחלה לסוף: מה הדמות קיבלה ומה היא עושה אחר כך.",
                           "בהתחלה ג'ונה מקבל חצי תפוז. בסוף הוא משאיר שקית תפוזים. הוא מחזיר את מה שקיבל."),
    "lit_t_story_who": (FIND, "כתוב A woman he did not know offered him half her orange. אישה שהוא לא מכיר."),
    "lit_t_poem_image": (POEM, "המדרגה זוכרת כל מפתח מאוחר ולא מספרת. היא שומרת את החושך עוד קצת: They keep the dark a little longer."),
    "lit_t_poem_tone": (TONE, "does not forgive נשמע קשה, וdoes not tell נשמע שקט. לכן quiet and a little strict."),
    "lit_rev1_q": ("הסבר: משווים את ההתחלה לסוף: מה הדמות קיבלה ומה היא עושה אחר כך.",
                   "ג'ונה קיבל תפוז ומחזיר שקית תפוזים: Jonah returns the kindness."),
    "lit_t_essay_p1": ("הסבר: פתיחה על סיפור אומרת מה קורה בו ומה הדעה שלך, במשפט שלם.",
                       "Jonah pays the woman back, and I think that is fair אומר מה קרה ומה אני חושב."),
    "lit_t_essay_p2": ("הסבר: בחיבור על סיפור הסיבה באה ממה שקורה בסיפור עצמו.",
                       "הסיבה צריכה לבוא ממשהו שג'ונה עושה בסיפור, למשל השקית שהוא משאיר."),
    "lit_t_poem2_p1": (POEM, "it does not tell פירושו שהמדרגה לא מספרת, כלומר שומרת סוד."),
    "lit_t_poem2_p2": ("הסבר: בשאלת מה לא נכון בודקים כל תשובה מול השיר ומחפשים את זו שהשיר סותר.",
                       "בשיר יש תמונה ברורה של מדרגה ומפתח, לכן המשפט שאין בו תמונה אינו נכון. השניים האחרים נכונים."),
    "lit_rev2_q": (POEM, "המדרגה לא סולחת ולא מספרת, כלומר שומרת את החושך: They keep the dark a little longer."),
    "lit_final_check": (TONE, "המילים does not forgive וdoes not tell שקטות וקצת קשות: Quiet and a little strict."),
}
