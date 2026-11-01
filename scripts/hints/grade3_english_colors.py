"""Hints and per choice feedback. H = {id: (hint, {wrong_choice_id: feedback})}."""
H = {'practice_red': ('אדום הוא צבע של עגבנייה.', {'a': 'blue הוא כחול.', 'c': 'green הוא ירוק.'}),
 'practice_blue': ('תחשבו על השמיים ביום בהיר.', {'b': 'yellow הוא צהוב, כמו השמש.', 'c': 'black הוא שחור, כמו הלילה.'}),
 'practice_yellow': ('השמש צהובה. איזו מילה אומרת צהוב?', {'b': 'green הוא ירוק.', 'c': 'black הוא שחור.'}),
 'practice_orange': ('כתום הוא גם שם של פרי.', {'a': 'purple הוא סגול.', 'c': 'white הוא לבן.'}),
 'check_purple': ('זה צבע של ענבים כהים.', {'a': 'אדום הוא red.', 'c': 'ירוק הוא green.'}),
 'check_mix': ('זה צבע של דשא.', {'a': 'אדום הוא red.', 'b': 'כחול הוא blue.'})}
