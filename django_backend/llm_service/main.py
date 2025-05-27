from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os


openai_api_key = os.getenv("OPENROUTER_API_KEY")
openai_api_base = "https://openrouter.ai/api/v1"
DEFAULT_MODEL = "meta-llama/llama-4-maverick:free"

app = FastAPI()

import ast
import re

def clean_llm_output(text):
    # If it's like "\"text\"" → convert to 'text'
    try:
        text = ast.literal_eval(text)
    except Exception:
        pass  # If not evaluable, leave it

    # Now strip any leftover weird quotes just in case
    return re.sub(r'^["“”\']+|["“”\']+$', '', text.strip())

class LLMRequest(BaseModel):
    prompt: str
    model: str = DEFAULT_MODEL

@app.post("/generate")
async def generate_response(payload: LLMRequest):
    client = openai.OpenAI(
        api_key=openai_api_key,
        base_url=openai_api_base
    )
    try:
        response = client.chat.completions.create(
            model=payload.model,
            messages=[
                {"role": "system", "content": "You are a helpful support assistant."},
                {"role": "user", "content": payload.prompt}
            ]
        )
        # return clean_llm_output(response.choices[0].message.content.strip())
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
