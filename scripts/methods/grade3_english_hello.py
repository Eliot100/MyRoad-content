"""Methods and wrong answer explanations. Keyed by node id."""
W = "הסבר: קוראים את המילה באנגלית ונזכרים מה היא אומרת בעברית."
M = {
    "practice_hello": ("הסבר: כשנפגשים אומרים Hello, וכשנפרדים אומרים Goodbye.", "שלום כשנפגשים הוא Hello. Goodbye הוא להתראות."),
    "practice_goodbye": ("הסבר: כשנפגשים אומרים Hello, וכשנפרדים אומרים Goodbye.", "כשנפרדים אומרים Goodbye, להתראות."),
    "practice_please": ("הסבר: כשמבקשים משהו יפה מוסיפים Please, בבקשה.", "Please היא בבקשה. Happy הוא שמח וSad הוא עצוב."),
    "practice_happy": (W, "Happy הוא שמח, כמו כשמחייכים."),
    "check_sad": (W, "Sad הוא עצוב, כמו כשבוכים."),
    "check_tired": (W, "Tired הוא עייף, כשרוצים לישון."),
}

# Kids: the wrong answer text opens with a soft retry.
M = {k: (m, "נסו שוב. " + w) for k, (m, w) in M.items()}
