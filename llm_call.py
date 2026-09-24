import os
from dotenv import load_dotenv
load_dotenv()

api_key= os.getenv("GROQ_API_KEY")

import requests
url="https://api.groq.com/openai/v1/chat/completions"

#headers contains additional information that you're sending along with the HTTP request.
headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

#payload contains the actual information you're sending to the LLM.
payload={
    "model": "openai/gpt-oss-20b",
    "messages":[
        {"role":"user","content":"In one sentence, what is root cause localization in the context of log anomaly detection?"}
        ]
}

response = requests.post(url, headers=headers, json=payload)
#print(response.status_code)
#print(response.json())
answer=response.json()["choices"][0]["message"]["content"]
print(answer)