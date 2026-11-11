# Physics 5-unit bagrut from zero — road outline

**status: planning**

> Docs-only outline. Not learner path JSON. Do not place any `.json` under `planning/`.

## 1. Learner, start, target

| Field | Definition |
|-------|------------|
| Learner | Adult (MyRoad v1 audience): Hebrew/English/Arabic UI later; content samples in English with Hebrew labels where useful |
| Start | Near zero physics: can do arithmetic and basic algebra (fractions, linear equations); no assumed high-school physics |
| Target | Israel MoE **Physics 5 יח"ל** bagrut readiness for the written external exams in **Mechanics** and **Electricity & Magnetism**, plus awareness of the remaining 5-unit components (radiation & matter; lab / investigative alternative) |
| Content originality | Sample sentences and vignettes in this doc are **original**. Do not copy exam items. Future practice items must be original or clearly licensed. |

Hebrew glossary (approved MyRoad terms): מקצוע → סדרה → דרך → שלב → משבצת.

Proposed path family (future JSON, not here): `physics_bagrut5` series of roads or one long road with stages.

## 2. Verified public sources

Checked with `curl` (HTTP 200) on 2026-11-06 (Asia/Jerusalem):

| Source | URL | What we take from it |
|--------|-----|----------------------|
| MoE pedagogical space — Physics curriculum | https://pop.education.gov.il/tchumey_daat/physics/high-school/pedagogy/curriculum/ | 5 יח"ל “meaningful learning” program from תשע"ה: topics **מכניקה**, **חשמל ומגנטיות**, **קרינה וחומר**, plus lab assessment; all examinees take Mechanics and Electricity on the same questionnaires |
| MoE — Bagrut exams (Physics) | https://pop.education.gov.il/tchumey_daat/physics/high-school/pedagogy/matriculation-exams/ | Written questionnaires include Mechanics **036-361** and Electricity **036-371**; answer rules (e.g. choose among questions); lab oral/written questionnaire codes; 5-unit structure also includes lab and radiation/matter or “Physics through an investigative approach” alternatives |
| MoE free prep courses (Mechanics & Electricity) | https://pop.education.gov.il/sherutey-tiksuv-bachinuch/students-online-courses/preparatory-courses-matriculation/physics/ | Confirms focus of free MoE prep on Mechanics and Electricity chapters for 5 יח"ל |

**Not invented:** exact hour allocations, formula sheets, and full topic tables live in MoE PDF curriculum packs linked from the curriculum page. Those PDFs were **not** fully downloaded/parsed in this planning pass. Treat fine-grained topic lists below as a **pedagogical scaffold aligned to the three named MoE content blocks**, to be reconciled against the official full curriculum PDF before any content JSON is authored.

