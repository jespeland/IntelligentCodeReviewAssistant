from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    event = request.json
    print("📦 Webhook received:")
    print(event)
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(port=5000)

