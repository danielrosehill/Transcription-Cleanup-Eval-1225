# GPT-4O-AUDIO-PREVIEW - 6 - 02-filler-removal

**Audio:** 6.mp3
**Prompt:** 02-filler-removal
**Model:** gpt-4o-audio-preview

---

The purpose of this repository is to evaluate transcription tools, especially their ability to handle audio in a multimodal AI context. The goal is to explore models that can consolidate transcription and rewriting into a single step for efficiency and ease of use. Over the past year, I’ve used transcription tools daily and now want to test both familiar and unfamiliar tools to see how they perform with tasks like cleaning up transcripts and reformatting them for specific purposes.

I’m particularly interested in models that can handle “audio to text” or “omni” tasks locally and via cloud inference services. While I’ve had good experiences with tools like Gemini and OpenAI, I want to see whether running these models locally is also viable using open-source alternatives, such as Focstra, Phi-Multimodal, and OmniAudio. 

I’ve already tested Focstra and found that it works, but it heavily throttles my GPU despite its relatively small size. I plan to evaluate other models like Phi-Multimodal (2.6B) and others that might have smaller, quantized versions. It’s possible that audio understanding inherently requires larger models than traditional ASR, making local inference resource-heavy.

The purpose of this evaluation is to test how well different models perform in the following scenarios:
1. Clean-up transcription: Removing filler words, false starts, and pauses while preserving meaning.
2. Handling inferred instructions: For example, when I correct myself mid-sentence, can the model produce the intended text rather than the verbatim sequence.
3. Formatting adherence: Testing models’ ability to generate output in a specific format, such as an email, task list, or development instruction.

I plan to record one more sample focused specifically on handling self-corrections to see how well the models interpret those adjustments. The results of this evaluation will help determine which models perform best for these tasks and whether any viable local solutions exist.