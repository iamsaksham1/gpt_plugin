# Configuration guide

GPT Plugin Lab reads configuration from environment variables. It does not load `.env` files automatically, and it never needs a real API key for the unit tests.

## Supported variables

| Variable | Required | Default | Purpose |
| --- | --- | --- | --- |
| `OPENAI_API_KEY` | For live API calls | Unset | Bearer token sent to the provider. |
| `OPENAI_BASE_URL` | No | `https://api.openai.com/v1` | Base URL for an OpenAI-compatible API. |
| `OPENAI_TIMEOUT` | No | `30` seconds | Network timeout used by the client. |

`OPENAI_TIMEOUT` must be numeric and finite, and the client requires a positive timeout. Provider base URLs are validated and normalized: surrounding whitespace and trailing slashes are removed, the scheme is lowercased, and credentials, query strings, fragments, malformed hosts, and invalid ports are rejected. Use a trusted provider URL. See the [error guide](errors.md) for the current exception contract.

## Configuration precedence

There are two explicit ways to configure the client:

1. **Construct `ClientConfig` directly.** Values passed to the dataclass win; omitted fields use the dataclass defaults. Direct construction does not read the environment.
2. **Call `ClientConfig.from_env()`.** Values present in the environment override the defaults for the corresponding fields; absent or blank `OPENAI_BASE_URL` and `OPENAI_TIMEOUT` use their defaults. `OPENAI_API_KEY` remains unset if it is not provided.

After creating a config, `config.build_client()` uses that snapshot and does not re-read the environment. Alternatively, the lower-level `ChatCompletionClient` accepts explicit constructor arguments; when an argument is omitted, that client reads the corresponding environment variable where supported.

Example:

```python
from gpt_plugin import ClientConfig

config = ClientConfig.from_env()
client = config.build_client()
reply = client.complete(
    [{"role": "user", "content": "Explain what an API client does in one sentence."}]
)
print(reply)
```

The example makes a real network request and requires a valid API key and provider access. Do not run it in automated tests unless you deliberately configure a live integration test.

## Local setup (macOS/Linux)

From the repository root:

```bash
cp .env.example .env
```

Edit `.env` and put your key after `OPENAI_API_KEY=`. Keep the file private. To load the assignments into the current shell session:

```bash
set -a
. ./.env
set +a
```

Then run your Python program from that same shell. This shell command loads environment variables; the Python package itself does **not** parse `.env` files. Never commit a populated `.env` file or paste keys into source code, issues, logs, or screenshots.

For a one-off shell session, you can instead export the variable directly:

```bash
export OPENAI_API_KEY="your-key-here"
# Optional:
export OPENAI_BASE_URL="https://api.openai.com/v1"
export OPENAI_TIMEOUT="30"
```

Replace the placeholder locally; do not put a real key into the repository.

## Verify without calling an API

Run the offline test suite:

```bash
python -m unittest discover -s tests -v
```

Tests should not require a real credential or make live network requests. If a request reports a missing API key, verify that `OPENAI_API_KEY` is set in the same shell that launches Python. If a custom provider fails, check its base URL and whether it supports the chat-completions endpoint.
