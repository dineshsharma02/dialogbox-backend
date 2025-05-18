import chromadb
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_store")
# CHROMA_PATH = "/Users/dineshsharma/Documents/chroma_store"

client = chromadb.PersistentClient(CHROMA_PATH)
# collection = client.get_or_create_collection(name="faq_store")
# client.delete_collection(name="faq_store")
collection = client.get_or_create_collection(name="faq_store") 



# Get all vectors (or filter by tenant)
results = collection.get(
    # where={"tenant_id": "t1_demo"},  # or remove this to get all
    include=["documents", "embeddings", "metadatas"]
)


print("IDs:", results["ids"])
print("Docs:", results["documents"])
print("Embeddings:", results["embeddings"])
print("metadatas:",results["metadatas"])