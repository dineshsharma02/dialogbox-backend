import os
from chromadb import PersistentClient, HttpClient
from dotenv import load_dotenv

env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.env"))

load_dotenv(dotenv_path=env_path)



def get_chroma_collection():
    USE_HTTP = os.getenv("USE_CHROMA_HTTP", "false").lower() == "true"
    if USE_HTTP:
        client = HttpClient(host="localhost", port=8000)  # Docker hostname
    else:
        BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
        CHROMA_PATH = os.path.join(BASE_DIR, "chroma_store")
        print("Using local Chroma store at:", CHROMA_PATH)
        client = PersistentClient(path=CHROMA_PATH)
    collection = client.get_or_create_collection("faq_store")
    return collection




def add_documents(tenant_id: int, docs: list[str], embeddings: list[list[float]], ids: list[str]):
    collection = get_chroma_collection()
    metadatas = [{"tenant_id": tenant_id} for _ in docs]
    collection.add(documents=docs, embeddings=embeddings, metadatas=metadatas, ids=ids)
    print("Documents added. Current count:", collection.count())


def query_documents(tenant_id: int, query_embedding: list[float], top_k=10):
    collection = get_chroma_collection()
    try:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where={"tenant_id": tenant_id}
        )
    except Exception as e:
        print("Chroma error: ",e)
        return []

    if not results["documents"][0]:
        print(f"No match found for tenant {tenant_id}")
    return results


# Optional utility functions for local testing/debug
def count_documents():
    collection = get_chroma_collection()
    return collection.count()

def clear_documents():
    collection = get_chroma_collection()
    collection.delete(where={})
    print("Cleared all documents from collection.")
