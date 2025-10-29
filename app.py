from flask import Flask, render_template, request, jsonify
import os
import whisper

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load whisper model once
model = whisper.load_model("base")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['video']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Transcribe using Whisper
    result = model.transcribe(filepath)
    captions = result['segments']
    paragraph = " ".join([seg['text'] for seg in captions])

    return jsonify({
        'video_path': f"/static/uploads/{file.filename}",
        'captions': captions,
        'paragraph': paragraph
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
