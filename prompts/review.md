# Code and business review prompt

Review [DIFF / PR / REVISION] against [BASELINE], the applicable requirements and repository rules. Confirm revisions and read the code around changed call sites. Review only supported failure paths; distinguish existing defects from introduced regressions.

Prioritize correctness, authorization, data integrity, workflow transitions, concurrency, financial rounding, compatibility and migration order. Use realistic bounded examples. Run scoped checks where appropriate and record their actual limits.

For each actionable finding provide: priority with rationale, affected repository/file/line, trigger, expected versus observed behavior, impact, evidence, proposed correction and regression test. Label uncertainty. Do not flood the review with style preferences or speculative risks.

Map existing reviewer comments to addressed, open or evidence-backed disposition. Report source review separately from runtime testing. An independent review must be performed by a separate reviewer/session; self-review is not independent approval. If no actionable finding is supported, state that and list the verification boundary.
