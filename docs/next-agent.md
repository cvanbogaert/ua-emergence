# Next-Agent Brief

## Where we are (quick)
- Draft PR exists for `feat/pr-draft` → `main` (see PR #2).
- Local plan-only artifacts generate: `pr-draft/plan.json`, `pr-draft/plan.log`, `pr-draft/comment.md`.
- CI workflow exists: `.github/workflows/pr-draft.yml`. If no runs appear, ensure Actions are enabled.

## What to do next (ordered, atomic)
1. **Confirm Actions are enabled**: Repo → Settings → Actions → General → Allow GitHub Actions.
2. **Trigger/observe run**: Push a tiny README change to `feat/pr-draft` or apply label `plan-only`.
3. **Verify artifacts**: Download `pr-draft-<run_id>` (plan.json, plan.log, changes.patch).
4. **Wire a real “planner” (still non-mutating)**:
   - Prefer `terraform validate` + `terraform plan -no-color` if TF code exists, else `make -n plan`.
   - Parse output → summarize into `plan.json` (`ok`/`degraded`/`fail`, issues[], hints[]).
5. **Harden PR comment**:
   - Include status badge-style summary plus top N issues.
6. **(Optional) Add policy checks**:
   - Lint, format, basic policy gates in `policy/` (no mutations).

## Conventions to honor
- Always verify INTENT and return structured JSON after each one-paste action.
- Keep steps small; avoid assumptions about environment or cwd.
- Use the repo slug **without** `.git` when passing to `gh` commands.
- Labels `plan-only`, `tier:B` should trigger the plan-only workflow even if PR isn’t draft.

## Troubleshooting
- **Push of workflows rejected**: use HTTPS token with `workflow,repo` scopes.
- **No common history between branches**: reset feature branch onto `origin/main`, then reapply minimal diffs.
- **No CI run found**: ensure Actions is enabled; push a small commit; check branch filters.
