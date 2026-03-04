#!/usr/bin/env python3
"""Example 11: TTS – Archive job.

Demonstrates tts_client.tts.archive(job_id) – soft-delete a TTS job. Uses the most recent TTS job from list_jobs().

Usage:
    export GLSPEECH_TTS_API_KEY="your-tts-api-key"
    export GLSPEECH_TTS_BASE_URL="https://api.prosa.ai/v2/speech/"
    python 11_tts_archive.py
"""

import os

from gl_speech import SpeechClient

DEFAULT_BASE_URL = "https://api.prosa.ai/v2/speech/"


def main():
    tts_client = SpeechClient(
        api_key=os.getenv("GLSPEECH_TTS_API_KEY"),
        base_url=os.getenv("GLSPEECH_TTS_BASE_URL", DEFAULT_BASE_URL),
    )
    resp = tts_client.tts.list_jobs(per_page=1)
    if not resp.data:
        print("No TTS jobs. Run 07_tts_synthesize.py first.")
        return
    job_id = resp.data[0].job_id
    result = tts_client.tts.archive(job_id)
    print(f"Archived job: {result.job_id}")
    print(f"Status: {result.status}")


if __name__ == "__main__":
    main()
