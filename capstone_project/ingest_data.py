"""
LLM Zoomcamp Capstone: Ingest Course FAQ Data
"""
import requests
from elasticsearch import Elasticsearch
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer
import json

print("=== LLM ZOOMCAMP CAPSTONE: DATA INGESTION ===\n")

# Initialize clients
es = Elasticsearch("http://localhost:9200")
qdrant = QdrantClient("http://localhost:6333")
embedder = SentenceTransformer('all-MiniLM-L6-v2')

print("✅ Connected to Elasticsearch")
print("✅ Connected to Qdrant")
print(f"✅ Loaded embedding model")

# Sample FAQ data (simulating course docs)
faq_data = [
    {
        "question": "How do I submit homework?",
        "answer": "Submit homework via the Airtable form linked in the course Slack channel. Include your GitHub repository link.",
        "module": "General"
    },
    {
        "question": "What is the deadline for homework?",
        "answer": "Homework deadlines are specified in the course calendar. Late submissions are accepted but may not be peer-reviewed.",
        "module": "General"
    },
    {
        "question": "How do I install Docker?",
        "answer": "Download Docker Desktop from docker.com. For Linux, follow the official Docker installation guide for your distribution.",
        "module": "Module 1"
    },
    {
        "question": "What is Elasticsearch?",
        "answer": "Elasticsearch is a distributed search and analytics engine based on Lucene. It provides full-text search capabilities.",
        "module": "Module 1"
    },
    {
        "question": "How does vector search work?",
        "answer": "Vector search converts text to embeddings (vectors) and finds similar items by calculating cosine similarity between vectors.",
        "module": "Module 2"
    },
    {
        "question": "What is Qdrant?",
        "answer": "Qdrant is a vector similarity search engine optimized for neural network embeddings. It supports filtering and efficient search.",
        "module": "Module 2"
    },
    {
        "question": "How do I evaluate my RAG system?",
        "answer": "Use metrics like Hit Rate, MRR, and LLM-as-a-Judge. Also collect user feedback for real-world performance.",
        "module": "Module 3"
    },
    {
        "question": "What is monitoring in RAG?",
        "answer": "Monitoring tracks user queries, retrieved documents, generated answers, and user feedback to improve system performance.",
        "module": "Module 4"
    }
]

print(f"\n📄 Processing {len(faq_data)} FAQ documents...")

# Create Elasticsearch index
es.indices.delete(index="course-faq", ignore_unavailable=True)
es.indices.create(index="course-faq")
print("✅ Created Elasticsearch index: course-faq")

# Create Qdrant collection
qdrant.delete_collection("course-faq")
qdrant.create_collection(
    collection_name="course-faq",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)
print("✅ Created Qdrant collection: course-faq")

# Index documents
for i, doc in enumerate(faq_data):
    # Index in Elasticsearch
    es.index(index="course-faq", id=i, document=doc)
    
    # Embed and index in Qdrant
    text = f"{doc['question']} {doc['answer']}"
    embedding = embedder.encode(text).tolist()
    
    qdrant.upsert(
        collection_name="course-faq",
        points=[PointStruct(id=i, vector=embedding, payload=doc)]
    )

print(f"\n✅ Indexed {len(faq_data)} documents")
print("\n=== INGESTION COMPLETE ✅ ===")

# Save metadata
metadata = {
    "elasticsearch_index": "course-faq",
    "qdrant_collection": "course-faq",
    "embedding_model": "all-MiniLM-L6-v2",
    "embedding_size": 384,
    "documents": len(faq_data)
}
with open('ingestion_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)
print("✅ Metadata saved")
