# Place this at the root level of your backend project (same level as manage.py)
 
from api_gateway.vector.chroma_service import add_documents
from api_gateway.embedding.embedding_service import embed_text

add_documents(
  "t1_demo",
  ["How do I cancel subscription?", "Where is my billing info?"],
  embed_text(["How do I cancel subscription?", "Where is my billing info?"], is_query=False),
  ["faq-001", "faq-002"]
)

print("Successfully added dummy documents to ChromaDB for tenant t1_demo")
