"""Methods and wrong answer explanations. Keyed by #n, the n-th practice/check step (these nodes have no id)."""
G = "הסבר: כפל הוא חיבור של קבוצות שוות. 2 × 3 פירושו 2 קבוצות של 3: 3 + 3 = 6."
M = {
    "#1": (G, "2 צלחות של 5 עוגיות: 5 + 5 = 10."),
    "#2": (G, "3 שורות של 4 כוכבים: 4 + 4 + 4 = 12."),
    "#3": (G, "המספר 4 מופיע 4 פעמים בחיבור, לכן 4 × 4. התוצאה 16."),
}

# Kids: the wrong answer text opens with a soft retry.
M = {k: (m, "נסו שוב. " + w) for k, (m, w) in M.items()}
