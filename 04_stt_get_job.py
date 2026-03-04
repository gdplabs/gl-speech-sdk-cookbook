#!/usr/bin/env python3
"""Example 04: STT – Get job.

Demonstrates stt_client.stt.get_job(job_id). Uses the most recent STT job from list_jobs().

Usage:
    export GLSPEECH_STT_API_KEY="your-stt-api-key"
    export GLSPEECH_STT_BASE_URL="https://api.prosa.ai/v2/speech/"
    python 04_stt_get_job.py
"""

import os

from gl_speech import SpeechClient

DEFAULT_BASE_URL = "https://api.prosa.ai/v2/speech/"


def main():
    stt_client = SpeechClient(
        api_key=os.getenv("GLSPEECH_STT_API_KEY"),
        base_url=os.getenv("GLSPEECH_STT_BASE_URL", DEFAULT_BASE_URL),
    )
    resp = stt_client.stt.list_jobs(per_page=1)
    if not resp.data:
        print("No STT jobs. Run 02_stt_transcribe.py first.")
        return
    job_id = resp.data[0].job_id
    job = stt_client.stt.get_job(job_id)
    print(f"Job ID: {job.job_id}")
    print(f"Status: {job.status}")
    if job.result:
        print(f"Result: {job.result[:150]}...")


if __name__ == "__main__":
    main()
