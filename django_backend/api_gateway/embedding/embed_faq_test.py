from embedding_pipeline import embed_faqs

sample_faqs = [
    "How do I change my email address?",
    "Can I pause my subscription?",
    "What payment methods do you support?"
]

result = embed_faqs("t1_demo", sample_faqs)
print(result)