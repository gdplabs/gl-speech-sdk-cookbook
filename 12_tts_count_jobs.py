#!/usr/bin/env python3
"""Example 12: TTS – Count jobs.

Demonstrates tts_client.tts.count_jobs() – count TTS jobs (optional date/text filters).

Usage:
    export GLSPEECH_TTS_API_KEY="your-tts-api-key"
    export GLSPEECH_TTS_BASE_URL="https://api.prosa.ai/v2/speech/"
    python 12_tts_count_jobs.py
"""

import os

from gl_speech import SpeechClient

DEFAULT_BASE_URL = "https://api.prosa.ai/v2/speech/"


def main():
    tts_client = SpeechClient(
        api_key=os.getenv("GLSPEECH_TTS_API_KEY"),
        base_url=os.getenv("GLSPEECH_TTS_BASE_URL", DEFAULT_BASE_URL),
    )
    count = tts_client.tts.count_jobs()
    print(f"TTS job count: {count}")


if __name__ == "__main__":
    main()
