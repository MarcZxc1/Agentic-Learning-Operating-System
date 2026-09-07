---
status: active
updated: 2026-01-01
topic: learning-method
priority: execution
review_cycle: weekly
---

# AI Learning Protocol

Use AI without outsourcing your skill. This note is authoritative for how engineering sessions may use agents, copilots, and chat models.

Related: [[IAM]] principles · [[LEARNING_OPERATING_SYSTEM]] capacity · [[LEARNING_LOG]] evidence.

## Why This Exists

CRUD familiarity (e.g. copying an Express or Next.js template) feels like real skill. Auth, authorization, failure handling, debugging, and system design under constraints are a higher layer. Multi-file agents will happily ship those layers for you and leave you **familiar with the syntax, but completely unable to rebuild it from scratch**.

**North star:**

> AI may accelerate research, critique, and boilerplate — but I only ship code I can rewrite from a blank file (or from memory) without it.
>
> If AI wrote it, I still owe the learning. If I cannot rebuild it, it does not count.

## Non-Negotiable Rules

1. **Ownership gate:** Do not mark a learning outcome complete unless you can explain every critical line and rebuild the core path closed-book.
2. **No multi-file agent runs for learning goals.** Agent mode is for shipping patterns you already own, or for system integration after the critical path was hand-built once.
3. **First implementation of a new hard skill is manual.** Docs + types + tests allowed. Paste-generated modules are not.
4. **Stuck protocol:** Work alone ≥20–25 minutes. Then ask one narrow question about *your* approach—do not request a full rewrite.
5. **Review, do not replace:** Prefer AI as reviewer of *your* code over AI as author of the feature.
6. **Retype the core.** Accepting a large patch without retyping the critical 30–50 lines teaches almost nothing.
7. **Closed-book redo within 48–72 hours** for any new hard path (auth middleware, session store, password hash flow, state machine, etc.). Time it. Log it.
8. **Agent skill/tuning is not study.** Expanding prompts, skills, and agent configs does not count as coding practice unless it produces a tested artifact *you* can defend.
9. **Portfolio honesty:** Never claim fluency in a subsystem you cannot reimplement or walk through line by line.
10. **Count only evidence.** Videos, agent transcripts, and green demos without closed-book proof do not count as completion in [[LEARNING_LOG]].

## When AI Is Allowed vs Banned

| Stage | AI allowed? | You must do |
|---|---|---|
| Clarify problem / threat model / requirements | Yes — questions only | Write the goal, non-goals, and acceptance criteria yourself |
| Design (steps, data, trust boundaries) | Yes — critique your design | Produce a short design note or checklist first |
| First implementation of a new hard skill | **No** for the feature files | Blank file(s); official docs; existing project patterns |
| Stuck >20–25 min | Hint / Socratic only | One question: “What is wrong with *this* approach?” Show your code |
| Tests for *your* code | Yes for edge-case ideas; you write tests | Tests must match real risks (authz, expiry, boundary validation) |
| Review | Yes | AI reviews your PR; you decide; no silent multi-file rewrite |
| Boilerplate you already own (e.g. data model you could write cold) | Yes, sparingly | You still read and can recreate it |
| Refactor after green tests you understand | Yes, with diff review | You must explain every behavioral change |
| Merge / demo / portfolio claim | No AI merge of unread code | Closed-book explanation ready |

### Explicit bans during learning blocks

- “Implement full authentication / OAuth / RBAC for me”
- Auto-fixing until green without reading and explaining test failures
- Accepting multi-file agent PRs for skills you are trying to learn
- Regenerating an entire module when one function has a bug

### Explicit good uses

- “Quiz me on cookie flags vs JWT tradeoffs”
- “Attack this middleware; list edge cases and failure modes I missed”
- “Where does the official documentation explain transaction rollbacks?”
- “Diff my design against OWASP session guidance — do not rewrite my code”
- “I got error X; here is my stack and hypothesis — what should I inspect next?”

## Ownership Gates (Definition of Done)

A skill counts as **owned** only when all of the following are true:

- [ ] You wrote the first working version (or a deliberate rewrite) without agent authorship
- [ ] Happy path + at least three failure cases are tested or manually verified with notes
- [ ] You can explain trust boundaries: who is authenticated, what is authorized, what is secret
- [ ] Closed-book redo: blank file or fresh branch, core path rebuilt within a time box
- [ ] You can answer: what breaks under network failure, expired token, missing validation, or concurrent writes?

If any box fails, the feature may still exist in the repository as a **demo**, but it is not **learning complete**.

### Do not confuse correctness with ownership

For DSA and problem-solving, report three separate judgments:
1. **Algorithm** (`pass/fail`)
2. **Interview explanation** (`pass/minor repair/fail`)
3. **Ownership** (`owned/reviewed/demo`)

