from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    event = request.headers.get("X-GitHub-Event", "unknown")
    payload = request.json
    print(f"\n📬 Received GitHub Event: {event}")
    print(payload)  # log full payload to console

    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(port=5000)
