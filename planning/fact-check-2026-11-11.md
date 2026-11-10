# Fact check of planning facts (2026-11-11)

Overnight queue item C3. Each factual claim about bagrut questionnaires, unit levels, exam structure, the psychometric test (PET) and AMIRNET in `planning/*.md` was checked against official public sources only: education.gov.il (pop. / meyda.) and nite.org.il. I fetched every source with `curl` and extracted PDFs with `pdftotext` on 2026-11-10 at about 23:30 to 00:15 (Asia/Jerusalem). No outside AI tool was used and no business content was sent anywhere.

Verdicts: **confirmed** = the source says the same thing. **mismatch** = the source says something different, or the file leaves out something that matters for the road. **unverified** = I could not settle it from a public source in this pass.

This is a report only. No other planning file was edited.

## Summary

| Verdict | Count |
| --- | --- |
| confirmed | 44 |
| mismatch | 13 |
| unverified | 4 |
| **total** | **61** |

**Most important mismatches and corrections**

1. **History units** (`history-bagrut-from-zero.md:7`): the core history bagrut is **2 units**, not "typically 2–3". The optional extension (היסטוריה מורחב) adds a 3rd unit (022382 for externals, 022383 for school students) and units 4–5 (022381), for 5 in total.
2. **History codes for externals** (`history-bagrut-from-zero.md:26,82`, which were marked unverified): externals and re-takers sit **022261 (70%)** and **22262 (30%)**. New-immigrant externals sit 022264 and 022252. For externals the "30% school choice" is a written exam, not a school task.
3. **Chemistry for externals** (`chemistry-bagrut5-from-zero.md:13,99`): externals do **not** follow the 70% external / 30% internal split. They sit three external questionnaires: **037381 (55%) + 037382 (15%) + 037282 (30%)**. Also, the written paper 037381 is 55% of the 70%, not the whole 70%. The other 15% is the inquiry lab (037388 oral, or 037376).
4. **Computer science, unit 5 choices** (`computer-science-bagrut-from-zero.md:24`): MoE lists **four** choices, not three: AI core topics (נושאי ליבה בבינה מלאכותית), computational models, OOP, and algorithms. The unit 3 option is "מבוא לבינה מלאכותית" (intro to AI), not "machine learning". For externals, 899372 is the written exam that replaces the unit 3 task, and its listed syllabus is "מבוא לתכנות בסביבת אינטרנט" (intro to web programming). The 2026 focusing file pairs **899372 with 899282**. An adult road needs this content, not just "awareness".
5. **Math 35571 answer rules** (`math-bagrut5-from-zero.md:43`): the MoE page's *regular* structure says short questions are compulsory (answer 3 of 4). Both 2026 papers I checked used a different, eased rule: answer 2 of the 4 short items, and the paper is not compulsory as a whole (moed א: 5 questions, at least one from ch. 1 or 2 and one each from ch. 3 and 4). Simulations should follow the rule for the year the learner sits.
6. **Math 35571 duration** (`math-bagrut-4-to-5-upgrade.md:37,119`), now settled: **3 h 45 min is the regular duration**. The MoE page and the summer 2026 moed א paper both say so (5 × 20 pts). The moed ב paper's **4 h 20 min with 5 × 22 pts (max 100)** is a special-sitting variant. Use 3:45 as the default timer.
7. **4-unit math codes** (`math-bagrut-4-to-5-upgrade.md:42`, marked "not checked"): the new-curriculum 4-unit questionnaires are **35471 and 35472**.
8. **Hebrew 30% paper for externals** (`hebrew-lashon-bagrut-from-zero.md:7,43,160`, marked TODO): the תשפ"ד circular's table lists **11282, עברית: הבנה, הבעה 30%, for נבחני משנה ואקסטרניים**. 11283 is the school report code for general students.
9. **Literature code** (`literature-bagrut-from-zero.md:7,152`, marked unverified): the old-outline 70% external paper is **8281** (8284 for new immigrants). The summer 2026 paper takes 2.5 hours and has 4 chapters (short story, drama, novel/novella, poetry), of which you answer 3 (33⅓ pts each). Externals are given a list of works.

