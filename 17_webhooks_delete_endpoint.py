#!/usr/bin/env python3
"""Example 17: Webhooks – Delete endpoint.

Use GLSPEECH_WEBHOOK_SIDE=stt|tts to pick which client's endpoint to delete.

Usage:
    export GLSPEECH_STT_API_KEY, GLSPEECH_STT_BASE_URL
    export GLSPEECH_TTS_API_KEY, GLSPEECH_TTS_BASE_URL
    export GLSPEECH_WEBHOOK_SIDE="stt" or "tts"
    export GLSPEECH_WEBHOOK_ENDPOINT_ID="endpoint-id"   # required
    python 17_webhooks_delete_endpoint.py
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
        print("Set GLSPEECH_WEBHOOK_ENDPOINT_ID to the endpoint to delete.")
        return
    webhook_client.webhooks.delete_endpoint(endpoint_id)
    print(f"Deleted endpoint: {endpoint_id}")


if __name__ == "__main__":
    main()
