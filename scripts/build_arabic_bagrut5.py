#!/usr/bin/env python3
"""Write the Arabic 5-unit paths (batch 1): 00 placement and 01 from zero, stages 0 to 2.

Explanations are Hebrew (body_he). The Arabic being learned is in body_content and speak_text.

Variants (decided in Eliot100/MyRoad#161, #171): every tile exists with and without audio and
with and without writing. Each variant is a
node with the same base. Id suffix: __a1w0 (audio, no writing: the base), __a0w0, __a1w1, __a0w1.
Every non base node has variant_of=<base>__a1w0 and variant_when {audio, writing} (MyRoad#173);
the app shows one step per base.
Audio variants carry speak_text (TTS). No audio variants carry a Hebrew transliteration in body_he.
Writing variants ask the learner to write by hand on paper before choosing.

Run: python scripts/build_arabic_bagrut5.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import apply_methods  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "adult"

P00 = "path_arabic_bagrut5_00_placement"
P01 = "path_arabic_bagrut5_01_script"

VARIANTS = (
    ("a1w0", True, False, ""),
    ("a0w0", False, False, " (בלי שמע)"),
    ("a1w1", True, True, " (בכתיבה)"),
    ("a0w1", False, True, " (בלי שמע, בכתיבה)"),
)
WRITE_PRE = "קודם כתבו ביד על דף. "
WRITE_LEARN = " העתיקו ביד על דף שלוש פעמים."


def tile(
    base: str,
    ntype: str,
    title: str,
    body: str,
    content: str,
    *,
    translit: str,
    say: str | None = None,
    options: list[tuple[str, str]] | None = None,
    correct: str | list[str] | None = None,
    ok: str | None = None,
    try_: str | None = None,
    kind: str = "understanding",
    review: list[str] | None = None,
    writing: bool = True,
    record: bool = False,
) -> list[dict]:
    """One tile in all its variants. say = text for TTS (defaults to content)."""
    rows = []
    for suffix, audio, write, tag in VARIANTS:
        if write and not writing:
            continue
        b = body
        if write:
            b = (body + WRITE_LEARN) if ntype == "learn" else (WRITE_PRE + body)
        if not audio:
            b = f"{b} בלי שמע, כך זה נשמע: {translit}"
        row: dict = {
            "id": f"{base}__{suffix}",
            "type": ntype,
            "kind": kind,
            "title": title + tag,
            "body_he": b,
            "body_content": content,
        }
        if suffix != "a1w0":
            row["variant_of"] = f"{base}__a1w0"
            row["variant_when"] = {"audio": audio, "writing": write}
        if audio:
            row["speak_text"] = say or content
        if review:
            row["review_topic_ids"] = review
        if record:
            row["record"] = True
        if options:
            row["choices"] = [{"id": cid, "label": label} for cid, label in options]
            row["correct"] = correct
            row["feedback_ok"] = ok or "נכון."
            row["feedback_try"] = try_ or "עוד ניסיון. הסתכלו שוב על הנקודות והצורה."
        rows.append(row)
    return rows


def topic(tid: str, he: str, en: str, emoji: str, nodes: list[dict]) -> dict:
    return {"id": tid, "titles": {"he": he, "en": en}, "emoji": emoji, "node_ids": [n["id"] for n in nodes]}


def doc(pid, titles, blurbs, emoji, minutes, prereq, topics, nodes, route=None) -> dict:
    d = {
        "id": pid,
        "titles": titles,
        "blurbs": blurbs,
        "subject": "arabic",
        "group_ids": ["adult"],
        "emoji": emoji,
        "explain_locale": "he",
        "content_locale": "ar",
        "estimated_minutes": minutes,
        "prerequisite_path_ids": prereq,
        "topics": topics,
        "nodes": nodes,
    }
    if route:
        d["placement_route"] = route
    return d


def build(spec: list[tuple]) -> tuple[list[dict], list[dict]]:
    topics, nodes = [], []
    for tid, he, en, emoji, tiles in spec:
        tn = [n for t in tiles for n in t]
        topics.append(topic(tid, he, en, emoji, tn))
        nodes.extend(tn)
    return topics, nodes


# ---------------------------------------------------------------- 00 placement
def placement() -> dict:
    spec = [
        ("t_zero", "מתחילים מאפס?", "Starting from zero?", "🧭", [
            tile("plc_zero_learn", "learn", "לפני שמתחילים",
                 "זה מבדק בלי חומר חדש. אם אתם לא קוראים אותיות ערביות בכלל, אין צורך במבדק: "
                 "עברו ישר לדרך 01, ערבית מאפס. מי שלמד קצת ערבית בבית ספר ממשיך כאן.",
                 "مَرْحَبًا", translit="מַרְחַבַּא (שלום)"),
            tile("plc_zero_q", "practice", "האות הזו מוכרת לכם?",
                 "בחרו תשובה כנה. שתי התשובות נכונות. אם בחרתם מאפס, סגרו את המבדק ופתחו את דרך 01.",
                 "ب", translit="בּ",
                 options=[("a", "כן, אני מזהה אותה"), ("b", "לא, אני מתחיל מאפס")], correct=["a", "b"],
                 ok="תודה. מאפס: עוברים לדרך 01. מזהים: ממשיכים במבדק."),
        ]),
        ("t_script", "כתב", "Script", "✍️", [
            tile("plc_script_p1", "practice", "איזו אות?",
                 "איזו אות היא ت (ת)?", "ب ت ث ن", translit="תּ",
                 options=[("a", "ت"), ("b", "ب"), ("c", "ث"), ("d", "ن")], correct="a",
                 ok="ت: שתי נקודות למעלה.", try_="ب נקודה למטה, ن נקודה אחת למעלה, ث שלוש. ت שתיים למעלה."),
            tile("plc_script_chk", "check", "קריאת מילה",
                 "איך קוראים את המילה?", "بَاب", translit="בַּאבּ",
                 options=[("a", "באב"), ("b", "תאב"), ("c", "נאב"), ("d", "באן")], correct="a",
                 ok="בַּאבּ, דלת.", try_="שתי האותיות הן ب, נקודה אחת למטה."),
        ]),
        ("t_words", "מילים", "Words", "📚", [
            tile("plc_words_p1", "practice", "מה פירוש המילה?",
                 "בחרו תרגום.", "كِتَاب", translit="כִּתַאבּ",
                 options=[("a", "ספר"), ("b", "כותב"), ("c", "מכתב"), ("d", "שולחן")], correct="a",
                 ok="كتاب הוא ספר.", try_="כותב הוא كاتب, מכתב הוא رسالة. كتاب הוא ספר."),
            tile("plc_words_chk", "check", "מילה בלי ניקוד",
                 "בחרו תרגום. בבחינה אין ניקוד.", "بيت", translit="בֵּית",
                 options=[("a", "בית"), ("b", "בת"), ("c", "בן"), ("d", "דלת")], correct="a",
                 ok="بيت הוא בית.", try_="בת היא بنت, בן ابن. بيت הוא בית."),
        ]),
        ("t_noun", "משפט שמני", "Nominal sentence", "🧱", [
            tile("plc_noun_chk", "check", "משפט בלי פועל",
                 "מה פירוש המשפט?", "الْبَيْتُ كَبِيرٌ", translit="אַלְבַּיְתֻ כַּבִּירֻן",
                 options=[("a", "הבית גדול"), ("b", "בית גדול"), ("c", "הבית הגדול"), ("d", "הבתים גדולים")],
                 correct="a", ok="יידוע בנושא, בלי יידוע בנשוא: משפט שלם.",
                 try_="الْبَيْتُ مיודע ו كَبِيرٌ לא: זה משפט, הבית גדול."),
        ]),
        ("t_verb", "פועל", "Verb", "⚙️", [
            tile("plc_verb_p1", "practice", "שורש",
                 "מה השורש של הפועל?", "كَتَبَ", translit="כַּתַבַּ",
                 options=[("a", "ك ت ب"), ("b", "ك ت ا"), ("c", "ت ب ك"), ("d", "ك ب ت")], correct="a",
                 ok="כ ת ב, כמו בעברית.", try_="קוראים את האותיות לפי הסדר: ك ت ب."),
            tile("plc_verb_chk", "check", "זמן וגוף",
                 "מה פירוש הפועל?", "يَكْتُبُ", translit="יַכְּתֻבֻּ",
                 options=[("a", "הוא כותב"), ("b", "הוא כתב"), ("c", "אני כותב"), ("d", "היא כותבת")], correct="a",
                 ok="ي בהתחלה: הוא, בהווה.", try_="ي בהתחלה אומרת הוא; كَتَبَ זה עבר. يَكْتُبُ: הוא כותב."),
        ]),
        ("t_syntax", "תחביר", "Syntax", "🔗", [
            tile("plc_syntax_chk", "check", "כאן ואחיותיה",
                 "מה פירוש המשפט?", "كَانَ الْجَوُّ بَارِدًا", translit="כַּאנַ אלְגַ'וֻּ בַּארִדַן",
                 options=[("a", "מזג האוויר היה קר"), ("b", "מזג האוויר קר"), ("c", "מזג האוויר יהיה קר"), ("d", "מזג האוויר לא קר")],
                 correct="a", ok="كان: היה.", try_="كان מעביר את המשפט לעבר: היה קר."),
        ]),
        ("t_read", "קריאה", "Reading", "📰", [
            tile("plc_read_chk", "check", "קטע קצר",
                 "קראו בלי ניקוד וענו: איפה סמיר גר?",
                 "سمير طالب في الجامعة. هو يسكن في حيفا مع أخيه ويعمل في مطعم.",
                 translit="סַמִיר טַאלִבּ פִי אלְגַ'אמִעַה. הֻוַ יַסְכֻּן פִי חֵיפַא מַעַ אַח'יהִ וַיַעְמַל פִי מַטְעַם.",
                 options=[("a", "בחיפה"), ("b", "באוניברסיטה"), ("c", "במסעדה"), ("d", "אצל אחיו בעיר אחרת")],
                 correct="a", ok="يسكن في حيفا: גר בחיפה.",
                 try_="באוניברסיטה הוא לומד, במסעדה הוא עובד. يسكن הוא גר: בחיפה."),
        ]),
        ("t_speak", "ערבית מדוברת", "Spoken Arabic", "🗣️", [
            tile("plc_speak_p1", "practice", "תשובה בשיחה",
                 "חבר שואל אתכם בערבית מדוברת. מה עונים?", "كيفك؟", translit="כִּיפַכּ?",
                 options=[("a", "منيح، الحمد لله"), ("b", "اسمي إليوت"), ("c", "من حيفا"), ("d", "مع السلامة")],
                 correct="a", ok="מְנִיח, אַלְחַמְדֻלִלַּה: טוב, תודה לאל.",
                 try_="كيفك שואל מה שלומך. منيح: טוב."),
            tile("plc_speak_say", "speak", "אמרו בקול",
                 "הציגו את עצמכם במשפט אחד בערבית מדוברת: שם ומאיפה אתם. סמנו לעצמכם אם הצלחתם.",
                 "اسمي ... أنا من ...", say="اسمي إليوت. أنا من تل أبيب.",
                 translit="אִסְמִי ... אַנַא מִן ...", writing=False, record=True),
        ]),
        ("t_result", "תוצאה", "Result", "🏁", [
            tile("plc_result", "learn", "מה עושים עם הטעויות",
                 "בסיום המבדק המערכת פותחת לכם את הדרך המתאימה. כרגע נבנתה רק דרך 01, ואליה מגיעים מי שהתחילו "
                 "מאפס או טעו בכמה שאלות. מי שענה הכול נכון יקבל את הדרכים הבאות כשייבנו.",
                 "بِالتَّوْفِيق", translit="בִּאלתַּוְפִיק (בהצלחה)", writing=False),
        ]),
    ]
    topics, nodes = build(spec)
    return doc(
        P00,
        {"he": "מבדק רמה לערבית", "en": "Arabic level check", "ar": "اختبار مستوى العربية"},
        {"he": "מי שלא קורא אותיות ערביות עובר ישר לדרך 01. השאר: כתב, מילים, משפט, פועל, תחביר, קריאה ודיבור.",
         "en": "If you cannot read Arabic letters, go straight to road 01. Otherwise: script, words, sentence, verb, syntax, reading, speaking.",
         "ar": "من لا يقرأ الحروف العربية ينتقل مباشرة إلى الطريق 01."},
        "🧭", 40, [], topics, nodes,
    )


# ---------------------------------------------------------------- 01 from zero
def zero() -> dict:
    s0 = [
        tile("z0_dir_learn", "learn", "מימין לשמאל, כמו בעברית",
             "ערבית נכתבת מימין לשמאל, כמו עברית. אין אותיות גדולות. רוב האותיות מתחברות זו לזו בתוך מילה, "
             "ולכן לאות יש צורה קצת אחרת בהתחלה, באמצע ובסוף.",
             "عَرَبِيّ", translit="עַרַבִּיּ (ערבי)"),
        tile("z0_dir_p1", "practice", "מאיזה צד מתחילים?",
             "מאיפה מתחילים לקרוא את המילה?", "عَرَبِيّ", translit="עַרַבִּיּ",
             options=[("a", "מימין"), ("b", "משמאל"), ("c", "מלמעלה"), ("d", "מהאמצע")], correct="a",
             ok="מימין, כמו בעברית.", try_="כמו בעברית: מימין לשמאל."),
        tile("z0_join_learn", "learn", "אותיות מחוברות",
             "המילה באב (דלת) כתובה מ ب ו ا ו ب. האות ب מתחברת לאות שאחריה; האות ا לא.",
             "ب + ا + ب = بَاب", say="بَاب", translit="בַּאבּ (דלת)"),
        tile("z0_join_p1", "practice", "כמה אותיות?",
             "כמה אותיות יש במילה?", "بَاب", translit="בַּאבּ",
             options=[("a", "3"), ("b", "2"), ("c", "4"), ("d", "1")], correct="a",
             ok="ب ا ب: שלוש.", try_="ב, א, ב. שלוש אותיות."),
        tile("z0_hello_learn", "learn", "מילה ראשונה בדיבור",
             "בערבית מדוברת אומרים מַרְחַבַּא לשלום, ועונים אַהְלַן או מַרְחַבְּתֵין. "
             "שוּכְּרַן היא תודה.",
             "مَرْحَبًا ، أَهْلًا ، شُكْرًا", translit="מַרְחַבַּא, אַהְלַן, שֻׁכְּרַן"),
        tile("z0_hello_speak", "speak", "אמרו שלום",
             "אמרו בקול: שלום, ואחר כך תודה. סמנו לעצמכם שאמרתם.",
             "مَرْحَبًا ... شُكْرًا", translit="מַרְחַבַּא ... שֻׁכְּרַן", writing=False, record=True),
        tile("z0_hello_p1", "practice", "מה עונים?",
             "מישהו אומר לכם מַרְחַבַּא. מה עונים?", "مَرْحَبًا", translit="מַרְחַבַּא",
             options=[("a", "أَهْلًا"), ("b", "شُكْرًا"), ("c", "لَا"), ("d", "بَاب")], correct="a",
             ok="אַהְלַן, ברוך הבא.", try_="שֻׁכְּרַן זה תודה. על שלום עונים אַהְלַן."),
    ]
    s1 = [
        tile("z1_letters_learn", "learn", "שש אותיות ראשונות",
             "ا אַלִף (א, וגם תנועה א ארוכה). ب בַּא (ב דגושה, תמיד b). ت תַּא (ת). "
             "ن נוּן (נ). م מִים (מ). ل לַאם (ל). שימו לב לנקודות: ب אחת למטה, ت שתיים למעלה, ن אחת למעלה.",
             "ا ب ت ن م ل", translit="אַלִף, בַּא, תַּא, נוּן, מִים, לַאם", kind="review"),
        tile("z1_dots_p1", "practice", "איזו אות?",
             "איזו אות היא ב?", "ب ت ن ي", translit="בּ",
             options=[("a", "ب"), ("b", "ت"), ("c", "ن"), ("d", "ي")], correct="a", kind="review",
             ok="ב: נקודה אחת למטה.", try_="ت שתי נקודות למעלה, ن אחת למעלה, ي שתיים למטה. ב: אחת למטה."),
        tile("z1_dots_p2", "practice", "איזו אות?",
             "איזו אות היא נ?", "ن ب ت ل", translit="נ",
             options=[("a", "ن"), ("b", "ب"), ("c", "ت"), ("d", "ل")], correct="a", kind="review",
             ok="נ: קערה עם נקודה אחת למעלה.", try_="נוּן היא קערה עמוקה עם נקודה אחת למעלה."),
        tile("z1_sound_p1", "practice", "איזה צליל?",
             "מה הצליל של האות?", "م", translit="מ",
             options=[("a", "מ"), ("b", "ל"), ("c", "ה"), ("d", "ס")], correct="a", kind="review",
             ok="م היא מִים, מ.", try_="م היא עיגול קטן עם זנב: מ."),
        tile("z1_sound_p2", "practice", "איזה צליל?",
             "מה הצליל של האות?", "ل", translit="ל",
             options=[("a", "ל"), ("b", "א"), ("c", "כ"), ("d", "נ")], correct="a", kind="review",
             ok="ل היא לַאם, ל.", try_="ا היא קו ישר בלי זנב. ل יורדת ומתעקלת שמאלה: ל."),
        tile("z1_word_learn", "learn", "מילים משש האותיות",
             "בִּנְת היא בת. לַבַּן הוא לבן (יוגורט). אִבְּן הוא בן. שימו לב: ب ו ت ו ن נראות אחרת "
             "בהתחלה ובאמצע: רק שן קטנה עם הנקודות שלה.",
             "بِنْت ، لَبَن ، اِبْن", translit="בִּנְת, לַבַּן, אִבְּן"),
        tile("z1_word_p1", "practice", "קריאת מילה",
             "איך קוראים את המילה?", "بِنْت", translit="בִּנְת",
             options=[("a", "בִּנְת"), ("b", "תִּבְּן"), ("c", "נִבְּת"), ("d", "בִּית")], correct="a", kind="review",
             ok="בִּנְת, בת.", try_="מימין: ب (נקודה למטה), ن (למעלה), ت (שתיים למעלה)."),
        tile("z1_word_p2", "practice", "מה פירוש המילה?",
             "בחרו תרגום.", "لَبَن", translit="לַבַּן",
             options=[("a", "לבן (יוגורט)"), ("b", "בן"), ("c", "בת"), ("d", "דלת")], correct="a", kind="review",
             ok="לַבַּן, כמו בעברית.", try_="ל, ב, נ: לַבַּן."),
        tile("z1_name_learn", "learn", "איך קוראים לך?",
             "בערבית מדוברת שואלים שוּ אִסְמַכּ? (לגבר) או שוּ אִסְמֵכּ? (לאישה). עונים אִסְמִי ואת השם.",
             "شُو اِسْمَك؟ اِسْمِي ...", translit="שׁוּ אִסְמַכּ? אִסְמִי ..."),
        tile("z1_name_speak", "speak", "הציגו את עצמכם",
             "אמרו בקול: אִסְמִי ואת השם שלכם. סמנו לעצמכם שאמרתם.",
             "اِسْمِي ...", say="اِسْمِي إِلْيُوت", translit="אִסְמִי ...", writing=False, record=True),
        tile("z1_chk", "check", "בדיקה",
             "איזו מילה היא אִבְּן (בן)?", "أَيّ كَلِمَة؟", translit="אִבְּן",
             options=[("a", "اِبْن"), ("b", "بِنْت"), ("c", "لَبَن"), ("d", "بَاب")], correct="a", kind="review",
             ok="ا ب ن: אִבְּן.", try_="מחפשים ا בהתחלה ו ن בסוף."),
    ]
    s2 = [
        tile("z2_letters_learn", "learn", "עוד שש אותיות",
             "ي יַא (י, וגם תנועה אִי ארוכה). و וַאו (w, וגם תנועה אוּ ארוכה). س סִין (ס). "
             "ر רַא (ר מתגלגלת). د דַּאל (ד). ك כַּאף (כּ, תמיד k).",
             "ي و س ر د ك", translit="יַא, וַאו, סִין, רַא, דַּאל, כַּאף", kind="review"),
        tile("z2_shape_p1", "practice", "איזו אות?",
             "איזו אות היא ר?", "ر د و ز", translit="ר",
             options=[("a", "ر"), ("b", "د"), ("c", "و"), ("d", "ز")], correct="a", kind="review",
             ok="ر יורדת מתחת לשורה.", try_="د נשארת על השורה, و יש לה ראש עגול, ز יש לה נקודה. ر: בלי נקודה, יורדת."),
        tile("z2_shape_p2", "practice", "איזו אות?",
             "איזו אות היא ס?", "س ش ص ي", translit="ס",
             options=[("a", "س"), ("b", "ش"), ("c", "ص"), ("d", "ي")], correct="a", kind="review",
             ok="ס: שלוש שיניים בלי נקודות.", try_="ش יש לה שלוש נקודות, ص יש לה לולאה. س: שיניים בלי נקודות."),
        tile("z2_sound_p1", "practice", "איזה צליל?",
             "מה הצליל של האות?", "ك", translit="כּ",
             options=[("a", "כּ (k)"), ("b", "ל"), ("c", "ח"), ("d", "ק עמוקה")], correct="a", kind="review",
             ok="ك היא כּ, תמיד k.", try_="ل בלי הקו הקטן בפנים. ك: כּ."),
        tile("z2_nojoin_learn", "learn", "אותיות שלא מתחברות לשמאל",
             "ا د ر و לא מתחברות לאות שאחריהן. אחריהן יש רווח קטן בתוך המילה, וזה לא סוף המילה. "
             "למשל וַלַד (ילד): و לא מתחברת, ואחריה لد מחוברות.",
             "وَلَد ، دَرْس ، بَيْت", translit="וַלַד (ילד), דַּרְס (שיעור), בַּיְת (בית)"),
        tile("z2_nojoin_p1", "practice", "מי לא מתחברת?",
             "איזו אות לא מתחברת לאות שאחריה?", "د ب ن ت", translit="דּ",
             options=[("a", "د"), ("b", "ب"), ("c", "ن"), ("d", "ت")], correct="a",
             ok="د לא מתחברת שמאלה.", try_="ب ت ن מתחברות. ا د ر و לא."),
        tile("z2_word_p1", "practice", "קריאת מילה",
             "איך קוראים את המילה?", "كِتَاب", translit="כִּתַאבּ",
             options=[("a", "כִּתַאבּ"), ("b", "כַּאתִבּ"), ("c", "בִּתַאכּ"), ("d", "כִּנַאבּ")], correct="a", kind="review",
             ok="כִּתַאבּ, ספר.", try_="ك ت ا ب: כִּתַאבּ. ا באמצע היא א ארוכה."),
        tile("z2_word_p2", "practice", "מה פירוש המילה?",
             "בחרו תרגום.", "وَلَد", translit="וַלַד",
             options=[("a", "ילד"), ("b", "יד"), ("c", "בת"), ("d", "שיעור")], correct="a", kind="review",
             ok="وَلَد, ילד.", try_="יד היא يَد, שיעור دَرْس. وَلَد: ילד."),
        tile("z2_how_learn", "learn", "מה שלומך?",
             "בערבית מדוברת שואלים כִּיפַכּ? (לגבר) או כִּיפֵכּ? (לאישה). עונים מְנִיח (טוב) או מְנִיחַה (לאישה), "
             "ומוסיפים אַלְחַמְדֻלִלַּה.",
             "كِيفَك؟ مْنِيح، الْحَمْدُ لِلّه", translit="כִּיפַכּ? מְנִיח, אַלְחַמְדֻלִלַּה"),
        tile("z2_how_speak", "speak", "שיחה קצרה",
             "אמרו בקול שאלה ותשובה: כִּיפַכּ? מְנִיח, אַלְחַמְדֻלִלַּה. סמנו לעצמכם שאמרתם.",
             "كِيفَك؟ مْنِيح، الْحَمْدُ لِلّه", translit="כִּיפַכּ? מְנִיח, אַלְחַמְדֻלִלַּה", writing=False, record=True),
        tile("z2_how_p1", "practice", "מה עונים?",
             "שואלים אתכם כִּיפַכּ? מה עונים?", "كِيفَك؟", translit="כִּיפַכּ?",
             options=[("a", "مْنِيح"), ("b", "اِسْمِي دَان"), ("c", "مَرْحَبًا"), ("d", "شُكْرًا")], correct="a",
             ok="מְנִיח: טוב.", try_="כִּיפַכּ היא מה שלומך. עונים מְנִיח."),
    ]
    rev = [
        tile("z_rev_learn", "learn", "חזרה",
             "שתים עשרה אותיות עד עכשיו. ב ת נ י נבדלות רק בנקודות. ا د ر و לא מתחברות שמאלה.",
             "ا ب ت ن م ل ي و س ر د ك", translit="אַלִף, בַּא, תַּא, נוּן, מִים, לַאם, יַא, וַאו, סִין, רַא, דַּאל, כַּאף",
             kind="review", review=["s1_letters", "s2_letters"]),
        tile("z_rev_p1", "practice", "חזרה: איזו אות?",
             "איזו אות היא ת?", "ت ث ب ن", translit="תּ",
             options=[("a", "ت"), ("b", "ث"), ("c", "ب"), ("d", "ن")], correct="a",
             kind="review", review=["s1_letters"], ok="ת: שתי נקודות למעלה.", try_="ث שלוש נקודות. ت שתיים."),
        tile("z_rev_p2", "practice", "חזרה: מילה",
             "איך קוראים את המילה?", "بَيْت", translit="בַּיְת",
             options=[("a", "בַּיְת"), ("b", "בִּנְת"), ("c", "תַּיְבּ"), ("d", "נַיְת")], correct="a",
             kind="review", review=["s1_letters", "s2_letters"],
             ok="בַּיְת, בית.", try_="ب ي ت: ב, י, ת. בִּנְת היא بِنْت."),
        tile("z_rev_p3", "practice", "חזרה: בדיבור",
             "מה אומרים כשנפגשים?", "أَيّ كَلِمَة؟", translit="מַרְחַבַּא",
             options=[("a", "مَرْحَبًا"), ("b", "مْنِيح"), ("c", "اِسْمِي"), ("d", "لَبَن")], correct="a",
             kind="review", review=["s0_start"], ok="מַרְחַבַּא, שלום.", try_="שלום זה מַרְחַבַּא."),
        tile("z_rev_chk", "check", "בדיקת סוף שלב 2",
             "מה פירוש המילה?", "دَرْس", translit="דַּרְס",
             options=[("a", "שיעור"), ("b", "דלת"), ("c", "ילד"), ("d", "בית")], correct="a",
             kind="review", review=["s2_letters"], ok="دَرْس, שיעור.", try_="د ر س: דַּרְס, שיעור."),
    ]
    celebrate = [{
        "id": "z_done", "type": "celebrate", "kind": "understanding", "title": "שלב 2 הושלם",
        "body_he": "קראתם את המילים הראשונות שלכם בערבית ואמרתם שלום, שם ומה שלומך. השלב הבא: אותיות בלי מקבילה בעברית.",
        "body_content": "أَحْسَنْت!",
    }]
    spec = [
        ("s0_start", "שלב 0: מתחילים", "Stage 0: start", "🌱", s0),
        ("s1_letters", "שלב 1: שש אותיות ראשונות", "Stage 1: first six letters", "ب", s1),
        ("s2_letters", "שלב 2: עוד שש אותיות", "Stage 2: six more letters", "ك", s2),
        ("s2_review", "חזרה", "Review", "🔁", rev),
        ("s2_done", "סיום שלב 2", "Stage 2 done", "🎉", [celebrate]),
    ]
    topics, nodes = build(spec)
    return doc(
        P01,
        {"he": "ערבית מאפס", "en": "Arabic first letters", "ar": "العربية من الصفر"},
        {"he": "כתב ערבי מהיום הראשון: כיוון, אותיות ראשונות, מילים ראשונות, ושלום בערבית מדוברת.",
         "en": "Arabic script from day one: direction, first letters, first words, and hello in spoken Arabic.",
         "ar": "الخط العربي من اليوم الأول: الحروف والكلمات الأولى والتحية."},
        "🌱", 90, [], topics, nodes,
        route={"from_placement": P00, "band_min": 1, "band_max": 3},
    )


def main() -> None:
    for d in (placement(), zero()):
        missing = apply_methods.apply_doc(d)  # method in body_he, worked answer in feedback_try
        assert not missing, missing
        fp = OUT / f"{d['id']}.json"
        fp.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(fp.relative_to(ROOT), len(d["nodes"]), "nodes")


if __name__ == "__main__":
    main()