## Claims checked

### AMIRNET and PET (`amirnet-english-placement.md`)

| # | File:line | Claim | Verdict | Correct value / note | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | amirnet-english-placement.md:7,22,48 | AMIRNET is scored on a 50–150 scale, equivalent to AMIR, AMIRAM and the old PET English domain | confirmed | "AMIRNET scores are on a scale of 50 to 150 … equivalent to those on the AMIRAM, the AMIR, or the English domain of the Psychometric Entrance Test" | https://www.nite.org.il/other-tests/amirnet/scores/significance/?lang=en |
| 2 | amirnet-english-placement.md:22,48 | No single exemption cutoff; each institution decides placement, exemption and admission use | confirmed | "Each academic institution makes its own independent decisions" | https://www.nite.org.il/other-tests/amirnet/scores/significance/?lang=en |
| 3 | amirnet-english-placement.md:7,17,27 | From the winter (December) 2026 sitting, PET has only Verbal and Quantitative, and English is tested only in AMIRNET | confirmed | "Starting from the winter (December) 2026 test administration … only two domains … English proficiency will be tested separately via the AMIRNET test" | https://www.nite.org.il/news/notice-081026/?lang=en |
| 4 | amirnet-english-placement.md:27 | Two-domain score = Verbal 50% + Quantitative 50%, general score still 200–800 | confirmed | 50%/50% per the notice; the 200–800 scale is on the score-calculation page | https://www.nite.org.il/news/notice-081026/?lang=en ; https://www.nite.org.il/two-domain-psychometric-entrance-test/scores/calculation/?lang=en |
| 5 | amirnet-english-placement.md:27 | AMIRNET is the placement/waiver test unless an institution says otherwise | confirmed | "AMIRNET is the only test that is used to determine English-level placement or a waiver … unless an institution of higher education specifies otherwise" | https://www.nite.org.il/two-domain-psychometric-entrance-test/faqs/?lang=en |
| 6 | amirnet-english-placement.md:27 | PET and AMIRNET are registered for separately | confirmed | "You cannot register for both tests at the same time … register for each test separately" | https://www.nite.org.il/two-domain-psychometric-entrance-test/faqs/?lang=en |
| 7 | amirnet-english-placement.md:27 | A previous PET English score stays valid for at least 7 years | confirmed | "The English score is valid for at least 7 years, whether … the English domain of the PET or … AMIR, AMIRAM, or AMIRNET" | https://www.nite.org.il/two-domain-psychometric-entrance-test/faqs/?lang=en |
| 8 | amirnet-english-placement.md:41 | You must wait 35 days before retaking AMIRNET | confirmed | "wait at least 35 days … you can take the test again on the 35th day and onwards" | https://www.nite.org.il/other-tests/amirnet/registration-procedures/online-registration/?lang=en |
| 9 | amirnet-english-placement.md:47 | About 50 minutes, adaptive | confirmed | "The AMIRNET takes around 50 minutes"; adaptive by section | https://www.nite.org.il/other-tests/amirnet/faq/?lang=en |
| 10 | amirnet-english-placement.md:47 | 7 or 8 sections; six operational sections in the order SC, SC, RC, Restatement, Restatement, SC; the last section in the 7-section form is an experimental writing task | confirmed | Matches the FAQ word for word. Extra fact: in the experimental sections a wrong answer does not lower the score, but correct answers can raise it by 1–2 points | https://www.nite.org.il/other-tests/amirnet/faq/?lang=en |
| 11 | amirnet-english-placement.md:47 | No scheduled breaks; a missing answer counts as wrong; you can go back only within the same section | confirmed | Bathroom breaks are allowed with a proctor, and the clock keeps running. "a missing answer is marked as a wrong answer"; "go back to previous questions in the same section" | https://www.nite.org.il/other-tests/amirnet/faq/?lang=en |
| 12 | amirnet-english-placement.md:49 | Scores valid for placement/exemption for at least 7 years | confirmed | "for a minimum of seven (7) years" | https://www.nite.org.il/other-tests/amirnet/registration-procedures/online-registration/?lang=en |
| 13 | amirnet-english-placement.md:49 | Results appear in the personal area within 10 days and are not emailed | confirmed | "Within 10 days … see your score by logging onto the NITE website. Test scores will not be sent to examinees by email." Universities get scores within 10 business days | https://www.nite.org.il/other-tests/amirnet/?lang=en |
| 14 | amirnet-english-placement.md:51,97 | From 2027, sections are added in stages: listening and writing, then later speaking | confirmed | "The AMIRNET test will change in stages, beginning in 2027 … listening comprehension and writing and - further in the future - speaking". Today the test "does not assess speaking or writing" | https://www.nite.org.il/other-tests/amirnet/faq/?lang=en |
| 15 | amirnet-english-placement.md:114 | Exact item counts and per-section times are not published | unverified | Still not on the public AMIRNET pages. Keep it as a planning estimate | https://www.nite.org.il/other-tests/amirnet/faq/?lang=en |

