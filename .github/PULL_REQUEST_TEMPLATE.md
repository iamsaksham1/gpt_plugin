## Summary

<!-- Describe the problem and the behavior this pull request changes. -->

## Related issue

<!-- Link an issue or write "None". -->

## Change type

- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Tests or tooling
- [ ] Refactoring

## Implementation

<!-- Summarize the approach and any notable design decisions. -->

## Validation

<!-- List the exact commands you ran and their results. Do not mark a check complete unless it passed. -->

- [ ] `python -m black --check --diff gpt_plugin tests`
- [ ] `python -m ruff check gpt_plugin tests`
- [ ] `python -m unittest discover -s tests -v`
- [ ] Built a wheel when packaging or distribution files changed
- [ ] Added or updated regression tests for behavior changes

Checks not relevant to this change: explain why.

## Compatibility and documentation

- [ ] Considered the supported Python versions and public API compatibility
- [ ] Updated documentation or examples where behavior or usage changed
- [ ] No documentation update is needed for this change

## Security and data handling

- [ ] No API keys, tokens, private prompts, or customer data are included
- [ ] Any new network or external-input behavior has appropriate validation and offline tests
- [ ] No security-sensitive behavior is introduced, or the relevant implications are documented

## Review checklist

- [ ] The diff is focused and contains no unrelated churn or generated artifacts
- [ ] Tests are deterministic and do not require live provider credentials
- [ ] Limitations and follow-up work are stated accurately
