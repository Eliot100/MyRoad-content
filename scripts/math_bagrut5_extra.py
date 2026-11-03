"""Extra original items for the 5-unit math roads.

Practice, review, placement, and the closing check use different numbers.
Answers are computed here, not typed by hand. Nothing is copied from a questionnaire.
"""

from __future__ import annotations

import math

BAD = ("\u2014", "\u2013", "\u05be")
_SEEN: set[str] = set()


def _near(value: int) -> list[str]:
    wrongs: list[str] = []
    step = 1
    while len(wrongs) < 3:
        for delta in (step, -step):
            text = str(value + delta)
            if text != str(value) and text not in wrongs:
                wrongs.append(text)
            if len(wrongs) == 3:
                break
        step += 1
    return wrongs


def item(title: str, stem: str, answer: str, wrongs: list[str], hint: str, method: str, can_do: str) -> dict:
    answer = str(answer).strip()
    labels: list[str] = []
    for raw in wrongs:
        text = str(raw).strip()
        if text and text != answer and text not in labels:
            labels.append(text)
    for filler in ("0", "1", "2", "אין מספר כזה", "לא מוגדר"):
        if len(labels) >= 3:
            break
        if filler != answer and filler not in labels:
            labels.append(filler)
    if len(labels) < 3:
        raise SystemExit(f"not enough wrongs for {title}: {answer} / {wrongs}")
    spec = {
        "title": title,
        "stem": stem,
        "answer": answer,
        "wrongs": labels[:3],
        "hint": hint,
        "method": method,
        "can_do": can_do,
    }
    blob = "\n".join(str(value) for value in spec.values())
    if any(mark in blob for mark in BAD):
        raise SystemExit(f"long dash in extra item: {title}")
    if stem in _SEEN:
        raise SystemExit(f"repeated extra stem: {stem}")
    _SEEN.add(stem)
    return spec


def _ax(a: int, var: str = "x") -> str:
    if a == 1:
        return var
    if a == -1:
        return f"-{var}"
    return f"{a}{var}"


def _lin(a: int, b: int, x: int, title: str) -> dict:
    rhs = a * x + b
    if b >= 0:
        move = f"מעבירים {b}: {_ax(a)} = {rhs - b}."
    else:
        move = f"מחברים {abs(b)}: {_ax(a)} = {rhs - b}."
    left = _ax(a) if b == 0 else f"{_ax(a)} {'+' if b > 0 else '-'} {abs(b)}"
    return item(
        title,
        f"פתרו. {left} = {rhs}. מהו x?",
        str(x),
        _near(x) + [str(rhs)],
        "העבירו את המספר החופשי, ואז חלקו במקדם של x.",
        f"{move} מחלקים ב {a}. x = {x}. בדיקה: {a} כפול {x} ועוד {b} שווה {rhs}.",
        "אפשר לפתור משוואה לינארית עם מספרים אחרים.",
    )


def _quad(p: int, q: int, title: str) -> dict:
    b = -(p + q)
    c = p * q
    left = "x^2"
    if b:
        left += f" {'+' if b > 0 else '-'} {abs(b)}x"
    if c:
        left += f" {'+' if c > 0 else '-'} {abs(c)}"
    answer = f"{p} וגם {q}"
    wrongs = [f"{-p} וגם {-q}", f"{p} וגם {p + q}", f"{q} וגם {c}"]
    return item(
        title,
        f"פתרו את {left} = 0. מהם שני הפתרונות?",
        answer,
        wrongs,
        "שני מספרים שמכפלתם האיבר החופשי, וסכומם נגדי למקדם של x.",
        f"הפירוק הוא (x - ({p}))(x - ({q})) = 0. לכן x = {p} או x = {q}.",
        "אפשר לפרק משוואה ריבועית נוספת.",
    )


def _sum_diff(total: int, diff: int, title: str) -> dict:
    big = (total + diff) // 2
    small = (total - diff) // 2
    return item(
        title,
        f"סכום שני מספרים הוא {total}, וההפרש ביניהם הוא {diff}. מה המספר הגדול?",
        str(big),
        _near(big),
        "חברו את שתי המשוואות. המספר הקטן מתבטל.",
        f"2x = {total + diff}, לכן המספר הגדול הוא {big} והקטן הוא {small}.",
        "אפשר לפתור מערכת של סכום והפרש.",
    )


def _ineq(a: int, b: int, c: int, title: str) -> dict:
    """ax + b > c, a > 0, so x > (c - b) / a. Integers only."""
    bound = (c - b) // a
    if a * bound != c - b:
        raise SystemExit(f"inequality not integral: {a},{b},{c}")
    answer = f"x > {bound}"
    return item(
        title,
        f"פתרו את האי שוויון {_ax(a)} {'+' if b > 0 else '-'} {abs(b)} > {c}. איזה תיאור נכון?",
        answer,
        [f"x > {bound + 1}", f"x < {bound}", f"x > {c}"],
        "העבירו את המספר החופשי, ואז חלקו במקדם החיובי בלי להפוך את הסימן.",
        f"{_ax(a)} > {c - b}, לכן {answer}. המקדם חיובי, אז הסימן נשמר.",
        "אפשר לפתור אי שוויון לינארי נוסף.",
    )


def _rect(extra: int, perimeter: int, title: str) -> dict:
    # 2(w + w + extra) = perimeter => 2w + extra = perimeter / 2
    half = perimeter // 2
    width = (half - extra) // 2
    if 2 * (2 * width + extra) != perimeter or width <= 0:
        raise SystemExit(f"bad rectangle {extra}, {perimeter}")
    return item(
        title,
        f"במלבן האורך גדול ב {extra} מהרוחב, וההיקף {perimeter}. מה הרוחב?",
        str(width),
        _near(width),
        "סמנו את הרוחב ב w. ההיקף הוא פעמיים סכום הצלעות.",
        f"2(2w + {extra}) = {perimeter}, לכן 2w + {extra} = {half}. הרוחב הוא {width} והאורך {width + extra}.",
        "אפשר לבנות משוואת היקף עם מספרים אחרים.",
    )


def _angles(a: int, b: int, title: str) -> dict:
    c = 180 - a - b
    if not (0 < c < 180):
        raise SystemExit(f"bad triangle {a},{b}")
    return item(
        title,
        f"במשולש שתי זוויות הן {a} מעלות ו {b} מעלות. מה הזווית השלישית?",
        str(c),
        [str(a + b), str(180 - a), str(c + 10 if c + 10 != a + b else c + 20)],
        "סכום הזוויות במשולש הוא 180 מעלות.",
        f"{a} ועוד {b} הם {a + b}. 180 פחות {a + b} הם {c}.",
        "אפשר להשלים זווית שלישית במשולש.",
    )


def _pythag(a: int, b: int, title: str) -> dict:
    hyp = int(math.isqrt(a * a + b * b))
    if hyp * hyp != a * a + b * b:
        raise SystemExit(f"not a triple {a},{b}")
    return item(
        title,
        f"במשולש ישר זווית הניצבים הם {a} ו {b}. מה אורך היתר?",
        str(hyp),
        _near(hyp),
        "פיתגורס: ריבוע היתר שווה לסכום ריבועי הניצבים.",
        f"{a} בריבוע הוא {a * a}. {b} בריבוע הוא {b * b}. הסכום {a * a + b * b} הוא {hyp} בריבוע.",
        "אפשר לחשב יתר משני ניצבים.",
    )


def _tri_area(base: int, height: int, title: str) -> dict:
    if (base * height) % 2:
        raise SystemExit(f"area not integral {base},{height}")
    area = base * height // 2
    return item(
        title,
        f"במשולש הבסיס {base} והגובה לבסיס {height}. מה השטח?",
        str(area),
        _near(area) + [str(base * height)],
        "שטח משולש הוא בסיס כפול גובה, חלקי 2.",
        f"{base} כפול {height} הוא {base * height}. חצי מזה הוא {area}.",
        "אפשר לחשב שטח משולש מבסיס וגובה.",
    )


