"""Worked examples shown as learn steps after a topic's learn step, before its practice.
Keyed by topic id: list of (title, body_he, body_content).
Fresh sentences for SuperGrok topic plan (merge both): method shown, not passage copies.
Source plan: out/result-2.md / chat 02; sentences rewritten 2026-11-05.
"""
E = {
    "t_read": [
        ("דוגמה: רעיון בפתיחה", "המשפט הראשון מציג את הרעיון. כאן: המעבר פותר בעיה אחת ויוצר אחרת. זה הרעיון, לא פרט.", "Moving the clinic indoors stops the rain. It also puts the queue behind a locked gate."),
        ("דוגמה: פרט תומך", "פרט הוא עובדה כתובה שתומכת ברעיון. המחיר עלה, והקונים עוברים ליד בלי לקנות. זה פרט, לא מסקנה שלנו.", "The same fruit now costs more in sealed packs, and regular buyers walk past without stopping."),
        ("דוגמה: מה לא רעיון", "שם של אדם או מספר לבד אינם הרעיון המרכזי. הרעיון הוא הטענה על כל הקטע.", "A name or a single number is a detail. The main idea is the claim about the whole move."),
    ],
    "t_vocab": [
        ("דוגמה: מילה מהמשפט", "לא פותחים מילון קודם. קוראים את המשפט עם המילה ובודקים איזה פירוש משאיר אותו הגיוני.", "The stall was empty before nine, but a line formed at the one that still sold loose fruit."),
        ("דוגמה: far מההקשר", "far from the bus מתאר מרחק. מחיר או שעה לא מתאימים כאן.", "The hall is clean. It is also far from the bus."),
        ("דוגמה: loose מההקשר", "loose fruit מופיע מול plastic boxes. הניגוד אומר שהפרי לא בקופסה.", "One stall still sold loose fruit. The owner refused the plastic boxes."),
    ],
    "t_ref": [
        ("דוגמה: it אחורה", "it מחליף שם שכבר הופיע. במשפט שלפניו כתוב The hall is clean, לכן it הוא האולם.", "The hall is clean. It is also far from the bus."),
        ("דוגמה: She אחורה", "She counted. מחפשים אחורה את האישה האחרונה. כאן: A reporter.", "A reporter spent three mornings there. She counted empty seats by the door."),
        ("דוגמה: לא לנחש קדימה", "מילת ייחוס לא מצביעה על שם שעוד לא הופיע. קודם השם, אחר כך it או she.", "First the name appears. Only then does it or she replace that name."),
    ],
    "t_detail": [
        ("דוגמה: זמן כתוב", "כמה זמן היא הייתה שם? אם כתוב three mornings, זה פרט. לא מסיקים מעבר לכתוב.", "A reporter spent three mornings there."),
        ("דוגמה: סיבה כתובה", "למה קונים מבוגרים מפסיקים? אם כתוב far from the bus, זו הסיבה בטקסט.", "It is also far from the bus, so older buyers stop coming."),
        ("דוגמה: לא מסקנה", "פרט לא אומר מה אנחנו חושבים. הוא חוזר על מה שכתוב במפורש.", "A detail repeats a fact from the text. It does not add our opinion."),
    ],
    "t_infer": [
        ("דוגמה: שתי עובדות", "הסקה נשענת על שתי עובדות. מחיר גבוה ומרחק מהאוטובוס יחד מצביעים שחלק מהקונים עוזבים.", "Prices rose in sealed packs. The hall sits far from the bus. Together, some buyers leave."),
        ("דוגמה: לא ניחוש", "אם זה לא כתוב ולא נובע משתי עובדות, זו לא הסקה מותרת בבחינה.", "A guess with no line in the text is not a valid inference on the exam."),
        ("דוגמה: הצלחה בעיני מי", "המועצה קוראת להצלחה כי השכירות שולמה. נירה רואה חדר ששכח את הרחוב. שתי נקודות מבט מהטקסט.", "The council calls it a success because the rent is paid. Nira calls it a room that forgot the street."),
    ],
    "t_band": [
        ("דוגמה: חמש מילים במשפט", "בוחרים חמש מילים מהקטע וכותבים משפט חדש משלכם, לא מעתיקים שורה.", "buyers, sealed, packs, bus, leave"),
        ("דוגמה: משפט שלם", "המשפט החדש חייב להיות שלם עם נושא ונשוא, לא רשימת מילים.", "Older buyers leave when sealed packs cost more and the bus is far."),
        ("דוגמה: לא רשימת משרד", "אין צורך ברשימה רשמית. המטרה היא שימוש במילים מהקטע בהקשר חדש.", "Use words from the passage in a new situation, not a ministry word list."),
    ],
}
