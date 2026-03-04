#!/usr/bin/env python3
"""Example 18: Webhooks – Rotate secret.

Use GLSPEECH_WEBHOOK_SIDE=stt|tts to pick which client's endpoint.

Usage:
    export GLSPEECH_STT_API_KEY, GLSPEECH_STT_BASE_URL
    export GLSPEECH_TTS_API_KEY, GLSPEECH_TTS_BASE_URL
    export GLSPEECH_WEBHOOK_SIDE="stt" or "tts"
    export GLSPEECH_WEBHOOK_ENDPOINT_ID="endpoint-id"   # required
    python 18_webhooks_rotate_secret.py
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
        print("Set GLSPEECH_WEBHOOK_ENDPOINT_ID.")
        return
    ep = webhook_client.webhooks.rotate_secret(endpoint_id, days=3, hours=0)
    print(f"Rotated secret for endpoint: {ep.id}")


if __name__ == "__main__":
    main()
