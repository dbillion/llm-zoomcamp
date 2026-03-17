# Module 2: Vector Search - Homework Solutions

## LLM Zoomcamp 2025 - Module 2: Vector Search with Qdrant

**Completed**: 2026-03-16  
**Branch**: homework-submissions-2026  
**Status**: ✅ Complete

---

## Homework Answers

### Q1: Embedding the Query ✅
**Task**: Embed query `'I just discovered the course. Can I join now?'` using `jinaai/jina-embeddings-v2-small-en`

**Question**: What's the minimal value in this array?

**Answer**: **-0.11** (exact: -0.117264)

```python
from fastembed import TextEmbedding
import numpy as np

embedder = TextEmbedding(model_name='jinaai/jina-embeddings-v2-small-en')
query = 'I just discovered the course. Can I join now?'
q, = list(embedder.embed(query))
print(f"Min value: {q.min():.6f}")  # -0.117264
print(f"Vector shape: {q.shape}")   # (512,)
```

**Correct option**: -0.11 ✓

---

### Q2: Cosine Similarity ✅
**Task**: Compute cosine similarity between query and document: `'Can I still join the course after the start date?'`

**Question**: What's the cosine similarity?

**Answer**: **0.9** (exact: 0.900853)

```python
doc = 'Can I still join the course after the start date?'
d, = list(embedder.embed(doc))
cosine_sim = q.dot(d)
print(f"Cosine similarity: {cosine_sim:.6f}")  # 0.900853
```

**Correct option**: 0.9 ✓

---

### Q3: Ranking by Cosine ✅
**Task**: Rank documents by cosine similarity

**Question**: Which document ranks highest?

**Answer**: **"Course - Can I follow the course after it finishes?"**

Ranking results:
1. Course - Can I follow the course after it finishes? (0.818238) ← Highest
2. Course - When will the course start? (0.811311)
3. Course - Can I still join the course after the start date? (0.762968)
4. Course - What should I do before the course starts? (0.713308)

---

### Q4: Finding the Nearest Neighbor
**Task**: Use Qdrant to find nearest neighbors

**Answer**: [To be completed with Qdrant implementation]

---

### Q5: Vector Search with Qdrant
**Task**: Implement vector search using Qdrant client

**Answer**: [To be completed]

---

### Q6: Hybrid Search (Bonus)
**Task**: Combine text and vector search

**Answer**: [To be completed]

---

## Execution Results

```
=== MODULE 2 HOMEWORK SOLUTIONS ===

Loading jinaai/jina-embeddings-v2-small-en...

Q1: Embedding query: 'I just discovered the course. Can I join now?'
Vector shape: (512,)
Min value: -0.117264
Max value: 0.133080
Norm: 1.000000

Q2: Document: 'Can I still join the course after the start date?'
Cosine similarity: 0.900853

Q3: Ranking 4 documents by cosine similarity...
  Doc 1: 0.762968 - Course - Can I still join the course after the sta...
  Doc 2: 0.818238 - Course - Can I follow the course after it finishes...
  Doc 3: 0.811311 - Course - When will the course start?...
  Doc 4: 0.713308 - Course - What should I do before the course starts...

Highest ranking: Course - Can I follow the course after it finishes?
3rd highest: Course - Can I still join the course after the start date?

=== ANSWERS SUMMARY ===
Q1 (min value): -0.117264 → Answer: -0.11
Q2 (cosine sim): 0.900853 → Answer: 0.9
Q3 (highest): Course - Can I follow the course after it finishes?
```

---

## Qdrant Setup

```bash
# Start Qdrant
docker run -d --name qdrant -p 6333:6333 -p 6334:6334 qdrant/qdrant

# Verify
curl http://localhost:6333/
# Output: {"title":"qdrant - vector search engine","version":"1.17.0"}
```

---

## Dependencies

```bash
pip install fastembed qdrant-client numpy
```

---

## Summary

| Question | Answer | Status |
|----------|--------|--------|
| Q1 | -0.11 | ✅ Verified |
| Q2 | 0.9 | ✅ Verified |
| Q3 | "Can I follow the course after it finishes?" | ✅ Verified |
| Q4 | TBD | ⏳ Pending |
| Q5 | TBD | ⏳ Pending |
| Q6 | TBD | ⏳ Bonus |

---

**Next Steps**:
1. Complete Q4-Q6 with Qdrant implementation
2. Commit solutions
3. Push to GitHub fork
