"""Minimal, dependency-free client for OpenAI-compatible chat completions."""

from __future__ import annotations

import json
import math
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from ._validation import normalize_base_url, validate_timeout


SUPPORTED_MESSAGE_ROLES = frozenset(
    {"system", "developer", "user", "assistant", "tool"}
)


class ChatCompletionError(RuntimeError):
    """Raised for missing credentials or known request and response failures."""


class ChatCompletionClient:
    """Call an OpenAI-compatible chat-completions endpoint.

    The API key is read from the environment unless supplied explicitly.
    Network access is only used when :meth:`complete` is called.
    """

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: float = 30.0,
    ) -> None:
        self.api_key = api_key if api_key is not None else os.getenv("OPENAI_API_KEY")
        if base_url is None:
            base_url = os.getenv("OPENAI_BASE_URL") or "https://api.openai.com/v1"
        self.base_url = normalize_base_url(base_url)
        self.timeout = validate_timeout(timeout)

    def complete(
        self,
        messages: list[dict[str, str]],
        model: str = "gpt-4o-mini",
        temperature: float = 0.7,
    ) -> str:
        """Return the assistant's text response.

        Raises:
            ValueError: If messages or request parameters fail local validation.
            ChatCompletionError: If credentials are missing, an HTTP or
                transport failure occurs, response decoding fails, or the
                provider response lacks a text string at the expected path.

        Invalid documented inputs are rejected before network access. Known
        transport and response failures are normalized to ChatCompletionError;
        unexpected programming errors may still propagate as native exceptions.
        """
        if not self.api_key:
            raise ChatCompletionError(
                "Missing API key. Set OPENAI_API_KEY or pass api_key explicitly."
            )
        if not messages:
            raise ValueError("messages must contain at least one message")
        self._validate_messages(messages)
        if not isinstance(model, str) or not model.strip():
            raise ValueError("model must be a non-empty string")
        if (
            isinstance(temperature, bool)
            or not isinstance(temperature, (int, float))
            or not 0 <= temperature <= 2
            or not math.isfinite(temperature)
        ):
            raise ValueError("temperature must be a finite number between 0 and 2")

        payload = json.dumps(
            {"model": model, "messages": messages, "temperature": temperature}
        ).encode("utf-8")
        request = Request(
            f"{self.base_url}/chat/completions",
            data=payload,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            method="POST",
        )

        try:
            with urlopen(request, timeout=self.timeout) as response:
                body = json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            # Avoid echoing request headers or credentials into error messages.
            raise ChatCompletionError(
                f"API returned HTTP {exc.code} ({exc.reason})."
            ) from None
        except URLError as exc:
            raise ChatCompletionError(f"Could not reach API: {exc.reason}.") from None
        except (TimeoutError, json.JSONDecodeError, UnicodeDecodeError) as exc:
            raise ChatCompletionError(
                f"Could not read a valid API response ({type(exc).__name__})."
            ) from None

        try:
            content = body["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError):
            raise ChatCompletionError(
                "API response did not contain choices[0].message.content."
            ) from None

        if not isinstance(content, str):
            raise ChatCompletionError("API response content was not a text string.")
        return content

    @staticmethod
    def _validate_messages(messages: list[dict[str, str]]) -> None:
        """Reject unsupported chat-message roles and non-text content locally."""
        for index, message in enumerate(messages):
            if not isinstance(message, dict):
                raise ValueError(f"messages[{index}] must be a dictionary")

            role = message.get("role")
            if not isinstance(role, str) or role not in SUPPORTED_MESSAGE_ROLES:
                supported = ", ".join(sorted(SUPPORTED_MESSAGE_ROLES))
                raise ValueError(
                    f"messages[{index}].role must be one of: {supported}"
                )

            if not isinstance(message.get("content"), str):
                raise ValueError(f"messages[{index}].content must be a string")
