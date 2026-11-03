"""Worked examples shown as learn steps after a topic's learn step, before its practice.
Keyed by topic id: list of (title, body_he, body_content)."""
E = {
    "t_art": [
        ("דוגמה: a בפעם הראשונה", "מדברים על המפתח בפעם הראשונה. לכן a. We found a key.", "We found a key."),
        ("דוגמה: the כשכבר יודעים", "עכשיו כבר יודעים על איזה מפתח מדובר. לכן the. The key was under the mat.", "We found a key. The key was under the mat."),
        ("דוגמה: טעות: the על כללי", "טעות נפוצה: The cats like milk, כשמדברים על כל החתולים. על דבר כללי ברבים לא שמים מילה. נכון: Cats like milk.", "Cats like milk."),
    ],
    "t_perf": [
        ("דוגמה: has ועוד צורה שלישית", "הזמן עוד פתוח, עד עכשיו. עם she אומרים has. She has visited London twice.", "She has visited London twice."),
        ("דוגמה: last year", "last year זמן שנגמר, לכן עבר רגיל. She visited London last year.", "She visited London last year."),
        ("דוגמה: טעות: have עם last night", "טעות נפוצה: We have finished it last night. last night זמן שנגמר. נכון: We finished it last night.", "We finished it last night."),
    ],
    "t_if": [
        ("דוגמה: if עם are", "אחרי if בא הווה: are. בתוצאה בא will. If you are late, we will wait.", "If you are late, we will wait."),
        ("דוגמה: התוצאה קודם", "אפשר להתחיל בתוצאה. גם כך אחרי if בא הווה. We will go out if the sun shines.", "We will go out if the sun shines."),
        ("דוגמה: טעות: will אחרי if", "טעות נפוצה: If he will come, we will eat. אחרי if לא כותבים will. נכון: If he comes, we will eat.", "If he comes, we will eat."),
    ],
    "t_an": [
        ("דוגמה: an egg", "egg נפתחת בצליל תנועה. לכן an. She ate an egg.", "She ate an egg."),
        ("דוגמה: a house", "ב house שומעים את h. זה צליל עיצור, לכן a. They live in a house.", "They live in a house."),
        ("דוגמה: טעות: a orange", "טעות נפוצה: I want a orange. orange נפתחת בצליל תנועה. נכון: I want an orange.", "I want an orange."),
    ],
    "t_order": [
        ("דוגמה: נושא, פועל, מושא", "Dan הוא הנושא, bought הפועל, a phone המושא. Dan bought a phone.", "Dan bought a phone."),
        ("דוגמה: תואר לפני השם", "התואר small בא לפני השם flat. We live in a small flat.", "We live in a small flat."),
        ("דוגמה: טעות: תואר אחרי השם", "טעות נפוצה: He has a house big. באנגלית התואר בא לפני השם. נכון: He has a big house.", "He has a big house."),
    ],
    "t_for": [
        ("דוגמה: for עם משך", "six months זה משך. לכן for. She has worked here for six months.", "She has worked here for six months."),
        ("דוגמה: since עם נקודה", "2015 זו נקודת התחלה. לכן since. We have known them since 2015.", "We have known them since 2015."),
        ("דוגמה: טעות: since עם משך", "טעות נפוצה: I have lived here since five years. five years זה משך. נכון: I have lived here for five years.", "I have lived here for five years."),
    ],
}
