# Security and code-review report standard

Use the engagement's required template first. This kit supplies working conventions, not certification or a universal mandatory spreadsheet standard.

## Finding record

Stable ID; repository; title; status; evidence type; proposed priority and rationale; source CVSS version/score/vector; CWE/standard references where supported; detector and severity; file/line or endpoint; source/build; condition; impact/reachability; root cause; finding-specific verification procedure; restricted evidence reference; recommended fix; dependencies; regression/closure criteria; owner; issue/PR; due date; fix revision; retest and residual risk.

Distinguish historical candidates, package matches, observed configuration, reproduced primitives and demonstrated exploits. A scoped detector disposition is separate from a confirmed vulnerability and from accepted risk. Never create a CVSS score from a project's P-level.

## Excel register

Put summary and findings first, then remediation and coverage. Supporting advisory, SAST, quality, route, secret and ASVS tabs are useful only when the evidence requires them. Keep quality observations separate from security findings.

- Put ID, repository, title, status and priority near the left.
- Use filterable tables, frozen headers and identifier columns, one readable font and restrained fills.
- Keep dates/numbers typed. CVSS blanks mean unavailable, not zero. Preserve deliberate zero values.
- Wrap descriptions; fit row heights without clipping. Do not force all columns onto one printed page.
- Mark editable assignment, due date, action state, issue link, fix revision, retest and closure evidence fields. Preserve edits by finding ID during regeneration.
- Use status validation and formula-linked totals where supported. Do not count an item closed solely because code was committed.
- Export untrusted text safely: values beginning with =, +, -, @, tabs or line breaks must remain literal text. CSV consumers can interpret leading apostrophes differently; verify the intended importer.
- Check identifiers, totals, formulas, links, rendering and export integrity. Record whether native Excel was actually tested.

## Narrative report

Include document/date/assessor/status, executive summary and readiness, scope/method/tools/versions/accounts, requirement mapping, case results/coverage, findings, remediation sequence, risk acceptance, remaining work, evidence references and approval.

State material limits once and retain finding-specific uncertainty. Use standalone current-state prose. Exclude chat history, changelog phrasing, self-assessment and repeated boilerplate. Keep required technical detail even when the summary is shortened.

An interim report can be submitted for review while tests and remediation remain open. Final technical completion and formal owner/security approval are separate gates. Configure the engagement's P1/P2 acceptance and vendor-readiness policy explicitly.

## ASVS and evidence

Record the selected standard/version, requirement applicability, result, evidence, revision, method, owner and remaining verification. Obtain official requirement text and preserve attribution/license. This kit contains only a blank schema, not an official checklist or a compliance claim.
