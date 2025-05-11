from .vector.chroma_service import query_documents
from .embedding.embedding_service import embed_text
from api_gateway.retrieval.retrieval_service import retrieve_top_k_answers

from .cleaning.cleaning_service import clean_query


def embed_query(cleaned_text: str) -> list[float]:
    return embed_text([cleaned_text], is_query=True)[0]

def process_user_query(question: str, tenant_id: int):
    cleaned = clean_query(question)
    retrieval = retrieve_top_k_answers(cleaned, tenant_id)
    if not retrieval["matched_docs"]:
        return {
            "answer": "Sorry, I couldn't find anything relevant.",
        }
    return {
        "cleaned_query": cleaned,
        "embedding": retrieval["query_embedding"],
        "top_results": retrieval["matched_docs"]
    }
