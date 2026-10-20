#!/usr/bin/env python3
"""Write the English 5-unit paths. Explanations are Hebrew. The English being learned is in body_content.

Run from anywhere. Writes adult/path_english_bagrut5_*.json next to this script's repo root.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "adult"

PASSAGE_SHORT = (
    "Maya works at home. She starts at eight. She drinks water and opens her mail. "
    "Some days she talks to a client. She stops at four and walks to the park."
)
PASSAGE_250 = (
    "The station library on Herzl Street used to close at noon. Last winter the city "
    "kept it open until eight, after a group of students wrote a letter to the mayor. "
    "They said the afternoon was the only time they could study, because the school "
    "building locked its doors at two. The mayor agreed, but she asked for a plan. "
    "The students offered to shelve books and to sit with younger children during homework hour. "
    "A retired teacher, Mr. Cohen, joined them on Mondays. He does not run the desk. "
    "He listens, and he asks one question before he gives an answer. "
    "Not everyone was pleased. Two shop owners said the evening light made the street noisy. "
    "The library staff counted the visitors for a month. On school nights the room was full. "
    "On Fridays it was quiet. The city did not add money for new books, so the students "
    "collected used ones from their neighbours. The rule is simple: a book can leave for two weeks, "
    "and a dictionary stays in the room. Maya, who works nearby, comes after four and reads the paper. "
    "She says the library is not a school and not a shop. It is the one room on the street where nobody asks her to hurry."
)
PASSAGE_E = (
    "When a town moves its market from the square to a closed hall, it solves the rain "
    "and creates a new problem. People who came for tomatoes now walk past shops that sell "
    "the same tomatoes in plastic boxes at a higher price. The hall is clean. It is also "
    "far from the bus, so older buyers stop coming. A reporter spent three Saturdays there. "
    "She counted empty stalls before nine and a queue at the one stall that still sold loose fruit. "
    "The owner, Nira, refused the plastic boxes. She said her customers know how to choose a peach. "
    "The council calls the hall a success because the rent is paid. Nira calls it a room that forgot the street."
)
PASSAGE_G = (
    "Cities tell young people to learn a trade and then act surprised when those people leave. "
    "A trade needs tools, a first client, and a room that does not cost more than the wage. "
    "In many towns the room is the part that fails. A carpenter can borrow tools. "
    "He cannot borrow a rent that doubles in a year. Some councils answer with a shared workshop: "
    "one address, many benches, a lease the city holds. The idea is not charity. "
    "The city keeps a worker who would otherwise take the skill to another place. "
    "Critics say a shared bench teaches people to wait for help. "
    "The record in the towns that tried it is plainer. The workshops that lasted "
    "charged a small fee, kept a waiting list, and asked every member to teach one hour a month. "
    "The workshops that were free and had no duty closed within a year. "
    "A skill grows when the room stays, and the room stays when someone besides the learner pays attention."
)
STORY = (
    "Jonah missed the last bus and waited under the pharmacy light. A woman he did not know "
    "offered him half her orange. He took it. In the morning he left a bag of oranges at the pharmacy "
    "with a note that said only: for the bus."
)
POEM = (
    "The stair remembers every late key.\n"
    "It does not forgive, and it does not tell.\n"
    "It only keeps the dark one step longer\n"
    "than the hand that finds the rail."
)


def choice(cid: str, label: str) -> dict:
    return {"id": cid, "label": label}


def node(
    nid: str,
    ntype: str,
    title: str,
    body_he: str,
    content: str,
    *,
    kind: str = "understanding",
    review: list[str] | None = None,
    options: list[tuple[str, str]] | None = None,
    correct: str | None = None,
    ok: str | None = None,
    try_: str | None = None,
    speak: str | None = None,
) -> dict:
    row: dict = {
        "id": nid,
        "type": ntype,
        "kind": kind,
        "title": title,
        "body_he": body_he,
        "body_content": content,
    }
    if review:
        row["review_topic_ids"] = review
    if speak:
        row["speak_text"] = speak
    if options:
        row["choices"] = [choice(cid, label) for cid, label in options]
        row["correct"] = correct
        row["feedback_ok"] = ok or "נכון."
        row["feedback_try"] = try_ or "עוד ניסיון. קראו שוב את המשפט."
    return row


def topic(tid: str, he: str, en: str, emoji: str, nodes: list[dict]) -> dict:
    return {
        "id": tid,
        "titles": {"he": he, "en": en},
        "emoji": emoji,
        "node_ids": [n["id"] for n in nodes],
    }


def path_doc(pid: str, he: str, en: str, blurb_he: str, blurb_en: str, emoji: str, minutes: int, prereq: list[str], topics: list[dict], nodes: list[dict]) -> dict:
    return {
        "id": pid,
        "titles": {"he": he, "en": en},
        "blurbs": {"he": blurb_he, "en": blurb_en},
        "subject": "english",
        "group_ids": ["adult"],
        "emoji": emoji,
        "explain_locale": "he",
        "content_locale": "en",
        "estimated_minutes": minutes,
        "prerequisite_path_ids": prereq,
        "topics": topics,
        "nodes": nodes,
    }


def pack(prefix: str, spec: list[tuple]) -> tuple[list[dict], list[dict]]:
    """spec items: (tid, he, en, emoji, learn_he, learn_en, exercises).

    An exercise is (suffix, type, title, body_he, content, options, correct, ok, try, kind, review_ids).
    """
    topics: list[dict] = []
    nodes: list[dict] = []
    for item in spec:
        tid, he, en, emoji, learn_he, learn_en, exercises = item
        built = [
            node(f"{prefix}_{tid}_learn", "learn", he, learn_he, learn_en),
        ]
        for ex in exercises:
            suffix, ntype, title, body, content, options, correct, ok, try_, kind, review = ex
            built.append(
                node(
                    f"{prefix}_{tid}_{suffix}",
                    ntype,
                    title,
                    body,
                    content,
                    kind=kind,
                    review=review,
                    options=options,
                    correct=correct,
                    ok=ok,
                    try_=try_,
                    speak=content if ntype == "speak" else None,
                )
            )
        topics.append(topic(tid, he, en, emoji, built))
        nodes.extend(built)
    return topics, nodes


def mc(suffix: str, title: str, body: str, content: str, options: list[tuple[str, str]], correct: str, ok: str, try_: str, *, kind: str = "understanding", review: list[str] | None = None, ntype: str = "practice") -> tuple:
    return (suffix, ntype, title, body, content, options, correct, ok, try_, kind, review)


# --- placement: no new teaching, four probes plus a result ---

def placement() -> dict:
    p = "plc"
    spec = [
        (
            "t_letters", "אותיות וצלילים", "Letters and sounds", "א",
            "אין כאן שיעור חדש. סמנו מה שכבר ברור. אם זה לא ברור, זו הרמה, לא כישלון.",
            "A is a letter.",
            [
                mc("p1", "האות הראשונה", "איזו אות פותחת את המילה?", "cat",
                   [("a", "c"), ("b", "t"), ("c", "a")], "a", "המילה נפתחת ב-c.", "הצליל הראשון הוא c, לא a."),
                mc("chk", "צליל בסוף", "איזו אות נשמעת בסוף?", "dog",
                   [("a", "g"), ("b", "d"), ("c", "o")], "a", "הסוף הוא g.", "התחלה היא d. הסוף הוא g.", ntype="check"),
            ],
        ),
        (
            "t_be", "יש לי am ו-are", "am, is, are", "ב",
            "עדיין לא לומדים. רק בודקים אם המשפט עומד בלי חור.",
            "I am here.",
            [
                mc("p1", "I", "מה חסר אחרי I?", "I ___ a student.",
                   [("a", "am"), ("b", "is"), ("c", "are")], "a", "אחרי I בא am.", "is הולך עם he או she. אחרי I בא am."),
                mc("chk", "you", "מה חסר אחרי you?", "You ___ ready.",
                   [("a", "is"), ("b", "am"), ("c", "are")], "c", "אחרי you בא are.", "am שייך רק ל-I.", ntype="check"),
            ],
        ),
        (
            "t_present", "הווה", "Present", "ג",
            "בדיקה של הרגל: he מקבל s, ושאלה מתחילה ב-do או does.",
            "She works at home.",
            [
                mc("p1", "he", "איזה משפט תקין?", "He ___ every day.",
                   [("a", "work"), ("b", "works"), ("c", "working")], "b", "אחרי he נוסיף s.", "אחרי he הפועל מקבל s: works."),
                mc("chk", "שאלה", "איזו שאלה תקינה?", "___ you live here?",
                   [("a", "Do"), ("b", "Does"), ("c", "Are"),], "a", "עם you שואלים Do.", "Does הולך עם he, she, it.", ntype="check"),
            ],
        ),
        (
            "t_time", "עבר ועתיד", "Past and future", "ד",
            "בדיקה קצרה. לא מלמדים כאן את הצורה.",
            "Yesterday I walked home.",
            [
                mc("p1", "אתמול", "איזה משפט על אתמול?", "Yesterday she ___ the door.",
                   [("a", "open"), ("b", "opened"), ("c", "opens")], "b", "אתמול: opened.", "opens הוא הווה. אתמול צריך opened."),
                mc("chk", "מחר", "איזה משפט על מחר?", "Tomorrow they ___ early.",
                   [("a", "will leave"), ("b", "left"), ("c", "leaves")], "a", "מחר: will leave.", "left הוא עבר.", ntype="check"),
            ],
        ),
        (
            "t_read", "קטע של כמאתיים וחמישים מילים", "A longer passage", "ה",
            "קראו את הקטע. השאלות הן רעיון מרכזי, פרט, הסקה, ומילה מהקשר.",
            PASSAGE_250,
            [
                mc("idea", "רעיון מרכזי", "על מה הקטע?", PASSAGE_250,
                   [("a", "Students kept a library open in the evening."), ("b", "The mayor closed the school."), ("c", "Maya bought the street.")],
                   "a", "הסטודנטים השאירו את הספרייה פתוחה בערב.", "העירייה לא סגרה את בית הספר. הספרייה נפתחה לערב."),
                mc("detail", "פרט", "מה מר כהן עושה?", PASSAGE_250,
                   [("a", "He runs the desk."), ("b", "He listens and asks one question."), ("c", "He sells books.")],
                   "b", "הוא מקשיב ושואל שאלה אחת.", "כתוב שהוא לא מנהל את הדלפק."),
                mc("infer", "הסקה", "למה הספרייה שקטה בימי שישי?", PASSAGE_250,
                   [("a", "The text says school nights are full and Fridays are quiet."), ("b", "The mayor locked the door."), ("c", "There are no books.")],
                   "a", "בערבי לימודים מלא, ובימי שישי שקט.", "אין בטקסט נעילה ביום שישי."),
                mc("word", "מילה מהקשר", "מה פירוש neighbours כאן?", PASSAGE_250,
                   [("a", "people who live nearby"), ("b", "library fines"), ("c", "bus drivers")],
                   "a", "שכנים, אנשים שגרים קרוב.", "הם הביאו ספרים משומשים, לא קנסות.", ntype="check"),
            ],
        ),
        (
            "t_write", "משפט כתוב", "A written sentence", "ו",
            "עוד אין חיבור. רק משפט אחד תקין שאפשר להרחיב אחר כך.",
            "I think the library should stay open.",
            [
                mc("p1", "משפט דעה", "איזה משפט עומד לבד?", "Choose the sentence that is complete.",
                   [("a", "I think the library should stay open."), ("b", "Because the library."), ("c", "Should stay.")],
                   "a", "יש נושא ופועל ודעה.", "Because לבד הוא לא משפט."),
                mc("chk", "אורך", "איזה משפט מתאים לפתיחת חיבור קצר?", "Choose a clear opening.",
                   [("a", "In my opinion, evening hours help students."), ("b", "Hours students help."), ("c", "Opinion because.")],
                   "a", "פתיחה ברורה.", "השני והשלישי לא משפטים.", ntype="check"),
            ],
        ),
        (
            "t_speak", "משפט בקול", "One spoken sentence", "ז",
            "אמרו את המשפט. אין רשימת מילים חדשה.",
            "I am ready.",
            [
                (
                    "say", "speak", "אמרו", "אמרו את המשפט לאט, ואז סמנו שהמשכתם.",
                    "I am ready.", None, None, None, None, "understanding", None,
                ),
            ],
        ),
        (
            "t_end", "מה יוצא מהמבדק", "What the check means", "ח",
            "אם היו הרבה טעויות, השרשרת פותחת את הדרך מההתחלה. אם היו מעט, היא פותחת מזמן וסיפור. אם עברתם נקי, היא פותחת משאלון E. הדרכים שמעל הפער נשארות סגורות עד שסוגרים אותו.",
            "The chain opens at the weak band.",
            [],
        ),
    ]
    # t_end has no exercises: pack still adds a learn. Add a celebrate by hand after pack.
    topics, nodes = pack(p, spec)
    nodes.append(
        node(
            "plc_t_end_done",
            "celebrate",
            "סיום המבדק",
            "המבדק נגמר. חזרו לשרשרת. הדרך עם הסימון התחילו כאן היא הפער, לא עונש.",
            "Start at the marked road.",
        )
    )
    topics[-1]["node_ids"].append("plc_t_end_done")
    return path_doc(
        "path_english_bagrut5_00_placement",
        "מבדק רמה לאנגלית",
        "English level check",
        "ארבעה אזורים בלי חומר חדש: אותיות, הווה, זמן, וקטע. לפי הטעויות נפתחת הדרך שסוגרת את הפער.",
        "No new material. Letters, present, time, and a passage. Mistakes open the road that closes the gap.",
        "🧭",
        40,
        [],
        topics,
        nodes,
    )


def _review_block(prefix: str, n: int, review_ids: list[str]) -> tuple[dict, list[dict]]:
    bank = REV[prefix]
    content, options, correct, ok, try_ = bank[(n - 1) % len(bank)]
    rev_nodes = [
        node(
            f"{prefix}_rev{n}_learn",
            "learn",
            "חזרה מעורבת",
            "שאלות ממה שכבר נגמר. אין מילה חדשה.",
            "Review only.",
            kind="review",
            review=review_ids,
        ),
        node(
            f"{prefix}_rev{n}_q",
            "practice",
            "חזרה",
            "בחרו את המשפט התקין מתוך מה שכבר למדתם.",
            content,
            kind="review",
            review=review_ids,
            options=options,
            correct=correct,
            ok=ok,
            try_=try_,
        ),
    ]
    rev_topic = topic(f"t_review_{n}", "חזרה מעורבת", "Mixed review", "↻", rev_nodes)
    return rev_topic, rev_nodes


def teach(pid: str, he: str, en: str, blurb_he: str, blurb_en: str, emoji: str, minutes: int, prereq: str, prefix: str, spec: list) -> dict:
    """Content topics, a mixed review after every three, then a final check."""
    topics, nodes = pack(prefix, spec)
    built_topics: list[dict] = []
    built_nodes: list[dict] = []
    chunk: list[str] = []
    review_n = 0
    by_id = {n["id"]: n for n in nodes}
    for item in topics:
        built_topics.append(item)
        built_nodes.extend(by_id[nid] for nid in item["node_ids"])
        chunk.append(item["id"])
        if len(chunk) == 3:
            review_n += 1
            rev_topic, rev_nodes = _review_block(prefix, review_n, chunk)
            built_topics.append(rev_topic)
            built_nodes.extend(rev_nodes)
            chunk = []
    final_content, final_options, final_correct, final_ok, final_try = FIN[prefix]
    end = [
        node(
            f"{prefix}_final_check", "check", "בדיקת סוף", "שאלה אחת על כל הדרך.", final_content,
            options=final_options, correct=final_correct, ok=final_ok, try_=final_try,
        ),
        node(
            f"{prefix}_celebrate", "celebrate", "סוף הדרך",
            "הדרך הזו נגמרה. חזרו לשרשרת. אם זו הייתה דרך הפער, הדרך הבאה נפתחת.",
            "This road is done.",
        ),
    ]
    end_topic = topic("t_end", "סיום", "End", "✓", end)
    built_topics.append(end_topic)
    built_nodes.extend(end)
    return path_doc(pid, he, en, blurb_he, blurb_en, emoji, minutes, [prereq], built_topics, built_nodes)


BE = [
    mc("p1", "I", "מה נכון?", "I ___ tired.", [("a", "am"), ("b", "is"), ("c", "are")], "a", "I am.", "is לא בא אחרי I."),
    mc("p2", "she", "מה נכון?", "She ___ at home.", [("a", "are"), ("b", "am"), ("c", "is")], "c", "She is.", "are בא אחרי you או they."),
]
THERE = [
    mc("p1", "אחד", "שם אחד.", "There ___ a book.", [("a", "is"), ("b", "are"), ("c", "am")], "a", "There is a book.", "a book הוא אחד, לכן is."),
    mc("p2", "כמה", "יותר מאחד.", "There ___ two books.", [("a", "is"), ("b", "are"), ("c", "am")], "b", "There are two books.", "two צריך are."),
]
QUEST = [
    mc("p1", "you", "שאלה עם you.", "___ you work here?", [("a", "Do"), ("b", "Does"), ("c", "Is")], "a", "Do you.", "Does לא הולך עם you."),
    mc("p2", "she", "שאלה עם she.", "___ she live here?", [("a", "Do"), ("b", "Does"), ("c", "Are")], "b", "Does she.", "עם she שואלים Does, בלי s על הפועל."),
]
PAST = [
    mc("p1", "אתמול", "עבר רגיל.", "Yesterday he ___ the letter.", [("a", "sends"), ("b", "sent"), ("c", "will send")], "b", "sent.", "sends הוא הווה."),
    mc("p2", "שלילה", "שלילה בעבר.", "She ___ not go.", [("a", "did"), ("b", "does"), ("c", "is")], "a", "did not go.", "אחרי did הפועל נשאר go, בלי ed."),
]
FUT = [
    mc("p1", "מחר", "עתיד.", "Tomorrow I ___ early.", [("a", "leave"), ("b", "will leave"), ("c", "left")], "b", "will leave.", "left הוא אתמול."),
    mc("p2", "תוכנית", "תוכנית קרובה.", "We ___ the bus at seven.", [("a", "are catching"), ("b", "caught"), ("c", "catches")], "a", "are catching.", "זו תוכנית מסודרת, לא עבר."),
]
ART = [
    mc("p1", "ראשון", "פעם ראשונה.", "I saw ___ bird.", [("a", "a"), ("b", "the"), ("c", "an")], "a", "a bird.", "the כשמדובר בציפור שכבר הזכרנו."),
    mc("p2", "ידוע", "כבר דיברנו עליו.", "___ bird was blue.", [("a", "A"), ("b", "The"), ("c", "An")], "b", "The bird.", "אחרי שהזכרנו, The."),
]
PERF = [
    mc("p1", "ניסיון", "עד עכשיו.", "I ___ this film.", [("a", "have seen"), ("b", "saw"), ("c", "seen")], "a", "have seen.", "saw צריך זמן כמו yesterday."),
    mc("p2", "אתמול", "זמן סגור.", "I ___ it yesterday.", [("a", "have seen"), ("b", "saw"), ("c", "seen")], "b", "saw yesterday.", "עם yesterday לא משתמשים ב-have."),
]
COND = [
    mc("p1", "אם", "תנאי ראשון.", "If it rains, we ___ home.", [("a", "will stay"), ("b", "stayed"), ("c", "stays")], "a", "will stay.", "אם אפשרי עכשיו: will."),
    mc("p2", "סדר", "סדר מילים.", "Which order is English?",
       [("a", "I always drink water."), ("b", "I drink always water."), ("c", "Always I drink water the.")],
       "a", "always לפני הפועל.", "always לא נכנס בין הפועל למושא."),
]

# Review item and final check, one per road. They reuse the road's own sentences.
REV = {
    "z": [
        ("I ___ a student.", [("a", "am"), ("b", "is"), ("c", "are")], "a", "I am.", "אחרי I בא am."),
        ("You ___ ready.", [("a", "are"), ("b", "is"), ("c", "am")], "a", "You are.", "am שייך רק ל-I."),
    ],
    "pr": [
        ("She ___ at home.", [("a", "work"), ("b", "works"), ("c", "working")], "b", "works.", "אחרי she יש s."),
        ("There ___ two books.", [("a", "are"), ("b", "is"), ("c", "am")], "a", "There are.", "two צריך are."),
    ],
    "tm": [
        ("Yesterday he ___ home.", [("a", "walked"), ("b", "walks"), ("c", "walking")], "a", "walked.", "אתמול הוא עבר."),
        ("Tomorrow we ___ early.", [("a", "will leave"), ("b", "left"), ("c", "leaves")], "a", "will leave.", "left הוא אתמול."),
    ],
    "ac": [
        ("I ___ this film yesterday.", [("a", "saw"), ("b", "have seen"), ("c", "seen")], "a", "saw yesterday.", "עם yesterday אין have."),
        ("If it rains, we ___ home.", [("a", "will stay"), ("b", "stayed"), ("c", "stays")], "a", "will stay.", "תנאי אפשרי: will."),
    ],
    "e": [
        ("The hall is clean. It is also far.", [("a", "It means the hall."), ("b", "It means the rain."), ("c", "It means the bus.")], "a", "it הוא האולם.", "הגשם אינו הנושא."),
        ("What does stalls mean here?", [("a", "tables where people sell"), ("b", "bus tickets"), ("c", "plastic boxes")], "a", "דוכנים.", "הכתבת ספרה דוכנים."),
    ],
    "g": [
        ("Choose a reason, not a repeat.", [("a", "A fee gives a reason to keep the lease."), ("b", "A fee is a fee."), ("c", "Because fee.")], "a", "זה נימוק.", "חזרה אינה נימוק."),
        ("Which workshops lasted?", [("a", "Ones with a fee and a duty."), ("b", "Free rooms with no duty."), ("c", "Rooms with double rent.")], "a", "דמי שימוש וחובה.", "החינם בלי חובה נסגר."),
    ],
    "lit": [
        ("What changes in the story?", [("a", "Jonah returns the kindness."), ("b", "The bus comes back."), ("c", "The poem locks the door.")], "a", "החסד חוזר.", "האוטובוס כבר הלך."),
        ("What do the stairs do?", [("a", "They keep the dark a little longer."), ("b", "They forgive the key."), ("c", "They call someone.")], "a", "החושך נשאר עוד רגע.", "כתוב שהן לא סולחות."),
    ],
    "ex": [
        ("Choose the essay shape.", [("a", "Opinion, a reason, a closing sentence."), ("b", "A list of prices."), ("c", "Because because.")], "a", "דעה, סיבה, סיום.", "מחירון אינו חיבור."),
        ("higher price means", [("a", "it costs more"), ("b", "it is closer"), ("c", "it is free")], "a", "עולה יותר.", "closer הוא מרחק."),
    ],
}
FIN = {
    "z": ("They ___ not late.", [("a", "are"), ("b", "is"), ("c", "am")], "a", "They are not.", "is לא הולך עם they."),
    "pr": ("___ there a book on the desk?", [("a", "Is"), ("b", "Are"), ("c", "Do")], "a", "Is there a book.", "a book הוא אחד."),
    "tm": ("Tomorrow we ___ early.", [("a", "will leave"), ("b", "left"), ("c", "leaves")], "a", "will leave.", "left הוא אתמול."),
    "ac": ("If it rains, I ___ a coat.", [("a", "will take"), ("b", "took"), ("c", "taken")], "a", "will take.", "תנאי ראשון: will."),
    "e": ("What is the writer's point?", [("a", "A clean hall can lose its buyers."), ("b", "Plastic is cheaper."), ("c", "The bus is the subject.")], "a", "האולם הנקי איבד קונים.", "הקופסה יקרה יותר, לא זולה."),
    "g": ("A 70-word essay when the range is 120 to 140.", [("a", "Length loses points. Content can still earn some."), ("b", "The whole paper is zero."), ("c", "Length is ignored.")], "a", "אורך לחוד, תוכן לחוד.", "לא מאפסים הכל בגלל אורך."),
    "lit": ("How does the poem sound?", [("a", "Quiet and a little strict."), ("b", "A joke."), ("c", "A shopping list.")], "a", "שקט וקצת קשוח.", "אין בדיחה."),
    "ex": ("Spelling in a reading answer.", [("a", "Spelling alone does not remove the reading points."), ("b", "One spelling error zeros the paper."), ("c", "Accuracy is ignored in the essay.")], "a", "בכתיב בקריאה לא מורידים.", "בחיבור הדיוק כן נספר."),
}


def all_paths() -> list[dict]:
    place = "path_english_bagrut5_00_placement"
    docs = [placement()]
    docs.append(teach(
        "path_english_bagrut5_01_zero", "מאפס", "First letters",
        "אותיות, צלילים, ומשפט עם am, is, are. זו הדרך שנפתחת כשהמבדק מראה בסיס רופף.",
        "Letters, sounds, and am, is, are.",
        "א", 90, place, "z",
        [
            ("t_letters", "אותיות", "Letters", "א", "אומרים את שם האות, ואז קוראים מילה קצרה.", "A, B, C.",
             [mc("p1", "פתיחה", "במה נפתחת המילה?", "sun", [("a", "s"), ("b", "n"), ("c", "u")], "a", "s.", "הסוף הוא n."),
              mc("p2", "סוף", "במה נגמרת?", "map", [("a", "m"), ("b", "p"), ("c", "a")], "b", "p.", "ההתחלה היא m.")]),
            ("t_be", "am is are", "am, is, are", "ב", "I הולך עם am. He, she, it עם is. You, we, they עם are.", "I am a student.",
             BE),
            ("t_not", "שלילה", "not", "ג", "שלילה: am not, is not, are not. לא מוסיפים do.", "She is not late.",
             [mc("p1", "שלילה", "מה תקין?", "They ___ ready.", [("a", "are not"), ("b", "is not"), ("c", "am not")], "a", "They are not.", "is לא הולך עם they."),
              mc("p2", "I", "שלילה של I.", "I ___ hungry.", [("a", "am not"), ("b", "is not"), ("c", "do not am")], "a", "I am not.", "אין do לפני am.")]),
            ("t_you", "you ו-we", "you and we", "ד", "you, we, they הולכים עם are. לא עם am.", "You are ready. We are here.",
             [mc("p1", "we", "מה נכון?", "We ___ students.", [("a", "are"), ("b", "is"), ("c", "am")], "a", "We are.", "am רק אחרי I."),
              mc("p2", "they", "הם.", "They ___ at school.", [("a", "are"), ("b", "is"), ("c", "am")], "a", "They are.", "is לא הולך עם they.")]),
            ("t_word", "מילה קצרה", "A short word", "ה", "קוראים את כל המילה, לא רק את האות הראשונה.", "sun, map, dog",
             [mc("p1", "קריאה", "איזו מילה זו?", "s-u-n", [("a", "sun"), ("b", "bus"), ("c", "son")], "a", "sun.", "bus מתחיל ב-b."),
              mc("p2", "אות", "איזו אות חסרה?", "c_t", [("a", "a"), ("b", "o"), ("c", "e")], "a", "cat.", "המילה הקצרה היא cat.")]),
            ("t_sent", "משפט", "A sentence", "ו", "משפט מתחיל באות גדולה ונגמר בנקודה. יש בו מישהו ופועל.", "I am here.",
             [mc("p1", "שלם", "איזה משפט שלם?", "Choose.",
                 [("a", "I am here."), ("b", "Am here."), ("c", "I here.")], "a", "יש I ויש am.", "בלי פועל זה לא משפט."),
              mc("p2", "גדולה", "איך פותחים משפט?", "___ am a student.",
                 [("a", "I"), ("b", "i"), ("c", "am")], "a", "I גדולה.", "i קטנה לא פותחת משפט.")]),
        ],
    ))
    docs.append(teach(
        "path_english_bagrut5_02_present", "הווה ויום יום", "Present and daily life",
        "Present Simple, there is, ושאלות. קטע קצר בסוף.",
        "Present Simple, there is, and questions.",
        "ב", 120, place, "pr",
        [
            ("t_simple", "Present Simple", "Present Simple", "א", "הרגל. אחרי he, she, it הפועל מקבל s.", "She works at home.",
             [mc("p1", "he", "השלימו.", "He ___ coffee.", [("a", "drink"), ("b", "drinks"), ("c", "drinking")], "b", "drinks.", "אחרי he יש s."),
              mc("p2", "they", "בלי s.", "They ___ early.", [("a", "starts"), ("b", "start"), ("c", "starting")], "b", "start.", "they לא מקבל s.")]),
            ("t_there", "there is", "there is", "ב", "יש אחד: there is. יש כמה: there are.", "There is a book on the desk.",
             THERE),
            ("t_q", "שאלות", "Questions", "ג", "שאלה בהווה: Do או Does בהתחלה, והפועל בלי s.", "Do you live here?",
             QUEST),
            ("t_day", "יום רגיל", "A normal day", "ד", "always יושב לפני הפועל העיקרי.", PASSAGE_SHORT,
             [mc("idea", "רעיון", "מה מאיה עושה?", PASSAGE_SHORT,
                 [("a", "She works at home."), ("b", "She closes the library."), ("c", "She drives a bus.")],
                 "a", "היא עובדת מהבית.", "אין אוטובוס בקטע."),
              mc("detail", "שעה", "מתי היא מתחילה?", PASSAGE_SHORT,
                 [("a", "at eight"), ("b", "at four"), ("c", "at noon")],
                 "a", "at eight.", "at four היא עוצרת.")]),
            ("t_neg", "שלילה בהווה", "don't and doesn't", "ה", "שלילה: do not או does not, והפועל בלי s.", "She does not work on Friday.",
             [mc("p1", "she", "שלילה.", "She ___ like coffee.", [("a", "does not"), ("b", "do not"), ("c", "is not")], "a", "does not.", "עם she יש does."),
              mc("p2", "they", "רבים.", "They ___ live here.", [("a", "do not"), ("b", "does not"), ("c", "are not work")], "a", "do not.", "they הולך עם do.")]),
            ("t_freq", "תדירות", "always and never", "ו", "always ו-never יושבים לפני הפועל העיקרי.", "Maya always starts at eight.",
             [mc("p1", "always", "איפה always?", "Choose the English order.",
                 [("a", "She always walks."), ("b", "She walks always."), ("c", "Always she walks the.")], "a", "לפני הפועל.", "always לא אחרי הפועל."),
              mc("p2", "never", "שלילה רכה.", "He ___ late.", [("a", "is never"), ("b", "never is"), ("c", "does never")], "a", "is never.", "אחרי am/is/are התדירות באה מיד.")]),
        ],
    ))
    docs.append(teach(
        "path_english_bagrut5_03_time", "זמן וסיפור", "Time and story",
        "עבר, עתיד, וקטע קצר עם רעיון מרכזי והסקה.",
        "Past, future, and a short story.",
        "ג", 140, place, "tm",
        [
            ("t_past", "Past Simple", "Past Simple", "א", "אתמול: פועל עם ed, או צורה חריגה כמו went ו-saw.", "Yesterday I walked home.",
             PAST),
            ("t_fut", "עתיד", "Future", "ב", "מחר: will והפועל הבסיסי. תוכנית קרובה: am/is/are ו-ing.", "Tomorrow I will leave early.",
             FUT),
            ("t_story", "סיפור קצר", "A short story", "ג", "קראו וזהו את הרעיון ואת ההסקה.", STORY,
             [mc("idea", "רעיון", "מה קורה בסיפור?", STORY,
                 [("a", "A stranger shares an orange, and Jonah returns the kindness."), ("b", "Jonah buys the pharmacy."), ("c", "The bus never stops.")],
                 "a", "נדיבות קטנה שחוזרת.", "הוא לא קונה את בית המרקחת."),
              mc("infer", "הסקה", "למה הפתק קצר?", STORY,
                 [("a", "He does not need her name to return the kindness."), ("b", "He cannot write."), ("c", "The pharmacy is closed forever.")],
                 "a", "הנדיבות לא צריכה שם.", "אין בטקסט שהוא לא יודע לכתוב.")]),
            ("t_irreg", "עבר חריג", "went and saw", "ד", "לא כל עבר הוא ed. go נהיה went. see נהיה saw.", "Yesterday I went home. I saw the bus.",
             [mc("p1", "go", "אתמול.", "Yesterday she ___ home.", [("a", "went"), ("b", "goed"), ("c", "goes")], "a", "went.", "אין goed."),
              mc("p2", "see", "ראה.", "I ___ the note.", [("a", "saw"), ("b", "seed"), ("c", "seen")], "a", "saw.", "seen צריך have.")]),
            ("t_ago", "מתי", "ago and tomorrow", "ה", "ago מסתכל אחורה. tomorrow מסתכל קדימה. לא מערבבים.", "I saw her two days ago.",
             [mc("p1", "ago", "לפני יומיים.", "I met him two days ___.", [("a", "ago"), ("b", "tomorrow"), ("c", "will")], "a", "ago.", "tomorrow הוא מחר."),
              mc("p2", "מחר", "כיוון.", "___ I will call.", [("a", "Tomorrow"), ("b", "Ago"), ("c", "Yesterday")], "a", "Tomorrow.", "yesterday כבר עבר.")]),
            ("t_who", "מי ואיפה", "Who and where", "ו", "who שואל על אדם. where שואל על מקום.", STORY,
             [mc("p1", "who", "מי חיכה?", STORY,
                 [("a", "Jonah"), ("b", "the driver"), ("c", "Mr. Cohen")], "a", "Jonah.", "אין נהג שמחכה."),
              mc("p2", "where", "איפה?", STORY,
                 [("a", "under the pharmacy light"), ("b", "in the library"), ("c", "on the bus")], "a", "מתחת לאור של בית המרקחת.", "האוטובוס כבר הלך.")]),
        ],
    ))
    docs.append(teach(
        "path_english_bagrut5_04_accuracy", "דיוק", "Accuracy",
        "a ו-the, סדר מילים, Present Perfect מול עבר, ותנאי ראשון.",
        "Articles, word order, perfect versus past, and the first conditional.",
        "ד", 150, place, "ac",
        [
            ("t_art", "a ו-the", "a and the", "א", "a בפעם הראשונה. the כשכבר יודעים על מה מדובר.", "I saw a bird. The bird was blue.",
             ART),
            ("t_perf", "Perfect מול עבר", "Perfect and past", "ב", "have ועבר שלישי כשאין זמן סגור. זמן כמו yesterday דורש עבר רגיל.", "I have seen this film. I saw it yesterday.",
             PERF),
            ("t_if", "תנאי וסדר", "Conditional and order", "ג", "If ועתיד אפשרי: will. always לפני הפועל.", "If it rains, we will stay home.",
             COND),
            ("t_an", "an", "an", "ד", "an לפני צליל תנועה: an apple, an hour. a לפני צליל עיצור: a bird, a university.", "I ate an apple.",
             [mc("p1", "apple", "לפני apple.", "I want ___ apple.", [("a", "an"), ("b", "a"), ("c", "the")], "a", "an apple.", "apple נפתח בתנועה."),
              mc("p2", "university", "הצליל, לא האות.", "She has ___ university nearby.", [("a", "a"), ("b", "an"), ("c", "the")], "a", "a university.", "הצליל הראשון הוא y, כמו yes.")]),
            ("t_order", "סדר", "Word order", "ה", "הנושא בא לפני הפועל. never ו-always לא נכנסים בין הפועל למושא.", "I never drink coffee at night.",
             [mc("p1", "never", "איפה never?", "Choose.",
                 [("a", "I never drink coffee."), ("b", "I drink never coffee."), ("c", "Never drink I coffee.")], "a", "לפני הפועל.", "never לא בין הפועל למושא."),
              mc("p2", "נושא", "מה בא קודם?", "Choose the sentence.",
                 [("a", "The bird was blue."), ("b", "Was the blue bird sentence no."), ("c", "Blue was bird the.")], "a", "נושא ואז פועל.", "השלישי אינו סדר אנגלי.")]),
            ("t_for", "for ו-since", "for and since", "ו", "for עם משך: for two years. since עם נקודת התחלה: since 2020. yesterday לא הולך עם have.", "I have lived here for two years.",
             [mc("p1", "for", "משך.", "I have known her ___ a year.", [("a", "for"), ("b", "since"), ("c", "ago")], "a", "for a year.", "since צריך נקודה, לא משך."),
              mc("p2", "yesterday", "זמן סגור.", "I ___ her yesterday.", [("a", "saw"), ("b", "have seen"), ("c", "seen")], "a", "saw.", "yesterday סוגר את הזמן.")]),
        ],
    ))
    docs.append(teach(
        "path_english_bagrut5_05_module_e", "שאלון E", "Module E",
        "קטע לא מוכר, שאלות של רעיון, פרט, הסקה, מילה מהקשר, ומטרת הכותב. בלי חיבור ארוך.",
        "An unseen passage and the E question types. No long essay.",
        "ה", 180, place, "e",
        [
            ("t_read", "קטע E", "E passage", "א", "קראו פעם אחת בלי לעצור על כל מילה. אחר כך השאלות.", PASSAGE_E,
             [mc("idea", "רעיון מרכזי", "מה הטענה?", PASSAGE_E,
                 [("a", "A cleaner market can lose the people it was for."), ("b", "Plastic boxes are cheaper."), ("c", "The bus line closed.")],
                 "a", "השוק הנקי איבד את הקונים.", "הקופסאות דווקא יקרות יותר."),
              mc("purpose", "מטרת הכותב", "למה נכתב?", PASSAGE_E,
                 [("a", "to show a cost of moving the market"), ("b", "to sell peaches"), ("c", "to give bus times")],
                 "a", "להראות מחיר של המעבר.", "זו לא מודעת מכירה."),
              mc("word", "מהקשר", "מה פירוש stalls?", PASSAGE_E,
                 [("a", "tables where people sell"), ("b", "bus tickets"), ("c", "plastic boxes")],
                 "a", "דוכנים.", "הכתב ספרה דוכנים ריקים.")]),
            ("t_vocab", "אוצר מילים", "Vocabulary", "ב", "המילה מהמשפט, לא מהמילון לבד.", "The hall is far from the bus.",
             [mc("p1", "far", "far כאן הוא", "far from the bus",
                 [("a", "not close"), ("b", "very cheap"), ("c", "already closed")], "a", "לא קרוב.", "cheap הוא מחיר."),
              mc("p2", "loose", "loose fruit", "loose fruit",
                 [("a", "not in a box"), ("b", "very expensive"), ("c", "already gone")], "a", "לא בקופסה.", "הטקסט מנגיד את זה לקופסה.")]),
            ("t_ref", "מילת ייחוס", "Reference", "ג", "it ו-there מצביעים אחורה, לא קדימה אל ניחוש.", PASSAGE_E,
             [mc("p1", "it", "על מה it במשפט The hall is clean. It is also far?", PASSAGE_E,
                 [("a", "the hall"), ("b", "the rain"), ("c", "the reporter")], "a", "the hall.", "הגשם לא הנושא של המשפט הקודם."),
              mc("chk", "בדיקה", "מי מסרבת לקופסאות?", PASSAGE_E,
                 [("a", "Nira"), ("b", "the mayor"), ("c", "the reporter")], "a", "Nira.", "הכתבת סופרת, היא לא הדוכן.", ntype="check")]),
            ("t_detail", "פרט", "A detail", "ד", "פרט הוא עובדה שכתובה, לא מסקנה שלנו.", PASSAGE_E,
             [mc("p1", "שעה", "מתי הדוכנים ריקים?", PASSAGE_E,
                 [("a", "before nine"), ("b", "at noon only"), ("c", "the text never says")], "a", "לפני תשע.", "הכתבת ספרה לפני תשע."),
              mc("p2", "אוטובוס", "למה קונים מבוגרים מפסיקים?", PASSAGE_E,
                 [("a", "The hall is far from the bus."), ("b", "The peaches are gone."), ("c", "The mayor closed Friday.")], "a", "רחוק מהאוטובוס.", "אין סגירה ביום שישי.")]),
            ("t_infer", "הסקה", "Inference", "ה", "הסקה נשענת על שתי עובדות בטקסט, לא על ניחוש.", PASSAGE_E,
             [mc("p1", "הצלחה", "למה המועצה קוראת לזה הצלחה?", PASSAGE_E,
                 [("a", "The rent is paid."), ("b", "More older buyers come."), ("c", "Nira likes the boxes.")], "a", "השכירות משולמת.", "הקונים המבוגרים דווקא פחתו."),
              mc("p2", "נירה", "מה נירה רוצה?", PASSAGE_E,
                 [("a", "Customers who choose the fruit themselves."), ("b", "A higher rent."), ("c", "A closed hall.")], "a", "שהקונה יבחר.", "היא מסרבת לקופסה.")]),
            ("t_band", "מילים מהקטע", "Words from the passage", "ו", "חמש מילים מתוך הקטע, במשפט חדש. לא רשימת משרד.", "The queue was at the loose fruit.",
             [mc("p1", "queue", "queue", "a queue at the stall",
                 [("a", "a line of people waiting"), ("b", "a plastic box"), ("c", "a bus ticket")], "a", "תור.", "הקופסה היא box."),
              mc("p2", "refused", "refused", "She refused the boxes.",
                 [("a", "said no"), ("b", "paid more"), ("c", "opened early")], "a", "סירבה.", "היא לא שילמה יותר.")]),
        ],
    ))
    docs.append(teach(
        "path_english_bagrut5_06_module_g", "שאלון G", "Module G",
        "קטע ארוך יותר, ואז בחירה של פתיחה וגוף לחיבור דעה של 120 עד 140 מילים. המחוון: תוכן, ארגון, אוצר, ודיוק.",
        "A longer unseen, then an opinion essay judged on content, organization, vocabulary, and accuracy.",
        "ו", 200, place, "g",
        [
            ("t_read", "קטע G", "G passage", "א", "הכותב לא אומר שהסדנה היא צדקה. הוא אומר שהיא נשארת כשיש חובה ותשלום קטן.", PASSAGE_G,
             [mc("idea", "רעיון", "מה נשאר פתוח?", PASSAGE_G,
                 [("a", "Workshops with a fee and a duty."), ("b", "Free rooms with no duty."), ("c", "Higher rent.")],
                 "a", "דמי שימוש וחובת הוראה.", "החינם בלי חובה נסגר."),
              mc("purpose", "מטרה", "למה הפסקה על המבקרים?", PASSAGE_G,
                 [("a", "to answer the claim that help makes people wait"), ("b", "to sell tools"), ("c", "to list bus times")],
                 "a", "תשובה לטענה.", "אין רשימת אוטובוסים.")]),
            ("t_essay", "חיבור דעה", "Opinion essay", "ב", "120 עד 140 מילים. פתיחה עם דעה, שתי סיבות, ומשפט סיום. לא מתחילים ב-Because.", "In my opinion, a shared workshop should charge a small fee.",
             [mc("open", "פתיחה", "איזו פתיחה עומדת?", "Choose an opening.",
                 [("a", "In my opinion, a small fee keeps the room open."), ("b", "Because a fee."), ("c", "Fee room open people.")],
                 "a", "יש דעה ומשפט שלם.", "Because אינו פתיחה."),
              mc("org", "ארגון", "מה חסר בפסקה שהיא רק דוגמה?", "A paragraph of one story and no point.",
                 [("a", "a reason that ties the story to the opinion"), ("b", "another city name"), ("c", "a date")],
                 "a", "צריך סיבה, לא עוד שם.", "תאריך לא מחליף נימוק.")]),
            ("t_rubric", "מחוון", "Rubric", "ג", "תוכן ושכנוע, ארגון, אוצר מילים, ודיוק. אורך קצר מדי יורד לחוד, לא במקום התוכן.", "Content, organization, vocabulary, accuracy, and length.",
             [mc("len", "אורך", "חיבור של 70 מילים כשהטווח הוא 120 עד 140.", "70 words",
                 [("a", "It loses points for length and can still earn content points."), ("b", "It gets zero for everything."), ("c", "Length is ignored.")],
                 "a", "אורך לחוד, תוכן לחוד.", "לא מאפסים את כל החיבור בגלל אורך."),
              mc("chk", "בדיקה", "איזה משפט הוא נימוק ולא חזרה?", "Choose a reason.",
                 [("a", "A fee gives the city a reason to keep the lease."), ("b", "A fee is a fee."), ("c", "Because fee fee.")],
                 "a", "זה נימוק.", "חזרה על המילה אינה נימוק.", ntype="check")]),
            ("t_body", "גוף החיבור", "Two reasons", "ד", "אחרי הפתיחה באות שתי סיבות. כל סיבה במשפט שלם, לא ברשימת מילים.", "A small fee keeps the lease. A duty keeps the skill moving.",
             [mc("p1", "סיבה", "איזו סיבה עומדת?", "Choose.",
                 [("a", "A duty means every member teaches one hour."), ("b", "Duty duty hour."), ("c", "Because duty.")], "a", "משפט עם סיבה.", "השלישי אינו משפט."),
              mc("p2", "שתיים", "כמה סיבות לפני הסיום?", "120 to 140 words",
                 [("a", "two reasons, then a closing sentence"), ("b", "one word, ten times"), ("c", "no opinion at all")], "a", "שתי סיבות וסיום.", "בלי דעה אין חיבור.")]),
            ("t_close", "סיום", "A closing sentence", "ה", "הסיום חוזר לדעה בלי להעתיק את הפתיחה מילה במילה.", "That is why the room should not be free.",
             [mc("p1", "סיום", "איזה סיום מתאים?", "Choose a close.",
                 [("a", "For these reasons, a small fee is worth keeping."), ("b", "Because reasons reasons."), ("c", "Fee.")], "a", "משפט סיום.", "מילה אחת אינה סיום."),
              mc("p2", "העתקה", "מה חלש?", "The last sentence copies the first, word for word.",
                 [("a", "It adds nothing new."), ("b", "It is the best ending."), ("c", "Length no longer counts.")], "a", "אין בו חידוש.", "העתקה אינה סיום.")]),
            ("t_words", "אוצר לחיבור", "Words for the essay", "ו", "שלוש מילים מהקטע, לשימוש בחיבור. לא רשימה רשמית.", "lease, duty, fee",
             [mc("p1", "lease", "lease", "The city holds the lease.",
                 [("a", "the right to use the room"), ("b", "a free tool"), ("c", "a bus line")], "a", "הזכות להשתמש בחדר.", "זה לא אוטובוס."),
              mc("p2", "duty", "duty", "a duty to teach one hour",
                 [("a", "something you must do"), ("b", "a higher price only"), ("c", "a closed door")], "a", "חובה.", "מחיר לבד הוא fee.")]),
        ],
    ))
    docs.append(teach(
        "path_english_bagrut5_07_literature_oral", "ספרות ודיבור", "Literature and speaking",
        "גשר לסיפור ולשיר שנכתבו כאן, חיבור קצר על הטקסט, ושלוש אמירות בעל פה. לא מעתיקים יצירה מהרשימה.",
        "An original story, an original poem, a short essay on the text, and three spoken turns.",
        "ז", 180, place, "lit",
        [
            ("t_story", "סיפור קצר", "A short story", "א", "מי עושה מה, ומה משתנה בסוף. לא צריך את שם המחבר.", STORY,
             [mc("change", "שינוי", "מה משתנה?", STORY,
                 [("a", "Jonah gives back what he was given."), ("b", "The bus arrives at once."), ("c", "The woman moves away.")],
                 "a", "הוא מחזיר את החסד.", "האוטובוס כבר הלך."),
              mc("who", "דמות", "מי נותן את התפוז?", STORY,
                 [("a", "a woman he does not know"), ("b", "the driver"), ("c", "Mr. Cohen")],
                 "a", "אישה שהוא לא מכיר.", "אין נהג שנותן תפוז.")]),
            ("t_poem", "שיר קצר", "A short poem", "ב", "חפץ עושה משהו שאדם עושה. זו התמונה, לא חידה עם תשובה אחת.", POEM,
             [mc("image", "תמונה", "מה המדרגות עושות?", POEM,
                 [("a", "They keep the dark a little longer."), ("b", "They forgive the key."), ("c", "They call the police.")],
                 "a", "החושך נשאר עוד רגע.", "כתוב שהן לא סולחות ולא מספרות."),
              mc("tone", "טון", "איך נשמע השיר?", POEM,
                 [("a", "quiet and a little strict"), ("b", "a joke about buses"), ("c", "a shopping list")],
                 "a", "שקט וקצת קשוח.", "אין בדיחה על אוטובוס.")]),
            ("t_speak", "דיבור", "Speaking", "ג", "שלוש פניות: תגובה אישית, סיבה אחת, ומשפט על הטקסט. אומרים, לא קוראים רשימה.", "I think Jonah is fair because he returns the kindness.",
             [(
                 "s1", "speak", "תגובה", "אמרו משפט אחד: מה דעתכם על יונה.",
                 "I think Jonah is fair.", None, None, None, None, "understanding", None,
              ), (
                 "s2", "speak", "סיבה", "אמרו למה, עם because.",
                 "He is fair because he returns the kindness.", None, None, None, None, "understanding", None,
              )]),
            ("t_essay", "חיבור על הטקסט", "A short essay on the text", "ד", "100 עד 120 מילים על הטקסט: מה קורה, מה אתם חושבים, וסיבה מהסיפור. לא ביוגרפיה.", "Jonah is fair because he leaves the oranges.",
             [mc("p1", "על הטקסט", "איזו פתיחה על הסיפור?", "Choose.",
                 [("a", "Jonah pays the woman back, and I think that is fair."), ("b", "The author was born in."), ("c", "Because orange.")], "a", "על המעשה ועל הדעה.", "אין כאן ביוגרפיה."),
              mc("p2", "ראיה", "מאיפה הסיבה?", "Choose.",
                 [("a", "from something Jonah does in the story"), ("b", "from a fact that is not in the story"), ("c", "from the poem's stair")], "a", "מתוך הסיפור.", "המדרגות הן שיר אחר.")]),
            ("t_poem2", "שורה", "One line", "ה", "בוחרים שורה ואומרים מה היא עושה, לא מה היא 'באמת אומרת' במשפט אחד סגור.", POEM,
             [mc("p1", "שורה", "איזו קריאה צמודה לשורה?", POEM,
                 [("a", "The stair keeps a secret: it does not tell."), ("b", "The stair is a bus."), ("c", "The key is a mayor.")], "a", "היא לא מספרת.", "אין אוטובוס בשיר."),
              mc("p2", "לא חידה", "מה לא נכון לשיר?", POEM,
                 [("a", "There is one hidden answer and no picture."), ("b", "An object acts like a person."), ("c", "The tone is quiet.")], "a", "זו תמונה, לא חידה עם פתרון יחיד.", "החפץ כן פועל כמו אדם.")]),
            ("t_turn", "פנייה שלישית", "A third spoken turn", "ו", "הפנייה השלישית קושרת אתכם לטקסט במשפט אחד, בלי לקרוא רשימה.", "The story matters to me because a small gift can come back.",
             [(
                 "s3", "speak", "עליכם", "אמרו למה הסיפור נוגע בכם, במשפט אחד.",
                 "The story matters to me because a small gift can come back.", None, None, None, None, "understanding", None,
              ), (
                 "s4", "speak", "על השיר", "אמרו משפט אחד על המדרגות.",
                 "The stairs keep the dark a little longer.", None, None, None, None, "understanding", None,
              )]),
        ],
    ))
    docs.append(teach(
        "path_english_bagrut5_08_exam", "בחינה מלאה", "Full exam",
        "ערבוב של קריאה, אוצר מילים, חיבור ודיבור. אין נושא חדש. זה התרגול לרמה של 100.",
        "Reading, vocabulary, writing, and speaking together. No new topic.",
        "ח", 180, place, "ex",
        [
            ("t_mix", "קריאה מעורבת", "Mixed reading", "א", "אותן שאלות כמו בשאלונים, על קטע שכבר מהסוג המוכר.", PASSAGE_E,
             [mc("idea", "רעיון", "בחרו את הרעיון.", PASSAGE_E,
                 [("a", "Moving the market helps the rent and hurts the buyers."), ("b", "Nira loves plastic."), ("c", "Rain is the only subject.")],
                 "a", "השכירות עלתה, הקונים נפגעו.", "נירה מסרבת לפלסטיק."),
              mc("vocab", "מילה", "higher price", "at a higher price",
                 [("a", "it costs more"), ("b", "it is closer"), ("c", "it is free")],
                 "a", "עולה יותר.", "closer הוא מרחק.")]),
            ("t_write", "חיבור", "Essay", "ב", "פתחו בדעה, תנו סיבה מהקטע, וסיימו במשפט אחד. 120 עד 140 מילים כשזה חיבור מלא. כאן בודקים את הצורה.", "In my opinion, the stall should stay.",
             [mc("shape", "צורה", "איזו פיסקה מתאימה למחוון?", "Choose.",
                 [("a", "Opinion, one reason from the text, and a closing sentence."), ("b", "A list of prices only."), ("c", "Because because.")],
                 "a", "דעה, סיבה, סיום.", "מחירון אינו חיבור."),
              mc("chk", "בדיקה", "מה לא מורידים בקריאה לפי החוברת?", "Spelling in a reading answer.",
                 [("a", "Spelling alone does not remove the reading points."), ("b", "One spelling error zeros the paper."), ("c", "Grammar is ignored in the essay.")],
                 "a", "בכתיב בקריאה לא מורידים. בחיבור הדיוק כן נספר.", "בחיבור הדיוק כן נספר.", ntype="check")]),
            ("t_oral", "דיבור אחרון", "Last spoken turn", "ג", "תגובה אישית בלי לקרוא מהדף.", "I agree with Nira because customers should choose the fruit.",
             [(
                 "say", "speak", "אמרו", "אמרו את עמדתכם וסיבה אחת.",
                 "I agree with Nira because customers should choose the fruit.", None, None, None, None, "understanding", None,
              )]),
            ("t_read2", "הסקה בבחינה", "One inference", "ד", "בבחינה ההסקה עדיין חייבת להישען על הקטע.", PASSAGE_G,
             [mc("p1", "הסקה", "מה אפשר להסיק?", PASSAGE_G,
                 [("a", "A room with no duty did not last."), ("b", "Every carpenter leaves the town."), ("c", "Rent never changes.")], "a", "בלי חובה החדר לא נשאר.", "לא כתוב שכולם עוזבים."),
              mc("p2", "מטרה", "מה המטרה של המשפט האחרון?", PASSAGE_G,
                 [("a", "to say the room stays when someone pays attention"), ("b", "to sell a bench"), ("c", "to end without a point")], "a", "החדר נשאר כשמישהו שם לב.", "זו לא מודעה.")]),
            ("t_write2", "אורך ודיוק", "Length and accuracy", "ה", "בחיבור הדיוק נספר. בקריאה כתיב לבדו לא מוריד. האורך הוא סעיף נפרד.", "Accuracy counts in the essay. Spelling in a reading answer does not.",
             [mc("p1", "דיוק", "איפה הדיוק נספר?", "Choose.",
                 [("a", "in the essay"), ("b", "only in a one-word reading answer"), ("c", "nowhere")], "a", "בחיבור.", "בקריאה הקצרה הכתיב לא מוריד."),
              mc("p2", "אורך", "140 מילים כשהטווח הוא 120 עד 140.", "140 words",
                 [("a", "It is inside the range."), ("b", "It is too long and scores zero."), ("c", "It is too short.")], "a", "בתוך הטווח.", "140 הוא הקצה העליון, לא אפס.")]),
            ("t_last", "משפט אחרון", "One last sentence", "ו", "סוגרים במשפט אחד שאפשר לומר גם בעל פה.", "I would keep the stall, because the buyers know the fruit.",
             [mc("p1", "משפט", "איזה משפט סוגר?", "Choose.",
                 [("a", "I would keep the stall, because the buyers know the fruit."), ("b", "Because stall."), ("c", "Keep.")], "a", "דעה וסיבה.", "Because לבד אינו סיום."),
              mc("chk", "בדיקה", "אין נושא חדש.", "This road",
                 [("a", "It mixes reading, writing, and speaking. It teaches nothing new."), ("b", "It starts the alphabet."), ("c", "It replaces the placement.")], "a", "ערבוב בלי נושא חדש.", "האותיות היו בדרך הראשונה.", ntype="check")]),
        ],
    ))
    return docs


def main() -> None:
    # Arabic catalog chrome so a path that sorts first still satisfies the locale test on main.
    ar = {
        "path_english_bagrut5_00_placement": ("اختبار مستوى الإنجليزية", "بلا مادة جديدة. الأخطاء تفتح طريق الفجوة."),
        "path_english_bagrut5_01_zero": ("الحروف الأولى", "حروف وأصوات وجملة مع am و is و are."),
        "path_english_bagrut5_02_present": ("المضارع والحياة اليومية", "المضارع البسيط، و there is، والأسئلة."),
        "path_english_bagrut5_03_time": ("الزمن والقصة", "الماضي والمستقبل وقصة قصيرة."),
        "path_english_bagrut5_04_accuracy": ("الدقة", "أدوات التعريف، وترتيب الكلمات، والشرط الأول."),
        "path_english_bagrut5_05_module_e": ("استبيان E", "نص غير مألوف وأسئلة الفهم. بلا إنشاء طويل."),
        "path_english_bagrut5_06_module_g": ("استبيان G", "نص أطول ثم إنشاء رأي من 120 إلى 140 كلمة."),
        "path_english_bagrut5_07_literature_oral": ("الأدب والكلام", "قصة وشعر أصليان، وإنشاء قصير، وثلاث جمل منطوقة."),
        "path_english_bagrut5_08_exam": ("امتحان كامل", "قراءة ومفردات وكتابة وكلام معًا. بلا موضوع جديد."),
    }
    for doc in all_paths():
        title_ar, blurb_ar = ar[doc["id"]]
        doc["titles"]["ar"] = title_ar
        doc["blurbs"]["ar"] = blurb_ar
        path = OUT / f"{doc['id']}.json"
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(path.name, "topics", len(doc["topics"]), "nodes", len(doc["nodes"]))


if __name__ == "__main__":
    main()
