#!/usr/bin/env python3
"""Example 14: Webhooks – Create endpoint.

STT job webhooks use stt_client; TTS job webhooks use tts_client. Set
GLSPEECH_WEBHOOK_SIDE to "stt" or "tts" and use event_filters for that side.

Usage:
    export GLSPEECH_STT_API_KEY="your-stt-api-key"
    export GLSPEECH_STT_BASE_URL="https://api.prosa.ai/v2/speech/"
    export GLSPEECH_TTS_API_KEY="your-tts-api-key"
    export GLSPEECH_TTS_BASE_URL="https://api.prosa.ai/v2/speech/"
    export GLSPEECH_WEBHOOK_SIDE="stt" or "tts"
    export GLSPEECH_WEBHOOK_URL="https://your-server.com/webhook"   # optional
    python 14_webhooks_create_endpoint.py
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
    url = os.getenv("GLSPEECH_WEBHOOK_URL", "https://example.com/webhook")
    event_filters = ["stt.job.completed"] if side == "stt" else ["tts.job.completed"]
    ep = webhook_client.webhooks.create_endpoint(
        url=url,
        event_filters=event_filters,
        ssl_verification=True,
    )
    print(f"Created endpoint id={ep.id} ({side})")
    print(f"URL: {ep.url}")


if __name__ == "__main__":
    main()
