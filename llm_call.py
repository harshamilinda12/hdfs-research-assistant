import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key= os.getenv("GROQ_API_KEY")

def ask_llm(prompt,system_prompt="You are a helpful assistant."):
    url="https://api.groq.com/openai/v1/chat/completions"
    headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
    }
    payload={
    "model": "openai/gpt-oss-20b",
    "messages":[
        {"role": "system", "content": system_prompt},
        {"role":"user","content":prompt}
        ]
    }
    response=requests.post(url,headers=headers,json=payload)
    answer=response.json()["choices"][0]["message"]["content"]
    
    return answer

#headers contains additional information that you're sending along with the HTTP request.
#payload contains the actual information you're sending to the LLM.

#if __name__=="__main__":#this bit is for testing this file alone
  #   question = "In one sentence, what is root cause localization in the context of log anomaly detection?"
   #  print(ask_llm(question))

RESEARCH_TUTOR_PROMPT = """You are a research assistant helping an undergraduate student with their research on
Parameter-Aware Root Cause Localization for Session-Level Log Anomalies in HDFS.

Your role:
- Explain concepts clearly and patiently, as if teaching someone still learning the field.
- When explaining something technical, break it down step by step rather than assuming prior knowledge.
- Be precise about terminology from log anomaly detection, distributed systems, and machine learning.
- If you are unsure about something, say so explicitly rather than guessing.
"""

if __name__ == "__main__":
    question = "What does 'session-level' mean in the context of log anomaly detection, as opposed to other levels?"
    print(ask_llm(question, system_prompt=RESEARCH_TUTOR_PROMPT))