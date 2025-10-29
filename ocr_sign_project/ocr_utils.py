import cv2
import easyocr

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

def extract_text(video_path):
    """Extract text from video frames using EasyOCR"""
    cap = cv2.VideoCapture(video_path)
    full_text = ""
    frame_count = 0

    if not cap.isOpened():
        return "❌ Error: Cannot open video."

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % 10 != 0:
            continue  # process every 10th frame

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        try:
            result = reader.readtext(gray, detail=0, paragraph=True)
            if result:
                full_text += " ".join(result) + " "
        except Exception as e:
            print("⚠️ EasyOCR error:", e)

    cap.release()
    return full_text.strip() if full_text else "No readable text found."

def summarize_text(text):
    """Simple summarization"""
    if not text or "No readable text" in text:
        return "No text detected to summarize."
    sentences = text.split(".")
    summary = ". ".join(sentences[:3])
    return summary
