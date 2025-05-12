from llm_service import generate_answer

prompt = """User asked: "How do I reset my password?"
Context: "To reset your password, go to Account > Settings > Reset Password."""

print(generate_answer(prompt))