### Psychometric (two-domain) (`psychometric-quant-toward-800.md`, `psychometric-verbal-hebrew-toward-800.md`)

| # | File:line | Claim | Verdict | Correct value / note | Source |
| --- | --- | --- | --- | --- | --- |
| 16 | psychometric-quant-toward-800.md:24 ; psychometric-verbal-hebrew-toward-800.md:27 | The paper version has 6 sections; the writing task is 30 min (Hebrew) or 35 min (other languages); MC sections take 20 min | confirmed | Also confirmed: the writing task, 2 Verbal, 2 Quant and 1 experimental section; the whole test is **150 minutes** with no breaks; "exactly 20 minutes to each multiple-choice section" | https://www.nite.org.il/two-domain-psychometric-entrance-test/format/?lang=en ; https://www.nite.org.il/news/notice-081026/?lang=en |
| 17 | psychometric-quant-toward-800.md:121 | One unscored MC section exists | confirmed | "Of the five multiple-choice sections, only two in each domain (a total of four) are used" | https://www.nite.org.il/two-domain-psychometric-entrance-test/format/?lang=en |
| 18 | psychometric-quant-toward-800.md:25 ; psychometric-verbal-hebrew-toward-800.md:28 | Domain scores 50–150, general scores 200–800 | confirmed | — | https://www.nite.org.il/two-domain-psychometric-entrance-test/scores/calculation/?lang=en |
| 19 | psychometric-quant-toward-800.md:25 | Two-domain score weights V and Q equally; the quant-oriented score gives Q triple weight | confirmed | Also: the verbal-oriented score gives V triple weight. Per the notice, past quant/verbal-oriented scores stay three-domain and were not recalculated | same |
| 20 | psychometric-verbal-hebrew-toward-800.md:28,100,108 | The writing task is 25% of the Verbal domain score | confirmed | "The verbal reasoning score includes the score on the writing task, which is weighted at 25%" | same |
| 21 | psychometric-quant-toward-800.md:28 | Quant topic list (percentages … solids) | confirmed | Matches the format page; the math level is comparable to 3-unit bagrut | https://www.nite.org.il/two-domain-psychometric-entrance-test/format/?lang=en |
| 22 | psychometric-quant-toward-800.md:30 | Trig and calculus are not covered, and speed is not the main difficulty | confirmed | "trigonometry or differential and integral calculus are not covered" | same |
| 23 | psychometric-quant-toward-800.md:115 ; psychometric-verbal-hebrew-toward-800.md:103 | Within a type, items run from easy to hard | confirmed | The exception is Reading Comprehension, which follows the order of the text | same |
| 24 | psychometric-quant-toward-800.md:152 | Are Quantitative Comparisons in the current quant section? | confirmed (no) | The two-domain format page lists only **two** quant types: Questions and Problems, and Graph/Table Comprehension. Leave Comparisons out | same |
| 25 | psychometric-verbal-hebrew-toward-800.md:36,156 | Hebrew writing time and minimum length | unverified | 30 min for Hebrew is confirmed (row 16). The ≥25-line minimum comes from the EN PDF; I found no Hebrew page for it in this pass | https://www.nite.org.il/two-domain-psychometric-entrance-test/format/?lang=en |

### Math (`math-bagrut5-from-zero.md`, `math-bagrut-4-to-5-upgrade.md`)

