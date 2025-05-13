from llm_service import build_prompt, generate_answer
# when connecting with whole system
# prompt = build_prompt(query="How do I cancel my plan?", context_docs=ranked_results)


# for basic test purpose
prompt = build_prompt(query="How do I cancel my plan?", context_docs=["You can cancel your subscription anytime via the Billing section.", "To reset your password, go to Account Settings > Reset Password."])
response = generate_answer(prompt)
print(response)
