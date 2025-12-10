# Context Note - Edited Transcript

**Transcribed:** 10 Dec 2025
**Backend:** Gemini 2.0 Flash
**Type:** Lightly edited (filler removal, punctuation)

---

Here's the purpose of this repository. I'll also record this for the sake of adding context data, but it's going to be itself used in this evaluation.

I've been using transcription tools pretty much every day for the past year. I feel like I'm getting close to having a decisive set of tools that I can use on different environments for really using these as well as they can be used.

Something that I believe has enormous promise is audio multimodal - multimodal AI models that can take audio as a binary and produce text that is formatted for specific purposes. The difference compared to traditional ASR models is that with ASR you get a verbatim transcript and then you add a prompt to clean it up, remove filler words, remove pauses, or reformat it as an email. Why I'm very interested in exploring these models is that you can consolidate that to one step, making it much more efficient and easy to use.

The reason I created this little evaluation (and I emphasize it's just a quick test) is to try out the different models. I created a repo a few days ago where I looked at Hugging Face, Gemini, and OpenAI. Gemini and OpenAI are the ones I've been using mostly to date, and the Gemini tool is brilliant.

But I thought: is there any chance this could be done locally? To answer that question, I went looking for open source models with the audio modality. On Hugging Face, there's an audio-text-to-text task and an Omni task (any-to-any).

I created a repository to document what exists at this point in time. The only one I've tried locally is Voxtral. It basically would work but wouldn't work - I validated that it ran on my hardware, but it was throttling the GPU like crazy, using almost all of it. So it's viable - I was able to achieve inference and the prompts worked - but it's strange because it's 9B and didn't seem like it should be so difficult.

Looking at the list, there's also Phi multimodal (only 2.6B) and OmniAudio with a small quantized version. Maybe audio understanding inherently requires larger models than ASR and there's nothing to be done about it.

The purpose of this evaluation is to try out these models for audio understanding in the narrow context of "transcribe and rewrite" (maybe it's just called transcribe).

Something to note: model providers sometimes offer a transcription endpoint for multimodals, but if you want the transcribe-rewrite workflow (clean up, reformat as email, reformat as JSON task list - which is what I'm excited about), you actually need to use the chat API endpoint. That doesn't make a whole bunch of sense to me, but that's how Mistral has done it.

**Plan of action:**
- Gemini and OpenAI: familiar with them, but may as well add them
- Mistral, Flamingo, Qwen 2, Qwen Omni: the challenge is finding inference providers in the cloud since most can't run locally. Places like Fireworks do offer some.

This isn't going to be a big evaluation - just testing if Qwen is any good for this.

I've created six audio samples (this is the sixth). The previous five are reflective of the workflow I'd like to try: recording an instruction for an AI agent, a development prompt, an email. I don't want a verbatim transcript, but we might add that for completion to see how they fair.

**Evaluation levels:**
1. **Cleanup**: Remove ums, ahs, pauses
2. **Inferred instructions**: Handle cases like "I want to go out today at 6:00. Oh wait, sorry, I meant 5:00" - can they process that as an instruction and transcribe accordingly?
3. **Format adherence**: Test prompt #5 is a development instruction intended for an AI agent tool for editing a personal website - can they generate text to a specific format in response to audio input?
