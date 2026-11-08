# Computer Science bagrut from zero — road outline

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.

## 1. Learner, start, target

| Field | Definition |
|-------|------------|
| Learner | Adult (MyRoad v1 audience) with no formal programming course. Basic math and logic assumed. |
| Start | Near zero: can use a computer; no assumed language, IDE, or data-structure knowledge. |
| Target | Readiness for the MoE **theoretical-path Computer Science** bagrut, commonly taken as **5 יח"ל**: written papers for units 1–2 and 4–5. Unit 3 is a school performance task; this road can only build transferable project-thinking, not submit that task. |
| Content originality | Sample items are **original**. Do not copy exam questions or official exercise sheets. |

Proposed future path family (JSON later, never here): `cs_bagrut5`.

## 2. Verified public sources

Checked with `curl -I -L` (HTTP 200) on 2026-11-08 (Asia/Jerusalem):

| Source | URL | What we take from it |
|--------|-----|----------------------|
| MoE theoretical path (high school) | https://pop.education.gov.il/tchumey_daat/computer-science-software-engineering-cyber/high-school/pedagogy-of/high-school-theoretical-path/ | Written exams: **899371** (units 1–2) and **899271** (units 4–5). Internal performance task **899373** (unit 3) for school examinees. Externals/resits: **899372** (written). The page links a syllabus for units **1, 2, and 4**. **Unit 5** is a choice of **one** theoretical alternative, examined together with the other theoretical material on 899271: **computational models**, **object-oriented programming**, or **algorithms**. Unit 3 (performance task) teaches an additional domain (~60 hours) plus a project (~30 hours); listed domain options include databases and information systems; computer organization / assembly (two school-chosen variants); cryptography; intro to internet programming; machine learning; quantum computing. |
| MoE free prep courses | https://pop.education.gov.il/sherutey-tiksuv-bachinuch/students-online-courses/preparatory-courses-matriculation/computer-science/ | Free 5 יח"ל prep. The public course list describes foundations and data-structures practice in **C#** (variables, control flow, arrays, OOP, recursion, queue, stack, linked list, binary tree, complexity). Language of instruction for a future MyRoad path must follow the **current official materials**, not this outline’s preference. |
| תשפ"ו focusing PDF (mikud) | https://meyda.education.gov.il/files/portal_talmidim/mikud/2026/computers.pdf | Year-specific include/exclude checkmarks for questionnaires including 899271 and 899371 (and external/resit codes). This is **focusing for 2026**, not the full standing syllabus. Recheck before authoring JSON; do not treat an “X” as “the topic does not exist in the curriculum.” |

**Correction vs an earlier draft:** databases, cryptography, intro to internet programming, machine learning, and quantum computing are **unit 3 performance-task domain options**, not unit 5 exam choices. Unit 5 choices are computational models / OOP / algorithms.

Software-engineering and cyber tracks exist on the same pedagogical space and are larger; this outline stays on the **theoretical path**.

**Unverified / deferred:** the full official PDF syllabus for every unit (linked from the theoretical-path page, not fully parsed here); which unit 5 alternative an independent adult should pick first; whether C# or Java (or another language named in a specific unit booklet) is required in a given year.

## 3. Stages (שלבים)

Hours are **unverified estimates**. 3 levels per stage.

| Stage | Hebrew label | Goal | Target level | Est. hours (estimate) |
|-------|--------------|------|--------------|----------------------|
| 0 | הצבה | Placement: tracing vs writing vs jargon | Place into Stage 1 | 2–4 |
| 1 | יסודות תכנות (יחידות 1–2) | Variables, conditionals, loops, functions, strings, 1-D arrays; OOP basics as required for units 1–2 | L2 | 50–80 |
| 2 | מבני נתונים (יחידה 4) | Recursion, complexity intro, queue, stack, linked list, binary trees — include a topic only if it is in the standing units 1/2/4 syllabus, then apply that year’s mikud when building items | L2–L3 | 40–70 |
| 3 | יחידה 5 (בחירה) | One official unit 5 alternative: computational models **or** OOP (deeper) **or** algorithms. Default planning recommendation: pick the alternative whose public materials are thickest at build time; do not invent a fourth option. | L2–L3 | 30–50 |
| 4 | מטלת ביצוע (מודעות) | What a unit 3 project demands (scope, testing, write-up). Not a substitute for questionnaire 899373. | Awareness + checklists | 8–16 |
| 5 | סימולציית בגרות | Timed items in the style of 899371 and 899271 (original) | L3 under time | 30–50 |

**Total estimate:** about 160–270 hours. Estimates only.

## 4. Topics / tiles (משבצות)

Understanding then practice/review for: control flow and functions; arrays and strings; tracing code; writing short programs; recursion and complexity ideas; OOP basics (and deeper OOP only if that is the chosen unit 5); queue, stack, linked list, binary tree as listed in the official unit 4 materials; the chosen unit 5 alternative; project-thinking awareness for unit 3.

Do not treat “intro to AI” as a unit 5 exam topic. Machine learning appears on the official page as a **unit 3 domain option**.

## 5. Finish criteria

- Trace and write correct short programs for standard problems at units 1–2 depth.
- Explain the time-complexity idea of a simple algorithm in the learner’s own words.
- Answer multi-part theoretical questions covering units 1–2 and 4–5 (chosen alternative).
- End-check proposal: ≥80% at the stage’s target level; no review topic stuck at level 0.

## 6. Level-up and spacing

L1 read/trace code; L2 modify or write a small program; L3 design a solution and analyze it. Space weak constructs on the product’s default schedule.

## 7. Metrics

Same event family as other planning roads (`tile_complete`, `level_change`, `answer_submit`, `check_attempt`, session timing). Extra useful tag: `code_trace` vs `code_write` so later analytics can separate reading from writing. Honest zeros until real answers exist.

## 8. Schema gaps

1. A first-class **code** item type (trace output, fill-in, write-a-function) with hidden tests — may exceed current English-path node shapes.
2. Language/runtime choice (C# vs Java vs another official language) — product + content decision, not a schema invention to hide in planning JSON.
3. How unit 5 choice is stored (one path vs a fork).
4. Unit 3 project workflow vs scored tiles.
5. Subject tag `computer_science` and series ids.
6. Parse the official units 1/2/4 syllabus PDF and the current mikud before JSON.

## 9. Original sample items (not for JSON yet)

1. Write a short function that returns the sum of all even numbers in a 1-D array.
2. Explain in one sentence why binary search is faster than linear search on a sorted list, and name one case where binary search is the wrong tool.
3. Trace the output of a simple recursive function that counts down from 5 (the item will include original code; do not reuse an official worksheet).

## 10. Next steps (when leaving planning)

1. Parse the official units 1/2/4 syllabus PDF from the theoretical-path page.
2. Recheck the current year’s mikud PDF before writing items.
3. Choose a first unit 5 alternative based on the thickest official materials.
4. Confirm the programming language against those materials.
5. Author JSON under `adult/` (never under `planning/`).
