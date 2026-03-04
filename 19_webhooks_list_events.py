#!/usr/bin/env python3
"""Example 19: Webhooks – List events.

Use GLSPEECH_WEBHOOK_SIDE=stt|tts to list events for that side.

Usage:
    export GLSPEECH_STT_API_KEY, GLSPEECH_STT_BASE_URL
    export GLSPEECH_TTS_API_KEY, GLSPEECH_TTS_BASE_URL
    export GLSPEECH_WEBHOOK_SIDE="stt" or "tts"
    python 19_webhooks_list_events.py
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
    events = webhook_client.webhooks.list_events()
    print(f"Events: {len(events)}")
    for e in events[:10]:
        print(f"  - id={e.id} event_type={e.event_type}")
    if len(events) > 10:
        print(f"  ... and {len(events) - 10} more")


if __name__ == "__main__":
    main()
