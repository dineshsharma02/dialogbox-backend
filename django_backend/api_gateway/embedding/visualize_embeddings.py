import chromadb
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from api_gateway.vector.chroma_service import get_chroma_collection


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_store")
# CHROMA_PATH = "/Users/dineshsharma/Documents/chroma_store"

# client = chromadb.PersistentClient(CHROMA_PATH)

# client.delete_collection(name="faq_store")
collection = get_chroma_collection()
# collection = client.get_or_create_collection(name="faq_store")



# Get all vectors (or filter by tenant)
results = collection.get(
    # where={"tenant_id": "t1_demo"},  # or remove this to get all
    include=["documents", "embeddings", "metadatas"]
)


print("IDs:", results["ids"])
print("Docs:", results["documents"])
print("Embeddings:", results["embeddings"])
print("metadatas:",results["metadatas"])