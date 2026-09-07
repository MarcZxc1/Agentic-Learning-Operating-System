---
status: accepted
artifact: architecture-decision-record
---

# ADR-001: Relational Database Selection for Core State

- Date: 2026-01-01
- Status: accepted
- Owner: Engineering Lead
- Reviewers: Team / Self-Review

## Context

Our application requires persistent data storage for user accounts, resources, and transactional records. We need strict consistency guarantees, relational foreign keys to prevent orphan records, and robust migration tooling.

## Decision Drivers

- Need ACID transaction guarantees for multi-step mutations.
- Need structured relational modeling (users have many resources).
- Need mature, reversible schema migration tooling.
- Production readiness and community support.

## Options Considered

| Option | Benefits | Costs/risks | Evidence |
|---|---|---|---|
| **PostgreSQL** | Mature, ACID compliant, native JSON support, excellent migration tools (Prisma, Alembic, Flyway). | Requires hosting instance / container overhead. | Industry standard for relational workloads. |
| **MongoDB / NoSQL** | Flexible schema, fast prototyping. | Lacks native relational integrity checks; eventual consistency traps. | Risk of data anomalies without complex app-level checks. |
| **SQLite** | Zero setup, embedded single file. | Concurrency write bottlenecks in production multi-user environments. | Great for local testing, limited for high-concurrency API servers. |

## Decision

We select **PostgreSQL** as the primary datastore, running via Docker in local development and managed PostgreSQL in staging/production.

## Consequences

- **Positive:** Enforced relational integrity (foreign keys, unique constraints), transaction safety, and clean migration history.
- **Negative:** Requires running a PostgreSQL Docker container for local testing.
- **Follow-up / Reversal Trigger:** If read traffic exceeds single-node capacity by 10x, evaluate read replicas or Redis caching.

## Verification

- Automated integration tests execute migrations on a test database instance and verify foreign key cascading and transaction rollback.
