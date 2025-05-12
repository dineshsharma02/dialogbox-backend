import openai
import os
from dotenv import load_dotenv
load_dotenv() 

openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
# print(openrouter_api_key)
openrouter_api_base = "https://openrouter.ai/api/v1"

DEFAULT_MODEL = "mistralai/mixtral-8x7b-instruct" 

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