---
status: active
updated: 2026-01-01
review_cycle: monthly
priority: execution
---

# Engineering Learning Dashboard

Goal: Become a credible, hireable software engineer with verifiable project evidence, deep system fundamentals, and independent problem-solving skills.

Start with [[IAM]], choose today's capacity in [[LEARNING_OPERATING_SYSTEM]], pick an AI session mode from [[AI_LEARNING_PROTOCOL]], lock the daily plan in [[TODAY]], and execute through [[CORE_SKILLS_SCHEDULE]]. Record completed blocks in [[LEARNING_LOG]].

> [!important]
> Durable fundamentals and verifiable project evidence are the safest career preparation. Real engineering skill is what remains when the AI tooling is disconnected.

> [!warning] Lesson Freeze
> Do not endlessly add tutorials. Obsidian is the second memory for decisions and retrieval—not a second backlog. Search existing coverage, finish the active evidence gate, and remove or defer work before adding scope.

## Daily Active Surface

Open these notes by default during your daily workflow:

| Purpose | Authoritative Location |
|---|---|
| Today's one must-win outcome | [[TODAY]] |
| Current monthly ownership cycle | [[CORE_SKILLS_SCHEDULE]] |
| Completed work and exact next action | [[LEARNING_LOG]] |
| Current terminology retrieval queue | [[DEFINITION_OF_TERMS#Active Terminology Queue]] |
| Current algorithm mastery gate | [[DSA_INTERVIEW_PREP]] |
| Quick-reference vault rules | [[RULES_AT_A_GLANCE]] |

## Current Evidence Contract

“Learn technology X” is not an engineering goal. Maintain one active cycle contract:

| Contract Field | Commitment |
|---|---|
| Deliverable | [e.g. An explainable full-stack authentication and authorization vertical slice] |
| Acceptance criteria | [e.g. Protected route returns identity; 401/403/404 fail safely; IDOR prevented; DB tests pass] |
| Evidence required | [e.g. Request flow diagram, passing tests, clean git commits, ADR-001, closed-book demo] |
| Deadline | [YYYY-MM-DD] |
| Dependencies | [e.g. Database running in Docker, test runner configured] |
| Main risk | [e.g. Relying on AI agent code without being able to recreate the critical path] |
| Deferred scope | [e.g. Multi-tenant OAuth, complex microservices, Redis clustering] |

At month-end, update [[LEARNING_LOG#Monthly Evidence Reviews]]. If an acceptance check is not green, extend only the specific gap.

## Roadmap to Engineering Fluency

### Phase 1: Foundations & Architecture
- [ ] Establish personal profile and constraints in [[IAM]]
- [ ] Own basic algorithm derivation (Lessons 1–4) in [[DSA_INTERVIEW_PREP]]
- [ ] Initialize flagship project with reproducible environment (Docker / CLI)
- [ ] Draft initial Architectural Decision Records in `adrs/`

### Phase 2: Core Vertical Slice & Security
- [ ] Build end-to-end data flow (UI → API → Relational Database)
- [ ] Implement robust authentication, session lifecycle, and authorization (IDOR protection)
- [ ] Write risk-based unit and integration tests covering normal and failure paths
- [ ] Set up automated CI pipeline to run linter, type-checker, and tests

### Phase 3: Reliability & System Design
- [ ] Practice relational schema design, transactions, indexing, and query plan analysis
- [ ] Perform simulated operational recovery (backup/restore, rollback, and runbook)
- [ ] Deepen linear DSA patterns (sliding window, two pointers, hash map lookups)
- [ ] Practice junior system design tradeoffs (monolith vs microservices, caching, sync vs async)

### Phase 4: Portfolio Proof & Interview Readiness
- [ ] Produce clean public technical documentation and architectural case study
- [ ] Rehearse line-by-line codebase walkthroughs and closed-book technical derivations
- [ ] Prepare STAR engineering stories covering real bugs, constraints, and failures
- [ ] Begin targeted applications with proof-backed resume

## Capability Evidence Matrix

| Capability | What Proves It | Priority |
|---|---|---|
| Language Fluency | Type-safe code, clean error boundaries, zero syntax hesitation | Core |
| Backend & HTTP | Documented API, authentication, authorization, idempotency, failure states | Core |
| Relational Databases | Normalized schema, migrations, transactions, index query plans | Core |
| DevOps & Testing | Automated CI/CD, Dockerized dev environment, automated test suites | Core |
| Problem-Solving | Closed-book algorithm derivation with invariants and Big-O proofs | Core |
| Communication | Clear ADRs, structured PR descriptions, incident postmortems | Core |
