#!/usr/bin/env python3
"""Example 16: Webhooks – Update endpoint.

Use GLSPEECH_WEBHOOK_SIDE=stt|tts to pick which client's endpoint to update.

Usage:
    export GLSPEECH_STT_API_KEY, GLSPEECH_STT_BASE_URL
    export GLSPEECH_TTS_API_KEY, GLSPEECH_TTS_BASE_URL
    export GLSPEECH_WEBHOOK_SIDE="stt" or "tts"
    export GLSPEECH_WEBHOOK_ENDPOINT_ID="endpoint-id"
    export GLSPEECH_WEBHOOK_URL="https://updated.example.com/webhook"   # optional
    python 16_webhooks_update_endpoint.py
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
    url = os.getenv("GLSPEECH_WEBHOOK_URL", "https://example.com/webhook-updated")
    event_filters = ["stt.job.completed"] if side == "stt" else ["tts.job.completed"]
    ep = webhook_client.webhooks.update_endpoint(
        endpoint_id=endpoint_id,
        url=url,
        event_filters=event_filters,
        ssl_verification=True,
    )
    print(f"Updated endpoint id={ep.id}")
    print(f"URL: {ep.url}")


if __name__ == "__main__":
    main()
