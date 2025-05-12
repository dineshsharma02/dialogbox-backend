from .vector.chroma_service import query_documents
from .embedding.embedding_service import embed_text
from api_gateway.retrieval.retrieval_service import retrieve_top_k_answers, rank_results

from .cleaning.cleaning_service import clean_query


def embed_query(cleaned_text: str) -> list[float]:
    return embed_text([cleaned_text], is_query=True)[0]

def process_user_query(question: str, tenant_id: int):
    cleaned = clean_query(question)
    retrieval = retrieve_top_k_answers(cleaned, tenant_id)
    ranked_results = rank_results(retrieval, threshold=0.4)
    
    return {
        "query": cleaned,
        "embedding": retrieval["query_embedding"],
        "top_results": ranked_results,
        "answer": ranked_results[0]["text"] if ranked_results else "Sorry, no relevant answer found."
    }
