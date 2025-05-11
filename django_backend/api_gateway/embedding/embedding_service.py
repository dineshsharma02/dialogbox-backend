from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-base-en-v1.5")

def embed_text(texts: list[str], is_query=False):
    prefix = "passage: "
    if is_query:
        prefix = "query: "

    prepped_texts = [prefix + text.strip() for text in texts]
    embeddings = model.encode(prepped_texts, normalize_embeddings=True)
    return embeddings.tolist()
    