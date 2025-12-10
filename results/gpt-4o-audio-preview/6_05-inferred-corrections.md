# GPT-4O-AUDIO-PREVIEW - 6 - 05-inferred-corrections

**Audio:** 6.mp3
**Prompt:** 05-inferred-corrections
**Model:** gpt-4o-audio-preview

---

Here's the cleaned-up transcription with corrections incorporated:

---

For this evaluation, I’ve been using transcription tools pretty much every day for the past year. I feel like I’m getting close to having a decisive set of tools that I can use in different environments to really leverage them efficiently.

Something I believe has enormous promise is audio multimodal models—those that can take audio as input and produce formatted text for specific purposes. The difference, compared to traditional ASR models, is that with ASR you get a verbatim transcript and then can add a prompt like “clean it up,” “remove filler words and pauses,” or “reformat it as an email.” What’s interesting about multimodal models is that you can consolidate this into one step, making it much more efficient and easier to use.

What I’m looking to do in this evaluation is quickly test out different models. I created a repository a few days ago, and while I’ve mostly been using Gemini and OpenAI so far—with Gemini being brilliant—I’m now asking: can this be done locally?

To answer that question, I explored open-source multimodal models on Hugging Face. There’s an “audio-to-text” task and also an “omni” task (any-to-any). I only tried Focstral locally, and while it validated that it works on my hardware, it was throttling my GPU usage heavily. Even though it’s only 9 billion parameters, it seemed more demanding than expected. That’s something I'll have to investigate further.

I see there’s also Phi multimodal, which is 2.6 billion parameters, and OmniAudio, which has a smaller quantized version and might be easier to run. Maybe this audio understanding task just inherently requires larger models than ASR, and there’s nothing to be done about that.

The purpose of this particular evaluation is to try out these models for audio understanding in the narrow context of what I might call “transcribe and rewrite.” I don’t know if that’s the correct term, but essentially it’s transcription with immediate cleanup or reformatting—like reformatting as an email or a task list.

Something important to note is that many model providers offer a transcription endpoint for multimodal models, but if you want to do the transcribe-rewrite workflow (like cleaning up or reformatting), you often need to use the chat API instead. That’s the case with Mistral, and it doesn’t fully make sense to me, but that’s how it currently works.

Here’s the plan: I’m already familiar with Gemini and OpenAI, but I’ll include them for comparison. For the others—Mistral, Flamingo, Qwen—the challenge is usually finding cloud inference providers, since I can’t run them all locally. Most are non-starters for my hardware, but I’ll look at providers like Fireworks that support them.

This won’t be a big evaluation; it’s going to be a simple test to see if Qwen 3, for example, is any good for this. I’ve created six audio samples, and the previous five reflect the workflows I want to test. They include AI agent instructions, developer prompts, and emails. I don’t want a verbatim transcript, but I might still request it just for completeness.

The real evaluation is on their ability to clean up speech by removing “ums” and “uhs” and handling inferred instructions. For example, if I say “I want to go out at 6—oh wait, sorry, I mean 5 o’clock,” the model should correct it to “I want to go out at 5 o’clock.”

Finally, I also want to test format adherence. For example, one audio sample is a developer instruction prompt for an AI agent to make edits to a website. I’ll see how well the models can generate specific formats from the audio input.

---

Let me know if you need any further details!