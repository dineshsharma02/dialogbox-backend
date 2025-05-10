import chromadb
client = chromadb.PersistentClient("./chroma_store")
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