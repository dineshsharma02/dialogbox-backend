import openai
import os
from dotenv import load_dotenv
load_dotenv() 

openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
# print(openrouter_api_key)
openrouter_api_base = "https://openrouter.ai/api/v1"

DEFAULT_MODEL = "mistralai/mixtral-8x7b-instruct" 


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




def generate_answer(prompt:str, model:str = DEFAULT_MODEL):
    client = openai.OpenAI(
        api_key =openrouter_api_key,
        base_url=openrouter_api_base
    )
    try:
        response = client.chat.completions.create(
            model = model,
            
            messages=[
                {"role": "system", "content": "You are a helpful support assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None