# LLM Zoomcamp Capstone: Course FAQ RAG Chatbot

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│  Course     │────▶│  Elasticsearch│────▶│  Qdrant     │────▶│  FastAPI    │
│  FAQ Docs   │     │  (Text)      │     │  (Vectors)  │     │  RAG API    │
└─────────────┘     └──────────────┘     └─────────────┘     └──────────────┘
                                                                   │
                                                                   ▼
                                                            ┌──────────────┐
                                                            │  Streamlit   │
                                                            │  Frontend    │
                                                            └──────────────┘
```

## Project Components

### 1. Data Ingestion
- Downloads course FAQ documents
- Indexes in Elasticsearch (text search)
- Embeds and stores in Qdrant (vector search)

### 2. Hybrid Search
- BM25 text search (Elasticsearch)
- Semantic search (Qdrant)
- Reciprocal Rank Fusion for combining

### 3. RAG Pipeline
- Retrieves relevant context
- Builds prompt with context
- Calls LLM for answer generation

### 4. Frontend
- Streamlit chat interface
- Shows sources/retrieved documents
- User feedback collection

## Execution

```bash
# 1. Create venv
uv venv --python 3.11
source .venv/bin/activate

# 2. Install dependencies
uv pip install elasticsearch qdrant-client fastapi uvicorn streamlit openai sentence-transformers

# 3. Start services
docker run -d --name elasticsearch -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch:8.4.3
docker run -d --name qdrant -p 6333:6333 qdrant/qdrant

# 4. Ingest data
python3 ingest_data.py

# 5. Start API
uvicorn app:app --host 0.0.0.0 --port 8000

# 6. Start frontend
streamlit run frontend.py
```

## Status: ✅ BUILT & EXECUTED
