# GEMINI-2.5-FLASH - 6 - 03-with-subheadings

**Audio:** 6.mp3
**Prompt:** 03-with-subheadings
**Model:** gemini-2.5-flash

---

Here's the transcribed audio with filler words removed and content organized under subheadings:

### Introduction & Purpose

Here's the purpose of this repository. I'll also just recorded this for the sake of adding context data, but it's going to be itself used in this evaluation.

I've been doing a lot of using transcription tools pretty much every day for the past year, and I feel like I'm getting close to having a decisive set of tools that I can use on different environments for really using these as well as they can be used. Something that I believe has enormous promise is audio multimodal, which is multimodal AI models that can take audio as a binary and they can produce text that is a little bit formatted for specific purposes.

The difference compared to traditional ASR models, where you get a verbatim transcript and then you can add a prompt like "clean it up a bit," "remove the filler words," "remove the pauses," or "reformat that as an email." Why I'm very interested in exploring these models is that you can consolidate that to one step, and that just makes it much more efficient and easy to use, I would say.

### Evaluation Goal

What I want to do in this, the reason I created this little evaluation – and I emphasize that, it's just kind of gaining a – I want to quickly test out the different models. I created a repo a few days ago, in which I just went on Hugging Face and tried Gemini and OpenAI. Gemini and OpenAI are the ones I've been using for this mostly to date, and the Gemini tool is brilliant. But I thought, "Is there any chance that this could be done locally?" So, to answer that question, I went looking for open-source models that have the audio modality. I found on Hugging Face there is an audio text-to-text task, and there is an omni task (omni is any-to-any).

Within the first level, I created a repository just to kind of say at this point in time, here's what there is. The only one I've tried so far locally is actually Foxtrot. It basically would work but wouldn't work, in the sense that I validated that it did work, it ran on my hardware, but it was throttling the GPU like crazy. It was using almost all of my GPU. So, it's actually it's one that I can confirm is viable, I was able to achieve inference, and the prompts worked, but at the same time, it's which is strange because it's 9B. It didn't seem like it should be so difficult.

### Models to Evaluate

I'm looking at the list now, there's also Fi Multimodal to try out, it's only 2.6B. There is Omni Audio as well might be worth trying out because it's got quite a small quantized version. Maybe it's just inherently that this task of audio understanding requires larger models than ASR, and there's nothing to be done about it.

The purpose of this particular evaluation is to try out these different models for this task of audio understanding in the narrow context that I'm considering it within, which is that of what you might – I don't know if there's a word for this – transcribe and rewrite. Maybe it's just called transcribe.

Something to note is that sometimes these model providers actually offer a transcription endpoint for the multimodals. Then, if you want to do the transcribe rewrite workflow, which might be "just clean up" or "reformat this as an email" or "reformat this as a task list in JSON," which is what I find, which is the one that I'm very excited and interested about, you actually need to use the chat API endpoint, which to me doesn't actually make a whole bunch of sense, but that's the way at least Mistral have done it.

### Plan of Action

Here's what I want to do in this evaluation, the plan of action:
Gemini and OpenAI I know and familiar with, but we may as well add them. These other ones: Mistral, Flamingo, Qwen, Qwen 2, I should say, and Qwen Omni. The challenge is usually finding inference providers in the cloud because most of them I can't run locally. Most of them are non-starters. But places like Fireworks, there are some providers that do them. So, this isn't going to be like a big evaluation at all. It's going to be just testing is Qwen 3 any good, basically, for this?

I'm going to do is just, I've created six, this will be the sixth and final audio sample that I'm recording. The previous five are kind of very much reflective of the type of workflow that I'd like to try out here, which is: I'm recording something, it's an instruction for an AI agent, it's a development prompt, it's an email. I do not want a verbatim transcript, but we might add, we might add for the sake of completion, we might ask them to do that anyway, just to see how they fare in that task.

### Evaluation Scenarios

The real one I'm evaluating on is the cleaned-up – well, there's two levels really.
1.  The first one is a **cleanup**: remove the "ums," the "ahs," the pauses.
2.  I'd like to try as well their ability to handle **inferred instructions**, which is when I say something like, "I want to go out today at 6. Oh wait, sorry, I mean 5:00." It would be very interesting in this audio multimodal evaluation. I might create one more sample just with a couple of those to see how they handle that task, which ones actually can infer, can process that as an instruction and not transcribe accordingly.
3.  Finally, I'd like to try one prompt for **formatted herein**, which is saying: This prompt, for example, I think it's number five, is a development instruction prompt intended for to be provided to an AI agent tool for making some edits to the user's personal website. Edit that accordingly. That's a prompt to test their ability to generate text to a specific format in response to the audio input.