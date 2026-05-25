#!/usr/bin/env python3
"""Example 24: LiveKit – TTS plugin setup.

Demonstrates how to create and configure the GL Speech TTS plugin
for use with LiveKit agents. The plugin works as a drop-in TTS backend
in a VoicePipelineAgent (see example 25).

Requires: pip install "gl-speech[livekit]"

Usage:
    export GLSPEECH_TTS_API_KEY="your-tts-api-key"
    export GLSPEECH_TTS_WSS_URL="wss://your-tts-websocket-url"
    export GLSPEECH_TTS_MODEL="tts-dimas-formal"  # optional
    python 24_livekit_tts.py
"""

import os

from gl_speech.livekit import TTS

DEFAULT_MODEL = "tts-dimas-formal"


def main():
    tts = TTS(
        api_key=os.getenv("GLSPEECH_TTS_API_KEY"),
        wss_url=os.getenv("GLSPEECH_TTS_WSS_URL"),
        model=os.getenv("GLSPEECH_TTS_MODEL", DEFAULT_MODEL),
    )
    print(f"Provider   : {tts.provider}")
    print(f"Model      : {tts.model}")
    print(f"Sample rate: {tts.sample_rate} Hz")
    print(f"Channels   : {tts.num_channels}")
    print(f"Streaming  : {tts.capabilities.streaming}")
    print()
    print("Pass this plugin to a VoicePipelineAgent (see 25_livekit_agent.py):")
    print("    agent = VoicePipelineAgent(stt=..., llm=..., tts=tts)")


if __name__ == "__main__":
    main()