| # | File:line | Claim | Verdict | Correct value / note | Source |
| --- | --- | --- | --- | --- | --- |
| 26 | math-bagrut5-from-zero.md:15 ; math-bagrut-4-to-5-upgrade.md:7,24 | 5 units = questionnaires 35571 + 35572 (new curriculum) | confirmed | — | https://pop.education.gov.il/tchumey_daat/matmatika/chativa-elyona/teaching-mathematics/new-curriculum/ |
| 27 | math-bagrut5-from-zero.md:36 | 35571 weight 60%, 3 h 45 min; 35572 weight 40%, 2.5 h | confirmed | Page: "משקל השאלון: 60 אחוזים משך בחינה: 3 שעות וארבעים וחמש דקות"; 35572 "40 אחוזים … שעתיים וחצי". The summer 2026 35572 paper also says 2.5 h, answer 3 of 5 (33⅓ each) | same ; https://meyda.education.gov.il/sheeloney_bagrut/2026/6/HEB/35572.pdf |
| 28 | math-bagrut5-from-zero.md:43 | 35571 chapters: compulsory short items; probability/sequences/induction; plane geometry + trig; calculus | mismatch (answer rules) | The chapters are right. The *regular* structure on the MoE page is: ch. 1 compulsory, answer 3 of 4; ch. 2 1 of 2; ch. 3 1 of 2; ch. 4 2 of 3, 20 pts each. The summer 2026 papers used eased rules: answer **2 of 4** short items, 5 questions total (moed א: at least one from ch. 1 or 2, and one each from ch. 3 and 4). Build the sim rules per year | MoE page above ; https://meyda.education.gov.il/sheeloney_bagrut/2026/6/HEB/35571.pdf |
| 29 | math-bagrut5-from-zero.md:45 | 35572: analytic geometry + vectors (incl. space trig) + complex numbers; exp/log calculus | confirmed | The paper's ch. 2 title is "גדילה ודעיכה, פונקציות מעריכיות ולוגריתמיות" (growth and decay, exponential and log functions) | https://meyda.education.gov.il/sheeloney_bagrut/2026/6/HEB/35572.pdf |
| 30 | math-bagrut-4-to-5-upgrade.md:34 | 35571 moed ב 2026: 4 chapters, 8 questions, answer 2 of 4 short items, 5 × 22 pts (max 100), 4 h 20 min, non-graphing calculator | confirmed | Matches the paper | https://meyda.education.gov.il/sheeloney_bagrut/2026/8/HEB/35571.pdf |
| 31 | math-bagrut-4-to-5-upgrade.md:37,119 | 3:45 vs 4:20, which is the default? | mismatch (now settled) | **3 h 45 min is the default.** The summer 2026 moed א paper says 3:45 with 5 × 20 pts; moed ב (4:20, 5 × 22) is a special variant | https://meyda.education.gov.il/sheeloney_bagrut/2026/6/HEB/35571.pdf |
| 32 | math-bagrut-4-to-5-upgrade.md:42 | 4-unit questionnaire codes not checked | mismatch (gap filled) | New-curriculum 4 units = **35471 + 35472** (sample 4-unit exams listed under those codes) | https://pop.education.gov.il/tchumey_daat/matmatika/chativa-elyona/teaching-mathematics/new-curriculum/ |
| 33 | math-bagrut-4-to-5-upgrade.md:33 | The 4-unit curriculum PDF is dated February 2015, 120 h/year, three areas | confirmed (partly) | Date and 120 h/year confirmed. The per-topic hour split was not re-read, because the PDF's digits extract garbled | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/matematika/mat_4u.pdf |

### Physics (`physics-bagrut5-from-zero.md`)

