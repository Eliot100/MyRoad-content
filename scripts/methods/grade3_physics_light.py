"""Methods and wrong answer explanations. Keyed by #n, the n-th practice/check step (these nodes have no id)."""
L = "הסבר: אור הולך בקו ישר. כשחפץ עומד בדרך, מאחוריו, בצד שרחוק מהאור, נוצר צל."
M = {
    "#1": (L, "האור בא משמאל ונעצר בעץ. הצל נופל בצד השני, ימינה מהעץ."),
    "#2": (L, "צל נוצר רק כשיש אור. כשהחדר חשוך, אין אור שנחסם, ולכן קשה לראות צל ברור."),
    "#3": (L, "הדובון חוסם את אור הפנס, ולכן על הקיר מאחוריו מופיע צל של הדובון."),
}

# Kids: the wrong answer text opens with a soft retry.
M = {k: (m, "נסו שוב. " + w) for k, (m, w) in M.items()}
