# 💬 DialogBox — AI Chat Widget for Support Automation (Work in progress)

Built for startups and support teams who want plug-and-play automation — without sacrificing control, branding, or performance.

---

## 🚀 Features

-  **Plug & Play Widget** — Just copy an iframe snippet and embed anywhere
-  **Context-Aware RAG Engine** — Combines vector search with LLMs for accurate answers
-  **User Query API** — Lightweight FastAPI gateway for chat integrations
-  **Admin Dashboard** — Upload FAQs, monitor usage, and manage tenants
-  **Multi-Tenant Support** — Isolated contexts for each client or organization
-  **Dockerized Microservices** — Easy to deploy, extend, and scale
-  **ChromaDB Vector Store** — Fast, persistent retrieval layer for document embeddings

---

## Tech Stack

| Area         | Tech |
|--------------|------|
| Frontend     | React + Tailwind CSS (SDK-style widget) |
| Backend      | Django (API Gateway, Admin) |
| Microservices| FastAPI |
| LLMs         | Mistral / GPT via OpenRouter |
| Embeddings   | BGE / E5 + SentenceTransformers |
| Vector DB    | ChromaDB |
| Docker       | All services containerized for portability |



## How It Works

1. **Upload FAQs** → Admin panel supports CSV uploads (question + answer)
2. **Embedding** → Questions/answers are embedded into ChromaDB
3. **Chat Query** → Widget sends query to `/user/query?t=<tenant_id>`
4. **Retrieval** → Query is embedded + used to fetch top-K documents
5. **LLM Response** → Retrieved context passed to LLM for generation
6. **Response** → Sent back and rendered in chat
