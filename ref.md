# Audio Understanding Model Evaluation Reference

## Purpose

Evaluate cloud audio understanding models for their ability to:
1. Produce accurate raw transcriptions
2. Follow post-processing prompts (cleanup, formatting, restructuring)

## Related Resource

More comprehensive list: https://github.com/danielrosehill/Audio-Multimodal-AI-Resources

---
 

## Prompt Tests to Run

For each audio sample, test these transformation prompts:

1. **Raw transcription** - Baseline accuracy test
2. **Filler removal** - Remove ums, ahs, pauses, false starts
3. **Add subheadings** - Structure the content with headers
4. **Business logic format** - Extract as structured business requirements/logic
5. **Business formal language** - Professional tone, polished prose
6. **Casual language** - Conversational, relaxed tone
7. **Email format** - Format as a professional email
8. **Blog outline** - Format as a blog post outline with sections

---

## Cloud Audio Understanding Models

### Native Audio-to-Text Models (Can Follow Prompts)

These accept audio + text prompt and generate transformed text output:

#### Commercial APIs

| Provider | Model | Notes |
|----------|-------|-------|
| **OpenAI** | `gpt-4o-audio-preview` | Native audio input, can follow transformation prompts |
| **OpenAI** | `gpt-4o` | Audio input supported |
| **OpenAI** | `gpt-4o-mini` | Lower cost, audio capable |
| **Google** | `gemini-2.0-flash` | Fast, audio multimodal |
| **Google** | `gemini-1.5-pro` | Strong audio understanding, long context |
| **Google** | `gemini-1.5-flash` | Faster/cheaper with audio support |
| **Mistral** | `voxtral` (5B-24B) | Apache 2.0, audio-text-to-text |

#### Open Source (Self-Hosted or via Inference APIs)

| Model | Provider | Size | License |
|-------|----------|------|---------|
| **Qwen2-Audio** | Alibaba | 8B | Apache 2.0 |
| **Ultravox** | Fixie.ai | 8B-70B | MIT |
| **Phi-4-Multimodal** | Microsoft | 5.6B | MIT |
| **Kimi-Audio** | Moonshot AI | 10B | MIT/Apache 2.0 |
| **OmniAudio** | NexaAI | 2.6B | Apache 2.0 |
| **SALMONN** | ByteDance/Tsinghua | 7B-13B | Apache 2.0 |
| **Soundwave** | FreedomIntelligence | 9B | Apache 2.0 |
| **Step-Audio-Chat** | StepFun | 130B | Apache 2.0 |
| **Voxtral** | Mistral AI | 5B-24B | Apache 2.0 |
| **Qwen Omni** | Alibaba | 7B-35B | Apache 2.0 |
| **Gemma 3n** | Google | 2B-4B | Gemma license |

---

 