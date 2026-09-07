---
status: template
artifact: deployment-runbook
---

# Deployment Runbook

- Service/version:
- Environment:
- Owner:
- Last restore/rollback test:

## Preconditions

- [ ] CI checks pass and artifact is versioned
- [ ] Secrets/configuration validated without exposing values
- [ ] Migration compatibility and backup status reviewed
- [ ] Rollback or forward-repair path is ready

## Deploy and Verify

Number exact commands/actions. Include health, logs, critical journey, and migration checks.

## Rollback or Forward Repair

Define trigger, authority, steps, and data implications.

## Backup and Recovery

Define location, retention, restore steps, and latest tested recovery evidence.

## Escalation

Contacts, dependencies, known failure modes, dashboards, and logs.
