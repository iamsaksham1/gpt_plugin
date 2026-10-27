"""Unit tests for immutable client configuration."""

import math
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

    def test_environment_rejects_non_positive_or_non_finite_timeouts(self):
        for value in ("0", "-1", "nan", "inf", "-inf"):
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                    ValueError,
                    "OPENAI_TIMEOUT must be a finite number greater than zero",
                ):
                    ClientConfig.from_env({"OPENAI_TIMEOUT": value})

    def test_direct_configuration_rejects_invalid_timeouts(self):
        invalid_timeouts = (
            0,
            -1,
            math.nan,
            math.inf,
            -math.inf,
            True,
            "10",
            10**1000,
        )
        for timeout in invalid_timeouts:
            with self.subTest(timeout=timeout):
                with self.assertRaisesRegex(
                    ValueError, "timeout must be a finite number greater than zero"
                ):
                    ClientConfig(timeout=timeout)

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
