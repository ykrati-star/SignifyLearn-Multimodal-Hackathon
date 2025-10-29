import whisper
import os
import tempfile
import ffmpeg

def extract_audio_from_video(video_path):
    """
    Extracts audio (mono, 16kHz) from the input video using ffmpeg.
    Returns the path to a temporary WAV file.
    """
    temp_audio = tempfile.NamedTemporaryFile(suffix=".wav", delete=False).name
    try:
        ffmpeg.input(video_path).output(temp_audio, ac=1, ar='16k').run(quiet=True, overwrite_output=True)
    except Exception as e:
        print("FFmpeg error:", e)
    return temp_audio

def video_to_text(video_path):
    """
    Uses OpenAI Whisper to transcribe speech from video.
    """
    print("[INFO] Extracting audio...")
    audio_path = extract_audio_from_video(video_path)

    print("[INFO] Loading Whisper model...")
    model = whisper.load_model("base")  # options: tiny, base, small, medium, large

    print("[INFO] Transcribing...")
    result = model.transcribe(audio_path)

    os.remove(audio_path)
    return result["text"]
