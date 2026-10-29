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

To call an API, set `OPENAI_API_KEY`. The default endpoint is OpenAI's API; `OPENAI_BASE_URL` can point to another OpenAI-compatible provider. Never commit credentials. See the [configuration guide](docs/configuration.md) for variable defaults, precedence, and local setup, and the [error guide](docs/errors.md) for public exceptions and failure guarantees.

## 365-day project roadmap

The full day-by-day plan lives in [ROADMAP.md](ROADMAP.md). It covers configuration, client reliability, GPT capabilities, provider support, persistence, retrieval-augmented generation (RAG), controlled tool use, security, evaluation, application integrations, deployment, and release engineering.

Progress is tracked by calendar project day, not commit count. A day is marked complete only after a meaningful change is committed and verified; empty or backfilled commits are not part of the plan.

## Project principles

- Prefer small, reviewable changes over commit-count padding.
- Test behavior without requiring live API credentials.
- Document limitations and provider-specific assumptions.
- Never put secrets in logs, fixtures, or commits.

## Status

Early-stage project. Features and API compatibility will be documented as they are implemented.
