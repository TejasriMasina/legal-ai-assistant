# embedder.py
import os
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load summaries
with open("summaries.json", "r", encoding="utf-8") as f:
    cases = json.load(f)

# Load sentence embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Prepare embeddings
texts = [case["summary"] for case in cases]
embeddings = model.encode(texts, show_progress_bar=True)

# Build FAISS index
dimension = embeddings[0].shape[0]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

os.makedirs("faiss_index", exist_ok=True)

# Save index and cases mapping
faiss.write_index(index, "faiss_index/legal_cases.index")

with open("faiss_index/cases.json", "w", encoding="utf-8") as f:
    json.dump(cases, f, indent=2)



print("Embeddings saved and FAISS index created.")
