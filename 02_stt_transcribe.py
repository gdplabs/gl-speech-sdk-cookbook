#!/usr/bin/env python3
"""Example 02: STT – Transcribe.

Demonstrates stt_client.stt.transcribe() – submit speech-to-text (with minimal WAV).

Usage:
    export GLSPEECH_STT_API_KEY="your-stt-api-key"
    export GLSPEECH_STT_BASE_URL="https://api.prosa.ai/v2/speech/"  # optional
    python 02_stt_transcribe.py
"""

import base64
import os
import struct

from gl_speech import SpeechClient

DEFAULT_BASE_URL = "https://api.prosa.ai/v2/speech/"


def minimal_wav_base64() -> str:
    """Minimal valid WAV (16kHz mono, 0.1s silence) as base64."""
    sample_rate = 16000
    num_channels = 1
    bits_per_sample = 16
    num_samples = 1600
    audio_data = b"\x00\x00" * num_samples
    data_size = len(audio_data)
    fmt_chunk_size = 16
    file_size = 4 + (8 + fmt_chunk_size) + (8 + data_size)
    wav = b"RIFF"
    wav += struct.pack("<I", file_size)
    wav += b"WAVEfmt "
    wav += struct.pack("<I", fmt_chunk_size)
    wav += struct.pack("<HHIIHH", 1, num_channels, sample_rate,
                       sample_rate * num_channels * bits_per_sample // 8,
                       num_channels * bits_per_sample // 8, bits_per_sample)
    wav += b"data" + struct.pack("<I", data_size) + audio_data
    return base64.b64encode(wav).decode("utf-8")


def main():
    stt_client = SpeechClient(
        api_key=os.getenv("GLSPEECH_STT_API_KEY"),
        base_url=os.getenv("GLSPEECH_STT_BASE_URL", DEFAULT_BASE_URL),
    )
    models = stt_client.stt.list_models()
    model = models[0].get("name", "stt-general") if models else "stt-general"
    audio_b64 = minimal_wav_base64()
    result = stt_client.stt.transcribe(
        model=model,
        data=audio_b64,
        wait=True,
        label="example-transcribe",
    )
    print(f"Job ID: {result.job_id}")
    print(f"Status: {result.status}")
    if result.result:
        print(f"Result: {result.result[:200]}...")


if __name__ == "__main__":
    main()
