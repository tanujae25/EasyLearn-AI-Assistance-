from flask import Flask, request, jsonify, send_file  # ⬅️ use send_file instead
from flask_cors import CORS
import google.generativeai as genai
import os

# Set Gemini API key
os.environ["GOOGLE_API_KEY"] = "g.a000uwgVWl5p39EMpKQrBHVm5y0MoYEgh1gsBmJWPTkKnPavC5JwJ2CA8f0h8ALrOtNFih0naQACgYKAcISARESFQHGX2MiY1O3Kyb1NgfNXFQZwW6T5RoVAUF8yKr8I4Eu021NHHLGwvjQBgIB0076"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

app = Flask(__name__)
CORS(app)

@app.route('/')
def serve_html():
    return send_file('index.html')  # ⬅️ serve HTML file directly

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    
    return jsonify({'answer': response.text})

if __name__ == '__main__':
    app.run(port=5000)