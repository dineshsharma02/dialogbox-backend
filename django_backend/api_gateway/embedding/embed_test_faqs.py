import sys
import os
# Ensure base path is correct
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from api_gateway.embedding.embedding_pipeline import embed_faqs
from chromadb import PersistentClient
# Use relative base path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_store")
client = PersistentClient(path=CHROMA_PATH)
collection = client.get_or_create_collection("faq_store")

print("Document count (before):", collection.count())

# ✅ Sample test data with full Q+A
sample_data = {
    "1": [
        {"question": "This is tenant 1 question for just testing", "answer": "test answer"}
    ],
    "2": [
        {"question": "This is tenant 2 question for just testing", "answer": "test answer"}
    ]
}

for tenant_id, faqs in sample_data.items():
    result = embed_faqs(tenant_id, faqs)
    print(f"✅ Added FAQs for tenant {tenant_id} → {result['added_count']} docs")
print("Document count (after):", collection.count())
