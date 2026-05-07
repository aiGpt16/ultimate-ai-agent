from flask import Flask, request, jsonify, send_file
import google.generativeai as genai

app = Flask(__name__)

GEMINI_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=GEMINI_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

memory = []

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    msg = data["message"]

    memory.append(msg)

    prompt = """
    You are an advanced AI assistant.
    """ + "\n".join(memory) + msg

    response = model.generate_content(prompt)

    return jsonify({
        "reply": response.text
    })

app.run(
    host="0.0.0.0",
    port=5000
  )
