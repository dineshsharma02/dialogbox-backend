import chromadb

try:
    chroma_client = chromadb.HttpClient(host="localhost", port=8000)
    print("Connected to ChromaDB")
    print("Heartbeat:", chroma_client.heartbeat())

    collection = chroma_client.get_collection("faq_store")
    print("Count:", collection.count())

except Exception as e:
    print("Failed to connect to ChromaDB:", e)
