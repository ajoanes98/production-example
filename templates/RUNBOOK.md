# Runbook — Checkout Ops Service

## Service Overview

| Field | Value |
|-------|-------|
| Tier | tier-1 |
| Owning Team | platform-engineering |
| On-Call | checkout-oncall (PagerDuty) |

## Alerts

| Alert | Severity | First Response |
|-------|----------|----------------|
| High error rate | P1 | Check recent deploys, roll back if needed |
| Payment latency SLO breach | P2 | Inspect payment provider health |
| Cart abandon spike | P3 | Verify CDN / frontend deploys |

## Rollback

```bash
kubectl rollout undo deployment/checkout-ops
```

## Escalation

1. On-call engineer (PagerDuty)
2. Platform engineering lead
3. Engineering manager
