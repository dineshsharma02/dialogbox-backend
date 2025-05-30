import requests, os
from api_gateway.vector.chroma_service import add_documents
from api_gateway.embedding.embedding_service import embed_text

USE_REMOTE_EMBEDDING = os.getenv("USE_REMOTE_EMBEDDING", "false").lower() == "true"

def embed_faqs(tenant_id: int, faqs: list[dict]):
    """
    Each item in `faqs` should be a dict with 'question', 'answer', and 'id'.
    This function embeds "Q: ... A: ..." and stores it in Chroma.
    """

    # Step 1: Convert each FAQ to a document string
    docs = [f"Q: {faq['question']}\nA: {faq['answer']}" for faq in faqs]

    # ✅ Step 2: Use consistent, deterministic IDs
    ids = [f"{tenant_id}-{faq['id']}" for faq in faqs]

    # Step 3: Embed the documents
    if USE_REMOTE_EMBEDDING:
        try:
            response = requests.post("http://localhost:9001/embed", json={
                "texts": docs,
                "is_query": False
            })
            response.raise_for_status()
            embeddings = response.json()["embeddings"]
        except Exception as e:
            print("Embedding service failed:", e)
            raise
    else:
        embeddings = embed_text(docs, is_query=False)

    # Step 4: Add to Chroma
    add_documents(int(tenant_id), docs, embeddings, ids)

    return {
        "added_count": len(docs),
        "tenant_id": tenant_id,
        "doc_ids": ids
    }
