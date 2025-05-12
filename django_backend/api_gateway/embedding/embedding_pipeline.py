from api_gateway.embedding.embedding_service import embed_text
from api_gateway.vector.chroma_service import add_documents
import uuid

def embed_faqs(tenant_id: str, faqs: list[str]):
    """
    Embeds a list of FAQs and stores them in ChromaDB with tenant_id.
    """
    ids = [f"{tenant_id}-{uuid.uuid4().hex[:8]}" for _ in faqs]
    embeddings = embed_text(faqs, is_query=False)
    add_documents(tenant_id, faqs, embeddings, ids)

    return {
        "added_count": len(faqs),
        "tenant_id": tenant_id,
        "doc_ids": ids
    }
