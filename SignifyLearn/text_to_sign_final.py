from datasets import load_dataset
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import tempfile

def text_to_sign(text, max_samples=300):
    """
    Convert input text to ISL and generate a single stitched gesture video.
    """
    print(f"\n🔤 Input Text: {text}")
    print(f"⚡ Loading ISL dataset (first {max_samples} samples)...")

    # Load a limited subset for faster matching
    dataset = load_dataset("bridgeconn/sign-dictionary-isl", split=f"train[:{max_samples}]")

    words = text.lower().replace("?", "").replace(".", "").split()
    print("\n🎬 Searching for ISL gestures...\n")

    clips = []
    for word in words:
        found = False
        for entry in dataset:
            gloss = entry.get("label", "").lower()
            if word == gloss:
                print(f"✅ Found ISL sign for '{word}'")

                # Extract video content and save temporarily
                video = entry["video"]
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmpfile:
                    tmpfile.write(video.read())
                    tmp_path = tmpfile.name

                # Load video as a moviepy clip
                clip = VideoFileClip(tmp_path).resize(height=360)
                clips.append(clip)
                found = True
                break

        if not found:
            print(f"⚠ No ISL sign found for '{word}'")

    # If any clips found, concatenate them
    if clips:
        final_video = concatenate_videoclips(clips, method="compose")
        output_path = "_".join(words) + "_ISL.mp4"
        final_video.write_videofile(output_path, codec="libx264", fps=24)
        print(f"\n🎞 Final ISL video saved as: {output_path}\n")

        # Clean up temp clips
        for clip in clips:
            clip.close()
    else:
        print("\n❌ No matching ISL signs found for any words.\n")


if __name__ == "__main__":
    text = input("Enter text to convert to ISL: ")
    text_to_sign(text, max_samples=300)
