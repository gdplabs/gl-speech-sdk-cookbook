#!/usr/bin/env python3
"""Example 03: STT – List jobs.

Demonstrates stt_client.stt.list_jobs() – list STT jobs with optional pagination/filters.

Usage:
    export GLSPEECH_STT_API_KEY="your-stt-api-key"
    export GLSPEECH_STT_BASE_URL="https://api.prosa.ai/v2/speech/"
    python 03_stt_list_jobs.py
"""

import os

from gl_speech import SpeechClient

DEFAULT_BASE_URL = "https://api.prosa.ai/v2/speech/"


def main():
    stt_client = SpeechClient(
        api_key=os.getenv("GLSPEECH_STT_API_KEY"),
        base_url=os.getenv("GLSPEECH_STT_BASE_URL", DEFAULT_BASE_URL),
    )
    response = stt_client.stt.list_jobs(per_page=5)
    print(f"Length: {response.length}")
    print(f"This page: {len(response.data)} jobs")
    for j in response.data[:5]:
        print(f"  - {j.job_id} {j.status}")


if __name__ == "__main__":
    main()
