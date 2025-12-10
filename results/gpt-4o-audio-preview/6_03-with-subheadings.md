# GPT-4O-AUDIO-PREVIEW - 6 - 03-with-subheadings

**Audio:** 6.mp3
**Prompt:** 03-with-subheadings
**Model:** gpt-4o-audio-preview

---

### Introduction
This evaluation aims to explore and test different multimodal AI models that can process audio input and generate usable text outputs. The goal is to move beyond traditional automatic speech recognition (ASR) tools and evaluate models that can handle audio-to-text transformations, enabling both transcription and rewriting in a single step.

### Motivation for the Evaluation
Over the past year, there has been a lot of experimentation and exploration with transcription tools on a daily basis. The primary motivation is to streamline the workflows into a more efficient process that leverages multimodal AI, specifically those that take audio as a binary input, process it, and produce text that’s already cleaned up, formatted, and usable for specific types of tasks such as emails, instructional prompts, or task lists.

### Difference from Traditional ASR Models
Traditional ASR models generate a verbatim transcript. Post-transcription, users often add another layer of processing to clean up the transcript, remove filler words like "um" and "ah," and then reformat it according to specific needs (e.g., into an email or task list). The focus of this evaluation is on consolidating transcription and rewriting into one step using multimodal models, making the process more efficient and user-friendly.

### Exploration of Open Source Alternatives
Currently, most tests have been done using proprietary tools like Gemini and OpenAI, both of which have performed well. However, the purpose of this evaluation is to check if similar performance can be achieved with open-source models run locally, or at least off-cloud, to reduce reliance on external services.

To achieve this:
- **Discovery Phase**: The initial phase involved exploring open-source audio-to-text models available on platforms like Hugging Face. Models that handle audio-to-text tasks or even those marked as omnidirectional (any input to any output) were examined.
  
- **Initial Tests with VoxoL**: One of the models tested locally was VoxoL, a 9B parameter model. While it functioned as expected and prompts worked successfully, the GPU usage was extremely high, pushing local hardware to its limits. While it’s a viable option, it seemed more demanding than expected, which could be a limitation of this task compared to ASR.

### Additional Models for Evaluation
The next steps will involve trying out smaller models like:
- **Phi-2-Multimodal**: At 2.6B parameters, this model might be lighter on hardware, making it more feasible to run locally.
  
- **Omniaudio**: Another potentially interesting model with a quantized version available.
  
It’s worth noting that possibly the audio transcription and understanding task generally requires larger models than standard ASR, due to the additional cognitive load of properly formatting and rewriting on top of transcription.

### Cloud vs. Local Inference
Another challenge with this evaluation is finding providers that offer inference capabilities in the cloud since running these larger models locally is often not practical. Providers like Fireworks offer inference services for some of these models, making it easier to evaluate them without hardware bottlenecks.

### What This Evaluation Will Focus On
This evaluation isn’t meant to be exhaustive but will test whether specific models, such as those from Mistral, Flamingo, Qwen (particularly Qwen-2 and Qwen-Omni), perform well in this very focused task.

The evaluation is based on six distinct audio samples:
1. **General Workflow Description**: A sample explaining the type of workflow preferred.
2. **Instruction for an AI Agent**: Contains inferred instructions to see how the models handle corrections like "I want to go out at 6... oh wait, sorry, I meant 5."
3. **Email Example**: The model should reformat the transcript into a readable email structure.
4. **Task List Example**: Evaluating the ability of the model to generate a bulleted task list.
5. **Development Instruction Prompt**: A specific prompt asking the AI to structure the audio as a development instruction, which will be passed to another tool.
6. **General Context (This Recording)**: The current recording is the final audio sample, roughly summarizing the motivation, challenges, and goals of the evaluation.

### Levels of Transcription or Rewriting
There are essentially two levels of transcription or rewriting:
1. **Basic Cleanup**: This step removes filler words, pauses, and other irrelevant sounds, resulting in a clear, readable transcript that sticks closely to the original spoken content.
2. **Reformatting**: The second level involves reformatting the transcript based on the desired format, such as creating:
   - A cleaned-up transcript that’s structured like an email.
   - A task list that highlights action items.
   - Clear instructions for an AI agent.

Part of the evaluation will explore how well these models handle inferred instructions (e.g., spoken corrections like "wait, I meant 5 o’clock") and how they respond to formatting prompts.

### Known Issues
One key observation is that some providers (like Mistral) separate their transcription capabilities from their chat endpoints. For example, if you want to move from transcription to more high-level rewriting or formatting (like converting speech into an email format), you must use the chat API rather than a dedicated transcription API. While it might seem counterintuitive, that is how some implementations are structured.

### Conclusion
In summary, this evaluation will focus on three key dimensions:
1. **Accuracy of the Basic Transcription**: Without rewriting, do the models produce clean, filler-free transcripts?
2. **Handling of Inferred Instructions**: Can the models handle verbal corrections in real time and understand the final intended meaning?
3. **Formatting Adherence**: How well can the models reformulate transcriptions based on specific formatting needs, such as creating an email or a development instruction?

The findings will help curate a set of models that are performant for specific situations, particularly in workflows where users prefer a one-step transcription and rewrite process. This would not only enhance efficiency but also usability by removing the need to manually clean or reformat transcripts post-generation.