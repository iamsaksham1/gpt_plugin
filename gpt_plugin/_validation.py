"""Shared validation helpers for client configuration."""

import math
from urllib.parse import urlsplit


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


def normalize_base_url(value: object, *, name: str = "base_url") -> str:
    """Validate and normalize an absolute HTTP(S) provider base URL.

    Surrounding whitespace and trailing slashes are removed. Credentials,
    query strings, fragments, malformed hosts, invalid ports, and non-HTTP(S)
    schemes are rejected so endpoint construction stays unambiguous.
    """
    error = (
        f"{name} must be an absolute HTTP(S) URL without credentials, "
        "query, or fragment"
    )
    if not isinstance(value, str):
        raise ValueError(error)

    url = value.strip()
    if (
        not url
        or any(character.isspace() for character in url)
        or any(ord(character) < 32 for character in url)
        or "\\" in url
        or "?" in url
        or "#" in url
    ):
        raise ValueError(error)

    try:
        parsed = urlsplit(url)
        port = parsed.port
    except ValueError:
        raise ValueError(error) from None

    if (
        parsed.scheme.lower() not in {"http", "https"}
        or not parsed.netloc
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
        or (port is not None and not 1 <= port <= 65535)
    ):
        raise ValueError(error)

    return parsed._replace(scheme=parsed.scheme.lower()).geturl().rstrip("/")
