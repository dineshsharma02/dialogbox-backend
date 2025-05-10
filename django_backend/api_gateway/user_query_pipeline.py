from .vector.chroma_service import query_documents
from .embedding.embedding_service import embed_text

def clean_query(text: str) -> str:
    return text.strip().lower()


def embed_query(cleaned_text: str) -> list[float]:
    return embed_text([cleaned_text], is_query=True)[0]



def process_user_query(question: str, tenant_id: int):
    cleaned = clean_query(question)
    embedding = embed_query(cleaned)
    results = query_documents(tenant_id, embedding)
    return {
        "query": cleaned,
        "embedding": embedding,
        "results": results
    }