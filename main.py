# main.py
import time
from audio_processor import AudioProcessor
from vision_processor import VisionProcessor
from multimodal_engine import MultimodalFusionEngine
from sign_renderer import SignRenderer


audio_source = "lecture_audio_stream.mp3"
video_source = "teacher_video_feed.mp4"

audio_proc = AudioProcessor()
vision_proc = VisionProcessor()
fusion_engine = MultimodalFusionEngine()
sign_renderer = SignRenderer()

print("SignifyLearn Multimodal Engine Initialized.")


def run_live_simulation(chunk_size=5):
    """Simulates real-time processing of 5-second chunks."""
    
    for i in range(3): 
        print(f"\n--- Processing Chunk {i+1} ---")
        
        raw_text = audio_proc.process_audio(f"{audio_source} chunk {i}")
        
        gesture, visual_context = vision_proc.analyze_frame(f"{video_source} frame {i}")
        
        fusion_output = fusion_engine.fuse_data(raw_text, gesture, visual_context)
        
        sign_code = sign_renderer.get_sign_animation(fusion_output['summary'])
        
        print(f"-> Text Output: {fusion_output['summary']}")
        print(f"-> ISL Code: {sign_code}")
        
        time.sleep(1) 
if __name__ == "__main__":
    run_live_simulation()