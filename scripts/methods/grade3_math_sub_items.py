"""Methods and wrong answer explanations. Keyed by #n, the n-th practice/check step (these nodes have no id)."""
T = "הסבר: מורידים קודם עד 10, ואז את מה שנשאר. למשל 13 − 5: 13 − 3 = 10, ועוד 2 פחות זה 8."
M = {
    "#1": (T, "12 − 2 = 10, ונשארו עוד 2 להוריד מתוך ה 4. 10 − 2 = 8 תפוחים."),
    "#2": (T, "15 − 5 = 10, ונשאר עוד 1 להוריד מתוך ה 6. 10 − 1 = 9 בלונים."),
    "#3": (T, "14 − 4 = 10, ונשאר עוד 1 להוריד מתוך ה 5. 10 − 1 = 9."),
}

# Kids: the wrong answer text opens with a soft retry.
M = {k: (m, "נסו שוב. " + w) for k, (m, w) in M.items()}
