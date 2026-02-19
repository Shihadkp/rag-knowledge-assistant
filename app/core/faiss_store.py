import faiss
import numpy as np
from pathlib import Path

INDEX_PATH = Path("data/index/faiss.index")

index = None


def build_index(embeddings):
    global index

    if not embeddings:
        return None

    dim = len(embeddings[0])

    index = faiss.IndexFlatL2(dim)

    vectors = np.array(embeddings, dtype="float32")

    index.add(vectors)

    faiss.write_index(index, str(INDEX_PATH))

    return index


def load_index(embeddings=None):
    global index

    # If FAISS file exists, load it
    if INDEX_PATH.exists():
        index = faiss.read_index(str(INDEX_PATH))
        return index

    # Otherwise build from embeddings if available
    if embeddings:
        return build_index(embeddings)

    return None


def search(query_vector, top_k=3):
    global index

    if index is None:
        return []

    query = np.array([query_vector], dtype="float32")

    distances, indices = index.search(query, top_k)

    return indices[0]
