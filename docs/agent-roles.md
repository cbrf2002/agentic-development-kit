# Agent roles and handoff

One agent may perform several roles sequentially. Independent review requires a different reviewer/session. These roles do not grant tool access, repository write scope or publication authority.

| Role | Inputs | Deliverable |
| --- | --- | --- |
| Coordinator | Task, ownership, constraints and current context | Scoped plan, dependencies, work allocation and handoff |
| Implementer | Accepted criteria and authorized branch/worktree | Cohesive diff, tests and rollout notes |
| Code reviewer | Baseline/head revisions and engineering rules | Actionable defects or scoped no-findings verdict |
| Business reviewer | Requirements, invariants and changed behavior | Independent approval or specific required corrections |
| Security assessor | Written targets/actions/rates and evidence policy | Verified findings, coverage and remediation proposals |
| Report editor | Approved evidence model and report template | Consistent artifacts without changing assessment conclusions |

Assign one owner to shared entities, contracts and migration sequences. Parallel work should use separate worktrees and non-overlapping responsibilities. Coordinate shared changes before editing them. Keep heavy builds within the machine's agreed resource budget.

Every handoff records the task, repository/branch/SHA, current diff, executed checks, evidence, outstanding decisions and exact next step. Do not restart completed work or infer approval from a prior agent's summary. Verify mutable remote status before acting on it.
