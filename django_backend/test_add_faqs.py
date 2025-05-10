# Place this at the root level of your backend project (same level as manage.py)
 
from api_gateway.vector.chroma_service import add_documents

# Dummy FAQ docs for tenant t1_demo
docs = [
    "How do I reset my password?",
    "Where can I find my billing history?",
    "How to cancel my subscription?"
]

# Dummy embeddings (temporary — will use real ones after Day 28)
embeddings = [
    [0.1, 0.2, 0.3],
    [0.9, 0.4, 0.1],
    [0.3, 0.7, 0.6]
]

ids = ["faq-006", "faq-007", "faq-009"]

# Add to ChromaDB
add_documents("new_test", docs, embeddings, ids)

print("Successfully added dummy documents to ChromaDB for tenant comp_2_test")
