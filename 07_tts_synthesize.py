#!/usr/bin/env python3
"""Example 07: TTS – Synthesize.

Demonstrates tts_client.tts.synthesize() – text-to-speech (short text, wait=True).

Usage:
    export GLSPEECH_TTS_API_KEY="your-tts-api-key"
    export GLSPEECH_TTS_BASE_URL="https://api.prosa.ai/v2/speech/"
    python 07_tts_synthesize.py
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
    model = models[0].get("name", "tts-dimas-formal") if models else "tts-dimas-formal"
    result = tts_client.tts.synthesize(
        model=model,
        text="Halo, ini contoh sintesis suara.",
        wait=True,
        label="example-synthesize",
    )
    print(f"Job ID: {result.job_id}")
    print(f"Status: {result.status}")
    if result.result:
        print(f"Result (base64 length): {len(result.result)}")


if __name__ == "__main__":
    main()
