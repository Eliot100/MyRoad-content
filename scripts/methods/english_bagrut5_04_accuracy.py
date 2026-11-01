"""Methods and worked wrong answer explanations. Keyed by node id."""
ART = "הסבר: a או an כשמזכירים משהו בפעם הראשונה. the כשהוא כבר הוזכר או ששני הצדדים יודעים על מה מדובר."
PERF = "הסבר: have או has ואחריו צורת עבר שלישית (seen, eaten) מתארים משהו עד עכשיו. have עם I, you, we, they, וhas עם he, she, it."
IF = "הסבר: בתנאי ראשון: אחרי if הווה, ובחלק השני will. למשל If it is hot, we will swim."
AN = "הסבר: בוחרים לפי הצליל הראשון, לא לפי האות. an לפני צליל תנועה (a, e, i, o, u), וa לפני צליל אחר."
ORDER = "הסבר: הסדר באנגלית: מי, פועל, מושא, ואחר כך מקום וזמן. תואר בא לפני השם, וnever או always לפני הפועל."
FOR = "הסבר: for עם משך זמן (a year, two weeks). since עם נקודת התחלה (March, 2020). ago עם עבר רגיל ומשמעו לפני."
M = {
    "ac_t_art_p1": (ART, "זו הפעם הראשונה שמזכירים את הציפור, וbird נפתח בצליל b. לכן a: I saw a bird."),
    "ac_t_art_p2": (ART, "הציפור כבר הוזכרה, לכן The: The bird was blue."),
    "ac_t_art_p3": ("הסבר: על כל הסוג ברבים כותבים את השם בלי מילה לפניו. למשל Cats like milk.",
                    "המשפט על כל הכלבים, לכן בלי the: Dogs need water. a לא בא לפני רבים."),
    "ac_t_perf_p1": (PERF, "במשפט יש I, לכן have, ואחריו seen: I have seen this film."),
    "ac_t_perf_p2": ("הסבר: זמן שנגמר, כמו in 2019 או last year, הולך עם עבר רגיל, בלי have.",
                     "in 2019 היא שנה שנגמרה, לכן עבר רגיל: We went to Eilat in 2019."),
    "ac_t_perf_p3": (PERF, "השאלה עם ever היא עד עכשיו, ועם you בא Have: Have you ever eaten sushi?"),
    "ac_t_if_p1": (IF, "החלק עם if כבר בהווה (rains), לכן בחלק השני will: we will stay home."),
    "ac_t_if_p2": (IF, "אחרי if כותבים הווה, ועם she מוסיפים es: If she finishes early, she will call."),
    "ac_t_if_p3": (IF + " אפשר להתחיל בכל אחד מהחלקים.",
                   "if it rains בהווה, וwe will stay home עם will. לכן We will stay home if it rains."),
    "ac_rev1_q": (ART + " " + "an לפני צליל תנועה.",
                  "בפעם הראשונה umbrella, שנפתח בצליל תנועה, לכן an. בפעם השנייה כבר הוזכר, לכן The."),
    "ac_t_an_p1": (AN, "apple נפתח בצליל a, תנועה. לכן an apple."),
    "ac_t_an_p2": (AN, "university נשמע בהתחלה כמו yes, צליל y. לכן a university."),
    "ac_t_an_p3": (AN, "בhour הh שקטה, והצליל הראשון הוא תנועה. לכן an hour."),
    "ac_t_order_p1": (ORDER, "התואר red בא לפני השם car: She has a red car."),
    "ac_t_order_p2": (ORDER, "never בא לפני הפועל drink: I never drink coffee."),
    "ac_t_order_p3": (ORDER, "מי Dana, פועל reads, מושא the paper, ובסוף זמן every morning."),
    "ac_t_for_p1": (FOR, "a year הוא משך זמן, לכן for: I have known her for a year."),
    "ac_t_for_p2": (FOR, "March היא נקודת התחלה, לכן since: He has worked here since March."),
    "ac_t_for_p3": ("הסבר: How long עם עד עכשיו שואלים עם have או has ואחריו צורת עבר שלישית.",
                    "lived היא צורת עבר שלישית, והשאלה היא עד עכשיו. עם you בא have: How long have you lived in Haifa?"),
    "ac_rev2_q": (FOR, "2020 היא נקודת התחלה, לכן since. two years ago פירושו לפני שנתיים, לכן ago."),
    "ac_final_check": ("הסבר: עם last winter, זמן שנגמר, משתמשים בעבר רגיל בלי have. last בא בלי the לפניו.",
                       "Last winter זמן שנגמר, לכן kept. the library כי זו הספרייה שכבר הוזכרה. המשפט הנכון הוא הראשון."),
}
