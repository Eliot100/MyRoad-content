"""Full worked solutions (worked_method) per step: rule, apply to this item, the answer. Keyed by node id."""
W = {
    "e_t_read_idea": "הטענה המרכזית מחברת את פתיחת הקטע לסופו, ולא נשענת על פרט אחד.\nהקטע אומר שהאולם פתר את הגשם, אבל הוא רחוק ויקר, והקונים המבוגרים הפסיקו לבוא. קופסאות ואוטובוס הם רק פרטים.\nהתשובה: A cleaner market can lose the people it was for.",
    "e_t_read_purpose": "בשאלת מטרה שאלו מה הכותב רוצה שנבין אחרי כל הקטע.\nהכותב מונה מה הפסידו במעבר לאולם: מחיר גבוה, מרחק ודוכנים ריקים. הוא לא מוכר פירות ולא נותן לוח זמנים.\nהתשובה: to show a cost of moving the market.",
    "e_t_read_word": "מילה לא מוכרת מבינים מהמשפט שסביבה. בדקו כל פירוש במקומה.\nבקטע יש stalls ריקים, ותור ליד stall אחד שמוכר פירות. כרטיס או קופסה לא מוכרים פירות.\nהתשובה: tables where people sell.",
    "e_t_vocab_p1": "הציבו כל פירוש במקום המילה ובדקו שהמשפט נשאר הגיוני.\nfar from the bus מתאר מרחק מהאוטובוס, לא מחיר ולא שעה.\nהתשובה: not close.",
    "e_t_vocab_p2": "חפשו בקטע מילה שעומדת מול המילה החדשה. הניגוד עוזר להבין אותה.\nloose fruit מופיע מול plastic boxes, כלומר פרי שלא ארוז.\nהתשובה: not in a box.",
    "e_t_ref_p1": "it מחליפה שם שכבר הופיע. חפשו את השם במשפט שלפניה.\nהמשפט שלפני It הוא The hall is clean, והשם שם הוא the hall.\nהתשובה: the hall.",
    "e_t_ref_chk": "מצאו בקטע את הפועל מהשאלה וקראו מי עושה אותו.\nליד refused the plastic boxes כתוב The owner, Nira.\nהתשובה: Nira.",
    "e_rev1_q": "חזרו על הכלל: it מצביעה על השם האחרון שהופיע לפניה.\nלפני It כתוב The hall is clean. הגשם והאוטובוס לא מופיעים שם.\nהתשובה: It means the hall.",
    "e_t_detail_p1": "פרט מוצאים במילים עצמן. חפשו בקטע את empty stalls וקראו מה כתוב לידן.\nאחרי empty stalls כתוב before nine.\nהתשובה: before nine.",
    "e_t_detail_p2": "בשאלת למה חפשו מילת קישור של סיבה, כמו so או because.\nהמשפט It is also far from the bus, so older buyers stop coming נותן את הסיבה.\nהתשובה: The hall is far from the bus.",
    "e_t_infer_p1": "חפשו את השם מהשאלה, כאן the council, ואת המילה because שאחריו.\nבקטע המועצה קוראת לזה הצלחה because the rent is paid.\nהתשובה: The rent is paid.",
    "e_t_infer_p2": "כדי להבין מה דמות רוצה, חברו את מה שהיא עושה למה שהיא אומרת.\nנירה מסרבת לקופסאות ואומרת שהלקוחות יודעים לבחור פרי בעצמם.\nהתשובה: Customers who choose the fruit themselves.",
    "e_t_band_p1": "דמיינו את המצב שהמשפט מתאר ובחרו את הפירוש שמתאים לו.\na queue at the stall הוא אנשים שעומדים ליד הדוכן ומחכים.\nהתשובה: a line of people waiting.",
    "e_t_band_p2": "בדקו מה הדמות עשתה עם הדבר שבמשפט.\nנירה לא לקחה את הקופסאות, כלומר אמרה להן לא.\nהתשובה: said no.",
    "e_rev2_q": "חזרו לשיטה: פירוש של מילה בודקים לפי מה שקורה סביבה בקטע.\nב stalls מוכרים פירות ויש לידם תור, לכן אלה מקומות מכירה.\nהתשובה: tables where people sell.",
    "e_final_check": "הנקודה של הכותב היא המסקנה שכל הקטע מוביל אליה, בעיקר בסופו.\nהאולם נקי, אבל הקונים מפסיקים לבוא. האוטובוס והפלסטיק הם רק דוגמאות.\nהתשובה: A clean hall can lose its buyers.",
}
