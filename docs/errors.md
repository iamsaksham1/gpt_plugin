# Errors and failure guarantees

This guide describes the exceptions currently exposed by the synchronous
`ChatCompletionClient`. The client does not retry requests automatically.

## Exception types

| Exception | When it is raised | What callers can rely on |
| --- | --- | --- |
| `ValueError` | Invalid constructor settings (such as a malformed base URL or a non-positive/non-finite timeout), an empty message list, malformed messages, unsupported message roles, non-string message content, a blank/non-string model name, or a temperature outside the finite numeric range 0–2. | These documented validation failures are detected before a network request is sent. |
| `ChatCompletionError` | The API key is missing; the HTTP request returns an HTTP error; the provider cannot be reached; reading or decoding the response times out or fails; or the response lacks the expected text-content field. | Known request and response failures are presented as a single library-specific runtime exception. |

Import the public exception types from the package:

```python
from gpt_plugin import ChatCompletionClient, ChatCompletionError

client = ChatCompletionClient()
try:
    answer = client.complete([{"role": "user", "content": "Hello"}])
except ValueError as exc:
    # Fix the local input or configuration.
    print(f"Invalid request: {exc}")
except ChatCompletionError as exc:
    # Handle missing credentials, transport failures, or unusable responses.
    print(f"Chat completion failed: {exc}")
```

The example requires a configured API key if it is run; it is illustrative and
does not make a request as part of the documentation build.

## Error-message and security behavior

- Missing credentials are reported before opening a network connection.
- HTTP failures report the HTTP status code and reason, not the response body.
- The client does not put request headers into its formatted HTTP error message,
  so the bearer-token header is not intentionally echoed there.
- Transport, timeout, decoding, and response-shape failures are converted to
  `ChatCompletionError` with a short explanation.
- Do not assume arbitrary exception text from third-party runtimes or custom
  provider infrastructure is safe to publish. Avoid logging credentials and
  review exception messages before returning them to end users.

## Current limits

- Automatic retries and rate-limit backoff are not implemented yet.
- The client returns only assistant text; it does not yet expose structured
  provider error payloads or response metadata.
- Only the documented validation cases are normalized to `ValueError`.
  Unexpected programming errors or unsupported objects outside the documented
  input shape may still raise their native Python exceptions.

These guarantees describe the current implementation and may be refined as
retry handling, typed results, and richer provider support are added.
