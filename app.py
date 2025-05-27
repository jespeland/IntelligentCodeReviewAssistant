from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

@app.route("/webhook", methods=["POST"])
def webhook():
    event = request.json
    # Parse GitHub event here
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(port=5000)