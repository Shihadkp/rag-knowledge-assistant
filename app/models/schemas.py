from pydantic import BaseModel
from typing import List

class Source(BaseModel):
    chunk_id: int
    preview: str

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    sources: List[Source]

class UploadResponse(BaseModel):
    message: str
    total_chunks: int
