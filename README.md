# DialogBox — Chatbot as a Service

**Enterprise-grade conversational AI, built for scale.**

DialogBox is a **Chatbot-as-a-Service (CaaS)** platform that delivers intelligent, context-aware support automation. Built on a modern microservices architecture, it is designed for **great scalability** and **extreme potential for growth**—whether you're onboarding your first tenant or scaling to thousands of organizations worldwide.

---

## Why DialogBox?

- **True multi-tenant CaaS** — One platform, many brands. Each tenant gets isolated data, custom instructions, and a dedicated knowledge base without sacrificing performance or security.
- **RAG-powered accuracy** — Retrieval-augmented generation keeps answers grounded in your content. Fewer hallucinations, higher trust.
- **Built to scale** — Stateless API gateway, independent embedding and LLM services, and a dedicated vector store mean you can scale each layer independently as traffic grows.
- **Plug-and-play for developers** — Embed the chat widget with a snippet, call the REST API from any stack, or integrate with your existing auth and CRM.

---

## Features

| Feature | Description |
|--------|-------------|
| **Plug & Play Widget** | Copy an iframe or SDK snippet and embed the chatbot anywhere—websites, portals, internal tools. |
| **Context-Aware RAG** | Vector search + LLM synthesis. Queries hit your FAQs and docs; answers stay accurate and on-brand. |
| **User Query API** | Lightweight REST API for chat: `POST /user/query` with tenant context and get structured, low-latency responses. |
| **Admin Dashboard** | Upload FAQs (e.g. CSV), manage tenants, categories, and custom LLM instructions—all from one place. |
| **Multi-Tenant Isolation** | Tenant-scoped vector collections and metadata. Data and config are fully isolated per organization. |
| **Microservices Architecture** | Django API Gateway, FastAPI embedding service, FastAPI LLM gateway, ChromaDB—each service can scale and deploy independently. |
| **Vector Store (ChromaDB)** | Persistent, fast similarity search with tenant filtering. Ready to swap or shard as you grow. |

---

## End-to-End Architecture

DialogBox is built as a **layered, service-oriented system**. Request flow is linear and observable; each layer can be scaled, replaced, or optimized without rewriting the rest.

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              CLIENT LAYER                                             │
│  ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐             │
│  │  Web / Mobile    │    │  Third-party      │    │  Internal tools   │             │
│  │  (Chat Widget)   │    │  integrations     │    │  (API consumers)  │             │
│  └────────┬─────────┘    └────────┬─────────┘    └────────┬─────────┘             │
└───────────┼───────────────────────┼───────────────────────┼─────────────────────────┘
            │                       │                       │
            └───────────────────────┼───────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           API GATEWAY (Django)                                        │
│  • Auth (JWT)  • Tenant resolution (API key / header)  • Request validation           │
│  • POST /user/query  • Admin & token endpoints                                        │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                    │
            ┌───────────────────────┼───────────────────────┐
            ▼                       ▼                       ▼
┌───────────────────────┐ ┌───────────────────────┐ ┌───────────────────────┐
│   CLEANING SERVICE    │ │   RETRIEVAL PIPELINE  │ │   LLM ORCHESTRATION  │
│   Normalize & prep   │ │   Embed query →       │ │   Build prompt →      │
│   user query text    │ │   ChromaDB search →   │ │   Call LLM service →  │
│   (in-process)        │ │   Rank & filter       │ │   Return final answer │
└───────────────────────┘ └───────────┬───────────┘ └───────────┬───────────┘
                                      │                         │
            ┌─────────────────────────┼─────────────────────────┘
            ▼                         ▼
