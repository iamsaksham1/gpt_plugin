"""Immutable configuration for GPT Plugin Lab clients."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Mapping

from ._validation import normalize_base_url, validate_timeout

DEFAULT_BASE_URL = "https://api.openai.com/v1"
DEFAULT_TIMEOUT = 30.0


@dataclass(frozen=True, slots=True)
class ClientConfig:
    """Snapshot of the settings used to construct a chat-completions client."""

    api_key: str | None = None
    base_url: str = DEFAULT_BASE_URL
    timeout: float = DEFAULT_TIMEOUT

    def __post_init__(self) -> None:
        object.__setattr__(self, "base_url", normalize_base_url(self.base_url))
        object.__setattr__(self, "timeout", validate_timeout(self.timeout))

    @classmethod
    def from_env(
        cls, environ: Mapping[str, str] | None = None
    ) -> "ClientConfig":
        """Load configuration from environment variables.

        An optional mapping can be supplied to make configuration loading
        deterministic in tests or applications that manage their own settings.
        """
        source = os.environ if environ is None else environ
        raw_timeout = source.get("OPENAI_TIMEOUT")
        if raw_timeout is None or not raw_timeout.strip():
            timeout = DEFAULT_TIMEOUT
        else:
            try:
                timeout = float(raw_timeout)
            except ValueError:
                raise ValueError("OPENAI_TIMEOUT must be a number.") from None

        timeout = validate_timeout(timeout, name="OPENAI_TIMEOUT")

        return cls(
            api_key=source.get("OPENAI_API_KEY"),
            base_url=source.get("OPENAI_BASE_URL") or DEFAULT_BASE_URL,
            timeout=timeout,
        )

    def build_client(self):
        """Build a client using this snapshot, without re-reading the environment."""
        from .client import ChatCompletionClient

        return ChatCompletionClient(
            api_key=self.api_key if self.api_key is not None else "",
            base_url=self.base_url,
            timeout=self.timeout,
        )
