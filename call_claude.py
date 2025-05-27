import os
import requests
from venv import load_dotenv

load_dotenv()

def call_claude():
    api_key = os.getenv("CLAUDE_API_KEY")

    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    data = {
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": "Hello, world"}
        ]
    }

    response = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None
    
result = call_claude()
if result: 
    reply = result["content"][0]["text"]
    print(("Claude says:", reply))
else:
    print("API ERROR")