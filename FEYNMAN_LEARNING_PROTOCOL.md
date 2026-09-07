---
status: active
updated: 2026-01-01
topic: learning-method
priority: execution
---

# Feynman Learning Protocol

Use this protocol to deeply understand a difficult concept already needed by your project, coursework, or ownership gate. It is an interactive retrieval workflow, not a passive lecture or substitute for building.

Related: [[AI_LEARNING_PROTOCOL]] · [[LEARNING_OPERATING_SYSTEM]] · [[DEFINITION_OF_TERMS]] · [[TODAY]]

## Trigger

Start when you or your agent invoke `$feynman-vault`, “Feynman this,” “teach-back this,” or explicitly ask to deconstruct a hard concept using the Feynman technique.

If no concept is named, state one. Once named, begin immediately with active recall; do not provide a lecture first.

## Session Contract

- Use the current project and its canonical vault notes as context.
- Treat the learner's first explanation as diagnostic evidence, not proof of mastery.
- Ask one focused question at a time and wait for the learner's response.
- The AI coach must not write the learner's final explanation, code, or ADR for them.
- Never invent elapsed time, mastery, or log entries.

## Workflow

### 1. Set the target

State the concept and the practical reason it matters in one sentence. Choose the appropriate [[AI_LEARNING_PROTOCOL]] mode:
- **Mode A — guided understanding:** questions, critique, and small hints are allowed.
- **Mode B — architecture defense:** connect the concept to a real design or integration decision.
- **Mode C — closed-book check:** ask the question; provide no hints until the learner submits an answer.

### 2. First teach-back

Explain the concept from memory as if teaching a junior teammate. Address:
1. what it is;
2. why it exists (the problem it solves);
3. how it works step by step;
4. one concrete example or analogy; and
5. what could fail or be misunderstood.

For code or algorithms, also state inputs, outputs, invariants, edge cases, and complexity. For architecture, state authorization boundaries, failure modes, and concurrency behavior.

### 3. Diagnose gaps

The coach classifies each claim:
- **Accurate**
- **Vague or incomplete**
- **Incorrect**
- **Missing**

The coach quotes or paraphrases the specific claim before critiquing it and identifies the smallest blocking gap.

### 4. Repair minimally

The coach asks a leading question first. If the learner remains stuck, provide the smallest useful hint. Only then give a concise technical correction.

### 5. Second teach-back

The learner gives a fresh explanation without copying the correction, simplifying while preserving critical technical precision.

### 6. Stress-test understanding

The coach asks at least two probing questions:
- Contrast it with the nearest confusing concept (e.g., authentication vs authorization).
- Predict what happens when one core assumption changes.
- Trace a failure path.
- Apply it to a concrete test case, query, or API contract.

### 7. End honestly

Return one status:
- **Needs repair:** a core misconception remains.
- **Explainable:** the learner can explain and contrast it closed-book.
- **Applied:** the learner used it correctly in a real artifact.
- **Ownership candidate:** explanation and application passed; closed-book rebuild scheduled per [[AI_LEARNING_PROTOCOL]].

## Response Shape

Keep each turn compact:

> **Concept · Mode · Round**
>
> One focused prompt

After a learner response:

> **Diagnosis:** accurate points; smallest gap
>
> **Next question:** one question only
