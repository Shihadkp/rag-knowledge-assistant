from fastapi import APIRouter
from pathlib import Path
import ollama

from app.models.schemas import QueryRequest, QueryResponse
from app.core.rag import retrieve
from app.core.index_store import is_initialized


router = APIRouter()

BASE_DIR = Path(__file__).resolve().parents[2]
PDF_PATH = BASE_DIR / "data" / "uploaded_docs" / "Medical_book.pdf"

chunks = None
embeddings = None

"""
def get_index():
    global chunks, embeddings
    if chunks is None or embeddings is None:
        print("Building RAG index...")
        chunks, embeddings = build_rag_index(str(PDF_PATH))
        print("Index ready.")
    return chunks, embeddings
"""

@router.post("/ask", response_model=QueryResponse)
def ask_question(request: QueryRequest):
    if not is_initialized():
        return QueryResponse(
            answer="Knowledge base is empty. Please upload documents first.",
            sources=[]
        )

    results = retrieve(
        request.question,
        top_k=3
    )

    context = "\n\n".join(r["text"] for r in results)

    prompt = f"""
You are a knowledge assistant for company documents.
Answer ONLY using the provided context.
If the answer is not present in the context, say "I don't know".

Context:
{context}

Question:
{request.question}

Answer:
"""

    response = ollama.generate(
        model="llama3.2:3b",
        prompt=prompt
    )

    sources = [
        {
            "chunk_id": r["chunk_id"],
            "preview": r["text"][:200]
        }
        for r in results
    ]

    return QueryResponse(
        answer=response["response"],
        sources=sources
    )
