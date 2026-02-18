from app.core.persistence import save_index, load_index

chunks, embeddings = load_index()

def is_initialized() -> bool:
    return len(chunks) > 0 and len(embeddings) > 0

def append(new_chunks, new_embeddings):
    chunks.extend(new_chunks)
    embeddings.extend(new_embeddings)
    save_index(chunks, embeddings)
