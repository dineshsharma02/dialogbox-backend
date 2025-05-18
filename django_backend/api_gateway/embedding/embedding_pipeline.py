def embed_faqs(tenant_id: str, faqs: list[dict]):
    """
    Each item in `faqs` should be a dict with 'question' and 'answer'.
    This function embeds "Q: ... A: ..." and stores it in Chroma.
    """
    import uuid
    from api_gateway.vector.chroma_service import add_documents
    from api_gateway.embedding.embedding_service import embed_text

    #Step 1: Convert each FAQ to a document string
    docs = [f"Q: {faq['question']}\nA: {faq['answer']}" for faq in faqs]

    #Step 2: Embed the documents
    embeddings = embed_text(docs, is_query=False)

    #Step 3: Generate unique IDs
    ids = [f"{tenant_id}-{uuid.uuid4().hex[:8]}" for _ in docs]

    #Step 4: Add to Chroma
    add_documents(tenant_id, docs, embeddings, ids)

    return {
        "added_count": len(docs),
        "tenant_id": tenant_id,
        "doc_ids": ids
    }
