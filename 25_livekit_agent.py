#!/usr/bin/env python3
"""Example 25: LiveKit – full voice pipeline agent.

Demonstrates a complete LiveKit VoicePipelineAgent using GL Speech
STT and TTS plugins. Replace the `llm=` argument with any LLM plugin
supported by livekit-agents (e.g. livekit.plugins.openai).

Requires: pip install "gl-speech[livekit]" livekit-agents livekit-plugins-openai

Usage:
    export GLSPEECH_STT_API_KEY="your-stt-api-key"
    export GLSPEECH_STT_WSS_URL="wss://your-stt-websocket-url"
    export GLSPEECH_TTS_API_KEY="your-tts-api-key"
    export GLSPEECH_TTS_WSS_URL="wss://your-tts-websocket-url"
    export LIVEKIT_URL="wss://your-livekit-server"
    export LIVEKIT_API_KEY="your-livekit-api-key"
    export LIVEKIT_API_SECRET="your-livekit-api-secret"
    export OPENAI_API_KEY="your-openai-api-key"
    python 25_livekit_agent.py start
"""

import asyncio
import os

from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli
from livekit.agents.pipeline import VoicePipelineAgent
from livekit.plugins import openai

from gl_speech.livekit import STT, TTS

stt = STT(
    api_key=os.getenv("GLSPEECH_STT_API_KEY"),
    wss_url=os.getenv("GLSPEECH_STT_WSS_URL"),
    model=os.getenv("GLSPEECH_STT_MODEL", "stt-general-online"),
    language=os.getenv("GLSPEECH_STT_LANGUAGE", "id-ID"),
)

tts = TTS(
    api_key=os.getenv("GLSPEECH_TTS_API_KEY"),
    wss_url=os.getenv("GLSPEECH_TTS_WSS_URL"),
    model=os.getenv("GLSPEECH_TTS_MODEL", "tts-dimas-formal"),
)


async def entrypoint(ctx: JobContext):
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    agent = VoicePipelineAgent(
        stt=stt,
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=tts,
    )
    agent.start(ctx.room)

    await asyncio.sleep(float("inf"))


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
