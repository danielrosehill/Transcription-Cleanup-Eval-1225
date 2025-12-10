# CLAUDE.md - Audio Multimodal Evaluation

## Project Purpose

This repository evaluates audio multimodal AI models for "transcribe and rewrite" workflows - the ability to take audio input and produce cleaned/formatted text in a single step, rather than the traditional two-step ASR + LLM approach.

## Key Concepts

### Audio Multimodal vs Traditional ASR
- **Traditional ASR**: Audio → Verbatim text → LLM cleanup (2 steps)
- **Audio Multimodal**: Audio + Prompt → Formatted text (1 step)

### API Endpoint Distinction
Some providers (notably Mistral) separate:
- **Transcription endpoint**: Returns verbatim text only
- **Chat API endpoint**: Accepts audio + follows formatting prompts

When testing models, use the chat/completion endpoint if transcription endpoint doesn't follow prompts.

## Audio Samples

Six MP3 files in `audio/`:
- **1-5**: Real workflow samples (AI agent instructions, dev prompts, emails)
- **6**: Meta recording about this evaluation

## Evaluation Tasks

When running evaluations, test each model on:

1. **Raw transcription** - Verbatim accuracy baseline
2. **Filler removal** - "Remove ums, ahs, and false starts"
3. **Inferred instructions** - Can it handle "I meant X, not Y" corrections?
4. **Format adherence** - Generate specific formats (email, JSON, structured)

## Models to Test

### Priority (Cloud)
- OpenAI gpt-4o-audio-preview
- Gemini 2.0 Flash (known to work well)
- Qwen2-Audio / Qwen Omni (find via Fireworks or similar)
- Mistral Voxtral (use chat endpoint)

### Local Testing (if hardware permits)
- Voxtral 9B (works but GPU-heavy)
- Phi-4-Multimodal 2.6B
- OmniAudio 2.6B quantized

## Working with This Repo

### Running Evaluations
```bash
# Example structure for results
results/
├── model-name/
│   ├── sample-1-raw.md
│   ├── sample-1-cleaned.md
│   └── sample-1-formatted.md
```

### Adding New Samples
- Record to `audio/` as `N.mp3`
- Keep source text in `source-texts/` if applicable
- Update README sample table

## Reference Files

- `ref.md` - Detailed model list, LiteLLM examples, evaluation criteria
- `context/note-raw.md` - Verbatim project explanation
- `context/note-edited.md` - Cleaned project explanation

## Notes

- Gemini has been the best performer so far for this use case
- Local inference is challenging - even 9B models can saturate GPU
- The real test is format adherence, not just transcription accuracy
