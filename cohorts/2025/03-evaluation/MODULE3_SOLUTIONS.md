# Module 3: Evaluation - Homework Solutions

## LLM Zoomcamp 2025 - Module 3: Search Evaluation

**Status**: ⏳ In Progress  
**Packed**: Pending

---

## Homework Overview

In this homework, we evaluate vector search results using:
- **minsearch** for text and vector search
- **TF-IDF + SVD** for embeddings
- **Hit Rate** and **MRR** (Mean Reciprocal Rank) for metrics

---

## Q1: Minsearch Text Search

**Task**: Evaluate minsearch with:
- Text fields: `["question", "section", "text"]`
- Keyword fields: `["course", "id"]`
- Boost: `{'question': 1.5, 'section': 0.1}`

**Question**: What's the hit rate?

**Options**:
- 0.64
- 0.74
- 0.84
- 0.94

**Answer**: ⏳ [To be verified with correct minsearch version]

---

## Q2: Vector Search with TF-IDF + SVD

**Task**: Evaluate vector search using:
- TF-IDF with min_df=3
- TruncatedSVD with n_components=128
- minsearch VectorSearch

**Question**: What's the MRR?

**Answer**: ⏳ [To be verified]

---

## Setup

```bash
pip install minsearch scikit-learn qdrant_client
```

---

## Evaluation Metrics

### Hit Rate
```python
def hit_rate(relevance_total):
    cnt = 0
    for line in relevance_total:
        if True in line:
            cnt = cnt + 1
    return cnt / len(relevance_total)
```

### MRR (Mean Reciprocal Rank)
```python
def mrr(relevance_total):
    total_score = 0.0
    for line in relevance_total:
        for rank in range(len(line)):
            if line[rank] == True:
                total_score = total_score + 1 / (rank + 1)
    return total_score / len(relevance_total)
```

---

## Data

- **Documents**: 948 FAQ documents with IDs
- **Ground Truth**: 4627 question-answer pairs
- **Source**: [llm-zoomcamp/03-evaluation](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/03-evaluation)

---

## Notes

- minsearch API changed in recent versions
- Need to use correct version (>=0.0.4) for vector search
- Boost parameter syntax may vary by version

---

**Next Steps**:
1. Install correct minsearch version
2. Run evaluation with proper API
3. Extract Q1 and Q2 answers
4. Commit and push
