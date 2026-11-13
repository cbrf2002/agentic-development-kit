# Code quality and review

- Match the repository's architecture, naming and public contracts. Prefer explicit dependencies and established patterns.
- Validate boundaries; enforce authorization server-side. Test object-level access and workflow transitions where relevant.
- Preserve data and historical evidence. Handle concurrency, idempotency, retries and stale versions deliberately.
- For financial behavior, document units, rounding, totals, null-versus-zero semantics and reconciliation invariants.
- Keep changes cohesive. Avoid unrelated formatting, dependency upgrades and speculative abstractions.
- Use meaningful regression/integration tests at the relevant boundary. Record skipped and unavailable checks.
- Keep logs useful without secrets or unnecessary personal data. Do not expose implementation details in product UI without user value.
- Review migrations for compatibility, applied IDs, rollout order and rollback data loss.
- Review source and tests independently where required. A successful build or passing suite is not business approval.
- Write actionable findings with a specific trigger, location, impact and correction. State uncertainty and existing-versus-introduced scope.

Priorities are project-specific. Define the rubric before assigning them. Separate security CVSS and detector severity from delivery priority.
