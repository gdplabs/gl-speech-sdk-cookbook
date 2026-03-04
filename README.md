# GL Speech Examples

Example scripts for the **GL Speech** ([gl-speech on PyPI](https://pypi.org/project/gl-speech/)). Each example uses `from gl_speech import SpeechClient` and demonstrates one or more API endpoints for **Speech-to-Text (STT)**, **Text-to-Speech (TTS)**, and **Webhooks**.

## Prerequisites

1. **Install the library**

   ```bash
   pip install gl-speech
   ```

2. **Environment variables**

   STT and TTS each have their own API key and base URL. Set all four:

   ```bash
   export GLSPEECH_STT_API_KEY="your-stt-api-key"
   export GLSPEECH_STT_BASE_URL="https://api.prosa.ai/v2/speech/"   # or your STT endpoint
   export GLSPEECH_TTS_API_KEY="your-tts-api-key"
   export GLSPEECH_TTS_BASE_URL="https://api.prosa.ai/v2/speech/"   # or your TTS endpoint
   ```

   The examples use two `SpeechClient` instances (one for STT, one for TTS) when keys or URLs differ. If you use a single key and URL for both, you can set `GLSPEECH_API_KEY` and `GLSPEECH_BASE_URL` instead and use one client.

## Examples by endpoint

### STT (Speech-to-Text)

| File                    | Endpoint            | Description                                   |
| ----------------------- | ------------------- | --------------------------------------------- |
| `01_stt_list_models.py` | `stt.list_models()` | List available ASR models                     |
| `02_stt_transcribe.py`  | `stt.transcribe()`  | Submit transcription (minimal WAV, wait=True) |
| `03_stt_list_jobs.py`   | `stt.list_jobs()`   | List STT jobs with pagination                 |
| `04_stt_get_job.py`     | `stt.get_job()`     | Get a single STT job                          |
| `05_stt_get_status.py`  | `stt.get_status()`  | Get STT job status                            |

### TTS (Text-to-Speech)

| File                    | Endpoint            | Description                     |
| ----------------------- | ------------------- | ------------------------------- |
| `06_tts_list_models.py` | `tts.list_models()` | List available TTS models       |
| `07_tts_synthesize.py`  | `tts.synthesize()`  | Synthesize speech from text     |
| `08_tts_list_jobs.py`   | `tts.list_jobs()`   | List TTS jobs                   |
| `09_tts_get_job.py`     | `tts.get_job()`     | Get a single TTS job            |
| `10_tts_get_status.py`  | `tts.get_status()`  | Get TTS job status              |
| `11_tts_archive.py`     | `tts.archive()`     | Archive (soft-delete) a TTS job |
| `12_tts_count_jobs.py`  | `tts.count_jobs()`  | Count TTS jobs                  |

### Webhooks

| File                             | Endpoint                     | Description                     |
| -------------------------------- | ---------------------------- | ------------------------------- |
| `13_webhooks_list_endpoints.py`  | `webhooks.list_endpoints()`  | List webhook endpoints          |
| `14_webhooks_create_endpoint.py` | `webhooks.create_endpoint()` | Create a webhook endpoint       |
| `15_webhooks_get_endpoint.py`    | `webhooks.get_endpoint()`    | Get endpoint details            |
| `16_webhooks_update_endpoint.py` | `webhooks.update_endpoint()` | Update an endpoint              |
| `17_webhooks_delete_endpoint.py` | `webhooks.delete_endpoint()` | Delete an endpoint              |
| `18_webhooks_rotate_secret.py`   | `webhooks.rotate_secret()`   | Rotate endpoint secret          |
| `19_webhooks_list_events.py`     | `webhooks.list_events()`     | List webhook events             |
| `20_webhooks_get_event.py`       | `webhooks.get_event()`       | Get event details               |
| `21_webhooks_test_endpoint.py`   | `webhooks.test_endpoint()`   | Trigger test delivery           |
| `22_webhooks_list_deliveries.py` | `webhooks.list_deliveries()` | List deliveries for an endpoint |

## Optional environment variables

- **`GLSPEECH_WEBHOOK_URL`** – Used by examples 14, 16 for callback URL.
- **`GLSPEECH_WEBHOOK_ENDPOINT_ID`** – Used by webhook examples 15–18, 21, 22.
- **`GLSPEECH_WEBHOOK_SIDE`** – For webhook examples 13–22: `stt` or `tts`. Chooses which client’s webhooks to use (STT job webhooks vs TTS job webhooks). Default: `tts`.
- **`GLSPEECH_WEBHOOK_EVENT_ID`** – Used by example 20.

## Running an example

```bash
export GLSPEECH_STT_API_KEY="your-stt-api-key"
export GLSPEECH_STT_BASE_URL="https://api.prosa.ai/v2/speech/"
export GLSPEECH_TTS_API_KEY="your-tts-api-key"
export GLSPEECH_TTS_BASE_URL="https://api.prosa.ai/v2/speech/"

python examples/01_stt_list_models.py
python examples/07_tts_synthesize.py
python examples/13_webhooks_list_endpoints.py
```

## Quick reference

With separate STT and TTS credentials, use two clients:

```python
from gl_speech import SpeechClient

stt_client = SpeechClient(
    api_key="your-stt-api-key",      # or from GLSPEECH_STT_API_KEY
    base_url="https://...",          # or from GLSPEECH_STT_BASE_URL
)
tts_client = SpeechClient(
    api_key="your-tts-api-key",      # or from GLSPEECH_TTS_API_KEY
    base_url="https://...",          # or from GLSPEECH_TTS_BASE_URL
)
# Webhooks: STT job events use stt_client.webhooks, TTS job events use tts_client.webhooks
stt_client.webhooks.create_endpoint(url="https://...", event_filters=["stt.job.completed"])
tts_client.webhooks.create_endpoint(url="https://...", event_filters=["tts.job.completed"])
stt_client.webhooks.list_endpoints()   # STT webhook endpoints
tts_client.webhooks.list_endpoints()   # TTS webhook endpoints

# STT
stt_client.stt.list_models()
stt_client.stt.transcribe(model="stt-general", data=base64_audio, wait=True)
stt_client.stt.list_jobs(per_page=10)
stt_client.stt.get_job(job_id)
stt_client.stt.get_status(job_id)

# TTS
tts_client.tts.list_models()
tts_client.tts.synthesize(model="tts-dimas-formal", text="Hello", wait=True)
tts_client.tts.list_jobs()
tts_client.tts.get_job(job_id)
tts_client.tts.get_status(job_id)
tts_client.tts.archive(job_id)
tts_client.tts.count_jobs()

# Webhooks (use the client that matches the job type: STT or TTS)
stt_client.webhooks.list_endpoints()
stt_client.webhooks.create_endpoint(url="https://...", event_filters=["stt.job.completed"])
tts_client.webhooks.list_endpoints()
tts_client.webhooks.create_endpoint(url="https://...", event_filters=["tts.job.completed"])
stt_client.webhooks.get_endpoint(endpoint_id)
tts_client.webhooks.update_endpoint(endpoint_id, url="https://...")
tts_client.webhooks.delete_endpoint(endpoint_id)
tts_client.webhooks.rotate_secret(endpoint_id)
tts_client.webhooks.list_events()
tts_client.webhooks.get_event(event_id)
tts_client.webhooks.test_endpoint(endpoint_id)
tts_client.webhooks.list_deliveries(endpoint_id)
```
