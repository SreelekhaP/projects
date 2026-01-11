from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

PROJECTS = [
    {"name": "🔒 LinkShield", "desc": "Advanced URL threat detection", "skills": ["ML Security", "FastAPI", "Transformers"], "live": "https://huggingface.co/spaces/sreelekhaputta2/LinkShield", "video": "Linkshield.mp4"},
    {"name": "✨ Idealyze", "desc": "AI content optimization", "skills": ["NLP", "Transformers", "FastAPI"], "live": "https://huggingface.co/spaces/sreelekhaputta2/Idealyze", "video": "Idealyze.mp4"},
    {"name": "💬 Wiseverse", "desc": "AI conversational chatbot", "skills": ["LLMs", "Gradio", "PyTorch"], "live": "https://huggingface.co/spaces/sreelekhaputta2/Chatbot", "video": "Wiseverse.mp4"},
    {"name": "🎭 Avatarverse", "desc": "Real-time AI avatar generation", "skills": ["Computer Vision", "GANs", "WebGL"], "live": "https://huggingface.co/spaces/sreelekhaputta2/AvatarVerse", "video": "Avatarverse.mp4"},
    {"name": "📄 GenDoc AI", "desc": "Automated document generation", "skills": ["LLMs", "PDF Generation", "Streamlit"], "live": "https://huggingface.co/spaces/sreelekhaputta2/GenDoc_AI", "video": "GendocAI.mp4"},
    {"name": "🎵 DivineLoop", "desc": "Audio-visual looping generator", "skills": ["Audio Processing", "WebRTC", "FFmpeg"], "live": "https://huggingface.co/spaces/sreelekhaputta2/DivineLoop", "video": "Divineloop.mp4"}
]

@app.route('/')
def index():
    return render_template('index.html', projects=PROJECTS)

@app.route('/videos/<filename>')
def serve_video(filename):
    video_files = ['bg.mp4', 'Linkshield.mp4', 'Idealyze.mp4', 'Wiseverse.mp4', 
                   'Avatarverse.mp4', 'GendocAI.mp4', 'Divineloop.mp4']
    if filename in video_files and os.path.exists(filename):
        return send_from_directory('.', filename, mimetype='video/mp4')
    abort(404)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Accept-Ranges'] = 'bytes'
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
