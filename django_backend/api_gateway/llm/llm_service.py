import openai
import os
import requests
from dotenv import load_dotenv

load_dotenv()

USE_REMOTE_LLM = os.getenv("USE_REMOTE_LLM", "true").lower() == "true"
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
openrouter_api_base = "https://openrouter.ai/api/v1"

DEFAULT_MODEL = "meta-llama/llama-4-maverick:free"

def build_prompt(query: str, context_docs: list[str]) -> str:
    joined_context = "\n\n".join([f"- {doc}" for doc in context_docs])
    return f"""
You are a helpful customer support assistant.

Your job is to answer the user's question **only using the provided context** below.
If the answer is not in the context, reply with "I'm not sure based on current information."

---
Context:

{joined_context}
---
User Question:
{query}

Respond in a friendly and clear tone.
"""

def generate_answer(prompt: str, model: str = DEFAULT_MODEL):
    if USE_REMOTE_LLM:
        try:
            response = requests.post("http://llm:9002/generate", json={
                "prompt": prompt,
                "model": model
            })
            response.raise_for_status()

            return response

        except Exception as e:
            print(f"[LLM microservice error] {e}")
            return "There was an issue generating a response."

    else:
        client = openai.OpenAI(
            api_key=openrouter_api_key,
            base_url=openrouter_api_base
        )
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a helpful support assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content.strip()

        except Exception as e:
            print(f"[OpenRouter error] {e}")
            return "There was an issue generating a response."
