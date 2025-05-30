import openai
import os
import requests
from dotenv import load_dotenv
from api_gateway.cleaning.cleaning_service import clean_llm_output


load_dotenv()

USE_REMOTE_LLM = os.getenv("USE_REMOTE_LLM", "true").lower() == "true"
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
openrouter_api_base = "https://openrouter.ai/api/v1"

DEFAULT_MODEL = "meta-llama/llama-4-maverick:free"


def get_prompt_instructions(tenant_id):
    from admin_panel.models import Tenant
    DEFAULT_INSTRUCTIONS = "You are a helpful support assistant. Answer clearly and politely."

    try:
        tenant = Tenant.objects.select_related("category").get(pk = tenant_id)
        if tenant.instructions and tenant.instructions.strip():
            return tenant.instructions.strip()
        # 2. Otherwise fallback to category instructions
        if tenant.category and tenant.category.instructions:
            return tenant.category.instructions.strip()
        # 3. Otherwise fallback to system default
        return DEFAULT_INSTRUCTIONS
    except Tenant.DoesNotExist:
        return DEFAULT_INSTRUCTIONS




def build_prompt(query: str, context_docs: list[str], tenant_id) -> str:
    joined_context = "\n\n".join([f"- {doc}" for doc in context_docs])
    instructions = get_prompt_instructions(tenant_id)
    return f"""
    {instructions}

    Real Context:
    {joined_context}

    User Question:
    {query}
    Respond in a friendly and clear tone.
"""



def generate_answer(prompt: str, model: str = DEFAULT_MODEL):
    if USE_REMOTE_LLM:
        try:
            response = requests.post("http://localhost:9002/generate", json={
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
