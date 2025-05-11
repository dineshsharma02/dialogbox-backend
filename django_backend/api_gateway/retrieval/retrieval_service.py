from api_gateway.embedding.embedding_service import embed_text
from api_gateway.vector.chroma_service import query_documents

def retrieve_top_k_answers(question:str, tenant_id: int, k=3):
    query_embedding = embed_text([question],is_query=True)[0]
    results = query_documents(tenant_id, query_embedding, k)
    return {
        "query_embedding": query_embedding,
        "matched_docs": results["documents"][0],
        "matched_ids": results["ids"][0],
        "matched_metadata": results["metadatas"][0],
        "distances": results["distances"][0]
    }