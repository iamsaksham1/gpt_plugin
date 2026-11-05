# Contributing to GPT Plugin Lab

Thank you for helping improve GPT Plugin Lab. The project favors small, reviewable changes that are tested offline, documented clearly, and safe to run without provider credentials.

## Prerequisites

- Python 3.11 or newer
- Git
- pip

The minimum Python version is declared in `pyproject.toml`. The versions and platforms exercised by continuous integration are described in [the compatibility policy](docs/compatibility.md).

## Set up a local development environment

Clone the repository and enter its directory:

```bash
git clone https://github.com/iamsaksham1/gpt_plugin.git
cd gpt_plugin
```

Create and activate a virtual environment.

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the package in editable mode with its development tools:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run the checks

Run these commands from the repository root. They match the core checks in GitHub Actions:

```bash
python -m black --check --diff gpt_plugin tests
python -m ruff check gpt_plugin tests
python -m unittest discover -s tests -v
```

The unit tests use mocked HTTP responses and do not require an API key or make live provider requests. Keep tests deterministic and add regression coverage for changed behavior.

To verify that a wheel can be built locally:

```bash
python -m pip wheel . --no-deps --wheel-dir dist
```

GitHub Actions also checks that the built wheel contains the PEP 561 `gpt_plugin/py.typed` marker.

## Make a change

1. Start from an up-to-date `main` branch and create a focused feature or fix branch.
2. Keep the change scoped to one concern; avoid unrelated formatting or generated-file churn.
3. Add or update unit tests for behavior changes, including relevant invalid-input and failure cases.
4. Update documentation when public behavior, configuration, compatibility, or usage changes.
5. Run formatting, linting, and unit tests before opening a pull request.
6. Review the final diff for accidental secrets, local files, debug output, and unrelated changes.

Do not commit API keys, access tokens, private prompts, or real customer data. The test suite should remain runnable without `OPENAI_API_KEY`; do not add live API calls to routine unit tests.

## Pull requests

- Explain the problem and the intended behavior.
- Summarize the implementation and any compatibility implications.
- List the checks you ran and their results. Do not describe a check as passing unless it completed successfully.
- Link related issues when applicable.
- Call out limitations or follow-up work rather than implying unfinished behavior is complete.

Keep pull requests small enough to review. A change is ready when its behavior is tested, its documentation is accurate, and the automated checks pass.
