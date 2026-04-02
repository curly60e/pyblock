"""Astrolexis API client for PyBLOCK AI.

Handles authentication, top-up via Lightning, chat queries (streaming),
and usage tracking. All AI queries go through Astrolexis gateway.
"""

import json
import os

import requests

ASTROLEXIS_API = os.getenv("ASTROLEXIS_API", "https://api.astrolexis.space")


class AstrolexisClient:
    """Client for the Astrolexis AI Gateway."""

    def __init__(self, token, base_url=None):
        self.token = token
        self.base_url = (base_url or ASTROLEXIS_API).rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def verify(self):
        """Verify token and get balance."""
        r = requests.post(
            f"{self.base_url}/v1/auth/verify",
            headers=self.headers, timeout=10
        )
        r.raise_for_status()
        return r.json()

    def get_balance(self):
        """Get current balance in sats."""
        return self.verify()["balance_sats"]

    def topup(self, amount_sats):
        """Create a Lightning invoice for top-up."""
        r = requests.post(
            f"{self.base_url}/v1/topup",
            headers=self.headers,
            json={"amount": amount_sats},
            timeout=10,
        )
        r.raise_for_status()
        return r.json()

    def check_payment(self, payment_hash):
        """Check if a top-up invoice has been paid."""
        r = requests.get(
            f"{self.base_url}/v1/topup/check/{payment_hash}",
            headers=self.headers, timeout=10,
        )
        r.raise_for_status()
        return r.json()["paid"]

    def chat(self, messages, node_context=None,
             model="claude-sonnet-4-6", stream=True):
        """Send a chat query. Returns dict or yields SSE chunks."""
        payload = {
            "model": model,
            "messages": messages,
            "stream": stream,
            "max_tokens": 2048,
        }
        if node_context:
            payload["node_context"] = node_context

        if not stream:
            r = requests.post(
                f"{self.base_url}/v1/chat",
                headers=self.headers,
                json=payload,
                timeout=60,
            )
            r.raise_for_status()
            return r.json()

        return self._stream_chat(payload)

    def _stream_chat(self, payload):
        """Internal generator for streaming chat responses."""
        r = requests.post(
            f"{self.base_url}/v1/chat",
            headers=self.headers,
            json=payload,
            stream=True,
            timeout=60,
        )
        r.raise_for_status()

        for line in r.iter_lines(decode_unicode=True):
            if line and line.startswith("data: "):
                data = line[6:]
                if data == "[DONE]":
                    break
                try:
                    yield json.loads(data)
                except json.JSONDecodeError:
                    continue

    def usage(self, days=30):
        """Get usage statistics."""
        r = requests.get(
            f"{self.base_url}/v1/usage?days={days}",
            headers=self.headers, timeout=10,
        )
        r.raise_for_status()
        return r.json()
