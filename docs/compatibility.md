# Python compatibility policy

## Minimum version

GPT Plugin Lab requires **Python 3.11 or newer**, as declared by
`requires-python = ">=3.11"` in `pyproject.toml`.

## Verified CI matrix

The current compatibility baseline is the CPython minor-version matrix exercised
by GitHub Actions:

- Python 3.11
- Python 3.12
- Python 3.13
- Python 3.14

Each matrix job runs the formatting check, Ruff lint, unit tests, wheel build,
and PEP 561 marker verification on `ubuntu-latest`.

A Python version is considered CI-verified only after its matrix job completes
successfully. The open-ended package metadata allows installation on newer
Python versions, but does not by itself claim that an unlisted version has been
tested.

## Platform and implementation scope

The current automated compatibility check covers CPython on Ubuntu. Windows,
macOS, and alternative Python implementations such as PyPy are not yet part of
the CI matrix and should not be inferred as verified.

## Updating the policy

When adding a new CPython minor release:

1. Add it to the workflow matrix.
2. Confirm all matrix checks pass.
3. Update this guide only after successful verification.

The minimum supported Python version should be raised only through an explicit
compatibility decision and a corresponding change to `requires-python`.
