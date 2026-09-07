---
status: active
updated: 2026-01-01
topic: roadmap
difficulty: medium
priority: execution
---

# Core Skills Schedule: Project-First Integration

Follow [[LEARNING_OPERATING_SYSTEM]] for daily capacity, [[AI_LEARNING_PROTOCOL]] for AI session modes and ownership gates, [[TODAY]] for the locked plan, and [[AGENTS]] for the authoritative priority allocation. Do not create disconnected toy projects merely to touch every new technology.

## Weekly Allocation

Calibrate weekly focus across these core pillars:

| Focus | Target | Apply through |
|---|---:|---|
| Flagship Architecture & Delivery | 35% | requirements, scope, diagrams, contracts, features, review, integration, milestones |
| DevOps, Testing, and Deployment | 25% | Docker, CI pipelines, environments, automated tests, migrations, monitoring, backups |
| DSA and Algorithm Fluency | 20% | daily pattern practice, language syntax fluency, and problem-solving reasoning |
| System Design and Databases | 15% | schema tradeoffs, SQL indexing, concurrency, failure modes, caching, scaling |
| Communication and Career Proof | 5% | ADRs, task briefs, PR reviews, incident runbooks, case study documentation |

Use actual tracked minutes for a weekly review, but judge success by outcomes. Assign each session one primary category so time is not double-counted.

## Capacity Tiers

| Tier | Per day | Five-day maximum | Rule |
|---|---:|---:|---|
| Full-capacity | 4.5–5 focused hours | 22.5–25 hours | Only when the time genuinely exists after responsibilities and recovery |
| Standard | 3 focused hours | 15 hours | Default normal study/work day plan |
| Busy fallback | 1h45 focused | 8h45 | Preserve continuity without catch-up debt during heavy workloads |

The weekly maximum is not a quota. Never sacrifice sleep, health, or core obligations to fill it.

## Three Weekly Outcomes

Plan only:

1. one flagship project milestone or integrated vertical slice;
2. one delivery, testing, database, security, or reliability improvement attached to it;
3. one DSA/algorithm or verified interview preparation outcome.

Everything else is backlog or reference material. Remove or defer an outcome before adding another.

## Monthly Evidence Contract Rule

A monthly goal must describe a shipped or demonstrable outcome—not “learn,” “study,” “finish lessons,” or “become familiar with” a technology. Keep only one active ownership cycle.

Every cycle must state:

1. the deliverable and integration point;
2. observable acceptance criteria, including a relevant failure or unauthorized path;
3. required evidence links: code, tests, diagram/ADR, review, deployment/recovery record, or closed-book demonstration;
4. deadline, dependencies, owner, and main risk;
5. concepts that must be explained closed-book;
6. scope explicitly deferred;
7. the exact active work removed or deferred if new scope enters.

If a proposed cycle cannot fill these fields, keep it as reference.

## Monthly Ownership Cycles

Do not count a tutorial-sized feature as ownership. Each cycle takes **up to four focused weeks** and ends with an integrated artifact that passes the [[AI_LEARNING_PROTOCOL]] ownership gates.

Use this four-week shape:

| Week | Purpose | Required proof |
|---:|---|---|
| 1 | Mental model and smallest working core | Flow/trust-boundary note plus a core path written or rebuilt in Mode A/C |
| 2 | Real lifecycle and data behavior | Boundary cases, persistence, errors, and one consequential design decision |
| 3 | Security, failure, and concurrency | Unauthorized/failure tests and documented concurrent or repeated-request behavior |
| 4 | Integration and explanation | UI/API/DB integration, review evidence, and a closed-book walkthrough or rebuild |

If the gate is not green after week 4, record the exact gap and extend only that gap. Do not start another entire course. If the gate becomes green early, advance without padding the month.

### Example Cycle — Authentication and Authorization Ownership

**Goal:** Own user identity, token/session lifecycle, and resource ownership boundaries.

- **Week 1 (Core Auth):** Flow/trust-boundary diagram. Rebuild closed-book: input validation → password hashing/verification → safe lookup → token creation → `requireAuth`. Five failure cases tested safely.
- **Week 2 (Session/Token Lifecycle):** Define expiry, logout/revocation, cookie/header transport, and CORS/CSRF behavior. Enforce server-side revocation.
- **Week 3 (Authorization & IDOR):** Prove User A cannot read, modify, or delete User B's data. Add database unique constraints or transaction locks for concurrent requests.
- **Week 4 (Integration & Handoff):** Integrate frontend with API and database under happy and error states. Complete closed-book explanation and an Architectural Decision Record (ADR).

### Roadmap of Subsequent Cycles (Customize to Your Target Stack)

| Window | Focus | Deliverable | Green Gate |
|---|---|---|---|
| Cycle 1 | Auth & Authorization | Secure login, session/JWT lifecycle, IDOR guards | Closed-book rebuild of middleware + failure tests |
| Cycle 2 | Database & Performance | Relational schema, indexes, query plans, transactions | Real migration + execution plan analyzed |
| Cycle 3 | Frontend & UX State | Accessible UI, server/client state, form validations | Complete user journey wired to live API |
| Cycle 4 | DevOps & Delivery | Docker containerization, CI pipelines, automated tests | Clean deployment runbook + simulated rollback |

## The Weekday Rhythm

Choose the schedule that fits your current life constraints:

### Pattern A: Dedicated Study (Standard 5-Day Rhythm)
- **Monday:** 2 Sessions (Session 1: Algorithm fundamentals; Session 2: Hard concept using Session 1's knowledge).
- **Tuesday:** 1 Session (Algorithm fundamentals deep dive).
- **Wednesday:** 1 Session (Hard concept / project integration).
- **Thursday:** 1 Session (Algorithm fundamentals deep dive).
- **Friday:** 1 Session (Hard concept / project integration).

### Pattern B: Constrained / Working Professional Rhythm
- **Primary Day (e.g. Monday or Saturday):** 3–4 focused hours (Deep work: Algorithm derivation + flagship project milestone).
- **Workday Evenings:** Up to 1.5–2 hours max: retrieval, small bugfixes, test writing, or reading. No new complex Mode A concepts when mentally exhausted.
- **Rest Days:** At least one day per week of 100% protected rest with zero screen study.

## The Weekend Workflow (Review & Recovery)

Weekends are for spaced repetition, reflection, and rest — not introducing brand-new complex topics.

1. **Active Retrieval (30–60 mins):** Closed-book redo of an algorithm or flashcard/concept recall.
2. **Weekly Review (30 mins):** Fill out the Weekly Review section in [[LEARNING_LOG]]:
   - What integrated artifact shipped?
   - What was decided, tested, deployed, or recovered?
   - Where did actual time differ from targets?
   - What consumed time without producing evidence?
   - What is Monday's first 25-minute action?
3. **Hard Stop:** Close the laptop. Protect time for physical movement, relationships, and cognitive reset.
