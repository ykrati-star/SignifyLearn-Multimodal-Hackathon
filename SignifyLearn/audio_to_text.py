from transformers import pipeline
import torch

def speech_to_text(audio_path):
    model_id = "openai/whisper-small"   # fast, accurate
    asr = pipeline("automatic-speech-recognition", model=model_id)
    result = asr(audio_path)
    return result["text"]

if __name__ == "__main__":
    text = speech_to_text("test.wav")
    print("Recognized text:", text)
