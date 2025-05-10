from .vector.chroma_service import query_documents

def clean_query(text: str) -> str:
    return text.strip().lower()


def embed_query(cleaned_text: str) -> list[float]:
    # Replace this later with real embedding model
    return [0.1, 0.2, 0.3]



def process_user_query(question: str, tenant_id: int):
    cleaned = clean_query(question)
    embedding = embed_query(cleaned)
    results = query_documents(tenant_id, embedding)
    return {
        "query": cleaned,
        "embedding": embedding,
        "results": results
    }