from app.core.index_store import chunks, embeddings
from app.core.embeddings import embed_texts
from app.core.similarity import cosine_similarity

def retrieve(query: str, top_k: int = 3):
    if not chunks or not embeddings:
        return []

    query_embedding = embed_texts([query])[0]

    scores = []
    for i, emb in enumerate(embeddings):
        score = cosine_similarity(query_embedding, emb)
        scores.append((score, i))

    scores.sort(reverse=True)

    results = []
    for score, idx in scores[:top_k]:
        results.append({
            "chunk_id": idx,
            "score": score,
            "text": chunks[idx]
        })

    return results



""""
from app.core.loader import load_pdf_text
from app.core.chunker import chunk_text
from app.core.embeddings import embed_texts
from app.core.similarity import cosine_similarity

def build_rag_index(pdf_path: str):
    text = load_pdf_text(pdf_path)
    chunks = chunk_text(text)
    embeddings = embed_texts(chunks)
    return chunks, embeddings

def retrieve(query: str, chunks, embeddings, top_k: int = 3):
    query_embedding = embed_texts([query])[0]

    scores = []
    for i, emb in enumerate(embeddings):
        score = cosine_similarity(query_embedding, emb)
        scores.append((score, i))

    scores.sort(reverse=True)

    results = []
    for score, idx in scores[:top_k]:
        results.append({
            "chunk_id": idx,
            "score": score,
            "text": chunks[idx]
        })

    return results
"""