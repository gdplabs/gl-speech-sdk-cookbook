#!/usr/bin/env python3
"""Example 08: TTS – List jobs.

Demonstrates tts_client.tts.list_jobs() – list TTS jobs with optional filters.

Usage:
    export GLSPEECH_TTS_API_KEY="your-tts-api-key"
    export GLSPEECH_TTS_BASE_URL="https://api.prosa.ai/v2/speech/"
    python 08_tts_list_jobs.py
"""

import os

from gl_speech import SpeechClient

DEFAULT_BASE_URL = "https://api.prosa.ai/v2/speech/"


def main():
    tts_client = SpeechClient(
        api_key=os.getenv("GLSPEECH_TTS_API_KEY"),
        base_url=os.getenv("GLSPEECH_TTS_BASE_URL", DEFAULT_BASE_URL),
    )
    response = tts_client.tts.list_jobs(per_page=5)
    print(f"Length: {response.length}")
    print(f"This page: {len(response.data)} jobs")
    for j in response.data[:5]:
        print(f"  - {j.job_id} {j.status}")


if __name__ == "__main__":
    main()
