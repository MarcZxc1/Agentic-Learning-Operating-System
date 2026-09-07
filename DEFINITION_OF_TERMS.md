---
status: active
updated: 2026-01-01
topic: engineering-glossary
priority: reference-support
review_cycle: as-needed
---

# Engineering Definition of Terms

This is the shared technical vocabulary for your learning vault: software architecture, web development, relational databases, testing, DevOps, security, algorithms, and technical communication.

> [!important] Reference, Not Proof of Ownership
> Reading or recognizing a term does not make it owned. A term is owned only when you can define it in your own words, distinguish it from a nearby concept, and apply it to code, a test, a diagram, or an architectural decision without the definition open. Follow [[AI_LEARNING_PROTOCOL]].

## How to Use This Glossary

For any term you are learning, close this file and answer four prompts:

1. **Definition:** What is it in one precise sentence?
2. **Distinction:** What nearby concept is it commonly confused with?
3. **Example:** Where does it appear in your real codebase or API contract?
4. **Failure:** What breaks when it is misunderstood or omitted?

Use the status indicators honestly:
- **Unknown:** Cannot define it yet.
- **Recognized:** Remember seeing it, but cannot explain it precisely.
- **Explainable:** Can define and contrast it closed-book.
- **Applied:** Have used it correctly and can link to real code/tests.
- **Owned:** Can rebuild and defend the relevant subsystem closed-book.

## Active Terminology Queue

Keep only 5–10 terms in this queue. Test these concepts during your weekly active recall sessions.

| Concept Contrast | Why It Is Active | Evidence Required to Exit | Status |
|---|---|---|---|
| Authentication vs Authorization | Core security boundary | Cross-user denial test explained closed-book | Queued |
| `401` vs `403` vs privacy-preserving `404` | API test precision | Error-handling test suite with safe status codes | Queued |
| Password Hashing vs JWT Signing | Data integrity boundary | Closed-book explanation of crypto flows | Queued |
| Validation vs Sanitization | Trust boundary protection | Schema validation test + output escaping | Queued |
| Unit Test vs Integration Test | Testing discipline | Real-database test vs isolated function test | Queued |
| Database Migration vs CI/CD Pipeline | Delivery boundary | Migration runner script integrated into CI | Queued |
| Synchronous vs Asynchronous Work | System design fundamentals | Architecture diagram showing caller wait behavior | Queued |
| Structured Logs vs Metrics vs Traces | Observability foundation | Instrumented request showing all three signals | Queued |

## High-Yield Technical Distinctions

These core distinctions prevent critical architectural and interview mistakes:

| Concept A | Concept B | Crucial Distinction |
|---|---|---|
| **Authentication** | **Authorization** | Authentication verifies *who you are*; authorization determines *what you are permitted to do*. |
| **401 Unauthorized** | **403 Forbidden** | `401` means valid authentication credentials are missing or invalid; `403` means identity is known, but permission is denied for that resource. |
| **Password Hashing** | **JWT Signing** | Passwords pass through an intentionally slow one-way hash (e.g. bcrypt/argon2); JWTs are digitally signed using a secret or key pair so receivers can verify claims without storing server state. |
| **Database Migration** | **CI/CD Pipeline** | A migration is a versioned, reversible schema change script. CI/CD is the automated process that lints, tests, and deploys the code. CI/CD runs migrations, but is not the migration itself. |
| **Unit Test** | **Integration Test** | A unit test tests a single function or module in complete isolation (often with mocks). An integration test tests real boundaries together (e.g. HTTP route + actual PostgreSQL database). |
| **Input Validation** | **Sanitization** | Validation *rejects* malformed data that violates business rules. Sanitization *modifies* or cleans data. Sanitization should never replace strict input validation. |
| **Client-Side Validation** | **Server-Side Validation** | Client-side validation improves user experience by giving instant feedback, but can be bypassed with `curl`. The server must independently validate all incoming data. |
| **Synchronous Execution** | **Asynchronous Execution** | Synchronous callers block and wait for a response. Asynchronous workflows acknowledge receipt immediately and process the workload in the background (e.g. via queues and workers). |
| **Logs** | **Metrics** | Logs record individual timestamped events with context (e.g., "User 5 logged in"). Metrics are aggregated numerical measurements over time (e.g., "request rate is 45 req/s"). |
| **Smoke Test** | **Load Test** | A smoke test verifies that core system capabilities work before deep testing. A load test measures latency and resource limits under heavy traffic. |
| **INNER JOIN** | **LEFT JOIN** | `INNER JOIN` returns only rows that have matching values in both tables. `LEFT JOIN` returns all rows from the left table and matched rows from the right table (filling with `NULL` where unmatched). |
| **Modular Monolith** | **Microservices** | A modular monolith has clean internal module boundaries within a single deployable artifact. Microservices run separate processes communicating over the network with high operational overhead. |