| # | File:line | Claim | Verdict | Correct value / note | Source |
| --- | --- | --- | --- | --- | --- |
| 34 | physics-bagrut5-from-zero.md:26 | 5 units from תשע"ה: mechanics, electricity & magnetism, radiation & matter, plus a lab; all examinees take mechanics and electricity on the same questionnaires | confirmed | "כל הנבחנים, לרבות אקסטרניים ונבחני משנה, ייבחנו במכניקה וחשמל באותם השאלונים" (all examinees, externals included, sit the same mechanics and electricity questionnaires) | https://pop.education.gov.il/tchumey_daat/physics/high-school/pedagogy/curriculum/ |
| 35 | physics-bagrut5-from-zero.md:27 | Mechanics 036-361, Electricity 036-371 | confirmed | Each has 6 questions, answer 3. 036371 (track A) may be taken only by those who sat lab 036386. Track B electricity is 036351 with lab 036356. Mechanics + electricity alone can be grouped as 036-300 for 3 units | https://pop.education.gov.il/tchumey_daat/physics/high-school/pedagogy/matriculation-exams/ |
| 36 | physics-bagrut5-from-zero.md:32 | Which lab code an adult external must take | mismatch (gap filled) | Externals and re-takers: **036382** (written inquiry questionnaire) and **036282** (radiation & matter, 5 questions, answer 3). Confirm the exact pairing with אגף הבחינות (the exams department) | same |

### Chemistry (`chemistry-bagrut5-from-zero.md`)

