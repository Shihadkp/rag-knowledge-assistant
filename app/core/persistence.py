import json
import numpy as np
from pathlib import Path

INDEX_DIR = Path("data/index")
INDEX_DIR.mkdir(parents=True, exist_ok=True)

CHUNKS_FILE = INDEX_DIR / "chunks.json"
EMBEDDINGS_FILE = INDEX_DIR / "embeddings.npy"

def save_index(chunks, embeddings):
    with open(CHUNKS_FILE, "w", encoding="utf-8") as f:
        json.dump(chunks, f)

    np.save(EMBEDDINGS_FILE, np.array(embeddings, dtype=np.float32))

def load_index():
    if not CHUNKS_FILE.exists() or not EMBEDDINGS_FILE.exists():
        return [], []

    with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    embeddings = np.load(EMBEDDINGS_FILE).tolist()
    return chunks, embeddings
