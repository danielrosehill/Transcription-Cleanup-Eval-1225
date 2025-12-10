# Audio Multimodal Transcription Evaluation

Evaluating cloud audio understanding models for their ability to transcribe audio and follow post-processing prompts in a single step.

> **Note on Evaluation Methodology**: This is a subjective, non-rigorous evaluation. The quality of transcription cleanup and formatting is inherently subjective - there's no single "correct" output for tasks like filler removal or format conversion. Results reflect personal judgment of output quality for the specific workflows tested.

## Purpose

Traditional ASR (Automatic Speech Recognition) produces verbatim transcripts that require a second LLM call to clean up or reformat. **Audio multimodal models** can do both in one step - taking audio as input and producing formatted, cleaned text directly.

This evaluation tests various models on:
1. Raw transcription accuracy
2. Filler word removal (ums, ahs, pauses)
3. Handling inferred instructions ("I meant 5:00, not 6:00")
4. Format adherence (email, JSON task list, structured output)

## Audio Samples

| File | Description |
|------|-------------|
| `audio/1.mp3` - `audio/5.mp3` | Test samples representing real workflows: AI agent instructions, development prompts, emails |
| `audio/6.mp3` | Context recording about this evaluation (meta) |

## Models Under Evaluation

### Cloud APIs (Native Audio Multimodal)
- **OpenAI**: gpt-4o-audio-preview, gpt-4o, gpt-4o-mini
- **Google**: Gemini 2.0 Flash, Gemini 1.5 Pro/Flash
- **Mistral**: Voxtral (requires chat API endpoint for rewrite tasks)
- **Qwen**: Qwen2-Audio, Qwen Omni

### Local/Self-Hosted Options
- **Voxtral** (9B) - Tested, works but GPU-intensive
- **Phi-4-Multimodal** (2.6B) - Smaller, worth testing
- **OmniAudio** (2.6B) - Has small quantized versions

### Inference Providers
- Fireworks AI
- Replicate
- Direct API access (OpenAI, Google)

## Evaluation Prompts

Prompts are stored as individual text files in `prompts/` for transparency. These are universal prompts that work across any audio content:

1. **Raw transcription** - Baseline verbatim output
2. **Filler removal** - Remove ums, ahs, false starts
3. **With subheadings** - Structure with section headers
4. **Business formal** - Professional tone
5. **Inferred corrections** - Apply verbal corrections ("I meant X, not Y")

## Key Insight

Many providers offer separate endpoints:
- **Transcription endpoint**: Returns verbatim text
- **Chat API endpoint**: Required for transcribe-and-rewrite workflows

This is how Mistral handles it - the transcription endpoint won't follow formatting prompts.

## Related Resources

- [Audio Multimodal AI Resources](https://github.com/danielrosehill/Audio-Multimodal-AI-Resources) - Comprehensive model list
- [ref.md](ref.md) - Detailed reference with code examples and evaluation criteria

## Structure

```
.
├── audio/              # Test audio samples (1-6.mp3)
├── prompts/            # Evaluation prompts (one per .txt file)
├── context/            # Project context and notes
│   ├── note.mp3        # Voice note explaining this project
│   ├── note-raw.md     # Verbatim transcript
│   └── note-edited.md  # Cleaned transcript
├── results/            # Evaluation outputs by model
├── ref.md              # Detailed reference documentation
└── README.md
```