| # | File:line | Claim | Verdict | Correct value / note | Source |
| --- | --- | --- | --- | --- | --- |
| 37 | chemistry-bagrut5-from-zero.md:26 | 5-unit program from תשע"ה, 70% external / 30% internal; named external topics | confirmed | Topics match: bonding & structure, stoichiometry, redox, acids & bases, food chemistry (limited), energetics & dynamics 1 (limited), inquiry lab part 2. 15 weekly hours | https://pop.education.gov.il/tchumey_daat/chemistry/high-school/pedagogy/curriculum/ |
| 38 | chemistry-bagrut5-from-zero.md:27 | Written paper 037381, computerized alternative 037387 | confirmed | Both are 55% (part of the 70%). The paper: 8 MC × 2.5 = 20 pts, an unseen-article question 20 pts, then 3 of 5 open questions × 20. Main code 037580 | https://pop.education.gov.il/tchumey_daat/chemistry/high-school/pedagogy/matriculation-exams/ |
| 39 | chemistry-bagrut5-from-zero.md:13 | The target is the "70% external / 30% internal program, especially the written external questionnaire" | mismatch | For school students, 70% = **037381/037387 written (55%) + 037388/037376 lab (15%)**. **Externals** sit three external papers: **037381 (55%) + 037382 (15%) + 037282 (30%)**, with no internal part | same |
| 40 | chemistry-bagrut5-from-zero.md:99 | Confirm the external/resit codes | mismatch (gap filled) | 037381 + 037382 + 037282 (from summer תשע"ח on); a separate תשפ"ז focusing file exists for externals | same |

### Biology (`biology-bagrut5-from-zero.md`)

| # | File:line | Claim | Verdict | Correct value / note | Source |
| --- | --- | --- | --- | --- | --- |
| 41 | biology-bagrut5-from-zero.md:24 | 3 core topics (human body/homeostasis, cell, ecology); choose 1 of 3 deepening topics; weights 55% theory, 15% lab, 30% research | confirmed | Matches word for word | https://pop.education.gov.il/tchumey_daat/biologya/chativa-elyona/biology-pedagogy/curriculum-specialize/ |
| 42 | biology-bagrut5-from-zero.md:31,91 | Questionnaire numbers not checked | mismatch (gap filled) | Theory paper **43381** ("שאלות וניתוח מחקר מדעי בנושאי הליבה / שאלות בנושאי ההעמקה", core-topic and deepening questions): 4 chapters, 32/35/18/15 pts, 3.5 h (summer 2026 alternate sitting). Practical lab exam **43386** (3 h). Externals' codes are not confirmed | https://meyda.education.gov.il/sheeloney_bagrut/2026/6/HEB/43381.pdf ; https://meyda.education.gov.il/sheeloney_bagrut/2026/6/HEB/43386.pdf |
| 43 | biology-bagrut5-from-zero.md:33 | How much of the 30% research/lab can be done outside school | unverified | The weights are research 30% and lab 15% (separate parts). External rules were not found | same page |

### Computer science (`computer-science-bagrut-from-zero.md`)

| # | File:line | Claim | Verdict | Correct value / note | Source |
| --- | --- | --- | --- | --- | --- |
| 44 | computer-science-bagrut-from-zero.md:24 | 899371 (units 1–2), 899271 (units 4–5), 899373 (unit 3 task, internal), 899372 (externals, written) | confirmed | Structure in force from תשפ"ה | https://pop.education.gov.il/tchumey_daat/computer-science-software-engineering-cyber/high-school/pedagogy-of/high-school-theoretical-path/ |
| 45 | computer-science-bagrut-from-zero.md:24 | Unit 5 is one of: computational models, OOP, algorithms | mismatch | **Four** choices: נושאי ליבה בבינה מלאכותית (AI core topics), מודלים חישוביים, תכנות מונחה עצמים, אלגוריתמים | same |
| 46 | computer-science-bagrut-from-zero.md:24 | Unit 3 options include "machine learning" | mismatch | The option is "מבוא לבינה מלאכותית" (intro to AI). The others listed (databases, computer organization/assembly (1)/(2), cryptography, intro to web programming, quantum computing) and the 60 h + 30 h split are confirmed | same |
| 47 | computer-science-bagrut-from-zero.md:24,44 | For externals the unit 3 task is out of reach, so the road builds only "awareness" | mismatch (content gap) | Externals sit **899372**, whose listed syllabus is **"מבוא לתכנות בסביבת אינטרנט"** (intro to web programming). The 2026 focusing file pairs 899372 with **899282**. An adult road needs stage content for this paper | same ; https://meyda.education.gov.il/files/portal_talmidim/mikud/2026/computers.pdf |

### Civics (`civics-bagrut-from-zero.md`)

| # | File:line | Claim | Verdict | Correct value / note | Source |
| --- | --- | --- | --- | --- | --- |
| 48 | civics-bagrut-from-zero.md:7 | Civics is a 2-unit bagrut | confirmed | The circular refers to teaching "שתי יחידות הלימוד" (the two units); 5 units via הגבר or a final project | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/ezrachut/mafmartashpav.pdf |
| 49 | civics-bagrut-from-zero.md:86 | תשפ"ו: grade 12 old outline 34281 (80%) + performance task 34283 (20%); old outline 70% 34271; new outline 35/35/30 with task 034263; from תשפ"ז no focusing and no eased answer rules | confirmed | All codes and the תשפ"ז rule match | same |
| 50 | civics-bagrut-from-zero.md:87 | Externals sit 34281 (80%) + 34282 (20%, no focusing) | confirmed | "תלמידים אקסטרניים ונבחני משנה נדרשים לגשת לשתי בחינות חיצוניות: 34281 … 34282 (אין מיקוד לבחינה זו)" (externals and re-takers sit two external exams: 34281 … 34282, with no focusing for the second) | same |

### Hebrew lashon (`hebrew-lashon-bagrut-from-zero.md`)

| # | File:line | Claim | Verdict | Correct value / note | Source |
| --- | --- | --- | --- | --- | --- |
| 51 | hebrew-lashon-bagrut-from-zero.md:35 | Four curriculum chapters: forms, vocabulary, syntax, comprehension & expression | confirmed | The 15–20% / 40–50% time split was not re-read (glyph extraction issues) | https://meyda.education.gov.il/files/Curriculum/hebrew-7-12.pdf |
| 52 | hebrew-lashon-bagrut-from-zero.md:36,37 | 11281 regular: 3 h; Part 1 50 pts, Part 2 50 pts; ch. א compulsory, then choose ב (syntax) or ג (forms); 100–200-word writing task worth 25 pts | confirmed | Winter 2026 paper | https://meyda.education.gov.il/sheeloney_bagrut/2026/1/HEB/11281.pdf |
| 53 | hebrew-lashon-bagrut-from-zero.md:38 | Moed 8 (special instructions): 3.5 h; Part 1 44 pts (writing 22); Part 2 56 pts (4 × 14) | confirmed | — | https://meyda.education.gov.il/sheeloney_bagrut/2026/8/HEB/11281.pdf |
| 54 | hebrew-lashon-bagrut-from-zero.md:39 | 11281 = 70% general; 11282 = 30% written; 11283 = school 30% report code; 11271 = lashon-only paper for מיזם הכתיבה (writing-project) schools | confirmed | Plus new-immigrant codes 11284/11274/11272/11273 | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/Ivrit/hozermafmaralyesodi2023_2024.pdf |
| 55 | hebrew-lashon-bagrut-from-zero.md:7,43,160 | Externals sit 11282 instead of the school 30% (marked unverified/TODO) | confirmed | The table row reads "11282 עברית: הבנה, הבעה 30% — נבחני משנה ואקסטרניים" (Hebrew comprehension and expression, 30%, for re-takers and externals). The 11282 content scope is still unread | same |

### Literature (`literature-bagrut-from-zero.md`)

| # | File:line | Claim | Verdict | Correct value / note | Source |
| --- | --- | --- | --- | --- | --- |
| 56 | literature-bagrut-from-zero.md:24,35 | Base program = 2 units, 70% external / 30% school; four genres | confirmed | "תכנית הבסיס - שתי יחידות לימוד … 70% … 30%" (base program, two units, 70% / 30%) | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/sifrut/02sifrutmm2017.pdf |
| 57 | literature-bagrut-from-zero.md:36 | Old outline 70% + 30%; new outline 35% exam + two controlled tasks (35%) + 30%; cluster 1 = short story, novel/novella | confirmed | — | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/sifrut/chozer_mafmar_2026.pdf |
| 58 | literature-bagrut-from-zero.md:7,152 | The questionnaire code for externals is unverified | mismatch (gap filled) | The old-outline 70% paper is **8281** (8284 for new immigrants). The summer 2026 paper: 2.5 h, choose 3 of 4 chapters (33⅓ each), and "לנבחנים אקסטרניים ונבחני משנה: תימסר רשימת יצירות" (externals and re-takers are given a list of works). This supports the planning assumption (line 40) that externals sit the 70% paper | https://meyda.education.gov.il/sheeloney_bagrut/2026/6/HEB/8281.pdf ; circular above |

### History (`history-bagrut-from-zero.md`)

| # | File:line | Claim | Verdict | Correct value / note | Source |
| --- | --- | --- | --- | --- | --- |
| 59 | history-bagrut-from-zero.md:7,82 | "Typically 2–3 units" | mismatch | The core (mandatory) history is **2 units**. The optional מורחב (extension) adds a 3rd unit (022382 externals / 022383 internals) and units 4–5 (022381, choose 2 of 8 topics), for 5 in total | https://pop.education.gov.il/tchumey_daat/historya/chativa-elyona/pedagogia-historia/bhinot-bagrut-halofot-haraha/ |
| 60 | history-bagrut-from-zero.md:25,26,82 | 70% external + 30% school choice; codes unverified | mismatch (gap filled) | Internals: 70% exam + 30% alternative assessment on one of two topics (the Yishuv 1920–1945, or Israel 1977–1995). **Externals: 022261 (70%, partly open-book) + 22262 (30%) as exams**; new immigrants 022264 + 022252. 022281/022282 are the old program (last sat תשפ"א) | same ; https://pop.education.gov.il/tchumey_daat/historya/chativa-elyona/pedagogia-historia/bagrut/ |
| 61 | history-bagrut-from-zero.md:26 | Core themes: antisemitism, WWII, totalitarianism, Holocaust, Yishuv to State | unverified (incomplete) | The 22261 focusing list (2025) also has **nationalism and Zionism to 1920** and **issues in the history of the State of Israel** as major units. Re-check against the תשפ"ז focusing list before building content | https://meyda.education.gov.il/files/portal_talmidim/mikud/2025/history-klali-2025.pdf |

## Notes

- This pass did not cover estimated study hours, finish thresholds or originality notes, because they are product estimates, not facts.
- Several of the 2026 papers (math 35571 moed ב, Hebrew 11281 moed 8, biology 43381 alternate sitting) carry special instructions. When a road sets timers, use the regular-structure values from the MoE subject page, and label any special-sitting variant as such.
- Suggested follow-up (not done here, because it would edit other files): fold the corrections above into each planning file in a separate PR after review.
