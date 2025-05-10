import chromadb
from chromadb.config import Settings

client = chromadb.Client(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_store"
)


collection = client.get_or_create_collection(name="faq_store")


def add_documents(tenant_id: str, docs: list[str], embeddings: list[list[float]], ids: list[str]):
    metadatas = [{"tenant_id": tenant_id} for _ in docs]
    collection.add(documents=docs, embeddings=embeddings, metadatas=metadatas, ids=ids)



def query_documents(tenant_id: str, query_embedding: list[float], top_k=3):
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        where={"tenant_id": tenant_id}
    )
