#!/usr/bin/env python3
"""Example 13: Webhooks – List endpoints.

Demonstrates list_endpoints() for STT or TTS webhooks. STT job webhooks use the STT
client; TTS job webhooks use the TTS client. Choose with GLSPEECH_WEBHOOK_SIDE.

Usage:
    export GLSPEECH_STT_API_KEY="your-stt-api-key"
    export GLSPEECH_STT_BASE_URL="https://api.prosa.ai/v2/speech/"
    export GLSPEECH_TTS_API_KEY="your-tts-api-key"
    export GLSPEECH_TTS_BASE_URL="https://api.prosa.ai/v2/speech/"
    export GLSPEECH_WEBHOOK_SIDE="stt" or "tts"   # which client's webhooks to list (default: tts)
    python 13_webhooks_list_endpoints.py
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
    endpoints = webhook_client.webhooks.list_endpoints()
    print(f"Endpoints ({side}): {len(endpoints)}")
    for ep in endpoints:
        print(f"  - id={ep.id} url={ep.url[:50]!r}...")


if __name__ == "__main__":
    main()
