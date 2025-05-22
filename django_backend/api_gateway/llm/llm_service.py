import openai
import os
from dotenv import load_dotenv
import requests
load_dotenv() 

openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
# print(openrouter_api_key)
openrouter_api_base = "https://openrouter.ai/api/v1"

DEFAULT_MODEL = "meta-llama/llama-4-maverick:free" 


def build_prompt(query: str, context_docs: list[str]) -> str:
    joined_context = "\n\n".join([f"- {doc}" for doc in context_docs])

    return f"""
You are a helpful customer support assistant.

Your job is to answer the user's question **only using the provided context** below.
if the answer is not in the context, reply with "I'm not sure based on current information."

---
Context:

{joined_context}
---
User Question:
{query}



Respond in a friendly and clear tone.    
"""




def generate_answer(prompt: str, model: str = "mistralai/mixtral-8x7b-instruct"):
    res = requests.post("http://llm:9002/generate", json={
        "prompt": prompt,
        "model": model
    })
    return res.json()["response"]