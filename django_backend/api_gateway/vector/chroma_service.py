import chromadb
import os


# just for testing in local (with relative path issues with testing)
# CHROMA_PATH = "/Users/dineshsharma/Documents/chroma_store"


def get_collection():
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    CHROMA_PATH = os.path.join(BASE_DIR, "chroma_store")

    client = chromadb.PersistentClient(path=CHROMA_PATH)
    return client.get_or_create_collection(name="faq_store")


def add_documents(tenant_id: str, docs: list[str], embeddings: list[list[float]], ids: list[str]):
    collection = get_collection()
    metadatas = [{"tenant_id": tenant_id} for _ in docs]
    collection.add(documents=docs, embeddings=embeddings, metadatas=metadatas, ids=ids)
    print("✅ Documents added. Current count:", collection.count())


def query_documents(tenant_id: int, query_embedding: list[float], top_k=3):
    collection = get_collection()
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        where={"tenant_id": tenant_id}
    )
