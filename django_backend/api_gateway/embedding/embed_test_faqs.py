import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


from test_faq_data import sample_data
from embedding_pipeline import embed_faqs

from chromadb import PersistentClient

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_store")

client = PersistentClient(path=CHROMA_PATH)
collection = client.get_or_create_collection("faq_store")
print("Document count:", collection.count())


for tenant_id, faqs in sample_data.items():
    result = embed_faqs(tenant_id, faqs)
    print(f"Added FAQs for {tenant_id} → {result['added_count']} docs")


print("Document count (after):", collection.count())