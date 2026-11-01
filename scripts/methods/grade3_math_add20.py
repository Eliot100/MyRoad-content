"""Methods and wrong answer explanations. Keyed by node id."""
TEN = "הסבר: משלימים קודם ל 10, ואז מוסיפים את מה שנשאר. למשל 8 + 5: 8 + 2 = 10, ועוד 3 זה 13."
M = {
    "practice_balloons": (TEN, "7 + 3 = 10, ונשארו עוד 2 מתוך ה 5. 10 + 2 = 12 בלונים."),
    "practice_candy": (TEN, "9 + 1 = 10, ונשארו עוד 7 מתוך ה 8. 10 + 7 = 17 ממתקים."),
    "check_add": ("הסבר: מחברים את האחדות: 1 ועוד 6, והעשר נשאר. למשל 12 + 5: 2 + 5 = 7, כלומר 17.",
                  "ב 11 יש עשר ו 1. 1 + 6 = 7, ועם העשר זה 17."),
}

# Kids: the wrong answer text opens with a soft retry.
M = {k: (m, "נסו שוב. " + w) for k, (m, w) in M.items()}
