#!/usr/bin/env python3
"""Example 06: TTS – List models.

Demonstrates tts_client.tts.list_models() – list available TTS models.

Usage:
    export GLSPEECH_TTS_API_KEY="your-tts-api-key"
    export GLSPEECH_TTS_BASE_URL="https://api.prosa.ai/v2/speech/"
    python 06_tts_list_models.py
"""

import os

from gl_speech import SpeechClient

DEFAULT_BASE_URL = "https://api.prosa.ai/v2/speech/"


def main():
    tts_client = SpeechClient(
        api_key=os.getenv("GLSPEECH_TTS_API_KEY"),
        base_url=os.getenv("GLSPEECH_TTS_BASE_URL", DEFAULT_BASE_URL),
    )
    models = tts_client.tts.list_models()
    print(f"TTS models: {len(models)}")
    for m in models[:10]:
        print(f"  - {m.get('name', m)}")
    if len(models) > 10:
        print(f"  ... and {len(models) - 10} more")


if __name__ == "__main__":
    main()
