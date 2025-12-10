# Context Note - Raw Transcript

**Transcribed:** 10 Dec 2025
**Backend:** Gemini 2.0 Flash
**Type:** Verbatim (no cleanup)

---

Okay, so here's the purpose of this repository and I'll also just record this for the sake of

adding context data, but it's going to be itself used in this evaluation.

The I've been doing a lot of um, using transcription tools pretty much every day for the past year.

And um, feel like I'm getting close to having sort of a decisive set of tools that I can use on different environments for really using these to the as well as they can be used.

Um, something that I believe has enormous promise is audio multimodal, which is multimodal AI models that can take audio as a binary and they can produce text, uh, that is a little bit formatted for specific purposes.

Uh, the difference is compared to traditional ASR models where you get a verbatim transcript and then you can add a prompt like clean it up a bit, remove the filler words, remove the pauses or reformat that as an email.

And why I'm very interested in exploring these models is that you can consolidate that to one step and that just makes it much more efficient and uh, and easy to use, I would say.

So what I want to, um, do in this, the reason I've created this little evaluation and I emphasize that is just kind of a gaining a, I want to quickly test out the different models. I created a repo a few days ago in which I um just went on on uh hugging face and clearly um clearly Gemini and open it. So Gemini and open AI are the ones I've been using for this mostly to date and the Gemini tool is brilliant.

But I thought is there any chance that this could be done locally? So to answer that question, I went looking for open source um models that have the audio modality. And I found on hugging face there is an audio text to text task and there is an Omnitask. Omni is any to any.

But within the first level, um I created a repository just to kind of say at this point in time here's what there is. And I the only one I've tried so far locally is actually Vostro. Um, and it basically would work but wouldn't work. In the sense that I validated that it, it did work, it ran on my hardware. Um, but it was throttling the GPU like crazy. It was using almost all of my GPU. So it's actually it it's one that I can confirm is viable. I was able to achieve inference. And the prompts worked, but um at the same time for so it's which is strange because it's 9B. It didn't seem like it should be so difficult.

But I'm looking at the list now there's also Phi multimodal to try out. It's only 2.6B. And there is, let's see what else. Omni audio as well might be worth trying out because it's got quite a small uh quantized version. Maybe it's just inherently that the this task of audio understanding requires larger models than ASR and and there's nothing to be done about it. Um, the purpose of this particular evaluation is to run try out these different models for this task of audio understanding in the narrow context that I'm considering it within, which is that of what you might, I don't know if there's a word for this, transcribe and rewrite, maybe it's just called transcribe.

Something to note is that sometimes these model providers actually offer a transcription endpoint for the multimodals. And then if you want to do the transcribe rewrite workflow, which the workflow which might be just clean up or reformat this as an email, reformat this as a task list in JSON, which is what I find which is the one that I'm very excited and interested about, you actually need to use the chat API endpoint, which to me doesn't actually make a whole bunch of sense, but that's the way at least Mistral have done it. Um, so to here's what I want to do in this evaluation. Um, the plan, the plan of action. Gemini and Open AI I know familiar with, but we may as well add them. Now, all these other ones. Mistral, Flamingo, Qun. The question, Qun 2, I should say and Qun Omni. The challenge is usually finding inference providers in the cloud because um most of them I can't run locally. Most of them are non-starters. Um, but places like fireworks, there are some providers that do them. So this isn't going to be like a big evaluation at all. It's going to be just testing is Qun 3 any good basically for this. And what I'm going to do is just I've created six, this will be the sixth and final audio sample that I'm recording. And the previous five are kind of very much reflective of the type of workflow that I'd like to try out here, which is I'm recording something, it's a it's an instruction for an AI agent, it's a development prompt, it's an email. I don't do not want a verbatim transcript, but we might add we might add for the sake of completion. We might ask them to do that anyway, just to see how they fair in that task. Um, but the real one I'm evaluating on is the cleaned up. Well, there's two levels really. The first one is clean up. Remove the Ms, the s, the pauses. I'd like to try as well their ability to handle inferred instructions, which is when I say something like, um I want to go out today at 6:00. Oh wait, sorry, I meant 5:00. And it'd be very interesting in this audio multimodal uh evaluation. I might create one more sample just with a couple of those to see how they handle that um that task. Which ones actually can infer can can uh process that as an instruction and not as and transcribe accordingly. And finally, I'd like to try one prompt for format adherence, which is saying this prompt, for example, um I think it's number five is a development instruction prompt intended for to be provided to an AI agent tool for making some edits to the user's personal website and edit that accordingly. And that's a that's a prompt to test their ability to generate um text to a specific format in response to the audio input.
