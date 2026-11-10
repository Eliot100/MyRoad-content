"""Build math, physics, and Arabic bagrut5 roads from cited syllabus headings.

Original items only. No copied exam questions. Run from the repo root:

    python scripts/build_bagrut5_roads.py

Arabic road 01 is not rewritten here. Its band is narrowed in build_arabic_bagrut5.py.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ADULT = ROOT / "adult"

ROLES = (
    ("learn", "explanation"),
    ("learn", "worked_example"),
    ("practice", "guided_practice"),
    ("practice", "independent_practice"),
    ("check", "quick_check"),
)


def node(nid: str, ntype: str, role: str, title: str, body: str, item: dict | None) -> dict:
    out = {
        "id": nid,
        "type": ntype,
        "title": title,
        "body_he": body,
        "tile_role": role,
        "kind": "understanding",
    }
    if item:
        out["choices"] = [
            {"id": "a", "label": item["ok"]},
            {"id": "b", "label": item["bad"][0]},
            {"id": "c", "label": item["bad"][1]},
        ]
        out["correct"] = "a"
        out["feedback_ok"] = item["ok_he"]
        out["feedback_try"] = item["try_he"]
        if item.get("content"):
            out["body_content"] = item["content"]
        if item.get("speak"):
            out["speak_text"] = item["speak"]
    return out


def road(spec: dict) -> dict:
    nodes: list[dict] = []
    topics: list[dict] = []
    for index, stage in enumerate(spec["stages"]):
        level, tid, he, en, lead, item = stage
        ids = []
        for role_i, (ntype, role) in enumerate(ROLES):
            nid = f"{tid}_{role}"
            ids.append(nid)
            title = he if role == "explanation" else f"{he}: {role_i + 1}"
            body = f"{lead} {item['ask']}"
            use = item if ntype != "learn" else None
            if role == "worked_example":
                body = f"{lead} דוגמה: {item['ask']} התשובה היא {item['ok']}. {item['ok_he']}"
            built = node(nid, ntype, role, title, body, item=use)
            if role == "explanation" and item.get("speak"):
                built["speak_text"] = item["speak"]
            if item.get("content") and ntype == "learn":
                built["body_content"] = item["content"]
            nodes.append(built)
        topics.append(
            {
                "id": tid,
                "titles": {"he": he, "en": en},
                "emoji": spec["emoji"],
                "level": level,
                "node_ids": ids,
            }
        )
    nodes.append(
        {
            "id": "t_end",
            "type": "celebrate",
            "title": "סוף הדרך",
            "body_he": spec["end_he"],
        }
    )
    topics[-1]["node_ids"] = topics[-1]["node_ids"] + ["t_end"]
    doc = {
        "id": spec["id"],
        "titles": {"he": spec["he"], "en": spec["en"], "ar": spec["ar"]},
        "blurbs": {"he": spec["blurb_he"], "en": spec["blurb_en"], "ar": spec["blurb_ar"]},
        "subject": spec["subject"],
        "group_ids": ["adult"],
        "emoji": spec["emoji"],
        "explain_locale": "he",
        "content_locale": spec.get("content_locale", "he"),
        "estimated_minutes": spec["minutes"],
        "prerequisite_path_ids": [spec["place"]],
        "placement_route": {
            "from_placement": spec["place"],
            "band_min": spec["band"][0],
            "band_max": spec["band"][1],
        },
        "topics": topics,
        "nodes": nodes,
    }
    return doc


def placement(spec: dict) -> dict:
    nodes = []
    topics = []
    for index, item in enumerate(spec["items"]):
        nid = f"p{index}"
        nodes.append(
            {
                "id": nid,
                "type": "check",
                "title": item["title"],
                "body_he": item["ask"],
                "choices": [
                    {"id": "a", "label": item["ok"]},
                    {"id": "b", "label": item["bad"][0]},
                    {"id": "c", "label": item["bad"][1]},
                ],
                "correct": "a",
                "feedback_ok": item["ok_he"],
                "feedback_try": item["try_he"],
                "area": item["area"],
                "difficulty": item["b"],
            }
        )
        if item.get("content"):
            nodes[-1]["body_content"] = item["content"]
        topics.append(
            {
                "id": f"t{index}",
                "titles": {"he": item["title"], "en": item["en"]},
                "emoji": spec["emoji"],
                "node_ids": [nid],
            }
        )
    return {
        "id": spec["id"],
        "titles": {"he": spec["he"], "en": spec["en"], "ar": spec["ar"]},
        "blurbs": {"he": spec["blurb_he"], "en": spec["blurb_en"], "ar": spec["blurb_ar"]},
        "subject": spec["subject"],
        "group_ids": ["adult"],
        "emoji": spec["emoji"],
        "explain_locale": "he",
        "content_locale": spec.get("content_locale", "he"),
        "estimated_minutes": 25,
        "prerequisite_path_ids": [],
        "topics": topics,
        "nodes": nodes,
    }


def q(ask, ok, bad, ok_he, try_he, content=None, speak=None):
    return {"ask": ask, "ok": ok, "bad": bad, "ok_he": ok_he, "try_he": try_he, "content": content, "speak": speak}


MATH_PLACE = "path_math_bagrut5_00_placement"
PHYS_PLACE = "path_physics_bagrut5_00_placement"
AR_PLACE = "path_arabic_bagrut5_00_placement"


def build() -> list[tuple[str, dict]]:
    out: list[tuple[str, dict]] = []
    out.append(
        (
            MATH_PLACE,
            placement(
                {
                    "id": MATH_PLACE,
                    "subject": "math",
                    "emoji": "∑",
                    "he": "מבדק רמה במתמטיקה",
                    "en": "Math level check",
                    "ar": "اختبار مستوى الرياضيات",
                    "blurb_he": "ארבע שאלות קצרות. לפי הטעויות נפתחת הדרך, בלי חומר חדש.",
                    "blurb_en": "Four short questions. Mistakes open the road. No new material.",
                    "blurb_ar": "أربعة أسئلة قصيرة. الأخطاء تفتح الطريق.",
                    "items": [
                        {
                            "title": "שיפוע",
                            "en": "Slope",
                            "ask": "מה השיפוע בין (0, 1) ל־(2, 5)?",
                            "ok": "2",
                            "bad": ["4", "1"],
                            "ok_he": "נכון. (5−1)/(2−0) = 2.",
                            "try_he": "שינוי ב־y חלקי שינוי ב־x.",
                            "area": "analysis",
                            "b": -1.0,
                        },
                        {
                            "title": "משולש",
                            "en": "Triangle",
                            "ask": "במשולש ישר זווית, הניצבים 3 ו־4. מה אורך היתר?",
                            "ok": "5",
                            "bad": ["7", "12"],
                            "ok_he": "נכון. 3²+4²=25, והשורש הוא 5.",
                            "try_he": "משפט פיתגורס, לא סכום הניצבים.",
                            "area": "geometry",
                            "b": -0.2,
                        },
                        {
                            "title": "סדרה",
                            "en": "Sequence",
                            "ask": "סדרה חשבונית: 2, 5, 8. מה האיבר הרביעי?",
                            "ok": "11",
                            "bad": ["10", "16"],
                            "ok_he": "נכון. הפרש 3, אז 8+3=11.",
                            "try_he": "מוסיפים את אותו הפרש.",
                            "area": "sequences",
                            "b": 0.4,
                        },
                        {
                            "title": "הסתברות",
                            "en": "Probability",
                            "ask": "קובייה הוגנת. מה ההסתברות לתוצאה זוגית?",
                            "ok": "1/2",
                            "bad": ["1/6", "2/3"],
                            "ok_he": "נכון. 2, 4, 6 מתוך 6, כלומר 1/2.",
                            "try_he": "שלוש תוצאות זוגיות מתוך שש.",
                            "area": "probability",
                            "b": 0.8,
                        },
                    ],
                }
            ),
        )
    )
    math_roads = [
        {
            "id": "path_math_bagrut5_01_analysis",
            "he": "אנליזה",
            "en": "Analysis",
            "ar": "تحليل",
            "blurb_he": "מבוא לאנליזה של פונקציות וחשבון דיפרנציאלי של כיתה יוד, לפי תוכנית 5 יחידות.",
            "blurb_en": "Introduction to functions and grade-10 differential calculus, 5 units.",
            "blurb_ar": "مقدمة في تحليل الدوال حسب برنامج 5 وحدات.",
            "emoji": "∑",
            "minutes": 240,
            "band": (1, 1),
            "end_he": "סיימת את דרך האנליזה. השלב הבא בשרשרת הוא גאומטריה, אם המבדק פתח אותה.",
            "stages": [
                (1, "t_rate", "קצב שינוי", "Rate of change",
                 "שיפוע של ישר הוא כמה y משתנה כש־x גדל ב־1.",
                 q("מה השיפוע בין (1, 2) ל־(3, 8)?", "3", ["6", "1/3"],
                   "נכון. (8−2)/(3−1) = 3.", "שינוי ב־y למעלה, שינוי ב־x למטה.")),
                (2, "t_poly", "פולינום", "Polynomial",
                 "בפולינום, הנגזרת של x בחזקת n היא n כפול x בחזקת n פחות 1.",
                 q("מה הנגזרת של x²?", "2x", ["x", "x²"],
                   "נכון. החזקה יורדת ל־1 והמקדם הוא 2.", "הורידו חזקה והכפילו בה.")),
                (3, "t_root", "שורש ורציונלית", "Root and rational",
                 "לפונקציית שורש, התחום הוא איפה שהביטוי שבתוך השורש איננו שלילי.",
                 q("מה התחום של שורש x?", "x ≥ 0", ["x > 1", "כל x"],
                   "נכון. שורש מוגדר כש־x אינו שלילי.", "בתוך השורש אסור ערך שלילי.")),
            ],
        },
        {
            "id": "path_math_bagrut5_02_geometry",
            "he": "גאומטריה",
            "en": "Geometry",
            "ar": "هندسة",
            "blurb_he": "גאומטריה של המישור בכיתה יוד: משולש, מעגל ודמיון. בלי שאלון מועתק.",
            "blurb_en": "Grade-10 plane geometry: triangle, circle, and similarity.",
            "blurb_ar": "هندسة المستوي: مثلث ودائرة وتشابه.",
            "emoji": "△",
            "minutes": 220,
            "band": (2, 2),
            "end_he": "סיימת את דרך הגאומטריה.",
            "stages": [
                (1, "t_triangle", "המשולש", "The triangle",
                 "סכום הזוויות במשולש הוא 180 מעלות.",
                 q("במשולש שתי זוויות הן 40 ו־60. מה הזווית השלישית?", "80", ["100", "20"],
                   "נכון. 180−40−60 = 80.", "החסירו את שתי הזוויות מ־180.")),
                (2, "t_circle", "המעגל", "The circle",
                 "זווית מרכזית נשענת על קשת. זווית היקפית על אותה קשת היא חצי ממנה.",
                 q("זווית מרכזית היא 80 מעלות. מה הזווית ההיקפית על אותה קשת?", "40", ["80", "160"],
                   "נכון. היקפית היא חצי מהמרכזית.", "חלקו את הזווית המרכזית ב־2.")),
                (3, "t_similar", "דמיון", "Similarity",
                 "במשולשים דומים, יחס הצלעות שווה. השטח גדל לפי ריבוע היחס.",
                 q("יחס הדמיון הוא 2. מה יחס השטחים?", "4", ["2", "8"],
                   "נכון. יחס שטחים הוא ריבוע יחס הצלעות, 2²=4.", "ריבוע, לא אותו יחס.")),
            ],
        },
        {
            "id": "path_math_bagrut5_03_trigonometry",
            "he": "טריגונומטריה",
            "en": "Trigonometry",
            "ar": "مثلثات",
            "blurb_he": "טריגונומטריה במישור ומבוא לפונקציות הטריגונומטריות, כיתה יוד.",
            "blurb_en": "Plane trigonometry and an introduction to the trigonometric functions.",
            "blurb_ar": "مثلثات في المستوي ومقدمة للدوال.",
            "emoji": "∠",
            "minutes": 200,
            "band": (3, 3),
            "end_he": "סיימת את דרך הטריגונומטריה.",
            "stages": [
                (1, "t_right", "משולש ישר זווית", "Right triangle",
                 "במשולש ישר זווית, סינוס הזווית הוא הניצב שמול חלקי היתר.",
                 q("ניצב מול הזווית 3, יתר 5. מה הסינוס?", "3/5", ["5/3", "4/5"],
                   "נכון. מול חלקי יתר הוא 3/5.", "המול למעלה, היתר למטה.")),
                (2, "t_sine", "משפט הסינוסים", "Law of sines",
                 "בכל משולש, a/sin A = b/sin B.",
                 q("אם a=6 ו־sin A = 1/2, מה a/sin A?", "12", ["3", "6"],
                   "נכון. 6 חלקי 1/2 שווה 12.", "חילוק בשבר הוא כפל בהופכי.")),
                (3, "t_eq", "משוואה בסיסית", "Basic equation",
                 "sin x = 0 כש־x הוא כפולה שלמה של 180 מעלות, במעלות.",
                 q("פתרון אחד של sin x = 0 במעלות הוא?", "0", ["90", "45"],
                   "נכון. sin 0 = 0.", "90 מעלות נותן 1, לא 0.")),
            ],
        },
        {
            "id": "path_math_bagrut5_04_calculus",
            "he": "סדרות וחשבון אינטגרלי",
            "en": "Sequences and integral calculus",
            "ar": "متتاليات وتكامل",
            "blurb_he": "מכיתה יא: אינדוקציה וסדרות, ואחר כך אינטגרל. הנגזרת כבר נפתחה באנליזה.",
            "blurb_en": "Grade 11: induction and sequences, then the integral.",
            "blurb_ar": "الصف الحادي عشر: متتاليات ثم تكامل.",
            "emoji": "∫",
            "minutes": 260,
            "band": (4, 4),
            "end_he": "סיימת את דרך הסדרות והאינטגרל.",
            "stages": [
                (1, "t_seq", "סדרה חשבונית", "Arithmetic sequence",
                 "בסדרה חשבונית האיבר הכללי הוא a1 ועוד (n−1) כפול ההפרש.",
                 q("a1=2, הפרש 3. מה a4?", "11", ["8", "14"],
                   "נכון. 2+3×3 = 11.", "שלושה צעדים אחרי האיבר הראשון.")),
                (2, "t_induct", "אינדוקציה", "Induction",
                 "הוכחה באינדוקציה בודקת בסיס, ואז צעד מ־n אל n+1.",
                 q("מה חסר אם בדקתם רק את הבסיס?", "צעד האינדוקציה", ["המסקנה כבר הוכחה", "אין צורך בהנחה"],
                   "נכון. בלי הצעד אין מעבר לכל n.", "בסיס לבד אינו מכסה את כל המספרים.")),
                (3, "t_int", "אינטגרל", "Integral",
                 "האינטגרל של 2x הוא x² ועוד קבוע.",
                 q("מה האינטגרל הלא מסוים של 2x?", "x²+C", ["2", "x"],
                   "נכון. הנגזרת של x² היא 2x, והקבוע נעלם בגזירה.", "חזרו אחורה מהנגזרת, והוסיפו C.")),
            ],
        },
        {
            "id": "path_math_bagrut5_05_probability",
            "he": "הסתברות",
            "en": "Probability",
            "ar": "احتمال",
            "blurb_he": "הסתברות מכיתה יא. שאלות מקוריות, לא משאלון.",
            "blurb_en": "Grade-11 probability. Original questions, not a paper.",
            "blurb_ar": "احتمال الصف الحادي عشر. أسئلة أصلية.",
            "emoji": "½",
            "minutes": 180,
            "band": (5, 8),
            "end_he": "סיימת את דרך ההסתברות.",
            "stages": [
                (1, "t_simple", "מרחב שווה", "Equally likely",
                 "כשכל התוצאות שוות, ההסתברות היא מספר המתאימות חלקי מספר כולן.",
                 q("קובייה הוגנת. הסתברות ל־6?", "1/6", ["1/2", "6"],
                   "נכון. תוצאה אחת מתוך שש.", "מונה 1, מכנה 6.")),
                (2, "t_union", "מאורעות זרים", "Disjoint events",
                 "למאורעות זרים, הסתברות האיחוד היא סכום ההסתברויות.",
                 q("P(A)=1/6 ו־P(B)=1/6 ואין חיתוך. מה P(A או B)?", "1/3", ["1/6", "1/36"],
                   "נכון. 1/6+1/6=1/3.", "זרים: מחברים, לא כופלים.")),
                (3, "t_cond", "הסתברות מותנית", "Conditional",
                 "P(A|B) = P(A ו־B) חלקי P(B), כש־P(B) חיובי.",
                 q("P(A ו־B)=1/6 ו־P(B)=1/2. מה P(A|B)?", "1/3", ["1/6", "1/2"],
                   "נכון. (1/6)/(1/2)=1/3.", "חלקו את החיתוך ב־P(B).")),
            ],
        },
        {
            "id": "path_math_bagrut5_06_vectors",
            "he": "וקטורים",
            "en": "Vectors",
            "ar": "متجهات",
            "blurb_he": "כיתה יב: וקטור, תלות לינארית, מכפלה סקלארית, הצגה אלגברית, וגליל ישר. מתוך yodbet5.pdf.",
            "blurb_en": "Grade 12 vectors from the official 5-unit syllabus.",
            "blurb_ar": "متجهات الصف الثاني عشر.",
            "emoji": "→",
            "minutes": 220,
            "band": (6, 8),
            "end_he": "סיימת את דרך הווקטורים.",
            "stages": [
                (1, "t_vec", "כפל בסקלר", "Scalar multiple",
                 "לכל וקטור u ולכל מספר ממשי a, המכפלה a·u היא וקטור.",
                 q("a מספר ממשי ו־u וקטור. a·u הוא?", "וקטור", ["סקלר בהכרח", "נקודה בלי כיוון"],
                   "נכון. כפל בסקלר נשאר וקטור.", "התוצאה אינה מספר.")),
                (2, "t_dep", "תלות לינארית", "Linear dependence",
                 "וקטור תלוי לינארית בקבוצה אם הוא צירוף לינארי של הווקטורים בה.",
                 q("u = 2v. האם u תלוי לינארית ב־v?", "כן", ["לא", "רק כש־v הוא וקטור האפס"],
                   "נכון. כפולה היא צירוף לינארי.", "צירוף לינארי כולל כפל בסקלר.")),
                (2, "t_dot", "מכפלה סקלארית", "Scalar product",
                 "המכפלה הסקלארית היא מכפלת האורכים בקוסינוס הזווית שביניהם.",
                 q("הזווית בין שני וקטורים היא 90 מעלות. מה המכפלה הסקלארית?", "0", ["מכפלת האורכים", "1"],
                   "נכון. קוסינוס 90 מעלות הוא 0.", "לא מחברים אורכים.")),
                (3, "t_coord", "הצגה אלגברית", "Coordinates",
                 "וקטור שזנבו בראשית מיוצג על ידי נקודת הראש במרחב.",
                 q("זנב בראשית וראש ב־(1, 2, 3). מה הרכיב השלישי?", "3", ["1", "6"],
                   "נכון. הרכיב השלישי הוא 3.", "הראש קובע את הרכיבים.")),
                (3, "t_cyl", "גליל ישר", "Right cylinder",
                 "נפח גליל ישר הוא שטח הבסיס כפול הגובה.",
                 q("שטח הבסיס 10 וגובה 4. מה הנפח?", "40", ["14", "2.5"],
                   "נכון. 10×4 = 40.", "מכפלה של שטח וגובה.")),
            ],
        },
        {
            "id": "path_math_bagrut5_07_analytic",
            "he": "גאומטריה אנליטית",
            "en": "Analytic geometry",
            "ar": "هندسة تحليلية",
            "blurb_he": "כיתה יב: ישר, מעגל, פרבולה, אליפסה והיפרבולה. בלי חתכי חרוט שהם העשרה.",
            "blurb_en": "Grade-12 analytic geometry: line, circle, and the three conics.",
            "blurb_ar": "هندسة تحليلية للصف الثاني عشر.",
            "emoji": "○",
            "minutes": 220,
            "band": (6, 8),
            "end_he": "סיימת את דרך הגאומטריה האנליטית.",
            "stages": [
                (1, "t_div", "חלוקת קטע", "Dividing a segment",
                 "חלוקה פנימית ביחס m:n מ־A ל־B שמה נקודה במרחק m/(m+n) מאורך הקטע, החל מ־A.",
                 q("מ־0 עד 6 על ציר ה־x, יחס 1:2. מה x?", "2", ["3", "4"],
                   "נכון. 1/(1+2) מ־6 הוא 2.", "המונה הוא החלק הראשון.")),
                (2, "t_circ", "מעגל", "Circle",
                 "על מעגל שמרכזו בראשית ורדיוסו r מתקיים x²+y²=r².",
                 q("רדיוס 5. הנקודה (3, 4) נמצאת?", "על המעגל", ["בתוך המעגל", "מחוץ למעגל"],
                   "נכון. 9+16=25.", "השוו את סכום הריבועים ל־r².")),
                (3, "t_par", "פרבולה", "Parabola",
                 "בפרבולה, המרחק מנקודה למוקד שווה למרחקה מהמדריך.",
                 q("נקודה על הפרבולה. המרחק למוקד הוא 4. מה המרחק למדריך?", "4", ["2", "8"],
                   "נכון. שני המרחקים שווים.", "לא כופלים.")),
                (3, "t_ell", "אליפסה", "Ellipse",
                 "באליפסה, סכום המרחקים משני המוקדים קבוע.",
                 q("הסכום הקבוע הוא 10. מרחק למוקד אחד הוא 4. מה המרחק לשני?", "6", ["14", "2.5"],
                   "נכון. 10−4 = 6.", "מחברים ל־10, לא כופלים.")),
                (3, "t_hyp", "היפרבולה", "Hyperbola",
                 "בהיפרבולה, הפרש המרחקים משני המוקדים קבוע.",
                 q("ההפרש הקבוע הוא 2. המרחק למוקד הקרוב הוא 5. מה המרחק לרחוק?", "7", ["3", "10"],
                   "נכון. 5+2 = 7.", "ההפרש, לא הסכום.")),
            ],
        },
        {
            "id": "path_math_bagrut5_08_exp",
            "he": "מעריכית ולוגריתם",
            "en": "Exponential and logarithm",
            "ar": "أسيّة ولوغاريتم",
            "blurb_he": "כיתה יב: אלגברה של לוגריתם, נגזרת של e^x, ואינטגרל של 1/x. בלי חזקה עם מעריך שבור.",
            "blurb_en": "Grade-12 exponential and logarithm: algebra, derivative, integral.",
            "blurb_ar": "دوال أسية ولوغاريتمية.",
            "emoji": "e",
            "minutes": 200,
            "band": (6, 8),
            "end_he": "סיימת את דרך המעריכית והלוגריתם.",
            "stages": [
                (1, "t_log", "לוגריתם של מכפלה", "Log of a product",
                 "לוגריתם של מכפלה, באותו בסיס, הוא סכום הלוגריתמים.",
                 q("log 2 + log 5, אותו בסיס. זה שווה?", "log 10", ["log 7", "log 25"],
                   "נכון. סכום לוגריתמים הוא לוגריתם המכפלה.", "לא מחברים את המספרים עצמם.")),
                (2, "t_exp", "נגזרת מעריכית", "Exponential derivative",
                 "הנגזרת של e^x היא e^x.",
                 q("מה הנגזרת של e^x?", "e^x", ["x", "1"],
                   "נכון. הפונקציה שווה לנגזרת שלה.", "לא מורידים חזקה כמו בפולינום.")),
                (3, "t_ln", "אינטגרל של 1/x", "Integral of 1/x",
                 "האינטגרל של 1/x הוא ln|x| ועוד קבוע.",
                 q("מה האינטגרל הלא מסוים של 1/x?", "ln|x|+C", ["1/x²", "x"],
                   "נכון. זו פונקציה קדומה לוגריתמית, והקבוע נשאר.", "לא גוזרים את 1/x.")),
            ],
        },
        {
            "id": "path_math_bagrut5_09_complex",
            "he": "מספרים מרוכבים",
            "en": "Complex numbers",
            "ar": "أعداد مركبة",
            "blurb_he": "כיתה יב: i², ערך מוחלט, דה־מואבר, ושורשי היחידה. בלי הצגה מעריכית, שהיא העשרה.",
            "blurb_en": "Grade-12 complex numbers. The exponential form is enrichment and is not here.",
            "blurb_ar": "أعداد مركبة للصف الثاني عشر.",
            "emoji": "i",
            "minutes": 180,
            "band": (6, 8),
            "end_he": "סיימת את דרך המספרים המרוכבים.",
            "stages": [
                (1, "t_i", "המספר i", "The number i",
                 "המספר i מקיים i² = -1.",
                 q("מה i²?", "-1", ["1", "0"],
                   "נכון. זה הסימן של i.", "לא 1.")),
                (2, "t_mod", "ערך מוחלט", "Modulus",
                 "הערך המוחלט של a+bi הוא השורש של a²+b².",
                 q("מה הערך המוחלט של 3+4i?", "5", ["7", "12"],
                   "נכון. שורש של 9+16 הוא 5.", "לא מחברים את 3 ו־4.")),
                (3, "t_moivre", "דה־מואבר", "De Moivre",
                 "לפי משפט דה־מואבר, הזווית בהצגה הקוטבית מוכפלת במעריך.",
                 q("זווית 30 מעלות בחזקה 2. מה הזווית החדשה?", "60 מעלות", ["15 מעלות", "90 מעלות"],
                   "נכון. 30×2 = 60.", "כופלים את הזווית, לא מחלקים.")),
                (3, "t_unity", "שורשי היחידה", "Roots of unity",
                 "שורשי היחידה מסדר n יושבים כקודקודי מצולע משוכלל בעל n צלעות.",
                 q("שורשי היחידה מסדר 4 יושבים על קודקודי?", "ריבוע", ["משולש", "קטע"],
                   "נכון. ארבעה קודקודים הם ריבוע.", "מספר הצלעות הוא הסדר.")),
            ],
        },
    ]
    for spec in math_roads:
        spec.update(subject="math", place=MATH_PLACE, content_locale="he", ar=spec["ar"])
        out.append((spec["id"], road(spec)))

    out.append(
        (
            PHYS_PLACE,
            placement(
                {
                    "id": PHYS_PLACE,
                    "subject": "physics",
                    "emoji": "Φ",
                    "he": "מבדק רמה בפיזיקה",
                    "en": "Physics level check",
                    "ar": "اختبار مستوى الفيزياء",
                    "blurb_he": "ארבע שאלות: מכניקה, חשמל, גלים, וקרינה. המעבדה אינה כאן.",
                    "blurb_en": "Four questions: mechanics, electricity, waves, radiation. No lab.",
                    "blurb_ar": "أربعة أسئلة. بلا مختبر.",
                    "items": [
                        {
                            "title": "מהירות",
                            "en": "Speed",
                            "ask": "גוף נע 10 מטר ב־2 שניות במהירות קבועה. מה המהירות?",
                            "ok": "5 מטר לשנייה",
                            "bad": ["20 מטר לשנייה", "8 מטר לשנייה"],
                            "ok_he": "נכון. דרך חלקי זמן היא 5.",
                            "try_he": "חלקו דרך בזמן.",
                            "area": "mechanics",
                            "b": -1.0,
                        },
                        {
                            "title": "חוק אום",
                            "en": "Ohm",
                            "ask": "מתח 6 וולט, זרם 2 אמפר. מה ההתנגדות?",
                            "ok": "3 אום",
                            "bad": ["12 אום", "4 אום"],
                            "ok_he": "נכון. R = V/I = 3.",
                            "try_he": "מתח חלקי זרם.",
                            "area": "electricity",
                            "b": 0.0,
                        },
                        {
                            "title": "גל",
                            "en": "Wave",
                            "ask": "תדירות 2 הרץ ואורך גל 3 מטר. מה מהירות הגל?",
                            "ok": "6 מטר לשנייה",
                            "bad": ["1.5 מטר לשנייה", "5 מטר לשנייה"],
                            "ok_he": "נכון. v = fλ = 6.",
                            "try_he": "מכפלה, לא מנה.",
                            "area": "waves",
                            "b": 0.6,
                        },
                        {
                            "title": "פוטון",
                            "en": "Photon",
                            "ask": "אנרגיית פוטון גדלה כשהתדירות?",
                            "ok": "גדלה",
                            "bad": ["קטנה", "אינה משתנה"],
                            "ok_he": "נכון. E = hf, אז תדירות גבוהה יותר היא אנרגיה גבוהה יותר.",
                            "try_he": "האנרגיה יחסית לתדירות.",
                            "area": "modern",
                            "b": 1.0,
                        },
                    ],
                }
            ),
        )
    )
    physics = [
        {
            "id": "path_physics_bagrut5_01_mechanics",
            "he": "מכניקה",
            "en": "Mechanics",
            "ar": "ميكانيكا",
            "blurb_he": "קינמטיקה, חוקי ניוטון ואנרגיה. לפי תוכנית 5 יחידות, בלי מעבדה.",
            "blurb_en": "Kinematics, Newton's laws, and energy. No lab.",
            "blurb_ar": "حركة وقوانين نيوتن وطاقة.",
            "emoji": "Φ",
            "minutes": 240,
            "band": (1, 1),
            "end_he": "סיימת את דרך המכניקה.",
            "stages": [
                (1, "t_kin", "תנועה קצובה", "Constant velocity",
                 "במהירות קבועה, הדרך היא מהירות כפול זמן.",
                 q("מהירות 4 מטר לשנייה במשך 3 שניות. מה הדרך?", "12 מטר", ["7 מטר", "1.3 מטר"],
                   "נכון. 4×3 = 12.", "מכפלה, לא סכום.")),
                (2, "t_newton", "החוק השני", "Second law",
                 "החוק השני: הכוח השקול שווה מסה כפול תאוצה.",
                 q("מסה 2 קילוגרם ותאוצה 3 מטר לשנייה בריבוע. מה הכוח השקול?", "6 ניוטון", ["5 ניוטון", "1.5 ניוטון"],
                   "נכון. F = ma = 6.", "מסה כפול תאוצה.")),
                (3, "t_energy", "אנרגיה קינטית", "Kinetic energy",
                 "אנרגיה קינטית היא חצי מסה כפול מהירות בריבוע.",
                 q("מסה 2 קילוגרם ומהירות 3 מטר לשנייה. מה האנרגיה הקינטית?", "9 ג'ול", ["6 ג'ול", "18 ג'ול"],
                   "נכון. 0.5×2×9 = 9.", "ריבוע המהירות, ואז חצי המסה.")),
            ],
        },
        {
            "id": "path_physics_bagrut5_02_electricity",
            "he": "חשמל",
            "en": "Electricity",
            "ar": "كهرباء",
            "blurb_he": "זרם, חוק אום, ונגדים בטור. מגנטיות היא דרך נפרדת, לא שאלון מועתק.",
            "blurb_en": "Current, Ohm's law, and resistors in series.",
            "blurb_ar": "تيار وقانون أوم ومقاومات على التوالي.",
            "emoji": "Ω",
            "minutes": 200,
            "band": (2, 2),
            "end_he": "סיימת את דרך החשמל.",
            "stages": [
                (1, "t_ohm", "חוק אום", "Ohm's law",
                 "המתח שווה זרם כפול התנגדות.",
                 q("זרם 2 אמפר והתנגדות 4 אום. מה המתח?", "8 וולט", ["2 וולט", "6 וולט"],
                   "נכון. V = IR = 8.", "מכפלה של זרם והתנגדות.")),
                (2, "t_series", "טור", "Series",
                 "בטור, ההתנגדות הכוללת היא סכום ההתנגדויות.",
                 q("2 אום בטור עם 3 אום. מה הסכום?", "5 אום", ["6 אום", "1.2 אום"],
                   "נכון. 2+3 = 5.", "בטור מחברים.")),
                (3, "t_power", "הספק", "Power",
                 "ההספק שווה מתח כפול זרם.",
                 q("מתח 3 וולט וזרם 2 אמפר. מה ההספק?", "6 ואט", ["1.5 ואט", "5 ואט"],
                   "נכון. P = VI = 6.", "מכפלה, לא מנה.")),
            ],
        },
        {
            "id": "path_physics_bagrut5_03_waves",
            "he": "גלים ואופטיקה",
            "en": "Waves and optics",
            "ar": "موجات وبصريات",
            "blurb_he": "אופטיקה גיאומטרית וגלים חד־ממדיים, כפי שמופיעים בתוכנית 5 יחידות.",
            "blurb_en": "Geometric optics and one-dimensional waves.",
            "blurb_ar": "بصريات هندسية وموجات.",
            "emoji": "∿",
            "minutes": 200,
            "band": (3, 3),
            "end_he": "סיימת את דרך הגלים והאופטיקה.",
            "stages": [
                (1, "t_mirror", "החזרה", "Reflection",
                 "במראה מישורית, זווית הפגיעה שווה לזווית ההחזרה.",
                 q("זווית הפגיעה 30 מעלות. מה זווית ההחזרה?", "30 מעלות", ["60 מעלות", "0 מעלות"],
                   "נכון. הזוויות שוות.", "לא מחברים ל־90.")),
                (2, "t_wave", "מהירות גל", "Wave speed",
                 "מהירות הגל שווה תדירות כפול אורך גל.",
                 q("תדירות 5 הרץ ואורך גל 2 מטר. מה המהירות?", "10 מטר לשנייה", ["7 מטר לשנייה", "2.5 מטר לשנייה"],
                   "נכון. 5×2 = 10.", "מכפלה של תדירות ואורך.")),
                (3, "t_lens", "עדשה דקה", "Thin lens",
                 "בעדשה מרכזת, קרן מקבילה לציר עוברת אחרי העדשה דרך המוקד.",
                 q("קרן מקבילה לציר פוגעת בעדשה מרכזת. לאן היא ממשיכה?", "דרך המוקד", ["בלי לסטות", "אל המרכז בלבד"],
                   "נכון. קרן מקבילה נשברת אל המוקד.", "המרכז עצמו מעביר קרן בלי סטייה, לא את המקבילה.")),
            ],
        },
        {
            "id": "path_physics_bagrut5_04_modern",
            "he": "קרינה וחומר",
            "en": "Radiation and matter",
            "ar": "إشعاع ومادة",
            "blurb_he": "החלק המודרני בתוכנית: פוטון ורמות אנרגיה, בניסוח איכותי. בלי מעבדה.",
            "blurb_en": "The modern part: photon and energy levels, qualitative. No lab.",
            "blurb_ar": "الفوتون ومستويات الطاقة. بلا مختبر.",
            "emoji": "ℏ",
            "minutes": 160,
            "band": (4, 8),
            "end_he": "סיימת את דרך הקרינה והחומר.",
            "stages": [
                (1, "t_photon", "פוטון", "Photon",
                 "אנרגיית פוטון היא קבוע פלאנק כפול התדירות.",
                 q("אם התדירות מוכפלת, אנרגיית הפוטון?", "מוכפלת", ["נשארת", "יורדת לחצי"],
                   "נכון. E יחסית ל־f.", "הקבוע אינו משתנה.")),
                (2, "t_photo", "אפקט פוטואלקטרי", "Photoelectric",
                 "מתחת לתדירות סף אין פליטת אלקטרונים, גם אם האור חזק.",
                 q("תדירות מתחת לסף ואור חזק. האם נפלטים אלקטרונים?", "לא", ["כן", "רק אם המנורה קרובה"],
                   "נכון. הסף הוא בתדירות, לא בעוצמה.", "עוצמה אינה מחליפה תדירות סף.")),
                (3, "t_level", "רמות", "Levels",
                 "אטום פולט פוטון כשהוא יורד מרמה גבוהה לנמוכה. הפרש הרמות הוא אנרגיית הפוטון.",
                 q("ירידה מרמה גבוהה לנמוכה. מה קורה לאנרגיה?", "נפלט פוטון", ["נבלע פוטון בהכרח", "האטום נעלם"],
                   "נכון. הפרש הרמות יוצא כפוטון.", "בליעה היא עלייה, לא ירידה.")),
            ],
        },
        {
            "id": "path_physics_bagrut5_05_magnetism",
            "he": "מגנטיות",
            "en": "Magnetism",
            "ar": "مغناطيسية",
            "blurb_he": "מתוך טבלת 5 יחידות: מקורות השדה, כוח לורנץ, האמפר, וחוק פרדיי. לא ניסוי מעבדה.",
            "blurb_en": "5-unit magnetism: field sources, Lorentz force, the ampere, Faraday. Not a lab.",
            "blurb_ar": "مغناطيسية برنامج 5 وحدات. بلا مختبر.",
            "emoji": "Φ",
            "minutes": 180,
            "band": (6, 8),
            "end_he": "סיימת את דרך המגנטיות.",
            "stages": [
                (1, "t_src", "מקורות השדה", "Field sources",
                 "תיל ישר וארוך, כריכה מעגלית וסילונית הם מקורות לשדה מגנטי כשזורם בהם זרם.",
                 q("סילונית נושאת זרם. האם היא מקור לשדה מגנטי?", "כן", ["לא", "רק בלי זרם"],
                   "נכון. סילונית עם זרם מופיעה ברשימת המקורות.", "בלי זרם אין את המקור הזה.")),
                (2, "t_lorentz", "כוח לורנץ", "Lorentz force",
                 "כוח לורנץ פועל על מטען שנע בשדה מגנטי, לא על מטען שנח.",
                 q("מטען במנוחה בשדה מגנטי. האם פועל עליו כוח לורנץ?", "לא", ["כן", "רק אם המטען חיובי"],
                   "נכון. הכוח דורש תנועה.", "מנוחה אינה מספיקה.")),
                (2, "t_amp", "האמפר", "The ampere",
                 "האמפר מוגדר באמצעות הכוח בין שני תיילים מקבילים נושאי זרם.",
                 q("הגדרת האמפר נשענת על כוח בין?", "זרמים מקבילים", ["מטענים במנוחה בלבד", "שני מראות"],
                   "נכון. זה הכוח בין זרמים מקבילים.", "לא בין מטענים שנחים.")),
                (3, "t_faraday", "חוק פרדיי", "Faraday's law",
                 "כא״מ מושרה נוצר כשהשטף המגנטי דרך מעגל משתנה. חוק לנץ: הזרם המושרה מתנגד לשינוי.",
                 q("השטף דרך כריכה קבוע. האם יש כא״מ מושרה?", "לא", ["כן", "רק אם הכריכה מנחושת"],
                   "נכון. בלי שינוי בשטף אין כא״מ מושרה.", "החומר לבדו אינו יוצר כא״מ.")),
            ],
        },
    ]
    for spec in physics:
        spec.update(subject="physics", place=PHYS_PLACE, content_locale="he")
        out.append((spec["id"], road(spec)))

    arabic = [
        {
            "id": "path_arabic_bagrut5_02_words",
            "he": "מילים ומשפט קצר",
            "en": "Words and a short sentence",
            "ar": "كلمات وجملة قصيرة",
            "blurb_he": "אחרי האותיות: מילים ומשפט קצר בספרותית, ומילת דיבור אחת. לא שאלון.",
            "blurb_en": "After the letters: words and a short sentence in MSA, plus one spoken word.",
            "blurb_ar": "بعد الحروف: كلمات وجملة قصيرة.",
            "emoji": "ب",
            "minutes": 160,
            "band": (2, 3),
            "content_locale": "ar",
            "end_he": "סיימת את דרך המילים.",
            "stages": [
                (1, "t_hello", "שלום", "Hello",
                 "בספרותית אומרים مرحبا. בדיבור, לפי מאגר השאלות של המשרד, מופיע كيفك.",
                 q("איך אומרים שלום בספרותית?", "مرحبا", ["كتاب", "مدرسة"],
                   "נכון. مرحبا היא ברכה.", "كتاب היא ספר.", content="مرحبا", speak="مرحبا")),
                (2, "t_num", "מספרים", "Numbers",
                 "אחד בספרותית הוא واحد. שתיים הוא اثنان.",
                 q("מה פירוש واحد?", "אחד", ["שלוש", "בית"],
                   "נכון. واحد הוא אחד.", "אל תערבבו עם اثنان.", content="واحد")),
                (3, "t_sent", "משפט", "Sentence",
                 "هذا كتاب הוא משפט שמני: זה ספר.",
                 q("מה פירוש هذا كتاب?", "זה ספר", ["זה בית", "אני תלמיד"],
                   "נכון. هذا זה, كتاب ספר.",
                   "كتاب אינו בית.", content="هذا كتاب")),
            ],
        },
        {
            "id": "path_arabic_bagrut5_03_verbs",
            "he": "פועל",
            "en": "The verb",
            "ar": "الفعل",
            "blurb_he": "פועל בהווה ובעבר, בספרותית, עם דוגמה מדוברת אחת.",
            "blurb_en": "Present and past in MSA, plus one spoken form.",
            "blurb_ar": "المضارع والماضي.",
            "emoji": "ك",
            "minutes": 180,
            "band": (4, 4),
            "content_locale": "ar",
            "end_he": "סיימת את דרך הפועל.",
            "stages": [
                (1, "t_pres", "הווה", "Present",
                 "יكتب הוא הוא כותב. הקידומת ي מסמנת גוף שלישי.",
                 q("מה פירוש يكتب?", "הוא כותב", "הוא כתב|אני כותב".split("|"),
                   "נכון. يكتب הוא הווה, גוף שלישי.", "كتب בלי י היא עבר.", content="يكتب")),
                (2, "t_past", "עבר", "Past",
                 "كتب הוא הוא כתב.",
                 q("מה פירוש كتب?", "הוא כתב", ["הוא כותב", "היא כתבה"],
                   "נכון. كتب הוא עבר, הוא.", "ההווה הוא يكتب.", content="كتب")),
                (3, "t_spoken", "דיבור", "Spoken",
                 "בדיבור, בדוגמאות של מאגר המשרד, בدي מסמן רצון: אני רוצה.",
                 q("מה קרוב ל־بدي?", "אני רוצה", ["אני כתבתי", "ספר"],
                   "נכון. بدي הוא צורת דיבור של רצון.", "זו אינה מילת ספר.", content="بدي", speak="بدي")),
            ],
        },
        {
            "id": "path_arabic_bagrut5_04_reading",
            "he": "קריאה קצרה",
            "en": "A short reading",
            "ar": "قراءة قصيرة",
            "blurb_he": "קטע מקורי קצר. לא מעתיקים טקסט משאלון.",
            "blurb_en": "A short original passage. Not copied from a paper.",
            "blurb_ar": "نص قصير أصلي.",
            "emoji": "ق",
            "minutes": 180,
            "band": (5, 5),
            "content_locale": "ar",
            "end_he": "סיימת את דרך הקריאה.",
            "stages": [
                (1, "t_where", "מקום", "Place",
                 "הקטע המקורי: الطالب في البيت. הוא בבית, לא בבית הספר.",
                 q("איפה الطالب במשפט الطالب في البيت?", "בבית", ["בבית הספר", "ברחוב"],
                   "נכון. البيت הוא הבית.", "المدرسة היא בית הספר.", content="الطالب في البيت")),
                (2, "t_who", "מי", "Who",
                 "באותו משפט הנושא הוא الطالب, התלמיד.",
                 q("מי הנושא במשפט الطالب في البيت?", "התלמיד", ["הבית", "המורה"],
                   "נכון. الطالب הוא הנושא.",
                   "البيت הוא מקום, לא נושא.", content="الطالب")),
                (3, "t_not", "שלילה", "Negation",
                 "ليس في المدرسة: הוא אינו בבית הספר.",
                 q("מה פירוש ليس في المدرسة?", "אינו בבית הספר", ["הוא בבית הספר", "יש ספר"],
                   "נכון. ليس שולל.", "ليس אינו יש.", content="ليس في المدرسة")),
            ],
        },
        {
            "id": "path_arabic_bagrut5_05_exam",
            "he": "לקראת בחינה",
            "en": "Toward the exam",
            "ar": "نحو الامتحان",
            "blurb_he": "סוגי משימה: קריאה, משפט, ודיבור. בלי שאלה שהועתקה משאלון.",
            "blurb_en": "Task types: reading, a sentence, and speaking. No copied item.",
            "blurb_ar": "قراءة وجملة وكلام. بلا سؤال منسوخ.",
            "emoji": "ه",
            "minutes": 200,
            "band": (6, 8),
            "content_locale": "ar",
            "end_he": "סיימת את הדרך לקראת הבחינה. זה אינו ציון משרד.",
            "stages": [
                (1, "t_readq", "שאלת קריאה", "Reading question",
                 "שואלים איפה, מי, ולמה. התשובה נמצאת במשפט, לא מנחשים.",
                 q("במשפט الكتاب على الطاولة, איפה הספר?", "על השולחן", ["על הכיסא", "בתיק"],
                   "נכון. على الطاولة הוא על השולחן.", "המילה الطاولة היא השולחן.", content="الكتاب على الطاولة")),
                (2, "t_write", "משפט כתוב", "A written sentence",
                 "משפט שמני קצר: أنا طالب. אני תלמיד.",
                 q("מה פירוש أنا طالب?", "אני תלמיד", ["אתה תלמיד", "אני מורה"],
                   "נכון. أنا אני, طالب תלמיד.", "أنت הוא אתה.", content="أنا طالب")),
                (3, "t_oral", "תור דיבור", "A spoken turn",
                 "פותחים בדיבור בשם ובברכה. הדוגמה המקורית: أنا اسمي سامع, كيفك.",
                 q("מה מתאים לפתיחת דיבור?", "اسمي وברכה", ["רשימת דקדוק", "שקט"],
                   "נכון. אומרים שם וברכה.", "אין כאן שאלון בעל פה מועתק.", content="كيفك", speak="كيفك")),
            ],
        },
    ]
    for spec in arabic:
        spec.update(subject="arabic", place=AR_PLACE)
        out.append((spec["id"], road(spec)))
    return out


def main() -> None:
    for name, doc in build():
        path = ADULT / f"{name}.json"
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(path.name, "nodes", len(doc["nodes"]))


if __name__ == "__main__":
    main()
