import chromadb
chroma_client = chromadb.HttpClient(host='localhost', port=8000)

collection = chroma_client.get_collection("faq_store")
# print(collection.get(where={"":""}))
print(collection.count())



print(chroma_client.heartbeat())
