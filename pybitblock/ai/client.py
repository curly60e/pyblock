"""Astrolexis API client for PyBLOCK AI.

Handles authentication, top-up via Lightning, chat queries (streaming),
and usage tracking. All AI queries go through Astrolexis gateway.
"""

import json
import os

import requests

ASTROLEXIS_API = os.getenv("ASTROLEXIS_API", "https://api.astrolexis.space")
ASTROLEXIS_API_LOCAL = os.getenv("ASTROLEXIS_API_LOCAL", "http://localhost:10400")


class AstrolexisClient:
    """Client for the Astrolexis AI Gateway."""

    def __init__(self, token, base_url=None):
        self.token = token
        self.base_url = (base_url or ASTROLEXIS_API).rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def _request(self, method, path, **kwargs):
        """Make request with automatic local fallback."""
        kwargs.setdefault("timeout", 10)
        url = f"{self.base_url}{path}"
        try:
            r = method(url, headers=self.headers, **kwargs)
            if r.status_code == 404 and self.base_url != ASTROLEXIS_API_LOCAL:
                # Fallback to local if available
                r = method(
                    f"{ASTROLEXIS_API_LOCAL}{path}",
                    headers=self.headers, **kwargs
                )
            r.raise_for_status()
            return r
        except requests.exceptions.ConnectionError:
            if self.base_url != ASTROLEXIS_API_LOCAL:
                r = method(
                    f"{ASTROLEXIS_API_LOCAL}{path}",
                    headers=self.headers, **kwargs
                )
                r.raise_for_status()
                return r
            raise

    def verify(self):
        """Verify token and get balance."""
        r = self._request(requests.post, "/v1/auth/verify")
        return r.json()

    def get_balance(self):
        """Get current balance in sats."""
        return self.verify()["balance_sats"]

    def topup(self, amount_sats):
        """Create a Lightning invoice for top-up."""
        r = self._request(requests.post, "/v1/topup", json={"amount": amount_sats})
        return r.json()

    def check_payment(self, payment_hash):
        """Check if a top-up invoice has been paid."""
        r = self._request(requests.get, f"/v1/topup/check/{payment_hash}")
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
            r = self._request(requests.post, "/v1/chat", json=payload, timeout=60)
            return r.json()

        return self._stream_chat(payload)

    def _stream_chat(self, payload):
        """Internal generator for streaming chat responses."""
        r = self._request(
            requests.post, "/v1/chat", json=payload, stream=True, timeout=60
        )

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
        r = self._request(requests.get, f"/v1/usage?days={days}")
        return r.json()
