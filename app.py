from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__)

PROJECTS = [
    {
        "name": "🔒 LinkShield",
        "desc": "Advanced URL threat detection system with real-time phishing prevention using ML models",
        "skills": ["ML Security", "FastAPI", "Transformers", "Python"],
        "live": "https://huggingface.co/spaces/sreelekhaputta2/LinkShield",
        "video": "Linkshield.mp4"
    },
    {
        "name": "✨ Idealyze", 
        "desc": "AI-powered content optimization platform that enhances text for maximum engagement",
        "skills": ["NLP", "Transformers", "FastAPI", "Gradio"],
        "live": "https://huggingface.co/spaces/sreelekhaputta2/Idealyze",
        "video": "Idealyze.mp4"
    },
    {
        "name": "💬 Wiseverse",
        "desc": "Intelligent conversational AI chatbot with context-aware responses and memory",
        "skills": ["LLMs", "Gradio", "PyTorch", "LangChain"],
        "live": "https://huggingface.co/spaces/sreelekhaputta2/Chatbot",
        "video": "Wiseverse.mp4"
    },
    {
        "name": "🎭 Avatarverse",
        "desc": "Real-time AI avatar generation and animation platform with facial synthesis",
        "skills": ["Computer Vision", "GANs", "WebGL", "MediaPipe"],
        "live": "https://huggingface.co/spaces/sreelekhaputta2/AvatarVerse",
        "video": "Avatarverse.mp4"
    },
    {
        "name": "📄 GenDoc AI",
        "desc": "Automated document generation with AI-powered templates and customization",
        "skills": ["LLMs", "PDF Generation", "Streamlit", "LaTeX"],
        "live": "https://huggingface.co/spaces/sreelekhaputta2/GenDoc_AI",
        "video": "GendocAI.mp4"
    },
    {
        "name": "🎵 DivineLoop",
        "desc": "Real-time audio-visual looping generator with AI-enhanced effects",
        "skills": ["Audio Processing", "WebRTC", "Computer Vision", "FFmpeg"],
        "live": "https://huggingface.co/spaces/sreelekhaputta2/DivineLoop",
        "video": "Divineloop.mp4"
    }
]

@app.route('/')
def index():
    return render_template('index.html', projects=PROJECTS)

@app.route('/videos/<filename>')
def video(filename):
    if filename == 'bg.mp4' or any(p['video'] == filename for p in PROJECTS):
        return send_from_directory('.', filename)
    abort(404)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
