# Security assessment prompt

Assess [TARGETS] under [WRITTEN SCOPE / AUTHORITY]. Allowed environments/actions: [DETAILS]. Forbidden actions: [DETAILS]. Aggregate request ceiling, concurrency, testing window and stop conditions: [LIMITS]. Evidence location and access restrictions: [STORAGE POLICY]. Automatic remediation: [YES/NO; SCOPE].

Start with scope and source inventory. Record each repository SHA and distinguish source from deployed builds. Prioritize SCA and secrets review, then SAST/manual verification, followed by authorized DAST and load tests. Select tools supported by the stack, environment, entitlement and budget. Never substitute a successful pipeline for completed security coverage.

Use applicable OWASP ASVS requirements, WSTG, API risks, project requirements and legal/privacy obligations as references. Record the exact standard version and attribution. Obtain official requirement text from a licensed source rather than inventing identifiers. Leave unassessed requirements unassessed.

Record target, revision/build, timestamp, tool/version, account alias, result and restricted evidence reference for each test. Use approved synthetic data. Do not expose secrets or PII, validate historical credentials, create privileged identities or change infrastructure unless specifically authorized.

Execute only permitted actions. Passive observations, manual active payloads, writes, automated active scanning and load testing are separate permissions. Respect aggregate limits across tools and accounts and stricter endpoint limits. Stop on agreed error/availability thresholds. Do not bypass a fail-closed guard merely to continue testing.

Triage detector alerts individually. Distinguish advisory matches, source candidates, historical material, observed configuration and reproduced behavior. Preserve source CVSS version/vector/base score unchanged. Assign project priority separately using exposure, sensitivity, exploitability and controls. Do not turn UNKNOWN into zero or a detector alert into a confirmed remote exploit.

Group fixes by root cause and identify affected repositories and consumer release order. Provide concrete fixes and before/after regression criteria. When automatic fixes are excluded, compile recommendations without modifying product code. Treat owner assignment, risk acceptance and approval as explicit decisions.

Produce findings and test registers, a requirement-level coverage matrix, restricted evidence index, resolution plan and matching Markdown/HTML/Excel deliverables. Follow the reporting standard. Preserve partial, blocked, failed, skipped and excluded work; never present incomplete coverage as clearance. Report readiness under the agreed policy. Keep vendor assessment and formal owner/security acceptance distinct from assessor review.
