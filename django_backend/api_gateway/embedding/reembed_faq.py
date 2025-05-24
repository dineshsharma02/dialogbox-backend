import sys
import os
import chromadb
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from api_gateway.embedding.embedding_pipeline import embed_faqs
from admin_panel.models import FAQ
from api_gateway.vector.chroma_service import get_chroma_collection



print("Connected to ChromaDB")
collection = get_chroma_collection()
# print("Heartbeat:", client.heartbeat())
# client.delete_collection("faq_store")





for faq in FAQ.objects.all():
    embed_faqs(faq.tenant_id, {"question":FAQ.question, "answer":FAQ.answer}, ids=[f"{faq.tenant_id}"])


# collection = client.get_or_create_collection("faq_store")
# print(collection.count())