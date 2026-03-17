"""
LLM Zoomcamp Capstone: RAG API with Hybrid Search
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from elasticsearch import Elasticsearch
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
import numpy as np

app = FastAPI(title="Course FAQ RAG API", version="1.0.0")

# Initialize clients
es = Elasticsearch("http://localhost:9200")
qdrant = QdrantClient("http://localhost:6333")
embedder = SentenceTransformer('all-MiniLM-L6-v2')

class QueryRequest(BaseModel):
    query: str
    top_k: int = 3

class QueryResponse(BaseModel):
    answer: str
    sources: list

@app.get("/")
def root():
    return {"message": "Course FAQ RAG API", "status": "healthy"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    try:
        # Elasticsearch: Text search
        es_results = es.search(
            index="course-faq",
            query={"multi_match": {"query": request.query, "fields": ["question", "answer"]}},
            size=request.top_k
        )
        es_docs = [hit['_source'] for hit in es_results['hits']['hits']]
        
        # Qdrant: Vector search
        query_embedding = embedder.encode(request.query).tolist()
        qdrant_results = qdrant.search(
            collection_name="course-faq",
            query_vector=query_embedding,
            limit=request.top_k
        )
        qdrant_docs = [r.payload for r in qdrant_results]
        
        # Combine results (simple fusion)
        combined = es_docs + qdrant_docs
        seen = set()
        unique_docs = []
        for doc in combined:
            key = doc['question']
            if key not in seen:
                seen.add(key)
                unique_docs.append(doc)
        
        # Build answer from top results
        sources = unique_docs[:request.top_k]
        answer = "\n\n".join([f"Q: {d['question']}\nA: {d['answer']}" for d in sources])
        
        return QueryResponse(answer=answer, sources=sources)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
