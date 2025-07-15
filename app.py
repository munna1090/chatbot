from flask import Flask, request, jsonify, render_template
from google import genai
from google.genai import types
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "composite-depot-466005-f0-76af2b950c76.json"

app = Flask(__name__)

# ✅ Your Gemini 2.5 config
client = genai.Client(
    vertexai=True,
    project="composite-depot-466005-f0",
    location="global",
)

MODEL = "gemini-2.5-flash-lite-preview-06-17"

SYSTEM_INSTRUCTION = """You are a helpful AI/ML student mentor. Answer questions, help with study plans, predict topics, guide students. Never provide direct exam answers."""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_query = request.json.get("query")

    if not user_query:
        return jsonify({"error": "No input provided"}), 400

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_query)]
        )
    ]

    config = types.GenerateContentConfig(
        temperature=0.2,
        top_p=0.8,
        max_output_tokens=1024,
        system_instruction=[types.Part.from_text(text=SYSTEM_INSTRUCTION)],
        safety_settings=[
            types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="OFF"),
            types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="OFF"),
            types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="OFF"),
            types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="OFF"),
        ],
        thinking_config=types.ThinkingConfig(thinking_budget=0),
    )

    answer = ""
    for chunk in client.models.generate_content_stream(
        model=MODEL,
        contents=contents,
        config=config,
    ):
        answer += chunk.text

    return jsonify({"answer": answer})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

