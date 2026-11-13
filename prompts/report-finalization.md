# Report finalization prompt

Prepare a standalone [INTERIM / FINAL] security/code-review report from [EVIDENCE MODEL]. Follow [APPROVED TEMPLATE] and `standards/security-reporting.md`. Do not execute new tests or apply fixes unless separately authorized.

Check stable IDs, counts, source revisions, ratings, evidence references and scope. Remove duplicated narrative, chat history, generic boilerplate, self-congratulation, changelog language and tautological headings. Keep required root causes, evidence, reproduction/verification procedures, impact, fixes, dependencies and closure criteria. Each verification procedure must describe that finding's actual evidence; never reuse unrelated generic text.

Keep proposed priority separate from CVSS, detector severity and evidence type. Preserve missing data as unavailable. Identify affected repositories; leave unassigned owners and unagreed dates blank. Separate detector dispositions and quality observations from vulnerabilities.

Format Excel as a review register with identifiers/status/priority visible early, filters, frozen headers and identifier columns, readable wrapping, restrained colors, typed dates/numbers, safe literal strings and editable planning cells. Separate findings, remediation, tests, scope and supporting evidence according to reader need. Preserve existing planning inputs by stable ID.

Generate Markdown and self-contained HTML from the same approved data. Include useful navigation and print behavior. Keep raw evidence restricted. Verify cross-format counts, IDs, source CVSS/revisions, formula errors, redaction, links and rendered layout. Distinguish automated/rendered checks from native Excel or browser workflow acceptance.

Deliver artifacts, validation performed and the exact submission status. Do not invent signatures or promote interim findings into formal security approval.
