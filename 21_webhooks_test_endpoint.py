#!/usr/bin/env python3
"""Example 21: Webhooks – Test endpoint.

Use GLSPEECH_WEBHOOK_SIDE=stt|tts to test endpoint on that side.

Usage:
    export GLSPEECH_STT_API_KEY, GLSPEECH_STT_BASE_URL
    export GLSPEECH_TTS_API_KEY, GLSPEECH_TTS_BASE_URL
    export GLSPEECH_WEBHOOK_SIDE="stt" or "tts"
    export GLSPEECH_WEBHOOK_ENDPOINT_ID="endpoint-id"   # optional; uses first from list
    python 21_webhooks_test_endpoint.py
"""

import os

from gl_speech import SpeechClient

DEFAULT_BASE_URL = "https://api.prosa.ai/v2/speech/"


def main():
    stt_client = SpeechClient(
        api_key=os.getenv("GLSPEECH_STT_API_KEY"),
        base_url=os.getenv("GLSPEECH_STT_BASE_URL", DEFAULT_BASE_URL),
    )
    tts_client = SpeechClient(
        api_key=os.getenv("GLSPEECH_TTS_API_KEY"),
        base_url=os.getenv("GLSPEECH_TTS_BASE_URL", DEFAULT_BASE_URL),
    )
    side = os.getenv("GLSPEECH_WEBHOOK_SIDE", "tts").lower()
    webhook_client = stt_client if side == "stt" else tts_client
    endpoint_id = os.getenv("GLSPEECH_WEBHOOK_ENDPOINT_ID")
    if not endpoint_id:
        endpoints = webhook_client.webhooks.list_endpoints()
        if not endpoints:
            print("No endpoints. Set GLSPEECH_WEBHOOK_ENDPOINT_ID.")
            return
        endpoint_id = endpoints[0].id
    ticket = webhook_client.webhooks.test_endpoint(endpoint_id)
    print(f"Delivery tag: {ticket.delivery_tag}")
    print(f"Endpoint ID: {ticket.endpoint_id}")


if __name__ == "__main__":
    main()
