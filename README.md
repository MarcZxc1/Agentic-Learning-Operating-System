# Agentic Learning Operating System (ALOS)

> **"If AI wrote it, I still owe the learning. If I cannot rebuild it closed-book, it does not count."**

The **Agentic Learning Operating System (ALOS)** is a rigorous, anti-sycophantic, proof-driven operating system for engineering self-education. Built for **Obsidian**, **AI coding agents** (Google Antigravity, Claude Code, Cursor, Codex), and **focus timers** (StudyFlow / `studyctl`), it stops tutorial hell, prevents "vibe-coding" skill atrophy, and turns self-study into verifiable production artifacts.

---

## Table of Contents

- [The Problem ALOS Solves](#the-problem-alos-solves)
- [Core Philosophy](#core-philosophy)
- [Vault Architecture & Key Files](#vault-architecture--key-files)
- [The 4 AI Session Modes](#the-4-ai-session-modes)
- [Step-by-Step Setup Guide](#step-by-step-setup-guide)
- [The Daily Workflow](#the-daily-workflow)
- [DSA & Algorithm Problem-Solving Scaffold](#dsa--algorithm-problem-solving-scaffold)
- [Engineering Decision Templates](#engineering-decision-templates)
- [Customization & Principles](#customization--principles)

---

## The Problem ALOS Solves

Modern AI coding agents can generate entire applications in seconds. But this creates a dangerous trap for software engineers:

1. **The Familiarity Illusion:** You watch an AI agent generate auth middleware, database migrations, or React state management. It passes tests, and you feel like you understand it. But when an interviewer or an on-call incident asks: *"What breaks if this token expires?"* or *"Rebuild this query from a blank file,"* you freeze.
2. **Tutorial Hell & Backlog Bloat:** You bookmark dozens of repos, watch hours of YouTube tutorials, and collect hundreds of Obsidian notes that you never revisit.
3. **Sycophantic AI Coaches:** Most LLMs flatter the user, saying *"Great job! Your code looks amazing!"* while ignoring broken edge cases, unhandled race conditions, and lack of real ownership.

**ALOS solves this by transforming your local vault into a strict, supportive, and telemetry-tracked personal engineering coach.**

---

## Core Philosophy

1. **Ownership Over Familiarity:** You do not own a skill until you can derive the core logic closed-book in a blank file without looking at documentation or asking an AI agent.
2. **Three-Axis Evaluation:**
   - **Algorithm / Logic:** `pass/fail` (Correctness, edge cases, Big-O limits).
   - **Interview Explanation:** `pass/minor repair/fail` (Can you articulate trade-offs, invariants, and failure modes to a senior engineer?).
   - **Ownership:** `owned/reviewed/demo` (Did you build it cold, with assistance, or is it merely an unverified demo?).
3. **Daily Plan Lock:** You choose your capacity tier once in the morning (`Full`, `Standard`, or `Busy`). `TODAY.md` is locked. Shiny new ideas go to a backlog note, not today's plan.
4. **Verified Telemetry:** No guessed or inflated study hours. Every study block is tied to a timer (like `studyctl`) and recorded in `LEARNING_LOG.md`.
5. **Preflight Discipline:** Before the timer starts, the expected artifact format, acceptance criteria, and edge cases are made visible.

---

## Vault Architecture & Key Files

| File / Folder | Purpose |
|---|---|
| `IAM.md` | Your engineering profile: target roles, current tech stack, schedule constraints, and non-goals. |
| `AGENTS.md` | The authoritative system instructions for AI coding agents (Antigravity, Claude Code, etc.). |
| `CLAUDE.md` / `GEMINI.md` | Symlinks to `AGENTS.md`, ensuring all agent hosts follow identical behavioral rules. |
| `RULES_AT_A_GLANCE.md` | 10-bullet executive summary of your non-negotiable engineering rules. |
| `LEARNING_OPERATING_SYSTEM.md` | Neuro-optimized daily routines, capacity tiers (Full, Standard, Busy), and session preflights. |
| `AI_LEARNING_PROTOCOL.md` | Authoritative rules for when AI is permitted, restricted, or banned during study blocks. |
| `CORE_SKILLS_SCHEDULE.md` | Weekly focus allocation (35% Flagship / 25% DevOps / 20% DSA / 15% System Design / 5% Career) and 4-week monthly ownership cycles. |
| `DSA_INTERVIEW_PREP.md` | Daily problem-solving guide, 6-step hint ladder, and Active Foundation Gate. |
| `FEYNMAN_LEARNING_PROTOCOL.md` | Socratic teach-back protocol triggered by `$feynman-vault` or "Feynman this". |
| `TODAY.md` | Single source of truth for the day's locked learning blocks and acceptance checks. |
| `LEARNING_LOG.md` | Telemetry-backed session log, streak tracker, weekly reviews, and monthly retrospectives. |
| `Dashboard.md` | High-level navigation cockpit and graduation evidence matrix. |
| `DEFINITION_OF_TERMS.md` | High-yield engineering terminology queue and core conceptual distinctions. |
| `basics/` | 12 starter algorithm challenges (`algorithm_lesson_01.py` through `12.py`) with test suites and problem-solving guides. |
| `templates/` | Industry-grade engineering templates: Architectural Decision Records (ADRs), Task Briefs, PR Reviews, Incident Reports, and Runbooks. |

---

## The 4 AI Session Modes

Before starting any study block, declare your mode in `TODAY.md`:

- **Mode A — Skill Acquisition (Default for Leveling):**
  - **Goal:** Own a new hard concept (e.g., JWT vs sessions, database transaction locks, custom React hooks).
  - **AI Rule:** Research and review only. AI may **not** write multi-file implementations for you. You write the code; AI reviews your pull request.
- **Mode B — Project / Team Shipping:**
  - **Goal:** Ship an integration, vertical slice, or deployment pipeline for patterns you already understand.
  - **AI Rule:** AI assist allowed for glue code, configuration, and boilerplate.
- **Mode C — Closed-Book Drill (Interview Mode):**
  - **Goal:** Solve a problem or rebuild a critical path from a blank file with zero external help.
  - **AI Rule:** AI is completely off until the timer ends. Spend $\ge 15$ minutes reasoning before requesting any hint.
- **Mode D — Agent-Assisted Speed (Use Rarely):**
  - **Goal:** Rapidly prototype or unblock a production task.
  - **AI Rule:** Full agent generation allowed.
  - **Mandatory Tax:** Requires a 15–30 minute closed-book derivation or summary within 24–48 hours. If you cannot rebuild it, it was Mode A work in disguise.

---

## Step-by-Step Setup Guide

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/learning-vault.git ~/learning-vault
cd ~/learning-vault
```

### 2. Open in Obsidian
1. Download and install [Obsidian](https://obsidian.md/).
2. Click **"Open folder as vault"** and select `~/learning-vault`.
3. (Recommended) Enable Obsidian Core Plugins: *Backlinks*, *Outgoing Links*, and *Search*.

### 3. Personalize `IAM.md`
Open `IAM.md` and replace the bracketed placeholders with your details:
- Your target roles (e.g., Backend Engineer, Junior Full-Stack).
- Your current active stack (e.g., Node.js, Express, PostgreSQL, React, Docker).
- Your weekly schedule constraints and free hours.
- Your non-goals (what you are deliberately *not* studying right now).

### 4. Update Workspace Paths in `AGENTS.md`
Open `AGENTS.md` and update the paths to match your local setup:
```markdown
## Workspace Paths
- **Learning Vault**: /path/to/your/learning-vault
- **Flagship Project**: /path/to/your/flagship-repo
```

### 5. Pair with Your AI Agent
This vault is engineered to work out of the box with modern agentic CLI tools:
- **Google Antigravity CLI:** Reads `GEMINI.md` (which symlinks to `AGENTS.md`).
- **Claude Code:** Reads `CLAUDE.md` automatically.
- **Cursor / Windsurf:** Add `AGENTS.md` as custom context or rule file (`.cursorrules`).
- **OpenAI Codex CLI:** Reads `AGENTS.md` directly.

Whenever you start a session, your AI agent will read the authoritative rules:
- It will enforce the daily plan lock in `TODAY.md`.
- It will refuse to write your code during Mode A/C learning blocks.
- It will provide Socratic critique and grade on the 3-axis rubric.
- It will run the written preflight before your timer starts.

### 6. Focus Timer Setup (Optional but Recommended)
ALOS uses CLI focus tracking to ensure zero manual drift. You can use any focus timer, or install [StudyFlow](https://github.com/studyflow):
```bash
# Example StudyFlow CLI usage:
studyctl session start --minutes 60 --json
studyctl session status --json
studyctl session finish --reflection "Derived linear scan invariant closed-book" --json
```
If you use another timer (Pomodoro app, Kitchen timer), simply log the verified minutes in `TODAY.md` and `LEARNING_LOG.md`.

---

## The Daily Workflow

```
┌────────────────────────────────────────────────────────┐
│ 1. MORNING PLAN LOCK (TODAY.md)                        │
│    - Choose Capacity Tier: Full (4.5h) / Std (3h) / Busy│
│    - Select ONE Must-Win Outcome                       │
│    - Lock the schedule; no random browsing             │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ 2. PREFLIGHT FORMAT CHECK                              │
│    - Coach presents required format & acceptance tests │
│    - Learner confirms understanding before timer starts│
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ 3. TIMED EXECUTION BLOCK (25/5 or 50/10)               │
│    - Start timer                                       │
│    - Mode A (Write code) or Mode C (Closed-book solve) │
│    - Stuck? Use 20-min stuck protocol; no agent rewrite│
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ 4. THREE-AXIS REVIEW & TIMER FINISH                    │
│    - Grade: Algorithm / Explanation / Ownership        │
│    - Complete timer; record telemetry in LEARNING_LOG  │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ 5. RECOVERY & HARD STOP                                │
│    - Close laptop; zero late-night marathon sessions   │
└────────────────────────────────────────────────────────┘
```

---

## DSA & Algorithm Problem-Solving Scaffold

Before writing code for any algorithm problem, fill this exact scaffold in a blank file:

```text
Problem:
[One sentence naming the required behavior]

Input:
[Types, shapes, and constraints]

Output:
[Type and meaning of the returned value]

Rules / Edge Cases:
- Empty input:
- Duplicates:
- Negative values / zeros:
- Single-element input:

Manual Trace:
| Current Item / Position | State Before | State After |
|---|---|---|
| ... | ... | ... |

Plain-English Steps:
1. Initialize ...
2. Loop over ...
3. If condition met, update ...
4. Return ...

Loop Invariant:
[What fact remains true throughout every iteration among elements seen so far?]

Implementation:
[Your code here — written cold without AI autocomplete]

Assertions:
assert function_name(...) == expected_value

Complexity:
- Time: O(...) because ...
- Auxiliary Space: O(...) because ...
```

---

## Engineering Decision Templates

Located in the `templates/` directory:

- **Architectural Decision Records (`ADR_TEMPLATE.md`):** Capture context, alternatives considered, chosen design, trade-offs, and failure behavior.
- **Task Briefs (`TASK_BRIEF_TEMPLATE.md`):** Delegate or bound features with explicit owners, acceptance criteria, test matrices, and risks.
- **Pull Request Reviews (`PR_REVIEW_TEMPLATE.md`):** Evaluate PRs for security boundaries, invariants, edge cases, and test coverage.
- **Incident Reports (`INCIDENT_REPORT_TEMPLATE.md`):** Root cause analysis, timeline, mitigation, and preventative action items.

---

## Customization & Principles

- **Make It Your Own:** Modify `CORE_SKILLS_SCHEDULE.md` to match your stack (e.g. swap Python for Go, or React for Vue).
- **Obsidian Graph View:** Watch your knowledge base grow organically as your projects link to architecture notes and daily logs.
- **Open Source:** Feel free to fork, customize, and share your learning journey.

---

**License:** MIT. Free to use, adapt, and share.
