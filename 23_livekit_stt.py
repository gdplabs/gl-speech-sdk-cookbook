#!/usr/bin/env python3
"""Example 23: LiveKit – STT plugin setup.

Demonstrates how to create and configure the GL Speech STT plugin
for use with LiveKit agents. The plugin works as a drop-in STT backend
in a VoicePipelineAgent (see example 25).

Requires: pip install "gl-speech[livekit]"

Usage:
    export GLSPEECH_STT_API_KEY="your-stt-api-key"
    export GLSPEECH_STT_WSS_URL="wss://your-stt-websocket-url"
    export GLSPEECH_STT_MODEL="stt-general-online"   # optional
    export GLSPEECH_STT_LANGUAGE="id-ID"             # optional
    python 23_livekit_stt.py
"""

import os

from gl_speech.livekit import STT

DEFAULT_MODEL = "stt-general-online"
DEFAULT_LANGUAGE = "id-ID"


def main():
    stt = STT(
        api_key=os.getenv("GLSPEECH_STT_API_KEY"),
        wss_url=os.getenv("GLSPEECH_STT_WSS_URL"),
        model=os.getenv("GLSPEECH_STT_MODEL", DEFAULT_MODEL),
        language=os.getenv("GLSPEECH_STT_LANGUAGE", DEFAULT_LANGUAGE),
    )
    print(f"Provider : {stt.provider}")
    print(f"Model    : {stt.model}")
    print(f"Streaming: {stt.capabilities.streaming}")
    print(f"Interim  : {stt.capabilities.interim_results}")
    print()
    print("Pass this plugin to a VoicePipelineAgent (see 25_livekit_agent.py):")
    print("    agent = VoicePipelineAgent(stt=stt, llm=..., tts=...)")


if __name__ == "__main__":
    main()