For project work, similarly distinguish working code from interview-ready explanation and independent ownership. `Not owned` never means `nothing was learned` or `the working solution failed`; it means further independent closed-book proof is still due.

## Session Modes

Choose a mode before each block. Write it in [[TODAY]] or the log row.

### Mode A — Skill acquisition (default for leveling)

- Goal: own a hard path (e.g. session auth, custom hook, database transaction)
- AI: research and review only; no implementation authorship
- End: working code + tests/notes + next redo date

### Mode B — Project / team shipping

- Goal: integrate, review, unblock, deliver
- AI: allowed for glue, docs, tests, and patterns **you already own**
- New hard paths that only you will defend later still need a Mode A pass once
- Leadership artifacts still follow disciplined engineering templates

### Mode C — Interview / closed-book drill

- Goal: rebuild or solve without tools or external help
- Before the timer, complete [[LEARNING_OPERATING_SYSTEM#Written-output preflight — required every time]] and confirm that every required term and format is understood.
- AI: off until the timer ends
- DSA: ≥15 minutes thinking before any hint ([[DSA_INTERVIEW_PREP]], [[LEARNING_OPERATING_SYSTEM]])

### Mode D — Agent-assisted speed (use rarely)

- Goal: ship something you could already build cold
- AI: full assist allowed
- Tax: 15–30 min closed-book summary or redo of the critical path the same day or next day
- If you cannot summarize, it was Mode A work in disguise — redo properly

## Stuck Protocol (20–25 minutes)

1. Restate the expected vs actual behavior in one sentence.
2. Reproduce with the smallest request or test.
3. Read the error and one layer of stack trace; form a hypothesis.
4. Change **one** variable (header, cookie, query param, middleware order).
5. Write what you tried in a note or comment.
6. Only then ask AI a **narrow** question with your code and hypothesis.
7. If AI suggests a fix, implement the **smallest** diff yourself first.

## Closed-Book Redo Protocol

After first success on a hard skill:

| When | What | Pass bar |
|---|---|---|
| Same day (optional) | Explain the flow out loud or in markdown without looking | No blank gaps on order of operations |
| +48–72 hours | Rebuild core path from empty file / empty route module | Working feature; you did not paste agent code |
| +7–14 days | Spot quiz: tradeoffs, failure modes, one modification | Can answer without opening the repository first |

Log the redo in [[LEARNING_LOG]] with category and artifact path.

## Example Priority Skills Progression (Auth & Core Systems)

| Order | Skill | Ownership proof |
|---|---|---|
| 1 | Password hashing + register/login | Cold rebuild of hash + verify |
| 2 | Sessions **or** JWT access+refresh (one path fully) | Middleware + logout + `/me` |
| 3 | Authorization (IDOR-safe resource access) | User A cannot read User B's row |
| 4 | Auth failure tests | Wrong password, expired/missing session, unauthorized |
| 5 | Secrets and env discipline | No secrets in git; clear config story |
| 6 | Then: email verify / OAuth / RBAC | Only after 1–5 are owned |

Apply the same protocol to other subsystems (payments, background jobs, websockets, query optimization).

## Anti-Addiction Controls

Agent tuning and multi-agent workflows feel productive because demos go green fast. Real learning feels slower and has friction.

| Control | Practice |
|---|---|
| Cap | At most one Mode D block per day unless an emergency requires it |
| Order | 50 minutes manual before any agent implementation help |
| Urge redirect | 15-minute blank-file rewrite of the core function from memory |
| Metric | Closed-book redo time and failure-case tests — not “features agent shipped” |
| Weekly ask | What did I rebuild without AI? If nothing, rescope next week |

## How to Log AI-Aware Sessions

In [[LEARNING_LOG]], prefer honesty:

| Field | Guidance |
|---|---|
| Intended outcome | e.g. “Own cookie session login without agent authorship” |
| Artifact | Path to routes/middleware/tests you wrote |
| Result | Separate working result, explanation quality, and ownership. Use `owned` only if ownership gates pass. |
| Notes (in result or next action) | Mode A/B/C/D; whether redo is scheduled |

Example result text: `Mode A; login works; redo scheduled 2026-07-19; AI used only for cookie flag quiz.`

## Interview and Reality Check

Engineering interviewers and tech leads filter candidates with:
- line-by-line walkthrough of *your* repository
- “change X — what breaks?”
- live coding without copilots or autocomplete
- blank-board design of data models, trust boundaries, and APIs

This protocol optimizes for **those** checks, not for the fastest green CI from an agent.

## One-Line Summary

**If AI wrote it, I still owe the learning. If I cannot rebuild it, it does not count.**
