# Workshop Example — Production Readiness

Dummy **checkout ops** service used to demo the **Production Readiness** scorecard.

This repo is intentionally **Gold** on Production Readiness so attendees can change one rule and see the agentic fix workflow fire.

## Scorecard mapping

| Level | Rule | Evidence in this repo |
|-------|------|------------------------|
| Bronze | `require_runbook` | `RUNBOOK.md` |
| Silver | `require_on_call` | `oncall.json` |
| Gold | `require_slo` | `slo.yaml` |

## Suggested workshop degrade

```bash
rm RUNBOOK.md
# Then patch Port entity has_runbook=false
```

Or trigger a dry-run from Actions → **Port Agentic Scorecard Fixer** → `require_runbook`.

## Port entity

`example-production-service` — set `repository_url` to this repo after publish.
