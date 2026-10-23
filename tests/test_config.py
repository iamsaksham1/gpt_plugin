"""Unit tests for immutable client configuration."""

import unittest
from dataclasses import FrozenInstanceError

from gpt_plugin import ClientConfig, ChatCompletionClient


class ClientConfigTests(unittest.TestCase):
    def test_from_env_reads_values_from_supplied_mapping(self):
        config = ClientConfig.from_env(
            {
                "OPENAI_API_KEY": "env-key",
                "OPENAI_BASE_URL": "https://provider.example/v1",
                "OPENAI_TIMEOUT": "12.5",
            }
        )
        self.assertEqual(config.api_key, "env-key")
        self.assertEqual(config.base_url, "https://provider.example/v1")
        self.assertEqual(config.timeout, 12.5)

    def test_from_env_uses_defaults(self):
        config = ClientConfig.from_env({})
        self.assertIsNone(config.api_key)
        self.assertEqual(config.base_url, "https://api.openai.com/v1")
        self.assertEqual(config.timeout, 30.0)

    def test_configuration_is_immutable(self):
        config = ClientConfig(api_key="test-key")
        with self.assertRaises(FrozenInstanceError):
            config.timeout = 10.0

    def test_invalid_environment_timeout_has_a_clear_error(self):
        with self.assertRaisesRegex(ValueError, "OPENAI_TIMEOUT must be a number"):
            ClientConfig.from_env({"OPENAI_TIMEOUT": "fast"})

    def test_build_client_uses_the_configuration_snapshot(self):
        config = ClientConfig(
            api_key="snapshot-key",
            base_url="https://provider.example/v1",
            timeout=12.5,
        )
        client = config.build_client()
        self.assertIsInstance(client, ChatCompletionClient)
        self.assertEqual(client.api_key, "snapshot-key")
        self.assertEqual(client.base_url, "https://provider.example/v1")
        self.assertEqual(client.timeout, 12.5)


if __name__ == "__main__":
    unittest.main()
