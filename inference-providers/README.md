# Inference Providers

This folder tracks third-party inference providers that offer audio multimodal models.

## Providers with Direct API Access

- **OpenAI** - Direct API (see [../openai/](../openai/))
- **Google (Gemini)** - Direct API (see [../gemini/](../gemini/))

## Third-Party Providers to Evaluate

| Provider | Audio Multimodal Models | Notes |
|----------|------------------------|-------|
| Fireworks.ai | Qwen2-Audio? | Check availability |
| Together.ai | TBD | Check availability |
| Replicate | TBD | Check availability |
| OpenRouter | Routes to various | Meta-provider |

## Notes

When testing through inference providers, verify:
1. Audio input is supported (not just text)
2. Chat endpoint is used (not transcription-only endpoint)
3. Prompts are followed (not just verbatim transcription)
