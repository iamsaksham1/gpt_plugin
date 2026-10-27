"""Shared validation helpers for client configuration."""

import math


def validate_timeout(value: object, *, name: str = "timeout") -> float:
    """Return a finite, positive timeout as a float.

    Booleans are rejected even though bool is an int subclass. Converting to
    float inside the guarded block also handles integers too large to convert.
    """
    error = f"{name} must be a finite number greater than zero"
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(error)

    try:
        timeout = float(value)
    except (OverflowError, ValueError):
        raise ValueError(error) from None

    if not math.isfinite(timeout) or timeout <= 0:
        raise ValueError(error)
    return timeout
