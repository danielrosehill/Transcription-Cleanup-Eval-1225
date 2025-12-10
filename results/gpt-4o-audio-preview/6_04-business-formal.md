# GPT-4O-AUDIO-PREVIEW - 6 - 04-business-formal

**Audio:** 6.mp3
**Prompt:** 04-business-formal
**Model:** gpt-4o-audio-preview

---

I've transcribed and rewritten your audio in a professional, business-formal tone:

---

The purpose of this repository is to conduct an evaluation of various transcription and audio-to-text tools. Over the past year, I have extensively worked with such tools and have refined my selection of resources for different environments, aiming to optimize their efficiency and usability. I believe that audio-multimodal AI models hold significant promise. These models accept audio inputs directly and produce text that is pre-formatted for specific purposes.

Unlike traditional ASR (Automatic Speech Recognition) models, which generate verbatim transcriptions that may later need to be refined to remove filler words, pauses, or to reformat content as, for example, an email, audio-multimodal models integrate these steps into a single process. This consolidated workflow enhances efficiency and usability, making the technology more practical.

The objective of this evaluation is to test various models in the context of a specific use case—what could be termed as a "transcribe and rewrite" process. I have already gained extensive experience using tools like Gemini and OpenAI and have found their solutions to be effective. However, I am interested in determining whether this task can also be performed locally using open-source models.

To explore this, I identified a number of potential candidate models on platforms like Hugging Face. For example, I tested a model named 'Voxtral.' While functional, it placed a significant strain on my GPU resources, something unexpected given its size of only 9 billion parameters. Despite this, it demonstrated that local inference is achievable with the right hardware configuration.

Additionally, I plan to examine other smaller models such as Phi-Multimodal, which is only 2.6 billion parameters, and OmniAudio, which offers a smaller quantized version. It’s possible that this particular task—audio understanding—inevitably requires greater computational resources compared to standard ASR tasks. Thus, one of the goals will be to determine if local deployment is a viable option for this particular workflow.

The primary focus of this evaluation is to assess these models' ability to transcribe and refine text for specific tasks. For example, recording audio instructions for an AI agent, development prompts, or emails, and then converting them into coherent, refined text suitable for professional contexts. While verbatim transcription is one aspect, the real value lies in the models' ability to deliver polished output—removing filler words, correcting inadvertent instructions, and adhering to specific formatting requirements. 

Furthermore, I will be assessing how these models handle inferred instructions. For instance, in an audio input where the speaker corrects themselves — such as changing a time from “six o'clock” to “five o'clock”—evaluating the model's ability to process those implied instructions accurately is crucial. Additionally, another important factor is adherence to explicitly provided formatting instructions, such as converting development instructions into a template for AI agents.

In conclusion, this evaluation will encompass well-known models like Gemini and OpenAI while also focusing on a range of less common models, like Mistral and Flamingo, to understand their capabilities in this specific task. Although the availability of reliable inference providers—especially for cloud-based solutions—poses a challenge, certain platforms (e.g., Fireworks) do offer such services. Ultimately, the goal is to identify the most effective models for a seamless audio-to-text conversion process tailored toward specific formats and purposes.

--- 

Let me know if you'd like any modifications or further revisions.