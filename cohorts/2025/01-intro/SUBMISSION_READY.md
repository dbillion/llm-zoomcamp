# ✅ Module 1 Homework - Submission Ready

## LLM Zoomcamp 2025 - Module 1: Introduction to LLMs and RAG

**Student**: [Your Name]  
**GitHub**: [Your GitHub Username]  
**Date**: 2026-03-16  
**Submission Status**: Ready for Submission

---

## 📋 Homework Answers

### Q1: Running Elastic ✅
**Question**: What's the `version.build_hash` value?

**Answer**: `dbcbbbd0bc4924cfeb28929dc05d82d662c527b7`

From Elasticsearch 8.17.6:
```json
{
  "version": {
    "number": "8.17.6",
    "build_hash": "dbcbbbd0bc4924cfeb28929dc05d82d662c527b7",
    "build_date": "2025-04-30T14:07:12.231372970Z"
  }
}
```

---

### Q2: Indexing the Data ✅
**Question**: Which function do you use for adding your data to elastic?

**Answer**: `index`

```python
es_client.index(index=index_name, document=doc)
```

Options were: insert, **index**, put, add

---

### Q3: Searching ✅
**Question**: Search for "How do execute a command on a Kubernetes pod?" with question boost of 4. What's the score for the top ranking result?

**Answer**: **44.50** (44.50556)

Query used:
```python
query = {
    "query": {
        "multi_match": {
            "query": "How do execute a command on a Kubernetes pod?",
            "fields": ["question^4", "text"],
            "type": "best_fields"
        }
    }
}
```

---

### Q4: Filtering ✅
**Question**: Search for "How do copy a file to a Docker container?" filtered by `machine-learning-zoomcamp`. What's the 3rd question returned?

**Answer**: **"How do I debug a docker container?"**

Top 3 results:
1. How do I copy files from a different folder into docker container's working directory?
2. [2nd result]
3. **How do I debug a docker container?** ← 3rd result

---

### Q5: Building a Prompt ✅
**Question**: What's the length of the resulting prompt?

**Answer**: **1446** characters

Prompt template used:
```python
prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT:
{context}
""".strip()
```

---

### Q6: Tokens ✅
**Question**: How many tokens does our prompt have (using gpt-4o encoding)?

**Answer**: **320** tokens

```python
encoding = tiktoken.encoding_for_model("gpt-4o")
tokens = encoding.encode(prompt)
len(tokens)  # 320
```

---

## 📊 Summary of Answers

| Question | Answer | Points |
|----------|--------|--------|
| Q1 | `dbcbbbd0bc4924cfeb28929dc05d82d662c527b7` | ✅ |
| Q2 | `index` | ✅ |
| Q3 | `44.50` | ✅ |
| Q4 | "How do I debug a docker container?" | ✅ |
| Q5 | `1446` | ✅ |
| Q6 | `320` | ✅ |

---

## 🚀 How to Reproduce

### 1. Setup Environment
```bash
cd /home/deeone/projects/zoomcamp
source .venv/bin/activate
```

### 2. Start Elasticsearch
```bash
docker run -d --name elasticsearch \
  -p 9200:9200 -p 9300:9300 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  -e "ES_JAVA_OPTS=-Xms2g -Xmx2g" \
  docker.elastic.co/elasticsearch/elasticsearch:8.17.6
```

### 3. Run Solution Notebook
```bash
jupyter notebook llm-zoomcamp/cohorts/2025/01-intro/homework_solution.ipynb
```

### 4. Execute All Cells
- Run all cells in order
- Verify outputs match answers above

---

## 📦 Files for Submission

1. **Homework Solution**: `llm-zoomcamp/cohorts/2025/01-intro/homework_solution.ipynb`
2. **Packed Context**: `llm-zoomcamp/cohorts/2025/01-intro/homework-packed.xml` (5,498 tokens)
3. **This Summary**: `assignment_tracker.md`

---

## ✅ Submission Checklist

- [x] Homework completed
- [x] All 6 questions answered
- [x] Solution notebook executed
- [x] Answers verified against solution
- [ ] Push to GitHub
- [ ] Submit via Airtable form
- [ ] Complete 3 peer reviews

---

## 🔗 Submission Links

- **Airtable Submission Form**: [Link in course repo](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/cohorts/2025/01-intro/homework.md)
- **GitHub Repository**: `https://github.com/DataTalksClub/llm-zoomcamp`
- **Slack Channel**: `#course-llm-zoomcamp`

---

## 📝 Notes for Peer Review

When reviewing peer submissions, check:
1. Elasticsearch version matches (8.17.6)
2. Index mapping has `course` as `keyword` type
3. Search queries use correct field boosting
4. Prompt template matches course specification
5. Token count uses gpt-4o encoding

---

**Ready for submission! 🎉**

Next steps:
1. Push this folder to your GitHub
2. Submit the form with your answers
3. Review 3 classmates' submissions for 9 extra points
