from app.core.loader import load_pdf_text
from app.core.chunker import chunk_text
from app.core.embeddings import embed_texts
from app.core.index_store import append

def index_pdf(pdf_path: str, chunk_size: int = 500, overlap: int = 100):
    text = load_pdf_text(pdf_path)
    new_chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)
    new_embeddings = embed_texts(new_chunks)
    append(new_chunks, new_embeddings)
