---
status: active
updated: 2026-01-01
topic: dsa-python
difficulty: progressive
priority: role-dependent
current_phase: foundation-gate
current_lesson: 1
---

# DSA and Algorithms: Daily Problem-Solving Guide

**Language:** Python 3.12+ (or your primary language)  
**Time box:** 60–90 minutes per study session  
**Progression:** syntax fluency → arrays/strings → hash maps/sets → two pointers → sliding window → stacks/queues → binary search → trees/graphs

The goal is reliable derivation and engineering fluency, not an arbitrary problem count. One solution you can derive, test, analyze, and explain from memory is worth ten copied solutions.

## Required DSA Written Format — Show Before Every Problem

While the [[#Active Foundation Gate]] is open, display this full format before every DSA timer. Do not merely point to this note. Define unfamiliar terms before assessment, use an unrelated example if needed, and begin Mode C only after confirming the format is clear.

After the foundation gate is green, use the compact interview preflight: problem/input/output and edge cases; approach; implementation; tests; time/space complexity.

| Section | Meaning | Expected format |
|---|---|---|
| Problem | The behavior to implement | One sentence naming the required result |
| Input | Data the function receives | Type, shape, and relevant constraints |
| Output | Value the function returns | Type and meaning of the result |
| Rules / edge cases | Required behavior at boundaries | Short bullets for empty, invalid, duplicate, impossible, or boundary cases |
| Manual trace | One concrete example followed step by step | Current item or position, state before, and state after |
| Plain-English steps | The algorithm without programming syntax | Initialize → inspect → update → finish/return |
| Loop invariant | A fact about state that remains true throughout the loop | One general sentence about what the state represents among elements processed so far |
| Implementation | Your working solution | Clean code written without AI implementation help for Mode A/C ownership |
| Assertions | Executable checks that fail when behavior is wrong | Real `assert` statements covering normal and relevant edge cases |
| Complexity | How work and memory grow with input size | Big-O time plus Big-O auxiliary space, each with a concrete reason |

### Blank Preflight Template

```text
Problem:

Input:
Output:
Rules / edge cases:

Manual trace:
| Current item/position | State before | State after |
|---|---|---|

Plain-English steps:
1. 

Loop invariant:

Implementation:

Assertions:

Complexity:
- Time:
- Auxiliary space:
```

### Grading Calibration (Three Independent Axes)

Report three independent results after every DSA review:

1. **Algorithm:** `pass` when logic, edge cases, and complexity are correct; otherwise `fail` with the exact defect.
2. **Interview explanation:** `pass`, `minor repair`, or `fail` based on whether you can communicate and defend the approach clearly.
3. **Ownership:** `owned`, `reviewed`, or `demo` under [[AI_LEARNING_PROTOCOL]].

A correct algorithm does not become a failed solution simply because its verbal explanation needed a small wording repair.

## Active Foundation Gate

Do not jump directly to complex LeetCode patterns while this gate is open. Use the method in [[basics/ALGORITHM_PROBLEM_SOLVING_GUIDE]] and rebuild the first four exercises from [[basics/README_DSA_CHALLENGES]] in order:

1. `algorithm_lesson_01.py` — function input, processing, `return` versus `print`, assertions, and Big-O foundational mental model ($O(1)$ time & space);
2. `algorithm_lesson_02.py` — linear scan, current-best state, empty input sentinel, loop invariant, $O(n)$ time, and $O(1)$ space;
3. `algorithm_lesson_03.py` — `enumerate`, early return, not-found sentinel, and best/worst case;
4. `algorithm_lesson_04.py` — accumulator state, conditional update, empty input, and full-loop completion.

For each exercise, keep existing files closed and produce, in a clean buffer:
- input, output, and rules;
- one manual trace;
- plain-English steps;
- loop invariant;
- normal and edge-case assertions;
- time and space complexity;
- working implementation.

**Pass bar:** Complete Lessons 1–4 without AI implementation help and explain each term above from memory.

**How to close this gate:** When you believe Lessons 1–4 are retained, schedule one Mode C session. Pick any two foundation lessons at random, solve them from a blank file with the full written scaffold, and explain each term without notes. If both pass, mark the gate green and switch to the compact interview preflight going forward.

## Daily 60–90 Minute Session Breakdown

| Minutes | Activity |
|---:|---|
| 5 | Recall yesterday's pattern and complexity without notes |
| 10 | Restate today's problem, constraints, examples, and brute force |
| 20–30 | Implement independently; use the hint ladder only after 15 focused minutes |
| 10–15 | Test edge cases and repair the reasoning, not only the code |
| 10 | Explain invariant plus time/space complexity aloud or in writing |
| 10–20 | Rebuild cleanly from memory or review one previous problem |

Stop when the time box ends. Record the blocker and exact next step in [[LEARNING_LOG]] instead of copying an editorial answer.

## Hint Ladder

Use only one level at a time:

1. Re-read constraints and work a tiny example manually by hand.
2. Ask what repeated work makes the brute force slow.
3. Ask which data must be remembered while scanning.
4. Reveal the pattern name only (e.g. "Two Pointers" or "Hash Map complement").
5. Read pseudocode, close it, then implement independently.
6. Read a full solution only after recording why earlier attempts failed; rebuild it from scratch 24h later without viewing it.

## Core Patterns Overview

### Pattern 1 — Arrays and Strings
- **Core signals:** In-place compaction, prefix calculations, window tracking, sequence reversal.
- **Key question:** Does sorting simplify the lookup, or does it destroy essential index information?

### Pattern 2 — Hash Maps and Sets
- **Core signals:** Fast $O(1)$ membership checks, complement lookups (e.g. Two Sum), frequency counters.
- **Key question:** Does checking before inserting prevent using the same element twice?

### Pattern 3 — Two Pointers
- **Core signals:** Sorted sequences, searching for pairs with a target sum, reversing in-place, partitioning.
- **Key question:** Why does moving one pointer guarantee we do not discard a potential valid answer?

### Pattern 4 — Sliding Window
- **Core signals:** Contiguous subarrays or substrings with sum/length/uniqueness constraints.
- **Key question:** Can the window shrink monotonically from the left when the condition is violated?

### Pattern 5 — Stacks and Queues
- **Core signals:** Nested structures (parentheses), undo history, nearest greater element, FIFO order.
- **Key question:** Does the problem require LIFO (Stack) or FIFO (`collections.deque`) semantics?

### Pattern 6 — Binary Search
- **Core signals:** Monotonic condition over a sorted sequence or search space ("binary search on answer").
- **Key question:** What exact invariant keeps the target within `[left, right]`?

## Deferred Patterns

Trees, graphs, heaps, dynamic programming, and backtracking remain useful but should be deferred until the core linear patterns (1–6) are mastered and retained.
