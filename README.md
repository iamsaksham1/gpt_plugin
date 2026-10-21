# GPT Plugin Lab

A small, practical Python foundation for building GPT-powered applications. The project starts with a dependency-free client for OpenAI-compatible chat-completions APIs, then grows through tested, incremental improvements.

## Goals

- Keep API keys out of source control.
- Make requests explicit, configurable, and easy to test.
- Provide readable errors instead of silently swallowing failures.
- Add useful features with tests and clear documentation.

## Quick start

Requires Python 3.11 or newer.

```bash
python -m unittest discover -s tests -v
```

To call an API, set `OPENAI_API_KEY`. The default endpoint is OpenAI's API; `OPENAI_BASE_URL` can point to another OpenAI-compatible provider. Never commit credentials.

## Project roadmap

1. **Foundation:** configuration, HTTP client, and unit tests.
2. **Reliability:** timeouts, error handling, and response validation.
3. **Developer experience:** a small CLI and example prompts.
4. **Application patterns:** structured outputs, retries where appropriate, and usage examples.

## Project principles

- Prefer small, reviewable changes over commit-count padding.
- Test behavior without requiring live API credentials.
- Document limitations and provider-specific assumptions.
- Never put secrets in logs, fixtures, or commits.

## Status

Early-stage project. Features and API compatibility will be documented as they are implemented.
