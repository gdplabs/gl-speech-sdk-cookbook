#!/usr/bin/env python3
"""Example 01: STT – List models.

Demonstrates stt_client.stt.list_models() – list available ASR models.

Usage:
    export GLSPEECH_STT_API_KEY="your-stt-api-key"
    export GLSPEECH_STT_BASE_URL="https://api.prosa.ai/v2/speech/"  # optional
    python 01_stt_list_models.py
"""

import os

from gl_speech import SpeechClient

DEFAULT_BASE_URL = "https://api.prosa.ai/v2/speech/"


def main():
    stt_client = SpeechClient(
        api_key=os.getenv("GLSPEECH_STT_API_KEY"),
        base_url=os.getenv("GLSPEECH_STT_BASE_URL", DEFAULT_BASE_URL),
    )
    models = stt_client.stt.list_models()
    print(f"STT models: {len(models)}")
    for m in models[:10]:
        print(f"  - {m.get('name', m)}")
    if len(models) > 10:
        print(f"  ... and {len(models) - 10} more")


if __name__ == "__main__":
    main()
