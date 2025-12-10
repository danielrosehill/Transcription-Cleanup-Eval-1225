# GEMINI-2.5-FLASH - 6 - 04-business-formal

**Audio:** 6.mp3
**Prompt:** 04-business-formal
**Model:** gemini-2.5-flash

---

This recording serves to outline the purpose of this repository, which is dedicated to an ongoing evaluation.

I have been extensively using transcription tools daily for the past year. I feel I am nearing a decisive set of tools that can be effectively deployed across various environments. A technology with enormous promise is audio multimodal. These are multimodal AI models capable of processing audio as binary input and generating text formatted for specific purposes.

The key distinction from traditional ASR (Automatic Speech Recognition) models is that while ASR provides a verbatim transcript requiring subsequent prompting for clean-up (e.g., removing filler words, pauses) or reformatting (e.g., as an email), multimodal models consolidate these steps into a single, more efficient, and user-friendly process.

The purpose of this small-scale evaluation is to quickly test various models. I created a repository a few days ago where I sourced models from Hugging Face. To date, I have primarily used Gemini and OpenAI, finding the Gemini tool particularly effective. However, I wondered if this could be achieved locally. To explore this, I searched for open-source models offering audio modality.

On Hugging Face, I discovered an audio text-to-text task and an Omni task, which signifies 'any-to-any' functionality. In the initial phase, I created a repository to document the available models at this point. The only model I have tested locally so far is Foxtrot. While I validated that Foxtrot did run on my hardware, its performance was only partially successful. It heavily throttled the GPU, utilizing a significant portion of its resources. Nevertheless, it is a viable option for inference, and the prompts functioned correctly. This was surprising given it is a 9B model, as it seemed overly complex for its size.

Reviewing the list, FIMultiModal (2.6B) is another candidate for testing. OmniAudio also appears promising due to its relatively small quantized version. It is possible that the task of audio understanding inherently requires larger models than standard ASR, which would be an inherent limitation.

The purpose of this specific evaluation is to test various models for audio understanding within the narrow context I am considering: what I refer to as 'transcribe and rewrite' (though perhaps 'transcribe' alone suffices). It is worth noting that some model providers offer a dedicated transcription endpoint for multimodal models. If you wish to utilize the transcribe-rewrite workflow—which might involve cleanup, reformatting as an email, or even generating a task list in JSON (a capability I am particularly interested in)—you typically need to use the chat API endpoint. While this does not strike me as logically intuitive, it is how at least Mistral has implemented it.

So, here is the plan of action for this evaluation. I am familiar with Gemini and OpenAI, and they will be included. Other models include Mistral, Flamingo, Qwen (specifically Qwen 2), and Qwen Omni. The primary challenge often lies in securing cloud-based inference providers, as most of these models are not feasible for local execution. However, platforms like Fireworks do offer such providers.

Therefore, this will not be an extensive evaluation; the primary objective is to assess Qwen 3's suitability for this task. I have created six audio samples; this current one will be the sixth and final recording. The previous five samples are highly representative of the workflow I intend to test. This includes recording instructions for an AI agent, development prompts, and emails.

While I do not require a verbatim transcript, for comprehensive evaluation, we may request models to provide one to assess their performance on that specific task. My primary evaluation focuses on two levels of output. The first involves a cleanup process. This includes the removal of filler sounds ('ums') and pauses. I also want to test their ability to handle inferred instructions, such as when I say, "I want to go out today at six. Oh wait, sorry, I mean five o'clock." It would be very interesting in this audio multimodal evaluation; I might create one more sample specifically featuring a few instances of such corrections. This will determine which models can accurately infer and process such corrections as instructions, rather than transcribing them verbatim.

Finally, I intend to test a prompt for formatted output. Specifically, prompt number five is a development instruction prompt intended to be provided to an AI agent tool, guiding it to make edits to a user's personal website and perform those edits accordingly. This prompt will test the models' ability to generate text in a specific format in response to audio input.