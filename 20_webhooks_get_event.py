#!/usr/bin/env python3
"""Example 20: Webhooks – Get event.

Use GLSPEECH_WEBHOOK_SIDE=stt|tts to get event from that side.

Usage:
    export GLSPEECH_STT_API_KEY, GLSPEECH_STT_BASE_URL
    export GLSPEECH_TTS_API_KEY, GLSPEECH_TTS_BASE_URL
    export GLSPEECH_WEBHOOK_SIDE="stt" or "tts"
    export GLSPEECH_WEBHOOK_EVENT_ID="event-id"   # optional; uses first from list
    python 20_webhooks_get_event.py
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
    event_id = os.getenv("GLSPEECH_WEBHOOK_EVENT_ID")
    if not event_id:
        events = webhook_client.webhooks.list_events()
        if not events:
            print("No events. Set GLSPEECH_WEBHOOK_EVENT_ID.")
            return
        event_id = events[0].id
    ev = webhook_client.webhooks.get_event(event_id)
    print(f"Event ID: {ev.id}")


if __name__ == "__main__":
    main()
