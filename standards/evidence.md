# Evidence standard

Every verification record identifies target, source revision/build where known, environment, time, tool/version, method, expected result, observed result and evidence reference. Unknown values remain unknown.

| Evidence | What it can establish |
| --- | --- |
| Build | Compilation under the recorded toolchain |
| Source review | Behavior visible in the inspected source and callers |
| Unit/regression test | The tested assertions in that source environment |
| Integration test | Interactions actually exercised with recorded dependencies |
| Runtime request | The sampled route, account and response under those conditions |
| Rendered artifact | The inspected layout and supported interactions |
| Formal approval | The explicit decision recorded by an authorized approver |

Keep raw evidence immutable, restricted and outside Git. Store a hash index and sanitized references. Do not distribute real request bodies, credentials or PII. Preserve failed attempts and harness errors privately; do not classify an invalid harness assertion as a product vulnerability.

Coverage is separate from outcome. A passing subcheck does not complete a broader case. Never discard skips or merge overlapping helper assertions into a misleading unique test count. Record test applicability and remaining work explicitly.
