from .vector.chroma_service import query_documents
from .embedding.embedding_service import embed_text
from api_gateway.retrieval.retrieval_service import retrieve_top_k_answers, rank_results
from api_gateway.llm.llm_service import build_prompt, generate_answer

from .cleaning.cleaning_service import clean_query
from django.http import JsonResponse



def embed_query(cleaned_text: str) -> list[float]:
    return embed_text([cleaned_text], is_query=True)[0]

def process_user_query(question: str, tenant_id: int):
    cleaned = clean_query(question)
    # if not question or not isinstance(question, str):
    #     return JsonResponse({
    #         "query": cleaned,
    #         "answer": "Invalid or too short query.",
    #         "status": "error",
    #         "context_used": [],
    #     }, status=400)
    retrieval = retrieve_top_k_answers(cleaned, tenant_id)
    ranked_results = rank_results(retrieval, threshold=0.35)
   
    # if not ranked_results:
    #     return {
    #         "query": cleaned,
    #         "answer": "Sorry, I couldn’t find any relevant answer based on current information.",
    #         "context_used": [],
    #         "status": "no_match"
    # }
    

    context_docs = [item["text"] for item in ranked_results]
    prompt = build_prompt(query=cleaned, context_docs=context_docs, tenant_id = tenant_id)
    final_answer = generate_answer(prompt)


    return {
        "query": cleaned,
        "answer": final_answer,
        "context_used": context_docs,
        "matched_results": ranked_results,
        "status": "success"
    }
