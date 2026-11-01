"""Methods and wrong answer explanations. Keyed by #n, the n-th practice/check step (these nodes have no id)."""
P = "הסבר: דבר שעומד זז רק כשדוחפים או מושכים אותו. דחיפה חזקה יותר מזיזה אותו יותר."
M = {
    "#1": (P, "עגלה לא זזה לבד ולא כשמסתכלים עליה. צריך לדחוף או למשוך אותה."),
    "#2": (P, "דחיפה עדינה היא כוח קטן, לכן הכדור יזוז קצת."),
    "#3": (P, "מי שדוחף חזק יותר נותן כוח גדול יותר, ולכן הקופסה תזוז רחוק יותר."),
}

# Kids: the wrong answer text opens with a soft retry.
M = {k: (m, "נסו שוב. " + w) for k, (m, w) in M.items()}
