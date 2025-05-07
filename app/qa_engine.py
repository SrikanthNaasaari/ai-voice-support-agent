# Folder: app/qa_engine.py
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

EMBEDDING_PATH = "data/embeddings.pkl"
model = SentenceTransformer("all-MiniLM-L6-v2")

with open(EMBEDDING_PATH, "rb") as f:
    chunks, embeddings = pickle.load(f)


def get_faq_answer(query, threshold=0.65):
    query_vec = model.encode([query])[0]
    sims = np.dot(embeddings, query_vec) / (
        np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_vec)
    )
    top_idx = np.argmax(sims)
    if sims[top_idx] < threshold:
        return "", True
    return chunks[top_idx], False