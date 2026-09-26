import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key= os.getenv("GROQ_API_KEY")

def ask_llm(prompt):
    url="https://api.groq.com/openai/v1/chat/completions"
    headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
    }
    payload={
    "model": "openai/gpt-oss-20b",
    "messages":[
        {"role":"user","content":"In one sentence, what is root cause localization in the context of log anomaly detection?"}
        ]
    }
    response=requests.post(url,headers=headers,json=payload)
    answer=response.json()["choices"][0]["message"]["content"]
    
    return answer

#headers contains additional information that you're sending along with the HTTP request.
#payload contains the actual information you're sending to the LLM.

if __name__=="__main__":
     question = "In one sentence, what is root cause localization in the context of log anomaly detection?"
     print(ask_llm(question))