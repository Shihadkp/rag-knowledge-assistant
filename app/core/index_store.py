from app.core.persistence import save_index, load_index
from app.core.faiss_store import load_index as load_faiss, build_index

chunks, embeddings = load_index()

# Load or build FAISS automatically
faiss_index = load_faiss(embeddings)


def is_initialized():
    return len(chunks) > 0


def append(new_chunks, new_embeddings):
    chunks.extend(new_chunks)
    embeddings.extend(new_embeddings)

    save_index(chunks, embeddings)

    # rebuild FAISS index
    build_index(embeddings)
