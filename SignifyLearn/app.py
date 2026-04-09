from audio_to_text import speech_to_text
from text_to_text import translate_to_isl

def run_pipeline(audio_file):
    print("🎤 Transcribing speech...")
    text = speech_to_text(audio_file)
    print("🧠 Detected text:", text)

    print("🤟 Translating to ISL gloss...")
    isl_text = translate_to_isl(text)
    print("🧩 ISL Output:", isl_text)

if __name__ == "__main__":
    run_pipeline("sample_audio.wav")
    //done!
