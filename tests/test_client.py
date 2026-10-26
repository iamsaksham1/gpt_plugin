"""Unit tests for the GPT client; tests never make live network requests."""

import math
import unittest
from unittest.mock import patch

from gpt_plugin import ChatCompletionClient, ChatCompletionError


class ChatCompletionClientTests(unittest.TestCase):
    def test_missing_key_fails_before_network_call(self):
        with patch.dict("os.environ", {}, clear=True):
            client = ChatCompletionClient(api_key=None)
        with patch("gpt_plugin.client.urlopen") as urlopen:
            with self.assertRaisesRegex(ChatCompletionError, "OPENAI_API_KEY"):
                client.complete([{"role": "user", "content": "Hello"}])
        urlopen.assert_not_called()

    def test_empty_messages_are_rejected(self):
        client = ChatCompletionClient(api_key="test-key")
        with self.assertRaisesRegex(ValueError, "at least one"):
            client.complete([])

    def test_unsupported_message_role_is_rejected_before_network_call(self):
        client = ChatCompletionClient(api_key="test-key")
        messages = [{"role": "invalid_role", "content": "Follow this instruction"}]
        with patch("gpt_plugin.client.urlopen") as urlopen:
            with self.assertRaisesRegex(ValueError, r"messages\[0\]\.role"):
                client.complete(messages)
        urlopen.assert_not_called()

    def test_missing_message_role_is_rejected(self):
        client = ChatCompletionClient(api_key="test-key")
        with self.assertRaisesRegex(ValueError, r"messages\[0\]\.role"):
            client.complete([{"content": "Hello"}])

    def test_non_string_message_content_is_rejected(self):
        client = ChatCompletionClient(api_key="test-key")
        with self.assertRaisesRegex(ValueError, r"messages\[0\]\.content"):
            client.complete([{"role": "user", "content": None}])

    def test_non_dictionary_message_is_rejected(self):
        client = ChatCompletionClient(api_key="test-key")
        with self.assertRaisesRegex(ValueError, r"messages\[0\] must be a dictionary"):
            client.complete(["not a message"])

    def test_blank_or_non_string_model_is_rejected_before_network_call(self):
        client = ChatCompletionClient(api_key="test-key")
        messages = [{"role": "user", "content": "Hello"}]
        for model in ("", "   ", None, 42):
            with self.subTest(model=model):
                with patch("gpt_plugin.client.urlopen") as urlopen:
                    with self.assertRaisesRegex(ValueError, "model must be a non-empty string"):
                        client.complete(messages, model=model)
                urlopen.assert_not_called()

    def test_invalid_temperature_is_rejected_before_network_call(self):
        client = ChatCompletionClient(api_key="test-key")
        messages = [{"role": "user", "content": "Hello"}]
        invalid_values = (-0.1, 2.1, math.nan, math.inf, -math.inf, "0.5", True, 10**1000)
        for temperature in invalid_values:
            with self.subTest(temperature=temperature):
                with patch("gpt_plugin.client.urlopen") as urlopen:
                    with self.assertRaisesRegex(ValueError, "temperature must be a finite number"):
                        client.complete(messages, temperature=temperature)
                urlopen.assert_not_called()

    def test_temperature_is_validated(self):
        client = ChatCompletionClient(api_key="test-key")
        with self.assertRaisesRegex(ValueError, "between 0 and 2"):
            client.complete([{"role": "user", "content": "Hello"}], temperature=2.1)

    def test_timeout_must_be_positive(self):
        with self.assertRaisesRegex(ValueError, "greater than zero"):
            ChatCompletionClient(api_key="test-key", timeout=0)

    def test_returns_assistant_text(self):
        class FakeResponse:
            def __enter__(self):
                return self

            def __exit__(self, *args):
                return False

            def read(self):
                return b'{"choices":[{"message":{"content":"Hello there"}}]}'

        client = ChatCompletionClient(api_key="test-key")
        with patch("gpt_plugin.client.urlopen", return_value=FakeResponse()):
            result = client.complete([{"role": "user", "content": "Hello"}])
        self.assertEqual(result, "Hello there")


if __name__ == "__main__":
    unittest.main()
