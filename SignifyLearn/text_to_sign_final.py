from datasets import load_dataset
from PIL import Image
import os

def text_to_sign(text):
    # Load Indian Sign Language dictionary dataset
    dataset = load_dataset("bridgeconn/sign-dictionary-isl")

    # Create an output folder for saving frames
    os.makedirs("sign_frames", exist_ok=True)

    words = text.replace("?", "").replace(".", "").split()
    print("\nConverting words to ISL signs...\n")

    for word in words:
        word_lower = word.lower()
        found = False
        for i, label in enumerate(dataset["train"]["label"]):
            if label.lower() == word_lower:
                img = dataset["train"][i]["image"]
                img_path = os.path.join("sign_frames", f"{word_lower}.jpg")
                img.save(img_path)
                print(f"✓ {word_lower} → sign image saved to {img_path}")
                found = True
                break
        if not found:
            print(f"⚠ No ISL sign found for word: {word_lower}")

    print("\n✅ Conversion complete. Check the 'sign_frames' folder.")

if __name__ == "__main__":
    sentence = input("Enter text to convert to ISL: ")
    text_to_sign(sentence)
