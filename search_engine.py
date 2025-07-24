# search_engine.py

import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model and index
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("faiss_index/legal_cases.index")

with open("faiss_index/cases.json", "r", encoding="utf-8") as f:
    cases = json.load(f)

def search_similar_cases(query, top_k=5):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), top_k)

    results = []
    for i in I[0]:
        results.append({
            "case_name": cases[i]["case_name"],
            "summary": cases[i]["summary"],
            "court": cases[i].get("court", ""),
            "date_filed": cases[i].get("date_filed", "")
        })
    return results