**Unverified / deferred:** precise recommended classroom hours per subtopic; exact weighting of lab vs written in every examinee population. **Adult externals/re-takers (gap filled):** **036382** (written inquiry questionnaire) + **036282** (radiation & matter, 5 questions, answer 3) ([source](https://pop.education.gov.il/tchumey_daat/physics/high-school/pedagogy/matriculation-exams/)); confirm the exact pairing with אגף הבחינות. Mark as **schema/product decision + MoE PDF check** before shipping.

## 3. Stages (שלבים)

Each stage has a goal, a target capability level, and an **estimated** study hours band (estimate only — not MoE figures).

Level concept (MyRoad product): **3 levels per stage** — Level 1 recall/apply basic, Level 2 multi-step / mixed representations, Level 3 exam-like synthesis and error spotting. Difficulty rises after sufficient progress; more of the same topic is practiced at higher level (not a different subject).

| Stage | Hebrew label | Goal | Target level (end of stage) | Est. hours (unverified estimate) |
|-------|--------------|------|-----------------------------|----------------------------------|
| 0 | הצבה / כלים | Placement + math/physics language tools | Place into Stage 1 or skip light review | 2–4 |
| 1 | תנועה בקו ישר | 1D kinematics fluency | L2 on core tiles; L1 on extensions | 12–20 |
| 2 | כוחות וניוטון | Forces & Newton’s laws | L2–L3 simple systems | 16–28 |
| 3 | אנרגיה ותנע | Energy & momentum conservation | L2 multi-step; L3 intro | 14–24 |
| 4 | תנועה במרחב / מעגלית | 2D / circular / projectile patterns | L2 | 12–20 |
| 5 | חשמל סטטי וזרם | Electrostatics + DC circuits | L2 | 16–28 |
| 6 | מגנטיות והשראה | Magnetism & induction (exam-relevant core) | L2 | 12–22 |
| 7 | קרינה וחומר (סקירה) | Radiation & matter overview for 5-unit awareness | L1–L2 conceptual | 8–16 |
| 8 | מעבדה וחקר (מודעות) | Lab skills / investigative mindset (not a fake lab cert) | Checklists + reasoning tiles | 6–12 |
| 9 | סימולציית בגרות | Mixed Mechanics + Electricity exam sims | L3 under time | 10–18 |

**Finish criteria (road):** learner completes Stage 9 end-check at threshold (see §5) on both Mechanics-style and Electricity-style mixed sets; Stage 7–8 awareness checks passed at L1+. This is a **learning readiness** goal, not a guarantee of MoE bagrut grade.

## 4. Topics / tiles (משבצות) per stage

Tile kinds (aligned with existing MyRoad nodes):

- `learn` / **understanding** — one-time concept tile
- `practice` / **review** — returns with spacing
- `check` — stage end-check
- Optional later: worked method, can-do, listen/record modes (product already supports multiple practice modes; physics will need equation + diagram heavy UX — see schema gaps)

### Stage 0 — Tools
- Units & SI; significant figures (light)
- Graph reading: position/time, velocity/time
- Vector idea (magnitude/direction) without full 2D yet
- Algebra refresh: isolate variable; proportions
- Sample original vignette: “A delivery cart rolls 12 m east in 4 s at constant speed. What is its average velocity?”

### Stage 1 — 1D kinematics
- Displacement vs distance; average vs instantaneous speed/velocity
- Constant acceleration equations (use MoE-allowed formula sheet later; do not invent which formulas appear)
- Graphs ↔ motion stories
- Sample: “Maya’s e-bike speeds up from 2 m/s to 8 m/s in 3 s. Find average acceleration.”

### Stage 2 — Forces & Newton
- Free-body diagrams; net force
- Newton 1–3; weight vs mass; friction (static/kinetic qualitative → quantitative)
- Inclined plane (basic)
- Sample: “A crate on a flat floor is pulled with 40 N; friction is 15 N. Describe the acceleration qualitatively, then compute if mass is given in the item.”

### Stage 3 — Energy & momentum
- Work; kinetic & potential; conservation when appropriate
- Impulse & momentum; collisions (elastic vs inelastic at conceptual + basic calc level)
- Sample: “A 0.2 kg ball falls 5 m (ignore air). Compare kinetic energy at bottom with mgh at top — explain.”

### Stage 4 — 2D / circular / projectile
- Projectile components; range/time qualitative first
- Uniform circular motion: centripetal acceleration idea
- Sample: “A stone is thrown horizontally from a 20 m cliff at 5 m/s. Which quantity is zero just after release: horizontal accel or vertical velocity?”

### Stage 5 — Electrostatics & DC
- Charge, Coulomb qualitative → Coulomb law when curriculum requires
- Field / potential concepts at curriculum depth (reconcile with MoE PDF)
- Current, resistance, Ohm; series/parallel; power
- Sample: “Two identical resistors in series vs parallel across the same battery — which setup draws more current from the battery?”

### Stage 6 — Magnetism & induction
- Magnetic force on moving charge / wire (direction rules as taught in MoE materials)
- Flux & induction qualitative; simple quantitative where curriculum requires
- Sample: “A loop’s area shrinks in a constant magnetic field perpendicular to the loop. Does induced emf appear? Why?”

### Stage 7 — Radiation & matter (overview)
- Waves / light models historically (curriculum names particle/wave ideas)
- Photoelectric / atomic / nuclear topics **only as listed in official curriculum** — expand after PDF reconciliation
- Sample conceptual: “Name one observation that pushed physicists beyond a purely classical wave model of light.” (Keep non-exam-copy.)

### Stage 8 — Lab / investigative awareness
- Variables, controls, uncertainty qualitative
- Reading a simple experiment write-up; graph of measured data
- Note: MyRoad cannot replace MoE lab exam logistics; this stage builds transferable lab reasoning.

### Stage 9 — Exam simulation
- Mixed Mechanics sets styled like multi-part bagrut questions (original)
- Mixed Electricity sets
- Timed sections; error-log review
- Answer-choice strategy only as secondary skill (reasoning first)

## 5. Finish criteria per stage

- **End-check threshold (proposal):** ≥80% correct on stage check set at the stage’s target level, with **no review topic stuck at level 0**.
- Understanding tiles: completed once with comprehension micro-check.
- Review tiles: must reach the stage’s minimum level (usually L1 before leaving; L2 for core exam stages 1–6).
- Stage 9: two separate mixed checks (Mechanics-heavy, Electricity-heavy) both ≥ threshold under timebox (timebox value TBD; do not invent MoE exam duration here without citing MoE questionnaire instructions).

## 6. Level-up rules (3 levels / stage)

| Level | Meaning | Up when | Down when |
|-------|---------|---------|-----------|
| L1 | Correct on single-idea items; can state the idea | 3 consecutive successful practices on tile family **or** spaced successes per product SRS | 2 consecutive fails, or long dormancy reset policy (product default) |
| L2 | Multi-step / graph+equation / two-representation | Same with harder item pool | Fail streak on L2 pool |
| L3 | Exam-like synthesis, distractors, explain-a-mistake | Sustained L2 + L3 check | Fail L3 check → stay/drop to L2 practice |

Spacing intervals: reuse MyRoad product defaults (do not hardcode days here until product owner confirms). Physics-specific: prefer mixing symbolic and numeric forms so level-up is not pure memorization.

## 7. Metrics (road screen + metrics screen)

Aligned with Eliot’s MyRoad decisions (weekly progress vs goal on road; goals met/not on metrics):

| Metric | Formula (proposal) | Events needed |
|--------|--------------------|---------------|
| Weekly progress vs goal | `minutes_practiced_week / weekly_goal_minutes` and/or `tiles_leveled_up_week / weekly_tile_goal` | `session_start`, `session_end`, `tile_complete`, `level_change` |
| Stage mastery | fraction of stage tiles at ≥ target level | `tile_level` |
| Accuracy by topic | correct / attempted per topic tag | `answer_submit` with topic_id, correctness, latency |
| Exam-sim readiness | Stage 9 check scores over last N attempts | `check_attempt` |
| Goal met flag | weekly goals boolean | derived |

No fake baselines. Until real answers exist, UI shows empty/honest zeros.

## 8. Schema gaps (hand to format owner — do not change format here)

1. **Equation / symbolic answer** type beyond MC and short text — physics needs structured numeric+unit and multi-part answers.
2. **Diagram / FBD** interaction (upload sketch vs tap-to-place vectors) — not in current English-path node shapes.
3. **Formula-sheet mode** (show allowed formulas during practice vs hide) — flag on node or session.
4. **Multi-part bagrut-style item** grouping (part א/ב/ג) with shared stem.
5. **Lab checklist** node kind (non-scored awareness) vs scored check.
6. **Level field** on topics/nodes: content today often lacks an explicit level field; road UI uses automatic 3-way split — physics outline assumes explicit levels eventually.
7. **Unit-aware numeric grading** (tolerance, sig figs) — may need generator + grader support.
8. Subject tag `physics` and group ids for bagrut5 series — confirm naming with content publish pipeline.

## 9. Sample original micro-items (not for JSON yet)

1. “A tram moves at constant 8 m/s for 15 s. How far does it travel?”
2. “If net force on a 3 kg package is zero, what is its acceleration?”
3. “Two lamps in parallel; one burns out (open). What happens to current in the other (ideal battery)?”
4. “A charged particle moves parallel to a uniform magnetic field. Is the magnetic force zero or nonzero? Explain in one sentence.”

## 10. Next steps (when leaving planning)

1. Download/reconcile MoE full 5 יח"ל curriculum PDF topic tables and formula lists.
2. Decide one long path vs series (`path_physics_bagrut5_01_…`).
3. Resolve schema gaps with platform format owner.
4. Author content JSON under `adult/` (never under `planning/`).
