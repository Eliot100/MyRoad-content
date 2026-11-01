"""Hints and per choice feedback. H = {id: (hint, {wrong_choice_id: feedback})}."""
H = {'practice_hello': ('זו המילה שאומרים כשנפגשים.', {'a': 'Goodbye אומרים כשנפרדים.', 'c': 'Sorry אומרים כשמבקשים סליחה.'}),
 'practice_goodbye': ('זו המילה שאומרים כשהולכים.', {'a': 'Hello אומרים כשנפגשים.', 'c': 'Please אומרים כשמבקשים.'}),
 'practice_please': ('זו המילה שמוסיפים לבקשה.', {'b': 'Happy פירושו שמח.', 'c': 'Sad פירושו עצוב.'}),
 'practice_happy': ('תחשבו על פרצוף מחייך.', {'a': 'עצוב הוא sad.', 'c': 'עייף הוא tired.'}),
 'check_sad': ('זו ההרגשה כשבוכים.', {'a': 'שמח הוא happy.', 'c': 'רעב הוא hungry.'}),
 'check_tired': ('זו ההרגשה כשרוצים לישון.', {'b': 'שמח הוא happy.', 'c': 'רעב הוא hungry.'})}
