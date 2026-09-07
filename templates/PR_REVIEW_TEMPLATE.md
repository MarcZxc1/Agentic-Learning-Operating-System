---
status: template
artifact: pull-request-review
---

# Pull Request Review

## Author Checklist

- [ ] Task and acceptance criteria linked
- [ ] Change is bounded; non-goals identified
- [ ] Tests cover normal, boundary, failure, and unauthorized behavior as relevant
- [ ] Migration, configuration, security, observability, and rollback impacts documented
- [ ] No secrets or sensitive data in code, fixtures, screenshots, or logs

## Reviewer Checklist

- [ ] Behavior matches requirements
- [ ] Interfaces and data ownership remain coherent
- [ ] Errors, concurrency, retries, and failure modes are safe
- [ ] Tests would fail if the risky behavior regressed
- [ ] Documentation and architecture artifacts remain accurate

## Decision

Approve | Request changes | Blocked — include evidence and required next action.