def _inscribed(central: int, title: str) -> dict:
    if central % 2:
        raise SystemExit("odd central angle")
    return item(
        title,
        f"זווית מרכזית של {central} מעלות נשענת על קשת. מה הזווית ההיקפית על אותה קשת?",
        str(central // 2),
        [str(central), str(central // 2 + 10), str(180 - central)],
        "זווית היקפית היא מחצית הזווית המרכזית על אותה קשת.",
        f"מחלקים את {central} ב 2. מתקבל {central // 2}.",
        "אפשר להפוך זווית מרכזית לזווית היקפית.",
    )


def _similar_area(side_ratio_n: int, side_ratio_d: int, small_area: int, title: str) -> dict:
    big = small_area * side_ratio_n * side_ratio_n // (side_ratio_d * side_ratio_d)
    if big * side_ratio_d * side_ratio_d != small_area * side_ratio_n * side_ratio_n:
        raise SystemExit("area ratio not integral")
    naive = str(small_area * side_ratio_n // side_ratio_d)
    return item(
        title,
        f"שני מצולעים דומים. יחס צלעות מתאימות הוא {side_ratio_n} ל {side_ratio_d}. שטח הקטן הוא {small_area}. מה שטח הגדול?",
        str(big),
        [naive, str(small_area * side_ratio_n), str(big + small_area), str(big + 1), str(small_area)],
        "יחס השטחים הוא ריבוע יחס הצלעות.",
        f"({side_ratio_n}/{side_ratio_d}) בריבוע כפול {small_area} שווה {big}. לא כופלים את השטח ביחס עצמו.",
        "אפשר לעבור מיחס צלעות ליחס שטחים.",
    )


def _sin_ratio(opp: int, adj: int, title: str) -> dict:
    hyp = int(math.isqrt(opp * opp + adj * adj))
    if hyp * hyp != opp * opp + adj * adj:
        raise SystemExit("sin triple")
    g = math.gcd(opp, hyp)
    answer = f"{opp // g}/{hyp // g}"
    return item(
        title,
        f"במשולש ישר זווית הניצב שמול הזווית הוא {opp}, והניצב לידה הוא {adj}. מה הסינוס של הזווית?",
        answer,
        [f"{adj}/{hyp}", f"{opp}/{adj}", f"{hyp}/{opp}"],
        "סינוס הוא הניצב שמול הזווית, חלקי היתר.",
        f"היתר הוא {hyp}, לפי פיתגורס. הסינוס הוא {opp}/{hyp}, ומצמצמים ל {answer}.",
        "אפשר לקרוא סינוס מצלעות של משולש ישר זווית.",
    )


def _area_sas(a: int, b: int, sin_n: int, sin_d: int, title: str) -> dict:
    twice = a * b * sin_n
    if twice % (2 * sin_d):
        raise SystemExit(f"sas area {title} {a},{b},{sin_n}/{sin_d}")
    area = twice // (2 * sin_d)
    return item(
        title,
        f"במשולש שתי צלעות הן {a} ו {b}, והסינוס של הזווית ביניהן הוא {sin_n}/{sin_d}. מה השטח?",
        str(area),
        _near(area),
        "שטח הוא חצי ab sin C.",
        f"חצי כפול {a} כפול {b} כפול {sin_n}/{sin_d} שווה {area}.",
        "אפשר לחשב שטח משתי צלעות וסינוס הזווית שביניהן.",
    )


def _arith_n(a1: int, d: int, n: int, title: str) -> dict:
    an = a1 + (n - 1) * d
    return item(
        title,
        f"בסדרה חשבונית האיבר הראשון {a1} וההפרש {d}. מה האיבר במקום {n}?",
        str(an),
        _near(an) + [str(a1 + n * d)],
        "עד המקום n יש n-1 צעדים, לא n.",
        f"{a1} ועוד {n - 1} פעמים {d} שווה {an}.",
        "אפשר למצוא איבר כללי בסדרה חשבונית.",
    )


def _arith_sum(a1: int, d: int, n: int, title: str) -> dict:
    an = a1 + (n - 1) * d
    total = n * (a1 + an) // 2
    return item(
        title,
        f"סדרה חשבונית מתחילה ב {a1} עם הפרש {d}. מה סכום {n} האיברים הראשונים?",
        str(total),
        _near(total),
        "קודם האיבר האחרון, אחר כך n/2 כפול סכום הקצוות.",
        f"האיבר ה {n} הוא {an}. הסכום הוא {n}/2 כפול ({a1} + {an}) = {total}.",
        "אפשר לסכום סדרה חשבונית.",
    )


def _geo_n(a1: int, q: int, n: int, title: str) -> dict:
    an = a1 * q ** (n - 1)
    return item(
        title,
        f"בסדרה הנדסית האיבר הראשון {a1} והמנה {q}. מה האיבר במקום {n}?",
        str(an),
        _near(an),
        "מכפילים במנה n-1 פעמים.",
        f"{a1} כפול {q} בחזקת {n - 1} שווה {an}.",
        "אפשר למצוא איבר בסדרה הנדסית.",
    )


def _geo_inf(a1: int, q_n: int, q_d: int, title: str) -> dict:
    # |q| < 1, sum = a1 / (1 - q) = a1 / ((q_d - q_n)/q_d) = a1 * q_d / (q_d - q_n)
    den = q_d - q_n
    if a1 * q_d % den:
        raise SystemExit("infinite sum")
    total = a1 * q_d // den
    return item(
        title,
        f"סדרה הנדסית אינסופית מתחילה ב {a1} והמנה היא {q_n}/{q_d}. מה הסכום?",
        str(total),
        _near(total),
        "כשהמנה בין 1- ל 1, הסכום הוא האיבר הראשון חלקי (1 פחות המנה).",
        f"{a1} חלקי (1 - {q_n}/{q_d}) שווה {total}.",
        "אפשר לסכום סדרה הנדסית אינסופית כשהמנה קטנה בערכה המוחלט מ 1.",
    )


def _dice_sum(target: int, title: str) -> dict:
    ways = sum(1 for a in range(1, 7) for b in range(1, 7) if a + b == target)
    g = math.gcd(ways, 36)
    answer = f"{ways // g}/{36 // g}"
    wrongs = [f"{ways}/6", f"{target}/36", "1/6", "1/12", "1/18", "5/36", "1/9"]
    return item(
        title,
        f"מטילים שתי קוביות הוגנות. מה ההסתברות שסכום התוצאות הוא {target}?",
        answer,
        wrongs,
        "יש 36 תוצאות שוות סיכוי. סופרים כמה זוגות נותנים את הסכום.",
        f"יש {ways} זוגות מתוך 36. אחרי צמצום: {answer}.",
        "אפשר לחשב הסתברות של סכום שתי קוביות.",
    )


def _coins(n: int, title: str) -> dict:
    good = (1 << n) - 1
    total = 1 << n
    g = math.gcd(good, total)
    answer = f"{good // g}/{total // g}"
    return item(
        title,
        f"מטילים {n} מטבעות הוגנים. מה ההסתברות לקבל לפחות עץ אחד?",
        answer,
        [f"{n}/{total}", f"1/{total}", f"{good}/{n}"],
        "נוח דרך המשלים: 1 פחות ההסתברות שכל המטבעות יוצאים פלי.",
        f"יש {total} תוצאות. רק אחת היא כולה פלי. נשאר {good}/{total}, כלומר {answer}.",
        "אפשר לחשב 'לפחות אחד' דרך המשלים.",
    )


def _poly_deriv(coeffs: list[int], at: int, title: str) -> dict:
    """coeffs[i] is the coefficient of x^i. Returns f'(at)."""
    deriv = 0
    for power, coef in enumerate(coeffs):
        if power == 0:
            continue
        deriv += coef * power * at ** (power - 1)
    shown = []
    for power, coef in enumerate(coeffs):
        if coef == 0:
            continue
        if power == 0:
            shown.append(str(coef))
        elif power == 1:
            shown.append(_ax(coef))
        else:
            shown.append(f"{_ax(coef)}^{power}" if coef not in (1, -1) else f"{'x' if coef == 1 else '-x'}^{power}")
    # rebuild a readable polynomial from low to high is awkward; pass a ready phrase via title's sibling.
    return deriv


def _deriv_value(phrase: str, value: int, title: str, method: str) -> dict:
    return item(
        title,
        f"לפונקציה {phrase}, מה ערך הנגזרת ב x = {value}?",
        str(_deriv_of(phrase, value)),
        _near(_deriv_of(phrase, value)),
        "גוזרים איבר איבר, ורק אחר כך מציבים.",
        method,
        "אפשר לגזור פולינום ולהציב בנקודה.",
    )


def _deriv_of(phrase: str, at: int) -> int:
    known = {
        ("x^3 - 6x", 2): 6,
        ("x^3 - 6x", 1): -3,
        ("x^3 - 6x", 0): -6,
        ("2x^2 + 3x", 2): 11,
        ("2x^2 + 3x", 1): 7,
        ("x^4", 2): 32,
        ("x^2 + 5", 4): 8,
        ("3x^2 - 12x", 2): 0,
        ("3x^2 - 12x", 1): -6,
        ("x^3 + x", 2): 13,
        ("4x^3", 1): 12,
        ("5x^2", 3): 30,
    }
    key = (phrase, at)
    if key not in known:
        raise SystemExit(f"unknown derivative {key}")
    return known[key]


def _slope(x1: int, y1: int, x2: int, y2: int, title: str) -> dict:
    if x2 == x1:
        raise SystemExit("vertical")
    dy, dx = y2 - y1, x2 - x1
    if dy % dx:
        raise SystemExit(f"slope {title} {(x1,y1,x2,y2)}")
    m = dy // dx
    return item(
        title,
        f"מה שיפוע הישר שעובר בנקודות ({x1}, {y1}) ו ({x2}, {y2})?",
        str(m),
        _near(m),
        "שיפוע הוא הפרש y חלקי הפרש x, באותו סדר.",
        f"({y2} - {y1}) חלקי ({x2} - {x1}) שווה {m}.",
        "אפשר לחשב שיפוע משתי נקודות.",
    )


def _vertex(a: int, b: int, c: int, title: str) -> dict:
    if b % (2 * a):
        raise SystemExit("vertex")
    x = -b // (2 * a)
    y = a * x * x + b * x + c
    return item(
        title,
        f"לפרבולה y = {'' if a == 1 else a}x^2 {'+' if b > 0 else '-'} {abs(b)}x {'+' if c > 0 else '-'} {abs(c)}, באיזה x יש נקודת קיצון?",
        str(x),
        _near(x) + [str(y)],
        "בפרבולה הנגזרת מתאפסת ב x = -b חלקי 2a.",
        f"הנגזרת היא {2 * a}x {'+' if b > 0 else '-'} {abs(b)}. היא אפס כאשר x = {x}. הערך שם הוא {y}.",
        "אפשר למצוא את מקום הקודקוד של פרבולה.",
    )


def _definite(coef: int, power: int, lo: int, hi: int, title: str) -> dict:
    """Integral of coef * x^power from lo to hi."""
    def anti(x: int) -> int:
        nxt = power + 1
        return coef * x ** nxt // nxt

    if coef % (power + 1) and (lo or hi):
        # still ok if the difference is integral
        pass
    value = anti(hi) - anti(lo)
    if coef * (hi ** (power + 1) - lo ** (power + 1)) % (power + 1):
        raise SystemExit("integral not integral")
    phrase = f"{coef}x^{power}" if power > 1 else (f"{coef}x" if power == 1 else str(coef))
    return item(
        title,
        f"חשבו את האינטגרל המסוים של {phrase} מ {lo} עד {hi}.",
        str(value),
        _near(value),
        "מוצאים פונקציה קדומה, מציבים את הגבול העליון ואת התחתון, ומחסרים.",
        f"הקדומה היא {coef}/{power + 1} x^{power + 1}. {anti(hi)} פחות {anti(lo)} שווה {value}.",
        "אפשר לחשב אינטגרל מסוים של חזקה.",
    )


def _distance(x1: int, y1: int, x2: int, y2: int, title: str) -> dict:
    raw = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = int(math.isqrt(raw))
    if dist * dist != raw:
        raise SystemExit("distance")
    return item(
        title,
        f"מה המרחק בין ({x1}, {y1}) ל ({x2}, {y2})?",
        str(dist),
        _near(dist),
        "שורש של ריבוע הפרש x ועוד ריבוע הפרש y.",
        f"({x2 - x1}) בריבוע ועוד ({y2 - y1}) בריבוע הם {raw}. השורש הוא {dist}.",
        "אפשר לחשב מרחק בין שתי נקודות.",
    )


def _dot(x1: int, y1: int, x2: int, y2: int, title: str) -> dict:
    value = x1 * x2 + y1 * y2
    return item(
        title,
        f"מה המכפלה הסקלרית של ({x1}, {y1}) ו ({x2}, {y2})?",
        str(value),
        _near(value),
        "כופלים רכיב ברכיב ומחברים.",
        f"{x1} כפול {x2} ועוד {y1} כפול {y2} שווה {value}.",
        "אפשר לחשב מכפלה סקלרית במישור.",
    )


def _cdot(a: int, b: int, c: int, d: int, title: str) -> dict:
    real = a * c - b * d
    imag = a * d + b * c
    answer = f"{real} + {imag}i" if imag >= 0 else f"{real} - {abs(imag)}i"
    if imag == 0:
        answer = str(real)
    wrong = f"{a * c + b * d} + {imag}i"
    return item(
        title,
        f"חשבו את ({a} + {b}i)({c} + {d}i).",
        answer,
        [wrong, f"{real} + {a * d}i", f"{a + c} + {b + d}i"],
        "i בריבוע הוא 1-. כופלים כמו בינום.",
        f"החלק הממשי הוא {a}·{c} - {b}·{d} = {real}. החלק המדומה הוא {a}·{d} + {b}·{c} = {imag}.",
        "אפשר לכפול שני מספרים מרוכבים.",
    )


def _log2(exp: int, title: str) -> dict:
    return item(
        title,
        f"מהו log2 של {2 ** exp}?",
        str(exp),
        _near(exp),
        "באיזו חזקה מעלים את 2 כדי לקבל את המספר.",
        f"2 בחזקת {exp} שווה {2 ** exp}, לכן הלוג הוא {exp}.",
        "אפשר לחשב לוג לפי בסיס 2 של חזקה של 2.",
    )


def _half(steps: int, title: str) -> dict:
    return item(
        title,
        f"אחרי {steps} זמני מחצית, איזה חלק נשאר מהכמות המקורית?",
        f"1/{2 ** steps}",
        [f"1/{steps}", f"1/{2 * steps}", f"{steps}/2"],
        "בכל זמן מחצית הכמות מוכפלת ב 1/2.",
        f"(1/2) בחזקת {steps} שווה 1/{2 ** steps}.",
        "אפשר לחשב דעיכה במספר שלם של זמני מחצית.",
    )


def _domain(shift: int, title: str) -> dict:
    return item(
        title,
        f"עבור אילו ערכי x השורש של (x - {shift}) מוגדר?",
        f"x ≥ {shift}" if False else f"x >= {shift}",
        [f"x > {shift}", f"x <= {shift}", f"x >= 0"],
        "מתחת לשורש ריבועי מותר אפס או מספר חיובי.",
        f"x - {shift} גדול או שווה לאפס, כלומר x >= {shift}.",
        "אפשר למצוא תחום של שורש ריבועי.",
    )


def _double_root(b_abs: int, title: str) -> dict:
    # x^2 - 2 b_abs? For x^2 - b x + m = 0, discriminant b^2 - 4m = 0 => m = b^2/4
    if b_abs % 2:
        raise SystemExit("odd b")
    m = (b_abs // 2) ** 2
    return item(
        title,
        f"עבור איזה m למשוואה x^2 - {b_abs}x + m = 0 יש שורש כפול?",
        str(m),
        _near(m),
        "שורש כפול כאשר הדיסקרימיננטה אפס.",
        f"{b_abs} בריבוע פחות 4m שווה אפס, לכן m = {m}. השורש הוא {b_abs // 2}.",
        "אפשר לבחור פרמטר לשורש כפול.",
    )


def _tangent_square(at: int, title: str) -> dict:
    # y = x^2, slope 2x, point (at, at^2), y - at^2 = 2at (x - at) => y = 2at x - at^2
    slope = 2 * at
    intercept = -(at * at)
    answer = f"y = {slope}x - {at * at}" if intercept < 0 else f"y = {slope}x + {intercept}"
    if at == 0:
        answer = "y = 0"
    return item(
        title,
        f"מה משוואת המשיק ל y = x^2 בנקודה שבה x = {at}?",
        answer,
        [f"y = {slope}x + {at * at}", f"y = {at}x", f"y = {slope}x"],
        "השיפוע הוא הנגזרת בנקודה, והישר עובר בנקודה שעל הגרף.",
        f"הנגזרת 2x שווה {slope} ב x = {at}. הנקודה היא ({at}, {at * at}). מתקבל {answer}.",
        "אפשר לכתוב משיק לפרבולה בנקודה.",
    )


def extras_for(key: str, level: int) -> list[dict]:
    bank = _PRACTICE.get((key, level))
    if bank is None:
        raise SystemExit(f"missing extras for {key} level {level}")
    rows = bank()
    if len(rows) < 6:
        raise SystemExit(f"short extras {key} {level}")
    return rows


def reviews_for(key: str) -> list[dict]:
    rows = _REVIEW[key]()
    if len(rows) < 6:
        raise SystemExit(f"short review {key}")
    return rows


def placement_bank() -> list[tuple[str, float, dict]]:
    return [
        ("algebra", -1.2, _lin(7, 1, 2, "מבדק, משוואה")),
        ("geometry", -0.8, _angles(35, 65, "מבדק, זווית")),
        ("trig", -0.2, _sin_ratio(5, 12, "מבדק, סינוס")),
        ("sequences", -0.6, _arith_n(4, 3, 5, "מבדק, סדרה")),
        ("probability", -1.0, _dice_sum(2, "מבדק, קוביות")),
        ("calculus", 0.4, _deriv_value("2x^2 + 3x", 1, "מבדק, נגזרת", "הנגזרת היא 4x + 3. ב x = 1 מתקבל 7.")),
        ("extrema", 0.9, _vertex(1, -8, 7, "מבדק, קודקוד")),
        ("integrals", 0.7, _definite(3, 2, 1, 2, "מבדק, אינטגרל")),
        ("analytic", 0.3, _distance(0, 0, 6, 8, "מבדק, מרחק")),
        ("vectors", 0.6, _dot(2, 3, 4, -1, "מבדק, סקלרית")),
        ("complex", 0.8, _cdot(1, 2, 1, -2, "מבדק, מרוכב")),
        ("growth", 0.5, _log2(6, "מבדק, לוג")),
    ]


def exam_pack() -> tuple[list[tuple[str, str, dict]], list[dict]]:
    paper = [
        ("ex_algebra", "אלגברה", _double_root(10, "בחינה, שורש כפול")),
        ("ex_geometry", "גיאומטריה", _similar_area(3, 1, 4, "בחינה, יחס שטחים")),
        ("ex_trig", "טריגונומטריה", _area_sas(12, 10, 1, 2, "בחינה, שטח")),
        ("ex_sequences", "סדרות", _geo_inf(12, 1, 3, "בחינה, סכום אינסופי")),
        ("ex_probability", "הסתברות", _coins(6, "בחינה, לפחות עץ")),
        ("ex_functions", "פונקציות", _tangent_square(3, "בחינה, משיק")),
        ("ex_extrema", "קיצון", _vertex(1, -10, 21, "בחינה, קודקוד")),
        ("ex_integrals", "אינטגרלים", _definite(6, 2, 1, 2, "בחינה, אינטגרל")),
        ("ex_analytic", "אנליטית", _distance(2, -1, 6, 2, "בחינה, מרחק")),
        ("ex_vectors", "וקטורים", _dot(3, -2, 4, 6, "בחינה, סקלרית")),
        ("ex_complex", "מרוכבים", _cdot(2, 1, 1, -1, "בחינה, כפל")),
        ("ex_growth", "גידול ודעיכה", _half(5, "בחינה, מחצית")),
    ]
    review = [
        _lin(9, -4, 3, "חזרת בחינה, משוואה"),
        _pythag(8, 15, "חזרת בחינה, פיתגורס"),
        _arith_sum(5, 2, 8, "חזרת בחינה, סכום"),
        _dice_sum(7, "חזרת בחינה, קוביות"),
    ]
    return paper, review


def _PRACTICE_ALGEBRA_1() -> list[dict]:
    rows = [(7, 2, 3), (9, -5, 2), (4, 3, 6), (5, -2, 4), (8, 1, 3), (6, 5, 2)]
    return [_lin(a, b, x, f"עוד משוואה {i}") for i, (a, b, x) in enumerate(rows, 1)]


def _PRACTICE_ALGEBRA_2() -> list[dict]:
    return [
        _quad(1, 6, "עוד ריבועית 1"),
        _quad(-3, 2, "עוד ריבועית 2"),
        _quad(4, 5, "עוד ריבועית 3"),
        _sum_diff(14, 4, "עוד מערכת 1"),
        _sum_diff(18, 6, "עוד מערכת 2"),
        _ineq(3, 2, 11, "עוד אי שוויון"),
    ]


def _PRACTICE_ALGEBRA_3() -> list[dict]:
    return [
        _rect(5, 34, "עוד מלבן 1"),
        _rect(6, 44, "עוד מלבן 2"),
        _double_root(6, "עוד שורש כפול"),
        _double_root(8, "שורש כפול נוסף"),
        item(
            "תחום של מנה",
            "עבור אילו ערכי x הביטוי 1 חלקי (x - 4) מוגדר?",
            "כל x פרט ל 4",
            ["רק x = 4", "כל x פרט ל 0", "רק x > 4"],
            "המכנה אסור שיהיה אפס.",
            "x - 4 = 0 כאשר x = 4. בכל ערך אחר המנה מוגדרת.",
            "אפשר למצוא נקודת אי הגדרה של מנה.",
        ),
        item(
            "פישוט אחר",
            "לכל x שונה מ 3, (x^2 - 9) חלקי (x - 3) שווה לביטוי הבא. איזה?",
            "x + 3",
            ["x - 3", "x^2 - 9", "3x"],
            "x^2 - 9 הוא (x - 3)(x + 3).",
            "מצמצמים את (x - 3) כל עוד x שונה מ 3. נשאר x + 3.",
            "אפשר לצמצם הפרש ריבועים מול גורם לינארי.",
        ),
    ]


def _PRACTICE_GEOMETRY_1() -> list[dict]:
    return [
        _angles(25, 80, "עוד זווית 1"),
        _angles(15, 50, "עוד זווית 2"),
        _pythag(5, 12, "עוד יתר 1"),
        _pythag(7, 24, "עוד יתר 2"),
        _tri_area(10, 6, "עוד שטח 1"),
        _tri_area(12, 5, "עוד שטח 2"),
    ]


def _PRACTICE_GEOMETRY_2() -> list[dict]:
    return [
        _inscribed(80, "עוד היקפית 1"),
        _inscribed(140, "עוד היקפית 2"),
        _similar_area(2, 1, 9, "עוד דמיון 1"),
        _similar_area(3, 1, 2, "עוד דמיון 2"),
        _pythag(9, 12, "עוד אלכסון"),
        _tri_area(16, 9, "שטח משולש נוסף"),
    ]


def _PRACTICE_GEOMETRY_3() -> list[dict]:
    return [
        item(
            "היקף מול שטח",
            "למעגל שרדיוסו 3, מה ההיקף?",
            "6π",
            ["9π", "3π", "6"],
            "ההיקף הוא 2πr. השטח הוא πr בריבוע.",
            "2 כפול π כפול 3 הוא 6π. 9π היה השטח.",
            "אפשר להבדיל בין היקף מעגל לשטח עיגול.",
        ),
        item(
            "שטח עיגול",
            "מה שטח עיגול שרדיוסו 4?",
            "16π",
            ["8π", "4π", "16"],
            "שטח עיגול הוא π כפול ריבוע הרדיוס.",
            "4 בריבוע הוא 16, לכן השטח 16π.",
            "אפשר לחשב שטח עיגול מרדיוס.",
        ),
        item(
            "תיכון ליתר",
            "במשולש ישר זווית היתר הוא 18. מה אורך התיכון ליתר?",
            "9",
            ["18", "6", "12"],
            "התיכון ליתר במשולש ישר זווית הוא מחצית היתר.",
            "מחצית של 18 היא 9. היתר הוא קוטר של המעגל החוסם.",
            "אפשר לחשב את התיכון ליתר.",
        ),
        item(
            "זווית חיצונית",
            "במשולש שתי זוויות פנימיות שאינן צמודות לזווית החיצונית הן 40 ו 65. מה הזווית החיצונית?",
            "105",
            ["75", "40", "180"],
            "זווית חיצונית שווה לסכום שתי הפנימיות שאינן צמודות לה.",
            "40 ועוד 65 הם 105.",
            "אפשר לחשב זווית חיצונית.",
        ),
        _inscribed(100, "היקפית בבחינת משפט"),
        _similar_area(4, 2, 7, "שטחים ביחס מצומצם"),
    ]


def _PRACTICE_TRIG_1() -> list[dict]:
    return [
        _sin_ratio(3, 4, "עוד סינוס 1"),
        _sin_ratio(8, 15, "עוד סינוס 2"),
        _sin_ratio(7, 24, "עוד סינוס 3"),
        item(
            "ערך של טנגנס",
            "מה tan של 45 מעלות?",
            "1",
            ["0", "√2/2", "√3"],
            "בזווית 45 הניצב שמול שווה לניצב שליד.",
            "tan 45 = 1.",
            "אפשר לזהות טנגנס של 45 מעלות.",
        ),
        item(
            "ערך של קוסינוס",
            "מה cos של 60 מעלות?",
            "1/2",
            ["√3/2", "1", "0"],
            "cos 60 שווה ל sin 30.",
            "cos 60 = 1/2.",
            "אפשר לזהות קוסינוס של 60 מעלות.",
        ),
        item(
            "ערך של סינוס",
            "מה sin של 90 מעלות?",
            "1",
            ["0", "1/2", "√2/2"],
            "ב 90 מעלות הסינוס בשיא שלו.",
            "sin 90 = 1, ו cos 90 = 0.",
            "אפשר לזהות סינוס של 90 מעלות.",
        ),
    ]


def _PRACTICE_TRIG_2() -> list[dict]:
    return [
        _area_sas(6, 8, 1, 2, "עוד שטח סינוס 1"),
        _area_sas(10, 4, 1, 1, "עוד שטח סינוס 2"),
        _area_sas(5, 12, 1, 2, "עוד שטח סינוס 3"),
        item(
            "משפט הסינוסים",
            "צלע באורך 8 מול זווית שסינוסה 1/2. צלע אחרת מול זווית שסינוסה 1. מה אורך הצלע האחרת?",
            "16",
            ["8", "4", "12"],
            "צלע חלקי סינוס הזווית שמולה שווה בשתי הצלעות.",
            "8 חלקי 1/2 הוא 16. הצלע שמול סינוס 1 שווה 16.",
            "אפשר להשתמש במשפט הסינוסים כשיש זוג של צלע וסינוס.",
        ),
        item(
            "משפט הקוסינוסים בזווית ישרה",
            "שתי צלעות 6 ו 8, והזווית ביניהן 90 מעלות. מה הצלע השלישית?",
            "10",
            ["14", "2", "48"],
            "cos 90 הוא 0, אז נשאר משפט פיתגורס.",
            "6 בריבוע ועוד 8 בריבוע הם 100. השורש הוא 10.",
            "אפשר לראות שמשפט הקוסינוסים בזווית ישרה הוא פיתגורס.",
        ),
        item(
            "קוסינוס מסינוס",
            "זווית חדה עם sin = 3/5. מה cos שלה?",
            "4/5",
            ["3/4", "2/5", "5/3"],
            "sin בריבוע ועוד cos בריבוע שווה 1, והקוסינוס של זווית חדה חיובי.",
            "1 פחות 9/25 הוא 16/25. השורש החיובי הוא 4/5.",
            "אפשר למצוא קוסינוס חיובי מתוך סינוס של זווית חדה.",
        ),
    ]


def _PRACTICE_TRIG_3() -> list[dict]:
    return [
        item(
            "שני פתרונות לסינוס",
            "בתחום 0 עד 180 מעלות, אילו זוויות מקיימות sin x = 1/2?",
            "30 וגם 150",
            ["30 וגם 60", "150 בלבד", "45 וגם 135"],
            "הסינוס חיובי גם בזווית החדה וגם במשלימה שלה ל 180.",
            "sin 30 = 1/2 וגם sin 150 = 1/2.",
            "אפשר למצוא את שני הפתרונות של משוואת סינוס עד 180.",
        ),
        item(
            "סימן הקוסינוס",
            "מה הסימן של cos 120 מעלות?",
            "שלילי",
            ["חיובי", "אפס", "לא מוגדר"],
            "בין 90 ל 180 הקוסינוס שלילי.",
            "120 גדולה מ 90 וקטנה מ 180, לכן הקוסינוס שלילי. הערך הוא -1/2.",
            "אפשר לקבוע את סימן הקוסינוס ברביע.",
        ),
        _area_sas(9, 8, 1, 2, "שטח בשליטה"),
        item(
            "זהות בסיסית",
            "אם sin x = 0, מה cos בריבוע של x?",
            "1",
            ["0", "-1", "1/2"],
            "sin בריבוע ועוד cos בריבוע שווה 1.",
            "0 ועוד cos בריבוע שווה 1, לכן cos בריבוע הוא 1.",
            "אפשר להשתמש בזהות הפיתגורס הטריגונומטרית.",
        ),
        item(
            "טנגנס כמנה",
            "אם sin x = 1/2 ו cos x = √3/2, מה tan x?",
            "1/√3",
            ["√3", "1", "√3/2"],
            "טנגנס הוא סינוס חלקי קוסינוס.",
            "(1/2) חלקי (√3/2) שווה 1/√3.",
            "אפשר לחשב טנגנס מסינוס ומקוסינוס.",
        ),
        item(
            "זווית קהה בקוסינוסים",
            "במשולש הזווית בין הצלעות 5 ו 5 היא 120 מעלות. cos 120 = -1/2. מה ריבוע הצלע השלישית?",
            "75",
            ["25", "50", "0"],
            "c בריבוע = a בריבוע + b בריבוע - 2ab cos C. קוסינוס שלילי הופך את החיסור לחיבור.",
            "25 + 25 - 2·5·5·(-1/2) = 50 + 25 = 75.",
            "אפשר להציב קוסינוס שלילי במשפט הקוסינוסים.",
        ),
    ]


def _PRACTICE_SEQ_1() -> list[dict]:
    return [
        _arith_n(7, 4, 6, "עוד איבר חשבוני 1"),
        _arith_n(10, -2, 5, "עוד איבר חשבוני 2"),
        _arith_sum(2, 5, 6, "עוד סכום 1"),
        _arith_sum(1, 1, 20, "עוד סכום 2"),
        _arith_n(3, 7, 4, "עוד איבר חשבוני 3"),
        _arith_sum(8, 3, 4, "עוד סכום 3"),
    ]


def _PRACTICE_SEQ_2() -> list[dict]:
    return [
        _geo_n(3, 2, 5, "עוד איבר הנדסי 1"),
        _geo_n(5, 3, 3, "עוד איבר הנדסי 2"),
        _geo_inf(6, 1, 2, "עוד סכום אינסופי 1"),
        _geo_inf(9, 2, 3, "עוד סכום אינסופי 2"),
        _geo_n(2, 4, 4, "עוד איבר הנדסי 3"),
        item(
            "מתי אין סכום אינסופי",
            "לסדרה הנדסית שהמנה שלה היא 3, האם יש סכום אינסופי?",
            "לא",
            ["כן, והוא 0", "כן, והוא 3", "רק אם האיבר הראשון 1"],
            "הסכום האינסופי קיים רק כשערך המנה קטן מ 1.",
            "3 גדול מ 1, לכן האיברים לא שואפים לאפס והסכום לא קיים.",
            "אפשר להחליט מתי סכום אינסופי לא קיים.",
        ),
    ]


def _PRACTICE_SEQ_3() -> list[dict]:
    return [
        item(
            "נוסחת הסכום",
            "מה סכום המספרים השלמים מ 1 עד 40?",
            "820",
            ["800", "780", "40"],
            "הנוסחה היא n(n+1)/2.",
            "40 כפול 41 חלקי 2 שווה 820.",
            "אפשר להציב בנוסחת סכום המספרים הראשונים.",
        ),
        item(
            "צעד האינדוקציה",
            "מניחים שסכום 1 עד k הוא k(k+1)/2. אחרי הוספת k+1, לאיזה ביטוי צריך להגיע?",
            "(k+1)(k+2)/2",
            ["(k+1)(k+1)/2", "k(k+2)/2", "(k+2)(k+3)/2"],
            "הטענה ל k+1 היא אותה נוסחה עם k+1 במקום k.",
            "k(k+1)/2 + (k+1) = (k+1)(k/2 + 1) = (k+1)(k+2)/2.",
            "אפשר לזהות את יעד הצעד באינדוקציה.",
        ),
        _arith_sum(6, 4, 5, "סכום בשליטה"),
        _geo_n(4, 2, 6, "איבר הנדסי בשליטה"),
        _geo_inf(3, 1, 4, "סכום אינסופי בשליטה"),
        item(
            "בסיס חסר",
            "מה חסר בהוכחה שיש בה רק צעד אינדוקציה, בלי בדיקה של n = 1?",
            "הבסיס",
            ["הצעד", "ההנחה", "הנוסחה הסגורה"],
            "בלי מקרה ראשון שנבדק, השרשרת לא מתחילה.",
            "אינדוקציה צריכה בסיס וגם צעד. כאן חסר הבסיס.",
            "אפשר לזהות שהוכחה בלי בסיס אינה שלמה.",
        ),
    ]


def _PRACTICE_PROB_1() -> list[dict]:
    return [
        _dice_sum(8, "עוד סכום קוביות 1"),
        _dice_sum(9, "עוד סכום קוביות 2"),
        _dice_sum(12, "עוד סכום קוביות 3"),
        _coins(2, "עוד מטבעות"),
        item(
            "משלים",
            "ההסתברות של מאורע היא 2/7. מה ההסתברות של המשלים שלו?",
            "5/7",
            ["2/7", "7/2", "1/7"],
            "המשלים הוא 1 פחות ההסתברות.",
            "1 פחות 2/7 הוא 5/7.",
            "אפשר לחשב הסתברות של משלים.",
        ),
        item(
            "קובייה אחת",
            "מה ההסתברות לקבל מספר זוגי בקובייה הוגנת?",
            "1/2",
            ["1/6", "1/3", "2/3"],
            "התוצאות הזוגיות הן 2, 4 ו 6.",
            "3 תוצאות מתוך 6, כלומר 1/2.",
            "אפשר לחשב הסתברות בקובייה אחת.",
        ),
    ]


def _PRACTICE_PROB_2() -> list[dict]:
    return [
        item(
            "כפל של בלתי תלויים",
            "שני מאורעות בלתי תלויים, לכל אחד הסתברות 1/3. מה הסתברות החיתוך?",
            "1/9",
            ["2/3", "1/6", "2/9"],
            "לבלתי תלויים כופלים.",
            "1/3 כפול 1/3 הוא 1/9.",
            "אפשר לכפול הסתברויות של מאורעות בלתי תלויים.",
        ),
        item(
            "בלי החזרה",
            "בשק 4 כדורים אדומים ו 6 לבנים. שולפים שניים בלי החזרה. מה ההסתברות ששני הראשונים אדומים, בסדר הזה?",
            "12/90",
            ["16/100", "4/10", "8/90"],
            "השליפה השנייה רואה 9 כדורים, ומהם 3 אדומים.",
            "4/10 כפול 3/9 הוא 12/90. אפשר לצמצם ל 2/15, ושתי הצורות נכונות. כאן בוחרים את הצורה הלא מצומצמת שבין האפשרויות.",
            "אפשר לחשב שליפה בלי החזרה.",
        ),
        item(
            "תוחלת של פרס",
            "פרס של 12 בשקל בהסתברות 1/4, ואחרת 0. מה התוחלת?",
            "3",
            ["12", "4", "6"],
            "תוחלת היא ערך כפול הסתברות, ועוד הערך השני כפול ההסתברות שלו.",
            "12 כפול 1/4 ועוד 0 כפול 3/4 שווה 3.",
            "אפשר לחשב תוחלת של משתנה עם שני ערכים.",
        ),
        item(
            "תוחלת של סכום",
            "תוחלת של X היא 2 ותוחלת של Y היא 5. מה תוחלת של X + Y?",
            "7",
            ["10", "3", "2"],
            "תוחלת של סכום היא סכום התוחלות, גם אם המשתנים תלויים.",
            "2 ועוד 5 הם 7.",
            "אפשר לחבר תוחלות.",
        ),
        _coins(4, "ארבעה מטבעות"),
        _dice_sum(4, "סכום 4"),
    ]


def _PRACTICE_PROB_3() -> list[dict]:
    return [
        item(
            "בינומי קצר",
            "בשלושה ניסויים בלתי תלויים, הסתברות הצלחה 1/2 בכל אחד. מה ההסתברות לשתי הצלחות בדיוק?",
            "3/8",
            ["1/8", "1/2", "3/4"],
            "C(3,2) כפול (1/2) בחזקת 3.",
            "יש 3 סדרים, וכל סדר בהסתברות 1/8. ביחד 3/8.",
            "אפשר לחשב הסתברות בינומית קצרה.",
        ),
        item(
            "תוחלת בינומית",
            "עשרה ניסויים, הסתברות הצלחה 0.3 בכל אחד. מה תוחלת מספר ההצלחות?",
            "3",
            ["0.3", "10", "7"],
            "התוחלת הבינומית היא n כפול p.",
            "10 כפול 0.3 הוא 3.",
            "אפשר לחשב תוחלת בינומית בלי טבלה.",
        ),
        item(
            "בחירה",
            "כמה דרכים יש לבחור 2 פריטים מתוך 6, בלי חשיבות לסדר?",
            "15",
            ["30", "12", "36"],
            "C(6,2) = 6·5 / 2.",
            "30 חלקי 2 הוא 15.",
            "אפשר לחשב צירוף קטן.",
        ),
        _coins(3, "שלושה מטבעות"),
        item(
            "איחוד זר",
            "שני מאורעות זרים, הסתברויות 1/5 ו 2/5. מה הסתברות האיחוד?",
            "3/5",
            ["2/25", "2/5", "4/5"],
            "למאורעות זרים מחברים, לא כופלים.",
            "1/5 ועוד 2/5 הם 3/5.",
            "אפשר לחבר הסתברויות של מאורעות זרים.",
        ),
        item(
            "עץ",
            "בשלב ראשון הסתברות 1/2, ובשלב שני לאורך אותו מסלול שוב 1/2. מה הסתברות המסלול?",
            "1/4",
            ["1", "1/2", "3/4"],
            "לאורך מסלול כופלים.",
            "1/2 כפול 1/2 הוא 1/4.",
            "אפשר לכפול לאורך מסלול בעץ הסתברות.",
        ),
    ]


def _PRACTICE_FUN_1() -> list[dict]:
    return [
        _slope(0, 1, 3, 7, "עוד שיפוע 1"),
        _slope(2, 5, 6, -3, "עוד שיפוע 2"),
        _domain(5, "עוד תחום"),
        item(
            "הצבה בריבוע",
            "f(x) = x^2 - 2x. מה f(4)?",
            "8",
            ["16", "6", "12"],
            "מציבים, מעלים בריבוע, ואז מחסרים.",
            "16 פחות 8 הוא 8.",
            "אפשר להציב בפונקציה ריבועית.",
        ),
        item(
            "חיתוך עם הציר",
            "לישר y = -2x + 6, מה נקודת החיתוך עם ציר y?",
            "(0, 6)",
            ["(6, 0)", "(0, -2)", "(3, 0)"],
            "בחיתוך עם ציר y, x הוא 0.",
            "כש x = 0, y = 6. הנקודה היא (0, 6).",
            "אפשר לקרוא חיתוך עם ציר y מישר.",
        ),
        _domain(1, "תחום של שורש"),
    ]


def _PRACTICE_FUN_2() -> list[dict]:
    return [
        _deriv_value("x^3 - 6x", 2, "עוד נגזרת 1", "הנגזרת היא 3x^2 - 6. ב x = 2: 12 - 6 = 6."),
        _deriv_value("x^3 - 6x", 0, "עוד נגזרת 2", "3·0 - 6 = -6."),
        _deriv_value("x^2 + 5", 4, "עוד נגזרת 3", "הנגזרת היא 2x. ב x = 4 היא 8. הקבוע נעלם."),
        item(
            "עלייה",
            "ל f(x) = x^3 - 6x הנגזרת ב x = 2 חיובית. מה זה אומר על הפונקציה שם?",
            "היא עולה",
            ["היא יורדת", "יש שם חור", "היא לא מוגדרת"],
            "נגזרת חיובית אומרת שהפונקציה עולה באותה נקודה.",
            "3·4 - 6 = 6 > 0, לכן הפונקציה עולה ב x = 2.",
            "אפשר לקרוא עלייה מסימן הנגזרת.",
        ),
        item(
            "חור",
            "המנה (x^2 - 4) חלקי (x - 2) אינה מוגדרת בנקודה אחת. באיזו?",
            "x = 2",
            ["x = -2", "x = 4", "x = 0"],
            "המכנה מתאפס ב x = 2. מחוץ לנקודה אפשר לצמצם ל x + 2.",
            "ב x = 2 יש חור. הפישוט x + 2 נותן שם 4, אבל המנה המקורית לא מקבלת את הערך.",
            "אפשר לזהות חור במנה.",
        ),
        _slope(1, 1, 4, 10, "שיפוע מתוך גרף נקודות"),
    ]


def _PRACTICE_FUN_3() -> list[dict]:
    return [
        _tangent_square(2, "עוד משיק"),
        _tangent_square(4, "משיק נוסף"),
        item(
            "אסימפטוטה",
            "למנה (3x + 1) חלקי (x - 2), מה משוואת האסימפטוטה האופקית?",
            "y = 3",
            ["y = 2", "y = 1", "y = 0"],
            "כשחזקות המונה והמכנה שוות, y שווה ליחס המקדמים המובילים.",
            "3 חלקי 1 הוא 3. האסימפטוטה היא y = 3.",
            "אפשר לקרוא אסימפטוטה אופקית של מנה לינארית.",
        ),
        item(
            "נגזרת של 1/x",
            "מה הנגזרת של 1/x?",
            "-1/x^2",
            ["1/x^2", "ln x", "-1/x"],
            "1/x הוא x בחזקת 1-. מורידים את החזקה ומקטינים אותה ב 1.",
            "הנגזרת היא -1 כפול x בחזקת 2-, כלומר -1/x^2.",
            "אפשר לגזור 1/x.",
        ),
        item(
            "שפיץ",
            "האם |x| גזירה ב x = 0?",
            "לא",
            ["כן, והנגזרת 0", "כן, והנגזרת 1", "היא לא רציפה שם"],
            "הפונקציה רציפה ב 0, אבל השיפוע משמאל הוא 1- ומימין 1.",
            "השיפועים לא מסכימים, לכן אין נגזרת ב 0. הרציפות כן מתקיימת.",
            "אפשר להבחין בין רציפות לגזירות בערך מוחלט.",
        ),
        _deriv_value("4x^3", 1, "נגזרת של חזקה", "הנגזרת של 4x^3 היא 12x^2. ב x = 1 היא 12."),
    ]


def _PRACTICE_EXT_1() -> list[dict]:
    return [
        _vertex(1, -6, 1, "עוד קודקוד 1"),
        _vertex(1, -2, 5, "עוד קודקוד 2"),
        _vertex(2, -8, 3, "עוד קודקוד 3"),
        item(
            "מינימום או מקסימום",
            "ל y = 2x^2 - 8x + 3, איזה סוג קיצון יש בקודקוד?",
            "מינימום",
            ["מקסימום", "פיתול", "אין קיצון"],
            "מקדם חיובי של x^2 פותח את הפרבולה כלפי מעלה.",
            "המקדם של x^2 הוא 2, חיובי, לכן הקודקוד הוא מינימום.",
            "אפשר לסווג קודקוד של פרבולה לפי מקדם הריבוע.",
        ),
        item(
            "פיתול ולא קיצון",
            "ל y = x^3, הנגזרת מתאפסת ב x = 0. מה נכון?",
            "אין שם קיצון מקומי",
            ["יש מינימום", "יש מקסימום", "הפונקציה לא גזירה"],
            "הנגזרת 3x^2 אינה מחליפה סימן. היא נוגעת באפס ונשארת אי שלילית.",
            "הפונקציה ממשיכה לעלות, לכן x = 0 היא נקודת פיתול ולא קיצון.",
            "אפשר לא לקרוא לכל איפוס של נגזרת בשם קיצון.",
        ),
        _vertex(1, 4, 1, "קודקוד משמאל"),
    ]


def _PRACTICE_EXT_2() -> list[dict]:
    return [
        item(
            "מבחן נגזרת ראשונה",
            "הנגזרת שלילית משמאל לנקודה וחיובית מימין לה. מה יש בנקודה?",
            "מינימום",
            ["מקסימום", "פיתול בלי קיצון", "חור"],
            "מעבר משלילי לחיובי הוא מינימום.",
            "הפונקציה יורדת ואז עולה, לכן זה מינימום.",
            "אפשר לסווג קיצון לפי החלפת סימן.",
        ),
        item(
            "נגזרת שנייה",
            "בנקודה שבה הנגזרת הראשונה אפס, הנגזרת השנייה היא 4-. מה יש שם?",
            "מקסימום",
            ["מינימום", "פיתול", "אין החלטה"],
            "נגזרת שנייה שלילית בנקודה קריטית נותנת מקסימום.",
            "הנגזרת השנייה שלילית, לכן הקעירות כלפי מטה וזה מקסימום.",
            "אפשר לסווג לפי הנגזרת השנייה.",
        ),
        _vertex(-1, 6, 1, "פרבולה הפוכה"),
        item(
            "קצה קטע",
            "בקטע הסגור מ 0 עד 3, ל f(x) = x, איפה המקסימום?",
            "ב x = 3",
            ["ב x = 0", "ב x = 1.5", "אין מקסימום"],
            "הנגזרת 1 לא מתאפסת. בקטע סגור בודקים את הקצוות.",
            "f עולה, לכן הערך הגדול הוא בקצה הימני, x = 3.",
            "אפשר לבדוק קצוות של קטע סגור.",
        ),
        item(
            "איפוס של מינוס סינוס",
            "הנגזרת של cos x היא -sin x. היא מתאפסת כאשר",
            "sin x = 0",
            ["cos x = 0", "sin x = 1", "x = 1"],
            "מינוס סינוס אפס בדיוק כשהסינוס אפס.",
            "-sin x = 0 גורר sin x = 0.",
            "אפשר למצוא נקודה קריטית של קוסינוס.",
        ),
        _vertex(1, -12, 4, "קודקוד רחוק"),
    ]


def _PRACTICE_EXT_3() -> list[dict]:
    return [
        item(
            "מלבן בהיקף נתון",
            "מלבן שהיקפו 28. איזה אורך צלע נותן שטח מקסימלי, אם זו הצלע האחת מבין שתיים שוות?",
            "7",
            ["14", "4", "10"],
            "היקף 28 אומר שסכום שתי צלעות סמוכות הוא 14. שטח x(14-x).",
            "הנגזרת 14 - 2x מתאפסת ב x = 7. זה ריבוע, והשטח 49.",
            "אפשר למצוא מלבן מקסימלי בהיקף נתון.",
        ),
        item(
            "גדר מול קיר",
            "גדר באורך 24 מול קיר, עם שתי צלעות ניצבות שוות באורך x והחזית 24 - 2x. באיזה x השטח מקסימלי?",
            "6",
            ["12", "8", "4"],
            "השטח הוא x(24 - 2x). גוזרים.",
            "24x - 2x^2. הנגזרת 24 - 4x אפס כאשר x = 6. השטח 72.",
            "אפשר לפתור בעיית גדר מול קיר.",
        ),
        item(
            "ריבוע מרחק",
            "למה מותר למזער את ריבוע המרחק במקום את המרחק עצמו?",
            "השורש עולה, אז המינימום באותו מקום",
            ["כי ריבוע המרחק תמיד 1", "כי המרחק שלילי", "אסור, זה משנה את המקום"],
            "פונקציה עולה שומרת על מקום המינימום.",
            "השורש הריבועי עולה עבור מספרים אי שליליים, לכן הנקודה שבה הריבוע מינימלי היא גם הנקודה שבה המרחק מינימלי.",
            "אפשר להחליף מרחק בריבוע המרחק בבעיית מינימום.",
        ),
        _vertex(1, -14, 3, "קודקוד בבעיה"),
        item(
            "תחום של סיפור",
            "בגדר באורך 24 מול קיר, עם x אורך הצלע הניצבת, איזה תחום הגיוני ל x?",
            "בין 0 ל 12",
            ["כל x", "רק x = 6", "x גדול מ 24"],
            "שתי הצלעות הניצבות ביחד לא יכולות לעבור את אורך הגדר, וכל צלע חיובית.",
            "x גדול מ 0, ו 24 - 2x גדול מ 0, לכן x קטן מ 12.",
            "אפשר לכתוב תחום שבו סיפור הקיצון הגיוני.",
        ),
        item(
            "ערך הקודקוד",
            "ל y = x^2 - 6x + 1 הקודקוד ב x = 3. מה ערך הפונקציה שם?",
            "-8",
            ["1", "3", "-6"],
            "מציבים את x של הקודקוד בפונקציה עצמה, לא בנגזרת.",
            "9 - 18 + 1 = -8.",
            "אפשר לחשב את גובה נקודת הקיצון.",
        ),
    ]


def _PRACTICE_INT_1() -> list[dict]:
    return [
        _definite(2, 1, 0, 3, "עוד מסוים 1"),
        _definite(3, 2, 0, 1, "עוד מסוים 2"),
        _definite(4, 1, 1, 3, "עוד מסוים 3"),
        item(
            "הקבוע נעלם",
            "למה הקבוע C לא מופיע בערך של אינטגרל מסוים?",
            "הוא מופיע בגבול העליון וגם בתחתון, ומתבטל",
            ["כי אסור להוסיף קבוע", "כי C תמיד 0", "כי האינטגרל הוא שטח בלי מספר"],
            "F(b) + C פחות (F(a) + C) משאיר את F(b) - F(a).",
            "הקבוע מתווסף ומוחסר, לכן הוא מתבטל.",
            "אפשר להסביר למה C נעלם באינטגרל מסוים.",
        ),
        item(
            "גבולות שווים",
            "מה האינטגרל של x^2 מ 4 עד 4?",
            "0",
            ["4", "16", "1"],
            "מגבול עד אותו גבול אין רוחב.",
            "F(4) - F(4) = 0, לכל פונקציה קדומה.",
            "אפשר לדעת שאינטגרל מנקודה עד עצמה הוא אפס.",
        ),
        item(
            "קדומה של סינוס",
            "איזו פונקציה היא קדומה של sin x?",
            "-cos x",
            ["cos x", "-sin x", "sin x"],
            "גוזרים ובודקים. נגזרת של cos היא מינוס סינוס, אז נגזרת של מינוס קוסינוס היא סינוס.",
            "(-cos x)' = sin x. לכן קדומה של sin x היא -cos x, עד כדי קבוע.",
            "אפשר לזהות קדומה של סינוס.",
        ),
    ]


def _PRACTICE_INT_2() -> list[dict]:
    return [
        item(
            "אינטגרל מול שטח",
            "האינטגרל של x מ 1- עד 1 הוא 0. מה השטח הגיאומטרי בין הגרף לציר בקטע הזה?",
            "1",
            ["0", "2", "1/2"],
            "מתחת לציר האינטגרל שלילי. השטח הוא הערך המוחלט, ולכן מפצלים.",
            "מ 1- עד 0 השטח 1/2, ומ 0 עד 1 עוד 1/2. ביחד 1. האינטגרל מבטל את שני החצאים.",
            "אפשר להבדיל בין אינטגרל מסוים לשטח.",
        ),
        item(
            "קדומה של 1/x",
            "מה קדומה של 1/x, עבור x חיובי?",
            "ln x",
            ["1/x^2", "-1/x", "x"],
            "הנגזרת של ln x היא 1/x.",
            "ל x חיובי, (ln x)' = 1/x. באופן כללי כותבים ln|x|.",
            "אפשר לזהות את הקדומה של 1/x.",
        ),
        _definite(1, 2, 0, 3, "אינטגרל של x בריבוע"),
        item(
            "החלפת גבולות",
            "אם האינטגרל מ 0 עד 2 הוא 5, מה האינטגרל מ 2 עד 0?",
            "-5",
            ["5", "0", "1/5"],
            "החלפת גבולות מחליפה את הסימן.",
            "F(0) - F(2) = -(F(2) - F(0)) = -5.",
            "אפשר להחליף כיוון של אינטגרל.",
        ),
        item(
            "מהירות ודרך",
            "גוף נע במהירות חיובית של 4 יחידות זמן, במשך 3 יחידות זמן. איזה גודל נותן האינטגרל של המהירות?",
            "12",
            ["4", "3", "7"],
            "אינטגרל של מהירות חיובית לפי הזמן הוא הדרך.",
            "4 כפול 3 הוא 12.",
            "אפשר לקרוא דרך מתוך אינטגרל של מהירות חיובית.",
        ),
        _definite(5, 1, 0, 2, "אינטגרל של ישר"),
    ]


def _PRACTICE_INT_3() -> list[dict]:
    return [
        item(
            "בין ישר לפרבולה",
            "בין y = x ל y = x^2, מ 0 עד 1, הישר למעלה. מה השטח?",
            "1/6",
            ["1/2", "1/3", "1"],
            "משלבים את העליון פחות התחתון.",
            "האינטגרל של x הוא 1/2, של x^2 הוא 1/3. ההפרש מ 0 עד 1 הוא 1/6.",
            "אפשר לחשב שטח בין y = x ל y = x^2.",
        ),
        item(
            "מי למעלה",
            "אם חיסרנו את הגרף העליון מהתחתון וקיבלנו 4-, מה השטח בין הגרפים?",
            "4",
            ["-4", "0", "16"],
            "שטח הוא אי שלילי. סימן מינוס אומר שהסדר התהפך.",
            "הערך המוחלט של 4- הוא 4.",
            "אפשר להפוך אינטגרל שלילי בין עקומות לשטח.",
        ),
        _definite(2, 3, 0, 2, "אינטגרל בשליטה"),
        item(
            "שני ישרים",
            "בין y = 4 ל y = x, מ 0 עד 2, הישר האופקי למעלה. מה השטח?",
            "6",
            ["8", "4", "2"],
            "ההפרש הוא 4 - x. אפשר גם לראות טרפז.",
            "הקדומה 4x - x^2/2 מ 0 עד 2 היא 8 - 2 = 6.",
            "אפשר לחשב שטח בין שני ישרים.",
        ),
        item(
            "חיתוך כגבול",
            "y = x ו y = 2 חוצים זה את זה ב x = 2. למה זה חשוב לפני חישוב שטח?",
            "זה קובע את גבול הקטע ומי למעלה",
            ["זה אומר שהשטח אפס", "זה אומר שאין קדומה", "זה לא חשוב"],
            "בלי נקודות החיתוך לא יודעים מאיפה עד איפה, ומי העליון.",
            "נקודת החיתוך נותנת גבול. אחר כך בודקים בקטע מי הגרף הגבוה יותר.",
            "אפשר להשתמש בחיתוך כגבול של שטח בין גרפים.",
        ),
        _definite(2, 1, 2, 6, "עוד קטע"),
    ]


def _PRACTICE_AN_1() -> list[dict]:
    return [
        _distance(2, 1, 6, 4, "עוד מרחק 1"),
        _distance(0, 0, 9, 12, "עוד מרחק 2"),
        _slope(1, 4, 3, 10, "שיפוע אנליטי"),
        item(
            "אמצע",
            "מה אמצע הקטע בין (1, 5) ל (7, 9)?",
            "(4, 7)",
            ["(6, 4)", "(8, 14)", "(3, 2)"],
            "האמצע הוא ממוצע השיעורים.",
            "ממוצע ה x הוא 4. ממוצע ה y הוא 7.",
            "אפשר למצוא נקודת אמצע.",
        ),
        item(
            "מאונכים",
            "ישר ששיפועו 2. מה שיפוע ישר מאונך לו, אם שניהם לא אנכיים?",
            "-1/2",
            ["2", "1/2", "-2"],
            "מכפלת שיפועי ישרים מאונכים היא 1-.",
            "2 כפול m = -1, לכן m = -1/2.",
            "אפשר למצוא שיפוע מאונך.",
        ),
        item(
            "נקודה על ישר",
            "האם הנקודה (1, 5) נמצאת על הישר y = 3x + 2?",
            "כן",
            ["לא", "רק אם x = 0", "אי אפשר לדעת"],
            "מציבים את x ובודקים אם יוצא ה y.",
            "3 כפול 1 ועוד 2 הוא 5. הנקודה על הישר.",
            "אפשר לבדוק אם נקודה על ישר.",
        ),
    ]


def _PRACTICE_AN_2() -> list[dict]:
    return [
        item(
            "נקודה על מעגל",
            "האם (3, 4) על המעגל x^2 + y^2 = 25?",
            "כן",
            ["לא, היא מחוץ למעגל", "לא, היא בתוך המעגל", "המעגל לא מוגדר"],
            "מציבים. שוויון אומר על המעגל.",
            "9 + 16 = 25. הנקודה על המעגל.",
            "אפשר לבדוק נקודה מול מעגל שמרכזו בראשית.",
        ),
        item(
            "בתוך המעגל",
            "איפה הנקודה (1, 1) ביחס למעגל x^2 + y^2 = 25?",
            "בתוך המעגל",
            ["על המעגל", "מחוץ למעגל", "במרכז בלבד"],
            "אם אגף שמאל קטן מריבוע הרדיוס, הנקודה בפנים.",
            "1 + 1 = 2, ו 2 קטן מ 25. הנקודה בפנים.",
            "אפשר להבחין בין פנים, שפה וחוץ של מעגל.",
        ),
        item(
            "מעגל מקוטר",
            "הקוטר מחבר את (0, 0) ו (6, 0). מה מרכז המעגל?",
            "(3, 0)",
            ["(6, 0)", "(0, 0)", "(3, 3)"],
            "מרכז המעגל הוא אמצע הקוטר.",
            "ממוצע ה x הוא 3, וממוצע ה y הוא 0.",
            "אפשר למצוא מרכז מעגל מאמצע קוטר.",
        ),
        _distance(2, 2, 5, 6, "מרחק נוסף"),
        item(
            "ישר אנכי",
            "מה נכון על הישר x = 4?",
            "הוא אנכי ואין לו שיפוע סופי",
            ["השיפוע שלו 4", "הוא אופקי", "הוא y = 4"],
            "כל הנקודות על הישר בעלות אותו x. אי אפשר לחלק בהפרש x, כי הוא אפס.",
            "x = 4 הוא ישר אנכי. אין לו שיפוע סופי.",
            "אפשר לזהות ישר אנכי.",
        ),
        item(
            "רדיוס בריבוע",
            "מעגל שמרכזו (1, 2) ורדיוסו 3. מה באגף ימין של המשוואה?",
            "9",
            ["3", "6", "1"],
            "במשוואת המעגל יושב ריבוע הרדיוס, לא הרדיוס.",
            "(x-1)^2 + (y-2)^2 = 9.",
            "אפשר לכתוב את אגף ימין של משוואת מעגל.",
        ),
    ]


def _PRACTICE_AN_3() -> list[dict]:
    return [
        item(
            "מרחק מנקודה לישר",
            "מה המרחק מהנקודה (0, 0) לישר 3x + 4y - 10 = 0?",
            "2",
            ["10", "5", "0"],
            "המרחק הוא הערך המוחלט של ההצבה, חלקי שורש של a בריבוע ועוד b בריבוע.",
            "|-10| חלקי שורש של 9+16 שווה 10/5 = 2.",
            "אפשר לחשב מרחק מנקודה לישר.",
        ),
        item(
            "משיק או חותך",
            "מרחק ממרכז מעגל לישר שווה לרדיוס. מה היחס בין הישר למעגל?",
            "משיק",
            ["אין חיתוך", "שתי נקודות חיתוך", "הישר הוא קוטר"],
            "מרחק גדול מהרדיוס: אין חיתוך. שווה: משיק. קטן: שתי נקודות.",
            "שוויון בין המרחק לרדיוס אומר נקודת השקה אחת.",
            "אפשר לסווג ישר מול מעגל לפי מרחק.",
        ),
        item(
            "רדיוס ומשיק",
            "בנקודת ההשקה, מה היחס בין הרדיוס למשיק?",
            "הם מאונכים",
            ["הם מקבילים", "הם שווים באורך", "אין קשר"],
            "הרדיוס לנקודת ההשקה מאונך למשיק.",
            "זה נותן את שיפוע המשיק מתוך שיפוע הרדיוס, אם הרדיוס אינו אנכי.",
            "אפשר להשתמש בניצבות בין רדיוס למשיק.",
        ),
        _distance(3, 1, 3, 8, "מרחק אנכי"),
        item(
            "אנך חוצה מיתר",
            "האנך מהמרכז למיתר עושה מה?",
            "חוצה את המיתר",
            ["מאונך לרדיוס", "שווה לרדיוס תמיד", "לא נוגע במיתר"],
            "במעגל, האנך מהמרכז למיתר חוצה את המיתר.",
            "זו תכונה של מיתר ומעגל, והיא שימושית כשמחפשים אמצע מיתר.",
            "אפשר לזכור שהאנך מהמרכז חוצה מיתר.",
        ),
        _slope(-1, 2, 2, -4, "שיפוע שלילי"),
    ]


def _PRACTICE_VEC_1() -> list[dict]:
    return [
        _dot(1, 2, 3, 4, "עוד סקלרית 1"),
        _dot(2, -1, 1, 2, "מאונכים"),
        item(
            "אורך",
            "מה אורך הווקטור (6, 8)?",
            "10",
            ["14", "48", "100"],
            "שורש של סכום הריבועים.",
            "36 + 64 = 100. השורש הוא 10.",
            "אפשר לחשב אורך של וקטור.",
        ),
        item(
            "חיבור",
            "מה הסכום של (1, 4) ו (2, -1)?",
            "(3, 3)",
            ["(3, 5)", "(-1, 5)", "(2, -4)"],
            "מחברים רכיב רכיב.",
            "1+2 ו 4+(-1) נותנים (3, 3).",
            "אפשר לחבר שני וקטורים.",
        ),
        item(
            "מקבילים",
            "האם (2, 4) מקביל ל (1, 2)?",
            "כן",
            ["לא", "רק אם האורך שווה", "הם מאונכים"],
            "אחד הוא כפל של השני בסקלר.",
            "(2, 4) = 2 כפול (1, 2). הם מקבילים.",
            "אפשר לזהות וקטורים מקבילים.",
        ),
        _dot(-1, 5, 2, 1, "עוד סקלרית 2"),
    ]


def _PRACTICE_VEC_2() -> list[dict]:
    return [
        item(
            "זווית חדה או קהה",
            "המכפלה הסקלרית של שני וקטורים שאינם אפס היא 5-. מה אפשר לומר על הזווית ביניהם?",
            "היא קהה",
            ["היא חדה", "היא ישרה", "הם מקבילים בהכרח"],
            "מכפלה סקלרית שלילית אומרת קוסינוס שלילי, כלומר זווית קהה.",
            "המונה של הקוסינוס שלילי והמכנה חיובי, לכן הזווית קהה.",
            "אפשר לקרוא סוג זווית ממכפלה סקלרית.",
        ),
        item(
            "וקטור יחידה",
            "מה אורך וקטור יחידה בכיוון (3, 4), אחרי נרמול?",
            "1",
            ["5", "3", "7"],
            "מנרמלים על ידי חילוק באורך. התוצאה באורך 1.",
            "האורך המקורי 5. מחלקים כל רכיב ב 5 ומקבלים וקטור באורך 1.",
            "אפשר לנרמל וקטור.",
        ),
        item(
            "ישר פרמטרי",
            "הישר הוא (1, 2) + t(2, 0). האם הנקודה (5, 2) על הישר?",
            "כן, כאשר t = 2",
            ["לא", "כן, כאשר t = 5", "רק כאשר t = 0"],
            "מחפשים t אחד שמתאים לשני הרכיבים.",
            "1 + 2t = 5 נותן t = 2. הרכיב השני: 2 + 0 = 2. מתאים.",
            "אפשר לבדוק אם נקודה על ישר פרמטרי.",
        ),
        _dot(4, 1, 2, 3, "סקלרית נוספת"),
        item(
            "קוסינוס הזווית",
            "שני וקטורים מאורך 2, והמכפלה הסקלרית שלהם 2. מה cos של הזווית?",
            "1/2",
            ["2", "1", "0"],
            "cos שווה למכפלה הסקלרית חלקי מכפלת האורכים.",
            "2 חלקי (2 כפול 2) שווה 1/2.",
            "אפשר לחשב קוסינוס של זווית בין וקטורים.",
        ),
        item(
            "כיוון",
            "איזה וקטור הוא כיוון של הישר (0, 1) + t(3, -1)?",
            "(3, -1)",
            ["(0, 1)", "(3, 1)", "(1, 3)"],
            "הכיוון הוא הווקטור שמוכפל ב t, לא נקודת המוצא.",
            "הישר זז לפי (3, -1) כש t גדל ב 1.",
            "אפשר לקרוא וקטור כיוון מישר פרמטרי.",
        ),
    ]


def _PRACTICE_VEC_3() -> list[dict]:
    return [
        item(
            "אורך במרחב",
            "מה אורך הווקטור (2, 3, 6)?",
            "7",
            ["11", "36", "5"],
            "שורש של סכום שלושה ריבועים.",
            "4 + 9 + 36 = 49. השורש הוא 7.",
            "אפשר לחשב אורך של וקטור במרחב.",
        ),
        item(
            "סקלרית במרחב",
            "מה המכפלה הסקלרית של (1, 0, 2) ו (3, 4, -1)?",
            "1",
            ["5", "0", "9"],
            "סכום של שלוש מכפלות רכיבים.",
            "3 + 0 + (-2) = 1.",
            "אפשר לחשב מכפלה סקלרית במרחב.",
        ),
        item(
            "מכפלה וקטורית בסיסית",
            "מה i × j?",
            "k",
            ["i", "-k", "0"],
            "שני וקטורי הבסיס הראשונים נותנים את השלישי, בכיוון יד ימין.",
            "i × j = k.",
            "אפשר לזכור את המכפלה הווקטורית של i ו j.",
        ),
        item(
            "נורמל",
            "מה וקטור נורמל למישור 2x - y + 4z = 5?",
            "(2, -1, 4)",
            ["(2, 1, 4)", "(5, 0, 0)", "(1, 1, 1)"],
            "המקדמים של x, y, z הם רכיבי הנורמל.",
            "הנורמל הוא (2, -1, 4). האיבר החופשי לא נכנס לווקטור.",
            "אפשר לקרוא נורמל ממשוואת מישור.",
        ),
        item(
            "נקודה על מישור",
            "האם (1, 1, 1) על המישור x + y + z = 3?",
            "כן",
            ["לא", "רק אם היא הראשית", "אי אפשר לדעת"],
            "מציבים במשוואת המישור.",
            "1 + 1 + 1 = 3. הנקודה על המישור.",
            "אפשר לבדוק אם נקודה על מישור.",
        ),
        _dot(0, 5, 7, 0, "סקלרית של צירים"),
    ]


def _PRACTICE_CPX_1() -> list[dict]:
    return [
        _cdot(2, 3, 1, 1, "עוד כפל 1"),
        _cdot(4, -1, 1, 2, "עוד כפל 2"),
        item(
            "מודולוס",
            "מה המודולוס של 3 + 4i?",
            "5",
            ["7", "25", "12"],
            "שורש של סכום ריבועי החלקים.",
            "9 + 16 = 25. השורש הוא 5.",
            "אפשר לחשב מודולוס.",
        ),
        item(
            "צמוד",
            "מה הצמוד של 2 - 5i?",
            "2 + 5i",
            ["-2 - 5i", "-2 + 5i", "5 - 2i"],
            "הצמוד מחליף את סימן החלק המדומה.",
            "2 - 5i הופך ל 2 + 5i.",
            "אפשר לכתוב מספר צמוד.",
        ),
        item(
            "חיבור",
            "חשבו (1 + 2i) + (3 - 5i).",
            "4 - 3i",
            ["4 + 3i", "4 - 7i", "2 - 3i"],
            "ממשיים לחוד, מדומים לחוד.",
            "1+3 ו 2+(-5) נותנים 4 - 3i.",
            "אפשר לחבר מספרים מרוכבים.",
        ),
        item(
            "שוויון",
            "אם a + bi = 3 - 2i, מה b?",
            "-2",
            ["2", "3", "0"],
            "החלקים הממשיים שווים והמדומים שווים, כל זוג לחוד.",
            "b הוא המקדם של i, כלומר -2.",
            "אפשר להשוות חלקים של מספרים מרוכבים.",
        ),
    ]


def _PRACTICE_CPX_2() -> list[dict]:
    return [
        item(
            "זווית של 1+i",
            "מה הזווית של 1 + i, במעלות?",
            "45",
            ["90", "30", "60"],
            "שני החלקים שווים וחיוביים, אז הרביע הראשון וזווית 45.",
            "המודולוס √2 והזווית 45 מעלות.",
            "אפשר לקרוא את הזווית של 1+i.",
        ),
        item(
            "ריבוע קוטבי",
            "מה (1 + i) בריבוע?",
            "2i",
            ["2", "1 + i", "-2"],
            "בכפל המודולוסים נכפלים והזוויות מתחברות.",
            "מודולוס √2 כפול עצמו הוא 2, וזווית 45 ועוד 45 היא 90. זה 2i.",
            "אפשר להעלות 1+i בריבוע דרך הצגה קוטבית.",
        ),
        item(
            "כפל ב i",
            "כפל ב i עושה מה לנקודה במישור?",
            "סיבוב של 90 מעלות נגד כיוון השעון",
            ["הזזה ימינה", "שיקוף בציר x", "סיבוב של 180"],
            "i יושב בזווית 90, אז כפל בו מוסיף 90.",
            "המודולוס של i הוא 1, לכן האורך נשמר ורק הזווית גדלה ב 90.",
            "אפשר לתאר כפל ב i כסיבוב.",
        ),
        item(
            "אחד חלקי i",
            "מה 1/i?",
            "-i",
            ["i", "1", "-1"],
            "כופלים מונה ומכנה ב i, או זוכרים ש i כפול -i הוא 1.",
            "1/i = -i, כי i·(-i) = -i^2 = 1.",
            "אפשר לחשב 1/i.",
        ),
        _cdot(1, 1, 1, 1, "כפל של 1+i בעצמו"),
        item(
            "מודולוס של מכפלה",
            "מודולוס של 1+i הוא √2, ומודולוס של 2 הוא 2. מה מודולוס המכפלה?",
            "2√2",
            ["2", "√2", "4"],
            "בכפל המודולוסים נכפלים.",
            "√2 כפול 2 הוא 2√2.",
            "אפשר לכפול מודולוסים.",
        ),
    ]


def _PRACTICE_CPX_3() -> list[dict]:
    return [
        item(
            "שורשי 1-",
            "מהם פתרונות z^2 = -1?",
            "i וגם -i",
            ["1 וגם -1", "i בלבד", "-1 וגם i"],
            "i בריבוע הוא 1-, וגם מינוס i בריבוע.",
            "i^2 = -1 ו (-i)^2 = i^2 = -1.",
            "אפשר לפתור z בריבוע שווה 1-.",
        ),
        item(
            "דיסקרימיננטה שלילית",
            "למשוואה x^2 + 2x + 5 = 0, מה זוג השורשים?",
            "-1 + 2i וגם -1 - 2i",
            ["-1 וגם -5", "1 + 2i וגם 1 - 2i", "2i וגם -2i"],
            "הדיסקרימיננטה 4 - 20 = -16. שורש שלה הוא 4i.",
            "x = (-2 ± 4i) / 2, כלומר -1 ± 2i.",
            "אפשר לפתור משוואה ריבועית עם שורשים צמודים.",
        ),
        item(
            "צמוד הוא גם שורש",
            "לפולינום עם מקדמים ממשיים יש שורש 2 + i. מה עוד חייב להיות שורש?",
            "2 - i",
            ["-2 + i", "2 + i", "1 + 2i"],
            "שורש לא ממשי מגיע עם הצמוד שלו, כשהמקדמים ממשיים.",
            "הצמוד של 2 + i הוא 2 - i, והוא גם שורש.",
            "אפשר להשלים שורש צמוד.",
        ),
        item(
            "חזקה של i",
            "מה i^4?",
            "1",
            ["i", "-1", "-i"],
            "החזקות מחזוריות באורך 4.",
            "i^2 = -1, ו i^4 = (i^2)^2 = 1.",
            "אפשר לחשב חזקה מחזורית של i.",
        ),
        _cdot(2, -3, 1, 1, "כפל בשליטה"),
        item(
            "משוואה ממשית",
            "מהם פתרונות z^2 = 1 במרוכבים?",
            "1 וגם -1",
            ["i וגם -i", "1 בלבד", "1 וגם i"],
            "אין כאן חלק מדומה. אלה אותם שני שורשים ממשיים.",
            "z^2 - 1 = (z-1)(z+1) = 0.",
            "אפשר לא להמציא שורש מדומה כשהדיסקרימיננטה חיובית.",
        ),
    ]


def _PRACTICE_EXP_1() -> list[dict]:
    return [
        _log2(7, "עוד לוג 1"),
        _log2(8, "עוד לוג 2"),
        item(
            "לוג של 1",
            "מה log3 של 1?",
            "0",
            ["1", "3", "לא מוגדר"],
            "כל בסיס חוקי בחזקת 0 הוא 1.",
            "3^0 = 1, לכן הלוג הוא 0.",
            "אפשר לדעת שלוגריתם של 1 הוא 0.",
        ),
        item(
            "חוק המכפלה",
            "log2(4) + log2(8) שווה לביטוי הבא. איזה?",
            "log2(32)",
            ["log2(12)", "log2(2)", "32"],
            "סכום לוגים באותו בסיס הוא לוג של המכפלה.",
            "4 כפול 8 הוא 32, ו log2(32) = 5. גם 2 + 3 = 5.",
            "אפשר לחבר לוגים דרך מכפלה.",
        ),
        item(
            "חזקה יורדת",
            "מה 3 log2(5), כלוג יחיד?",
            "log2(125)",
            ["log2(15)", "log2(8)", "5"],
            "מקדם לפני לוג הופך לחזקה בתוך הלוג.",
            "3 log2(5) = log2(5^3) = log2(125).",
            "אפשר להוריד מקדם לחזקה.",
        ),
        item(
            "לוג עשרוני",
            "מה log10 של 10000?",
            "4",
            ["3", "5", "10000"],
            "סופרים את האפסים, או את החזקה של 10.",
            "10^4 = 10000.",
            "אפשר לחשב לוג עשרוני של חזקת 10.",
        ),
    ]


def _PRACTICE_EXP_2() -> list[dict]:
    return [
        item(
            "אותו בסיס",
            "פתרו 3^x = 81. מהו x?",
            "4",
            ["3", "27", "9"],
            "כותבים את שני הצדדים כחזקה של 3.",
            "81 = 3^4, לכן x = 4.",
            "אפשר לפתור משוואה מעריכית עם בסיס משותף.",
        ),
        item(
            "משוואת לוג",
            "פתרו log2(x) = 6. מהו x?",
            "64",
            ["12", "32", "8"],
            "חוזרים לחזקה: x הוא 2 בחזקת אגף ימין.",
            "x = 2^6 = 64.",
            "אפשר לפתור משוואת לוג קצרה.",
        ),
        item(
            "לוג ו exp",
            "מה e בחזקת ln 5?",
            "5",
            ["1", "e", "ln 5"],
            "המעריכית והלוג הטבעי מבטלים זה את זה.",
            "e^(ln 5) = 5.",
            "אפשר לצמצם e בחזקת ln.",
        ),
        _log2(9, "לוג גדול"),
        item(
            "תחום של לוג",
            "לאילו x הלוג של (x - 2) מוגדר, בבסיס חוקי?",
            "x > 2",
            ["x >= 2", "x ≠ 2", "x > 0"],
            "הארגומנט חייב להיות חיובי, לא אפס.",
            "x - 2 > 0, לכן x > 2. ב x = 2 הלוג לא מוגדר.",
            "אפשר למצוא תחום של לוגריתם.",
        ),
        item(
            "בסיסים שווים",
            "אם 5^a = 5^b, מה נכון?",
            "a = b",
            ["a = 5b", "a = b + 5", "אי אפשר לדעת"],
            "הפונקציה המעריכית חד חד ערכית.",
            "מבסיס שווה ומעריכים שאולי שונים מסיקים שהמעריכים שווים.",
            "אפשר להשוות מעריכים כשהבסיס אותו בסיס חוקי.",
        ),
    ]


def _PRACTICE_EXP_3() -> list[dict]:
    return [
        _half(4, "ארבע מחציות"),
        _half(6, "שש מחציות"),
        item(
            "גידול שכופל",
            "כמות שמוכפלת בכל שעה. פי כמה היא אחרי 4 שעות?",
            "16",
            ["8", "4", "12"],
            "כל שעה כפל ב 2, לא חיבור של 2.",
            "2^4 = 16. זה לא 2 כפול 4.",
            "אפשר לחשב גידול שמכפיל את עצמו.",
        ),
        item(
            "נגזרת מעריכית",
            "מה הנגזרת של e^(3x)?",
            "3e^(3x)",
            ["e^(3x)", "3e^x", "e^(3x)/3"],
            "הנגזרת של e^(kx) היא k כפול e^(kx).",
            "כאן k = 3, לכן הנגזרת 3e^(3x).",
            "אפשר לגזור אקספוננט עם מקדם במעריך.",
        ),
        item(
            "נגזרת של ln",
            "מה הנגזרת של ln x, עבור x חיובי?",
            "1/x",
            ["ln x", "e^x", "x"],
            "זו הנגזרת הבסיסית של הלוג הטבעי.",
            "(ln x)' = 1/x.",
            "אפשר לגזור ln x.",
        ),
        item(
            "שני זמני מחצית",
            "אחרי שני זמני מחצית נשאר",
            "1/4",
            ["1/2", "1/3", "0"],
            "חצי של חצי.",
            "(1/2)^2 = 1/4.",
            "אפשר לחשב שתי מחציות.",
        ),
    ]


_PRACTICE = {
    ("algebra", 1): _PRACTICE_ALGEBRA_1,
    ("algebra", 2): _PRACTICE_ALGEBRA_2,
    ("algebra", 3): _PRACTICE_ALGEBRA_3,
    ("geometry", 1): _PRACTICE_GEOMETRY_1,
    ("geometry", 2): _PRACTICE_GEOMETRY_2,
    ("geometry", 3): _PRACTICE_GEOMETRY_3,
    ("trig", 1): _PRACTICE_TRIG_1,
    ("trig", 2): _PRACTICE_TRIG_2,
    ("trig", 3): _PRACTICE_TRIG_3,
    ("sequences", 1): _PRACTICE_SEQ_1,
    ("sequences", 2): _PRACTICE_SEQ_2,
    ("sequences", 3): _PRACTICE_SEQ_3,
    ("probability", 1): _PRACTICE_PROB_1,
    ("probability", 2): _PRACTICE_PROB_2,
    ("probability", 3): _PRACTICE_PROB_3,
    ("functions", 1): _PRACTICE_FUN_1,
    ("functions", 2): _PRACTICE_FUN_2,
    ("functions", 3): _PRACTICE_FUN_3,
    ("extrema", 1): _PRACTICE_EXT_1,
    ("extrema", 2): _PRACTICE_EXT_2,
    ("extrema", 3): _PRACTICE_EXT_3,
    ("integrals", 1): _PRACTICE_INT_1,
    ("integrals", 2): _PRACTICE_INT_2,
    ("integrals", 3): _PRACTICE_INT_3,
    ("analytic", 1): _PRACTICE_AN_1,
    ("analytic", 2): _PRACTICE_AN_2,
    ("analytic", 3): _PRACTICE_AN_3,
    ("vectors", 1): _PRACTICE_VEC_1,
    ("vectors", 2): _PRACTICE_VEC_2,
    ("vectors", 3): _PRACTICE_VEC_3,
    ("complex", 1): _PRACTICE_CPX_1,
    ("complex", 2): _PRACTICE_CPX_2,
    ("complex", 3): _PRACTICE_CPX_3,
    ("exp_log", 1): _PRACTICE_EXP_1,
    ("exp_log", 2): _PRACTICE_EXP_2,
    ("exp_log", 3): _PRACTICE_EXP_3,
}


def _REVIEW_BUILD() -> dict[str, object]:
    return {
        "algebra": lambda: [
            _lin(11, 3, 2, "חזרה, משוואה"),
            _quad(6, -2, "חזרה, ריבועית"),
            _sum_diff(22, 8, "חזרה, מערכת"),
            _ineq(4, -3, 13, "חזרה, אי שוויון"),
            _rect(2, 36, "חזרה, מלבן"),
            _double_root(12, "חזרה, שורש כפול"),
        ],
        "geometry": lambda: [
            _angles(28, 53, "חזרה, זווית"),
            _pythag(20, 21, "חזרה, יתר"),
            _tri_area(14, 8, "חזרה, שטח"),
            _inscribed(60, "חזרה, היקפית"),
            _similar_area(5, 1, 3, "חזרה, שטחים"),
            item(
                "חזרה, עיגול",
                "מה שטח עיגול שרדיוסו 6?",
                "36π",
                ["12π", "6π", "36"],
                "π כפול ריבוע הרדיוס.",
                "36π.",
                "אפשר לחזור על שטח עיגול.",
            ),
        ],
        "trig": lambda: [
            _sin_ratio(9, 40, "חזרה, סינוס"),
            _area_sas(8, 10, 1, 2, "חזרה, שטח"),
            item("חזרה, sin 30", "מה sin של 30 מעלות?", "1/2", ["√3/2", "√2/2", "1"], "זה ערך סטנדרטי.", "sin 30 = 1/2.", "אפשר לשלוף sin 30."),
            item("חזרה, שני פתרונות", "בתחום 0 עד 180, sin x = √2/2. אילו זוויות?", "45 וגם 135", ["45 וגם 90", "30 וגם 150", "135 בלבד"], "הסינוס שווה גם בזווית המשלימה ל 180.", "sin 45 = sin 135 = √2/2.", "אפשר למצוא זוג פתרונות."),
            item("חזרה, cos 0", "מה cos של 0 מעלות?", "1", ["0", "1/2", "לא מוגדר"], "ב 0 הקוסינוס הוא 1.", "cos 0 = 1.", "אפשר לשלוף cos 0."),
            item(
                "חזרה, קוסינוסים",
                "צלעות 3 ו 4 והזווית ביניהן 60 מעלות, ו cos 60 = 1/2. מה ריבוע הצלע השלישית?",
                "13",
                ["25", "7", "37"],
                "c^2 = 9 + 16 - 2·3·4·(1/2).",
                "25 - 12 = 13.",
                "אפשר להציב במשפט הקוסינוסים.",
            ),
        ],
        "sequences": lambda: [
            _arith_n(9, 5, 7, "חזרה, איבר"),
            _arith_sum(4, 6, 5, "חזרה, סכום חשבוני"),
            _geo_n(6, 2, 4, "חזרה, הנדסית"),
            _geo_inf(8, 1, 5, "חזרה, אינסוף"),
            item("חזרה, סכום עד 15", "מה סכום השלמים מ 1 עד 15?", "120", ["105", "150", "15"], "n(n+1)/2.", "15·16/2 = 120.", "אפשר לסכום את הראשונים."),
            item("חזרה, בסיס", "באינדוקציה, מה בודקים בבסיס בדרך כלל?", "את המקרה n = 1 בחישוב ישיר", ["את הצעד בלבד", "את n אינסופי", "את הנגזרת"], "הבסיס הוא מקרה קטן שממנו השרשרת יוצאת.", "בודקים n = 1 ישירות, ואחר כך מוכיחים צעד.", "אפשר לתאר את בסיס האינדוקציה."),
        ],
        "probability": lambda: [
            _dice_sum(6, "חזרה, סכום 6"),
            _dice_sum(10, "חזרה, סכום 10"),
            _coins(5, "חזרה, חמישה מטבעות"),
            item("חזרה, משלים 1/4", "הסתברות 1/4. מה המשלים?", "3/4", ["1/4", "4/3", "1/2"], "1 פחות המאורע.", "3/4.", "אפשר משלים."),
            item("חזרה, תוחלת בינומית", "20 ניסויים עם p = 1/5. מה תוחלת מספר ההצלחות?", "4", ["5", "20", "1"], "n כפול p.", "20/5 = 4.", "אפשר תוחלת בינומית."),
            item("חזרה, צירוף", "כמה דרכים לבחור 2 מתוך 5?", "10", ["20", "25", "5"], "5·4/2.", "10.", "אפשר צירוף."),
        ],
        "functions": lambda: [
            _slope(2, 1, 5, 10, "חזרה, שיפוע"),
            _domain(4, "חזרה, שורש"),
            _deriv_value("5x^2", 3, "חזרה, נגזרת", "הנגזרת 10x. ב x = 3 היא 30."),
            _tangent_square(5, "חזרה, משיק"),
            item("חזרה, אסימפטוטה", "למנה (4x - 1)/(2x + 3), מה האסימפטוטה האופקית?", "y = 2", ["y = 4", "y = 3", "y = 1/2"], "יחס המקדמים המובילים.", "4/2 = 2.", "אפשר אסימפטוטה."),
            item("חזרה, קבוע", "מה הנגזרת של 7?", "0", ["7", "1", "לא מוגדר"], "נגזרת של קבוע היא 0.", "הישר אופקי, השיפוע 0.", "אפשר לגזור קבוע."),
        ],
        "extrema": lambda: [
            _vertex(1, -16, 2, "חזרה, קודקוד"),
            _vertex(2, -4, 9, "חזרה, קודקוד שני"),
            item("חזרה, סיווג", "נגזרת עוברת מחיובי לשלילי. מה בנקודה?", "מקסימום", ["מינימום", "פיתול", "קצה בלבד"], "עלייה ואז ירידה.", "זה מקסימום.", "אפשר לסווג לפי סימן."),
            item("חזרה, גדר", "גדר 20 מול קיר, שתי צלעות ניצבות שוות x. באיזה x השטח מקסימלי?", "5", ["10", "4", "20"], "שטח x(20-2x).", "20-4x=0 נותן x=5. השטח 50.", "אפשר בעיית גדר."),
            item("חזרה, היקף 36", "מלבן בהיקף 36. אורך הצלע בריבוע שממקסם את השטח?", "9", ["18", "6", "12"], "סכום שתי צלעות סמוכות 18, והמקסימום כשהן שוות.", "x=9.", "אפשר מלבן מקסימלי."),
            item("חזרה, ערך", "y = x^2 - 4x + 1 ב x = 2. מה y?", "-3", ["1", "2", "0"], "מציבים בפונקציה.", "4 - 8 + 1 = -3.", "אפשר ערך בקודקוד."),
        ],
        "integrals": lambda: [
            _definite(2, 2, 0, 3, "חזרה, אינטגרל"),
            _definite(1, 3, 0, 2, "חזרה, חזקה"),
            item("חזרה, סינוס", "מה הקדומה של sin x, עד כדי קבוע?", "-cos x", ["cos x", "sin x", "-sin x"], "נגזרת של מינוס קוסינוס היא סינוס.", "-cos x.", "אפשר קדומה של סינוס."),
            item("חזרה, שטח וסימן", "אינטגרל שלילי אומר שהשטח", "הוא הערך המוחלט, אם הגרף מתחת לציר ולא חוצה", ["הוא שלילי", "הוא אפס", "אינו קיים"], "שטח גיאומטרי אי שלילי.", "לוקחים ערך מוחלט אחרי שמבינים את הסימן.", "אפשר להפריד שטח מאינטגרל."),
            item("חזרה, בין גרפים", "האינטגרל של העליון פחות התחתון יצא 2/3. מה השטח?", "2/3", ["-2/3", "3/2", "0"], "ההפרש כבר חיובי, אז זה השטח.", "2/3.", "אפשר לקרוא שטח מהפרש חיובי."),
            item("חזרה, גבולות שווים", "אינטגרל מ 7 עד 7 של כל פונקציה רציפה הוא", "0", ["7", "1", "לא מוגדר"], "אין רוחב.", "F(7)-F(7)=0.", "אפשר גבולות שווים."),
        ],
        "analytic": lambda: [
            _distance(4, 1, 1, 5, "חזרה, מרחק"),
            _slope(0, 0, 4, 8, "חזרה, שיפוע"),
            item("חזרה, אמצע", "אמצע (2, 8) ו (6, 2)?", "(4, 5)", ["(4, 10)", "(8, 10)", "(2, 3)"], "ממוצע השיעורים.", "(4, 5).", "אפשר אמצע."),
            item("חזרה, על המעגל", "האם (6, 8) על x^2 + y^2 = 100?", "כן", ["לא", "בפנים", "בחוץ"], "36+64=100.", "הנקודה על המעגל.", "אפשר בדיקת מעגל."),
            item("חזרה, מרחק לישר", "מרחק מ (0,0) לישר 5x + 12y - 26 = 0?", "2", ["26", "13", "1"], "|-26| חלקי 13.", "26/13=2.", "אפשר מרחק לישר."),
            item("חזרה, מאונך", "שיפוע 1/3. שיפוע מאונך?", "-3", ["3", "-1/3", "1/3"], "מכפלה 1-.", "(1/3)m=-1 נותן m=-3.", "אפשר שיפוע מאונך."),
        ],
        "vectors": lambda: [
            _dot(5, 1, 2, -3, "חזרה, סקלרית"),
            item("חזרה, אורך", "אורך (5, 12)?", "13", ["17", "7", "60"], "25+144=169.", "השורש 13.", "אפשר אורך."),
            item("חזרה, מאונך", "מכפלה סקלרית 0, והווקטורים אינם אפס. מה הזווית?", "90 מעלות", ["0", "45", "180"], "קוסינוס אפס.", "הזווית ישרה.", "אפשר לזהות ניצבות."),
            item("חזרה, נורמל", "נורמל ל x - 2y + z = 4?", "(1, -2, 1)", ["(1, 2, 1)", "(4, 0, 0)", "(1, -2, 4)"], "המקדמים.", "(1, -2, 1).", "אפשר נורמל."),
            item("חזרה, i × j", "i × j שווה", "k", ["-k", "i", "0"], "בסיס ימני.", "k.", "אפשר מכפלה וקטורית בסיסית."),
            item("חזרה, יחידה", "אחרי נרמול, האורך הוא", "1", ["0", "האורך המקורי", "2"], "חילוק באורך.", "האורך 1.", "אפשר נרמול."),
        ],
        "complex": lambda: [
            _cdot(3, 1, 1, -1, "חזרה, כפל"),
            item("חזרה, מודולוס", "מודולוס של 5 + 12i?", "13", ["17", "7", "169"], "25+144=169.", "13.", "אפשר מודולוס."),
            item("חזרה, צמוד", "צמוד של -2 + 6i?", "-2 - 6i", ["2 - 6i", "-2 + 6i", "6 - 2i"], "מחליפים רק את סימן החלק המדומה.", "-2 - 6i.", "אפשר צמוד."),
            item("חזרה, i^3", "מה i^3?", "-i", ["i", "-1", "1"], "i^2=-1, כפול i הוא -i.", "-i.", "אפשר חזקת i."),
            item("חזרה, שורשים", "שורשי x^2 + 1 = 0?", "i וגם -i", ["1 וגם -1", "i בלבד", "אין פתרון"], "x^2 = -1.", "i ו -i.", "אפשר שורשי 1-."),
            item("חזרה, 1+i", "הזווית של 1+i במעלות?", "45", ["90", "0", "30"], "רביע ראשון, חלקים שווים.", "45.", "אפשר זווית."),
        ],
        "exp_log": lambda: [
            _log2(10, "חזרה, לוג"),
            _half(3, "חזרה, שלוש מחציות"),
            item("חזרה, 2^x", "פתרו 2^x = 32.", "5", ["4", "16", "6"], "32 הוא 2^5.", "x=5.", "אפשר מעריך."),
            item("חזרה, log", "פתרו log2(x) = 3.", "8", ["6", "9", "16"], "2^3.", "x=8.", "אפשר לוג."),
            item("חזרה, נגזרת", "נגזרת של e^(2x)?", "2e^(2x)", ["e^(2x)", "2e^x", "e^(2x)/2"], "כופלים במקדם שבמעריך.", "2e^(2x).", "אפשר נגזרת מעריכית."),
            item("חזרה, כפל", "כמות שמוכפלת כל שעה. אחרי 5 שעות היא גדולה פי", "32", ["10", "25", "16"], "2^5.", "32.", "אפשר גידול."),
        ],
    }


_REVIEW = _REVIEW_BUILD()
