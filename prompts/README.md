# Evaluation Prompts

Each text file contains a prompt to be used with audio multimodal models. These prompts are designed to be universal - they should work with any audio content regardless of subject matter.

## Prompts

| File | Purpose |
|------|---------|
| `01-raw-transcription.txt` | Baseline verbatim transcription with no cleanup |
| `02-filler-removal.txt` | Clean transcript with ums, ahs, false starts removed |
| `03-with-subheadings.txt` | Structured output with section headers |
| `04-business-formal.txt` | Professional, polished tone |
| `05-inferred-corrections.txt` | Apply verbal corrections ("I meant X, not Y") |

## Usage

These prompts are read by the evaluation scripts and sent alongside audio files to each model being tested.
