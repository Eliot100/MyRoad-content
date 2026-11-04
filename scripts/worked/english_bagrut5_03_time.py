"""Full worked solutions (worked_method) per step: rule, apply to this item, the answer. Keyed by node id."""
W = {
    "tm_t_past_p1": "חפשו את מילת הזמן. yesterday היא עבר. יש פעלים שמשתנים בעבר, למשל buy נהיה bought.\nsend משתנה בעבר ל sent.\nהתשובה: sent.",
    "tm_t_past_p2": "שלילה בעבר: did not, ואחריו הפועל בלי שינוי. למשל We did not eat.\nכאן הפועל go נשאר כמו שהוא.\nהתשובה: did.",
    "tm_t_fut_p1": "tomorrow היא עתיד. כותבים will ואחריו הפועל בלי שינוי. למשל will swim.\nleave לבד הוא הווה, ו left הוא עבר.\nהתשובה: will leave.",
    "tm_t_fut_p2": "לתוכנית קרובה שכבר נקבעה כותבים am, is, are ופועל עם ing. למשל She is flying on Monday.\nעם We בא are, ו catch נהיה catching.\nהתשובה: are catching.",
    "tm_t_story_idea": "הרעיון המרכזי מחבר את ההתחלה לסוף הסיפור.\nבתחילת הסיפור אישה שג'ונה לא מכיר חולקת איתו תפוז. בסוף הוא משאיר לה שקית תפוזים.\nהתשובה: A stranger shares an orange, and Jonah returns the kindness.",
    "tm_t_story_infer": "בשאלת למה חברו פרטים מהסיפור לסיבה הגיונית, בלי להמציא.\nג'ונה לא יודע איך קוראים לאישה, ובכל זאת רוצה להודות לה. אין בסיפור שהוא לא יודע לכתוב.\nהתשובה: He does not need her name to return the kindness.",
    "tm_rev1_q": "חזרו על הכלל: yesterday היא עבר, ופועל רגיל מקבל ed.\nwalk הוא פועל רגיל, לכן walked.\nהתשובה: walked.",
    "tm_t_irreg_p1": "go הוא פועל שמשתנה בעבר. לא מוסיפים לו ed.\nבעבר go נהיה went, ואין מילה goed.\nהתשובה: went.",
    "tm_t_irreg_p2": "see משתנה בעבר ל saw. הצורה seen באה רק אחרי have או has.\nאין כאן have, ו seed אינה צורה של see.\nהתשובה: saw.",
    "tm_t_ago_p1": "ago בא אחרי משך זמן ופירושו לפני. למשל five minutes ago.\ntwo days ago פירושו לפני יומיים.\nהתשובה: ago.",
    "tm_t_ago_p2": "התאימו את מילת הזמן לזמן של הפועל. will הוא עתיד.\nYesterday היא עבר, ו Ago לא פותחת משפט. רק Tomorrow מתאימה לעתיד.\nהתשובה: Tomorrow.",
    "tm_t_who_p1": "חפשו בקטע את הפועל מהשאלה וקראו מי עשה אותו.\nליד waited כתוב Jonah. הנהג ומר כהן לא מופיעים בסיפור.\nהתשובה: Jonah.",
    "tm_t_who_p2": "בשאלת איפה חפשו מילת מקום אחרי הפועל.\nאחרי waited כתוב under the pharmacy light.\nהתשובה: under the pharmacy light.",
    "tm_rev2_q": "חזרו על הכלל: מילה של עתיד הולכת עם will והפועל בלי שינוי.\nבמשפט יש Tomorrow, לכן will leave.\nהתשובה: will leave.",
    "tm_final_check": "בדקו את מילת הזמן קודם. left הוא עבר, ו leaves הוא הווה.\nTomorrow פירושו מחר, כלומר עתיד, ולכן צריך will.\nהתשובה: will leave.",
}
