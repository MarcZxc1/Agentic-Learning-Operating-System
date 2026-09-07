---
status: active
updated: 2026-01-01
priority: execution
review_cycle: weekly
---

# Learning Operating System

Use this system to turn your learning vault into completed, demonstrable engineering work. Hours are capacity limits, not targets to inflate.

## Non-Negotiable Rules

1. Choose one **must-win outcome** per day. It must produce an artifact, decision, test, or explained solution.
2. Keep one major task in progress. Finish, block, delegate, or deliberately stop it before starting another.
3. Reserve the explicit buffer shown for the tier and take 10–15 minute breaks between major blocks. Focused totals exclude buffers and breaks.
4. Use a timer. Stop when the block ends, record the next action, and reassess instead of silently extending the day.
5. Do not repay missed sessions with a late-night marathon. Move the highest-value unfinished outcome to the next realistic slot.
6. Track completed outcomes and actual time. Do not count videos watched, pages opened, copied solutions, or **agent-authored features you cannot rebuild** as completion. Follow [[AI_LEARNING_PROTOCOL]].
7. Protect sleep, coursework/work commitments, health, and project deadlines. Reduce the plan before reducing recovery.
8. For skill-acquisition blocks, choose a session mode (A/B/C/D) from [[AI_LEARNING_PROTOCOL]] before starting; default to Mode A when leveling a weak path (e.g. auth).
9. Do not add or expand a lesson unless [[AGENTS#New Lesson Gate — Default Freeze]] is satisfied. Search existing coverage first; curiosity goes to deferred/reference, not today's plan.

## Choose the Day's Capacity Once

Choose one tier before starting. Do not upgrade the tier late in the day to “catch up.”

| Tier | Focused total | Minimum practical window | Use when |
|---|---:|---:|---|
| Full-capacity | 4.5–5 hours | About 5h45–6h15 elapsed | The window genuinely exists after work, sleep, meals, commute, and responsibilities |
| Standard | 3 hours | About 3h15 elapsed | A normal work/study day with one protected buffer |
| Busy-day fallback | 1 hour 45 min | About 2h elapsed | High external pressure, deadlines, travel, illness, or unusually low energy |

## Full-Capacity Day (Neuro-Optimized)

Follow a rhythm that alternates high cognitive load (Deep Work) with recovery (Diffuse Mode).

**Morning: Prime & Reset**
- **Off-Screen Hobby:** Start the day with 20-30 mins of physical or tactile movement away from screens to clear brain fog.

**Session 1: High Cognitive Load (Deep Work)**
- **Block:** DSA and Algorithm Fundamentals (60–90 min). One problem explained, tested, and derived from memory.
- **Diffuse Break:** 15–20 minutes completely away from the screen.

**Session 2: Application & Building**
- **Block:** Flagship / Capstone project architecture or implementation (90 min cap). One bounded artifact or vertical-slice increment.
- **Long Break / Mid-Day Reset:** 45–60 minutes for lunch, walking, or a non-tech reset.

**Session 3: Practice & Polish**
- **Block:** DevOps, testing, deployment, or database (60 min). One reliability improvement.
- **Block:** Engineering communication and documentation (30 min). One ADR, task brief, review, or postmortem.

**Evening: Recovery**
- **Hard Stop:** Close the laptop. Engage in physical exercise or socialize to flush stress hormones.
- *Rule: Never work more than 90 minutes without leaving the screen.*

## Standard Day (Neuro-Optimized)

- **Morning Prime:** 15 min physical movement/reset before opening the laptop.
- **Session 1 (Deep Work):** 60 minutes: DSA and core syntax. Followed by a 15 min diffuse break.
- **Session 2 (Application):** 75 minutes: Flagship project architecture or backend feature. Followed by a 30 min mid-day reset.
- **Session 3 (Polish):** 30 minutes: DevOps/testing + 15 minutes: architecture docs + 15 minutes: buffer.
- **Hard Stop:** Total of 180 focused minutes. Disconnect fully.

## Busy-Day Fallback (Neuro-Optimized)

When work, classes, or deadlines reduce capacity, use this to preserve momentum without catch-up debt:

- **Morning Anchor (Before the day unfolds):** 30 minutes: Core syntax / DSA retrieval practice or one partial problem with a written next step.
- **Diffuse Mode (During the day):** Let background architectural problems simmer subconsciously while away from the laptop.
- **Evening Push (After recovery):** Take a mandatory 30 min screen-free reset upon returning home. Then, execute 60 minutes: the flagship project must-win outcome + 15 minutes: update tasks/risks for tomorrow.

## Daily Plan Lock

`[[TODAY]]` is the single source of truth for today's learning plan.

1. On the first planning request of a new date, ask the user for their capacity tier (Full, Standard, or Busy) before writing the plan. Once the user replies, choose the capacity tier once and initialize the day's plan.
2. Select one must-win outcome and make every non-DSA block support that outcome where practical.
3. Set `plan_status: locked` before presenting the plan.
4. When asked again on the same date, repeat the remaining locked plan; do not generate a different lesson.
5. Mark a block complete only from the learner's report or linked evidence. Record exact minutes only when known.
6. Change the locked plan only for a recorded blocker, new deadline or capacity constraint, completed work, or an explicit request to replan. Record the reason and keep completed entries.
7. Select replacements in this order: unfinished weekly outcome, current flagship milestone, highest-priority Core prerequisite, then current DSA mastery gate for the DSA block.

## Session Protocol

### Before

- Write one sentence: “By the end of this block, I will have ___.”
- Name the [[AI_LEARNING_PROTOCOL]] session mode (A skill / B project ship / C closed-book / D agent speed).
- Confirm the block appears in [[TODAY]] and uses the [[Dashboard#Daily Active Surface]]. Do not browse the full vault for a more interesting substitute.
- Start focus timer: execute `studyctl session start --minutes <minutes> --json` (or your preferred local timer). Confirm the timer is running before beginning.
- Open only the files and references required for that outcome.
- Put unrelated ideas in a parking-lot note; do not switch tasks.

#### Written-output preflight — required every time

Whenever a block asks the learner to write code, a trace, explanation, ADR, task brief, test plan, review, or other artifact, the coach must display the required format **before the timer starts**. Do not make the learner infer the expected structure from unfamiliar labels.

The preflight must:

1. name every required field or section;
2. define each field in plain language;
3. show a blank template or checklist that makes the expected form visible;
4. state the acceptance checks and artifact path;
5. use an unrelated example when a term is unfamiliar, without filling in the current task's answer; and
6. ask the learner to confirm that the format and terms are understood before starting Mode C.

Use this generic frame when a more specific canonical template is unavailable:

```text
Outcome:
Artifact/path:

Required sections:
- Field:
  - Meaning:
  - Expected format:

Acceptance checks:
- ...

Evidence to report afterward:
- Actual duration:
- Artifact:
- Result or blocker:
- Exact next action:
```

Freeze this acceptance format before the timer. Do not introduce hidden requirements during review. If a required term or format is unfamiliar, teach it in Mode A first; a fresh Mode C attempt may begin only after the learner understands the format and closes the teaching material. For DSA, display the complete format in [[DSA_INTERVIEW_PREP#Required DSA Written Format — Show Before Every Problem]] while the foundation gate is active; after it is green, use that note's compact interview preflight.

**Preflight fade rule (all block types):** When the learner has completed 10 or more sessions of the same artifact type (e.g. project ADRs, task briefs, DSA lessons) without a format misunderstanding, the coach may replace the full preflight with a compact one-line reminder of the artifact path and acceptance checks. Restore the full preflight only when the learner's output shows a recurring format gap or when a new field is introduced. The purpose is to reduce ceremony as habits mature, not to skip accountability.

### During

- Work for 25/5 or 50/10 intervals.
- If blocked for 20–25 minutes, write the evidence, attempt one smaller reproduction, then ask a narrow question—or delegate with context on team work. Do not request a full agent rewrite of a skill you are trying to own.
- For DSA, spend at least 15 minutes reasoning before viewing a hint. Rebuild the final solution without copying.
- In Mode A, no multi-file agent implementation; AI is research/review only.

### After

- Complete focus timer: execute `studyctl session finish --reflection "<reflection>" --json` (or stop your local timer). Use verified actual minutes for [[LEARNING_LOG]] and [[TODAY]].
- Record actual minutes, artifact link, result, blocker, and exact next action in [[LEARNING_LOG]].
- Note mode and whether the outcome is `owned` vs `demo only` per [[AI_LEARNING_PROTOCOL]].
- Schedule a closed-book redo (+48–72h) when a new hard path first went green.
- Never estimate or invent elapsed time. Mark an uncertain entry for confirmation.
- Mark the outcome complete only when its stated definition of done is satisfied **and** ownership gates pass for learning claims.

## Weekly Planning

- Limit the week to three outcomes: one flagship project milestone, one delivery/reliability improvement, and one learning/interview outcome.
- Check actual time against your target allocation (e.g. 35/25/20/15/5). Correct large drift next week; do not micromanage every day to exact percentages.
- Remove or defer work before adding a fourth outcome.
- Review what shipped, what failed, what was delegated, and what evidence changed the plan.
- Reserve one half-day with no planned technical work.

## Stop Conditions

Stop and rescope when:

- the task has no acceptance criteria or owner;
- the work does not support the flagship project, core curriculum, or a verified target-role need;
- a new tool is being introduced without solving a measured limitation;
- fatigue causes repeated mistakes or copying without understanding;
- the planned block is over and continuing would compromise the next commitment.

## Evidence Cadence (Close the Plan–Proof Gap)

Strong lesson notes are not portfolio evidence. Use this minimum cadence so the vault does not outrun your actual proof:

| Cadence | Required evidence |
|---|---|
| Every focused block | One [[LEARNING_LOG]] row with artifact link (or explicit blocker + next action) |
| Every week | One integrated project demo **or** evidence-backed blocker; one reliability/test/migration improvement |
| Every two weeks | At least one of: reviewed PR, ADR, task brief, risk-register update, contribution-log update |
| Every ML / Core milestone | Baseline under a clear split, comparison table, and model card / spec |
| Every month | Answer [[IAM#Monthly Check]]; drop work that produced no artifact |

If the week produced only reading and no file, PR, diagram, test, or decision note, the week does not count as engineering progress—rescope next week’s three outcomes.

## Monthly Evidence Check

Use the questions in [[IAM#Monthly Check]] and complete [[LEARNING_LOG#Monthly Evidence Reviews]]. Archive or downgrade activities that consume time without producing real evidence.

The monthly review must also answer:

- What integrated outcome shipped, and where is the evidence?
- Which concept moved from recognition to applied or owned through closed-book evidence?
- What produced reading or organization but no artifact?
- What will be removed, consolidated, delegated, or downgraded next month?
- Was any lesson added? If yes, link the demonstrated need and all four fields required by [[AGENTS#New Lesson Gate — Default Freeze]]; otherwise record `none`.
