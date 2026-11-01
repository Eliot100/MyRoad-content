"""Methods and wrong answer explanations. Keyed by node id."""
W = "הסבר: קוראים את המילה באנגלית ונזכרים מה היא אומרת בעברית."
M = {
    "practice_dog": (W, "dog היא החיה שנובחת, כלב."),
    "practice_cat": (W, "cat היא החיה שאומרת מיאו, חתול."),
    "check_fish": ("הסבר: קודם מבינים איזו חיה זו, ואז חושבים איפה היא חיה.", "fish הוא דג, ודגים חיים במים."),
    "practice_cow": (W, "cow היא החיה שנותנת חלב, פרה."),
    "practice_horse": (W, "horse היא החיה שרוכבים עליה, סוס."),
    "check_mix": ("הסבר: קודם מבינים איזו חיה זו, ואז חושבים איפה היא עפה.", "bird היא ציפור, וציפורים עפות בשמיים."),
}

# Kids: the wrong answer text opens with a soft retry.
M = {k: (m, "נסו שוב. " + w) for k, (m, w) in M.items()}
