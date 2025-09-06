# UA Cleanroom Seed (Tier A: plan-only, safe & cheap)
This repository is a clean-room starter for a Universal Agent that emerges by repeating a cheap, fun, and informative cycle:
**plan → sandboxed run → evidence → refine → unlock**.

## How to ask a chatbot to iterate
> I have a project at this URL. Please iterate on it. Read `INTENT.md`, `planner/minimal_prompt.md`, and `policy/global.yaml`. 
> Produce a plan and a **plan-only run** that writes `runs/<id>/plan.json` and propose the next safe unlock (a PR-draft patch, no network writes).

## Quick start (local)
```bash
./scripts/run.sh
# Inspect new folder under ./runs/<id>/plan.json
```

## Next safe unlock (what to implement next)
- Add `scripts/pr_draft.sh` and `scripts/new_run.sh` so the agent can produce a **local patch** (`artifacts/changes.patch`) and a brief `PR_SUMMARY.md` inside the run directory — **without** any network writes.

---
This seed is intentionally minimal and idempotent, with no external side-effects beyond local files in `./runs`.
