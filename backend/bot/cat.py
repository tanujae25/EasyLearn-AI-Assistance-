from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

genai.configure(api_key="g.a000vgigAxiSKXKPRYKdIMZspGYH2PSMLjU5GVil0parrb3bY3hTO_LoNXkDfdZV3hAGCwRyPAACgYKAV0SARUSFQHGX2MipFAQyFHNp7X8kFN6iSg7PxoVAUF8yKqcI483g3Y3FAbMRiqikLBs0076")
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

@app.route('/chat', methods=['POST'])
def chat_with_bot():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_input = data["message"]
    response = chat.send_message(user_input)
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)  # 👈 this is the key line
