#!/usr/bin/env python3
"""
Audio Multimodal Evaluation Script

Runs audio samples through OpenAI and Gemini with each evaluation prompt,
saving results to the results/ directory.
"""

import os
import sys
import base64
from pathlib import Path

# Directories
BASE_DIR = Path(__file__).parent
AUDIO_DIR = BASE_DIR / "audio"
PROMPTS_DIR = BASE_DIR / "prompts"
RESULTS_DIR = BASE_DIR / "results"


def load_prompts() -> dict[str, str]:
    """Load all prompt files from prompts/ directory."""
    prompts = {}
    for prompt_file in sorted(PROMPTS_DIR.glob("*.txt")):
        prompt_name = prompt_file.stem  # e.g., "01-raw-transcription"
        prompts[prompt_name] = prompt_file.read_text().strip()
    return prompts


def get_audio_files() -> list[Path]:
    """Get all audio files from audio/ directory."""
    return sorted(AUDIO_DIR.glob("*.mp3"))


def encode_audio_base64(audio_path: Path) -> str:
    """Encode audio file to base64."""
    with open(audio_path, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")


def run_openai(audio_path: Path, prompt: str) -> str:
    """Run audio through OpenAI gpt-4o-audio-preview."""
    try:
        from openai import OpenAI
    except ImportError:
        return "ERROR: openai package not installed. Run: pip install openai"

    client = OpenAI()
    audio_b64 = encode_audio_base64(audio_path)

    response = client.chat.completions.create(
        model="gpt-4o-audio-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_audio",
                        "input_audio": {
                            "data": audio_b64,
                            "format": "mp3"
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )

    return response.choices[0].message.content


def run_gemini(audio_path: Path, prompt: str) -> str:
    """Run audio through Gemini 2.0 Flash."""
    try:
        import google.generativeai as genai
    except ImportError:
        return "ERROR: google-generativeai package not installed. Run: pip install google-generativeai"

    # Configure API key
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "ERROR: GEMINI_API_KEY or GOOGLE_API_KEY environment variable not set"
    genai.configure(api_key=api_key)

    # Upload the audio file
    audio_file = genai.upload_file(audio_path)

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content([audio_file, prompt])

    return response.text


def save_result(model: str, audio_name: str, prompt_name: str, result: str):
    """Save result to results/{model}/{audio}_{prompt}.md"""
    output_dir = RESULTS_DIR / model
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{audio_name}_{prompt_name}.md"

    header = f"""# {model.upper()} - {audio_name} - {prompt_name}

**Audio:** {audio_name}.mp3
**Prompt:** {prompt_name}
**Model:** {model}

---

"""
    output_file.write_text(header + result)
    print(f"  Saved: {output_file.relative_to(BASE_DIR)}")


def run_evaluation(models: list[str] = None, audio_files: list[str] = None,
                   prompts: list[str] = None):
    """Run the full evaluation."""

    all_prompts = load_prompts()
    all_audio = get_audio_files()

    # Filter if specified
    if prompts:
        all_prompts = {k: v for k, v in all_prompts.items() if k in prompts}
    if audio_files:
        all_audio = [a for a in all_audio if a.stem in audio_files]

    available_models = {
        "gpt-4o-audio-preview": run_openai,
        "gemini-2.0-flash": run_gemini,
    }

    if models:
        available_models = {k: v for k, v in available_models.items() if k in models}

    print("Running evaluation:")
    print(f"  Models: {list(available_models.keys())}")
    print(f"  Audio files: {[a.name for a in all_audio]}")
    print(f"  Prompts: {list(all_prompts.keys())}")
    print()

    for model_name, model_fn in available_models.items():
        print(f"\n=== {model_name.upper()} ===")

        for audio_path in all_audio:
            print(f"\nProcessing: {audio_path.name}")

            for prompt_name, prompt_text in all_prompts.items():
                print(f"  Prompt: {prompt_name}...", end=" ", flush=True)

                try:
                    result = model_fn(audio_path, prompt_text)
                    save_result(model_name, audio_path.stem, prompt_name, result)
                except Exception as e:
                    print(f"ERROR: {e}")
                    save_result(model_name, audio_path.stem, prompt_name, f"ERROR: {e}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run audio multimodal evaluation")
    parser.add_argument("--models", "-m", nargs="+",
                        choices=["gpt-4o-audio-preview", "gemini-2.0-flash"],
                        help="Models to test (default: all)")
    parser.add_argument("--audio", "-a", nargs="+",
                        help="Audio file stems to test, e.g., '1 2 3' (default: all)")
    parser.add_argument("--prompts", "-p", nargs="+",
                        help="Prompt names to test (default: all)")

    args = parser.parse_args()

    run_evaluation(
        models=args.models,
        audio_files=args.audio,
        prompts=args.prompts
    )
