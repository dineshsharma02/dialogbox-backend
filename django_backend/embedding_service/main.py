from fastapi import FastAPI, Request
import numpy as np
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import os

MODEL_NAME = "BAAI/bge-base-en-v1.5"

app = FastAPI()

model = SentenceTransformer(MODEL_NAME)

class TextRequest(BaseModel):
    texts: list[str]
    is_query:bool = False


@app.post("/embed")
async def embed_text(req: TextRequest):
    prefix = "query: " if req.is_query else "passage: "
    prepped = [prefix + text.strip() for text in req.texts]
    embeddings = model.encode(prepped,normalize_embeddings=True)
    return {"embeddings": np.array(embeddings).tolist()}
