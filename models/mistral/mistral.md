# Mistral API - Voxtral

**Direct API Access**: Yes (api.mistral.ai)

Docs: https://docs.mistral.ai/capabilities/audio_transcription

## Important: Endpoint Distinction

Mistral has two different endpoints:

| Endpoint | Use Case | Follows Prompts? |
|----------|----------|------------------|
| `v1/chat/completions` | Multimodal chat | **Yes** - use this for transcribe-and-rewrite |
| `v1/audio/transcriptions` | Transcription only | No - verbatim only |

**For this evaluation, use the chat endpoint with Voxtral Small or Mini.**

## Models

### Chat Models (Multimodal)

Use these for transcribe-and-rewrite workflows:

| Model ID | Notes |
|----------|-------|
| voxtral-small-latest | Larger, more capable |
| voxtral-mini-latest | Smaller, faster |

Endpoint: `https://api.mistral.ai/v1/chat/completions`

### Transcription-Only Model

| Model ID | Notes |
|----------|-------|
| voxtral-mini-latest | Same model, different endpoint |

Endpoint: `https://api.mistral.ai/v1/audio/transcriptions`

## Code Example (Chat with Audio)

```python
from mistralai import Mistral
import base64

client = Mistral(api_key="your-api-key")

# Base64 encode audio file
with open("audio.mp3", "rb") as f:
    audio_b64 = base64.standard_b64encode(f.read()).decode("utf-8")

response = client.chat.complete(
    model="voxtral-small-latest",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "audio_url",
                    "audio_url": f"data:audio/mp3;base64,{audio_b64}"
                },
                {
                    "type": "text",
                    "text": "Transcribe this audio and remove filler words."
                }
            ]
        }
    ]
)

print(response.choices[0].message.content)
```

## Features

- Language detection (automatic)
- Timestamp granularity support (transcription endpoint)
- Combines audio + text prompts in single request (chat endpoint)