┌───────────────────────┐   ┌───────────────────────┐   ┌───────────────────────┐
│  EMBEDDING SERVICE    │   │  VECTOR STORE         │   │  LLM SERVICE          │
│  (FastAPI, port 9001) │   │  (ChromaDB, 8000)     │   │  (FastAPI, port 9002) │
│  BGE / E5 models      │   │  Tenant-scoped        │   │  OpenRouter / Mistral │
│  Query & passage      │   │  collections          │   │  GPT / LLaMA, etc.    │
│  embeddings           │   │  Persistent storage   │   │  Model-agnostic API   │
└───────────────────────┘   └───────────────────────┘   └───────────────────────┘
```

### Request flow (simplified)

1. **Client** sends a question to the API Gateway with tenant identification (e.g. API key or header).
2. **Gateway** validates the request, resolves the tenant, and runs the **user query pipeline**.
3. **Cleaning** normalizes the query (lowercasing, punctuation, etc.) for consistent retrieval.
4. **Retrieval**:
   - Query is sent to the **Embedding Service** → vector representation.
   - Vector is used to **query ChromaDB** with tenant filter → top-K similar FAQ/documents.
   - Results are **ranked** by similarity/confidence and filtered by threshold.
5. **LLM**:
   - Gateway builds a **prompt** from the query and retrieved context (with tenant/category instructions).
   - **LLM Service** is called → generates the final answer.
6. **Gateway** returns a structured JSON response (query, matched context, final answer, latency).

### Data and configuration

- **Tenants** and **Company Categories** (with optional LLM instructions) are stored in the Django DB.
- **FAQs** are embedded via the Admin pipeline and stored in ChromaDB with `tenant_id` metadata.
- **Vector store** can run in-process (PersistentClient) or as a separate ChromaDB server (HttpClient) for production scaling.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | React, Tailwind CSS (embedding SDK / chat widget) |
| **API & Admin** | Django, Django REST Framework, JWT (Simple JWT) |
| **Embedding** | FastAPI, SentenceTransformers (e.g. BGE-base-en-v1.5) |
| **LLM** | FastAPI, OpenRouter (Mistral, GPT, LLaMA, etc.) |
| **Vector DB** | ChromaDB (persistent, HTTP or in-process) |
| **Deployment** | Docker, Docker Compose (all services containerized) |

---

## Scalability & Growth

- **Horizontal scaling**: Run multiple API Gateway, Embedding, or LLM instances behind a load balancer; ChromaDB can be deployed as a separate cluster.
- **Tenant isolation**: Every retrieval and config path is tenant-scoped—no cross-tenant leakage as you add organizations.
- **Stateless services**: Embedding and LLM services are stateless; scale out by adding replicas.
- **Swap-friendly**: Replace ChromaDB with another vector store, or the LLM service with a different provider, without changing the gateway contract.
- **Observability-ready**: Latency and structured responses (e.g. `latency`, `matched_answers`) support metrics and monitoring as you grow.

---

## Quick Start

### Prerequisites

- Docker & Docker Compose  
- `.env` with at least:
  - `OPENROUTER_API_KEY` (for LLM service)
  - Optional: `USE_CHROMA_HTTP=true` if using ChromaDB as a separate container

### Run with Docker Compose

```bash
docker-compose up --build
```

- **API Gateway**: http://localhost:8080  
- **ChromaDB**: http://localhost:8000 (if using HTTP client)  
- **Embedding service**: http://localhost:9001  
- **LLM service**: http://localhost:9002  

### Example: Ask the chatbot

```bash
curl -X POST http://localhost:8080/user/query \
  -H "Content-Type: application/json" \
  -H "X-Tenant-ID: <tenant_id>" \
  -d '{"question": "What is covered under the ESC plan?"}'
```

(Use your actual tenant resolution header or API key as configured.)

---

## Project Layout (high level)

```
dialogbox-backend/
├── django_backend/           # API Gateway & Admin
│   ├── api_gateway/          # User query pipeline, retrieval, LLM wiring, tenant models
│   ├── admin_panel/          # FAQ upload, tenant/category management
│   ├── embedding_service/   # FastAPI embedding microservice
│   ├── llm_service/         # FastAPI LLM proxy (OpenRouter)
│   └── chroma_store/        # Persistent vector data (if local)
├── frontend-sdk/             # React chat widget / embedding SDK
├── docker-compose.yml        # Full stack: backend, chroma, embedding, llm
└── README.md
```

---

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
MIT © 2025 DialogBox
