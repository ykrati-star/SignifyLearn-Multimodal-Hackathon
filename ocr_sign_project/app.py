from flask import Flask, render_template, request
from ocr_utils import extract_text, summarize_text
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_video():
    file = request.files.get("file")
    if not file:
        return "No file uploaded", 400

    video_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(video_path)

    extracted_text = extract_text(video_path)
    summary = summarize_text(extracted_text)

    return render_template(
        "index.html",
        extracted_text=extracted_text,
        summary=summary,
        filename=file.filename
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)
