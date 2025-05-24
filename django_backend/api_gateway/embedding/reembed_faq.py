import sys
import os
import chromadb
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from api_gateway.embedding.embedding_pipeline import embed_faqs
from admin_panel.models import FAQ

client = chromadb.HttpClient(host="chroma", port=8000)
# client.delete_collection("faq_store")
# print("Connected to ChromaDB")
# print("Heartbeat:", client.heartbeat())



# for faq in FAQ.objects.all():
#     embed_faqs(faq.tenant_id, [faq.question], ids=[f"{faq.tenant_id}-{faq.id}"])


# collection = client.get_or_create_collection("faq_store")
# print(collection.count())