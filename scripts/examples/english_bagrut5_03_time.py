"""Worked examples shown as learn steps after a topic's learn step, before its practice.
Keyed by topic id: list of (title, body_he, body_content)."""
E = {
    "t_past": [
        ("דוגמה: ed אחרי הפועל", "זה קרה אתמול. מוסיפים ed לפועל. Yesterday she cooked dinner.", "Yesterday she cooked dinner."),
        ("דוגמה: עבר עם last night", "last night זה עבר. לכן played עם ed. We played cards last night.", "We played cards last night."),
        ("דוגמה: טעות: הווה עם yesterday", "טעות נפוצה: Yesterday he open the door. yesterday דורש עבר. נכון: Yesterday he opened the door.", "Yesterday he opened the door."),
    ],
    "t_fut": [
        ("דוגמה: will", "מחר. will ואחריו הפועל הבסיסי. Tomorrow she will call her mom.", "Tomorrow she will call her mom."),
        ("דוגמה: תוכנית קרובה", "יש תוכנית ליום שני. are ועוד ing. We are meeting Dana on Monday.", "We are meeting Dana on Monday."),
        ("דוגמה: טעות: s אחרי will", "טעות נפוצה: Tomorrow he will goes. אחרי will בא הפועל הבסיסי, בלי s. נכון: Tomorrow he will go.", "Tomorrow he will go."),
    ],
    "t_story": [
        ("דוגמה: פרט בסיפור", "שאלה: What did the woman give Jonah? קראו את המשפט השני: offered him half her orange. התשובה: half her orange.", "A woman he did not know offered him half her orange."),
        ("דוגמה: הסקה על הזמן", "שאלה: Was it day or night? בסיפור כתוב last bus ו pharmacy light, ובהמשך In the morning. לכן זה היה בלילה.", "Jonah missed the last bus and waited under the pharmacy light."),
        ("דוגמה: טעות: להוסיף מה שלא כתוב", "טעות נפוצה: רואים pharmacy וחושבים ש Jonah עובד שם. הסיפור לא אומר את זה. הוא רק חיכה ליד האור שלה.", "Jonah missed the last bus and waited under the pharmacy light."),
    ],
    "t_irreg": [
        ("דוגמה: came", "לא כל עבר הוא ed. come נהיה came. She came home late.", "She came home late."),
        ("דוגמה: had", "have נהיה had. We had a long day.", "We had a long day."),
        ("דוגמה: טעות: buyed", "טעות נפוצה: He buyed bread. buy הוא פועל חריג. נכון: He bought bread.", "He bought bread."),
    ],
    "t_ago": [
        ("דוגמה: ago בסוף", "ago בא אחרי משך הזמן ומסתכל אחורה. The bus left ten minutes ago.", "The bus left ten minutes ago."),
        ("דוגמה: tomorrow עם will", "tomorrow מסתכל קדימה, לכן will. Tomorrow we will visit Dana.", "Tomorrow we will visit Dana."),
        ("דוגמה: טעות: ago עם will", "טעות נפוצה: We will meet three days ago. ago הולך עם עבר. נכון: We met three days ago.", "We met three days ago."),
    ],
    "t_who": [
        ("דוגמה: who על אדם", "שאלה: Who offered Jonah half her orange? who שואל על אדם. התשובה: a woman he did not know.", "A woman he did not know offered him half her orange."),
        ("דוגמה: who ו he", "שאלה: Who took the orange? בסיפור כתוב He took it. he הוא Jonah. התשובה: Jonah.", "He took it."),
        ("דוגמה: טעות: אדם במקום מקום", "טעות נפוצה: Where did Jonah leave the oranges? ועונים Jonah. where שואל על מקום. התשובה: at the pharmacy.", "In the morning he left a bag of oranges at the pharmacy."),
    ],
}
