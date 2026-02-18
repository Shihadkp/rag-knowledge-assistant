from fastapi import APIRouter, UploadFile, File
from pathlib import Path

from app.core.indexer import index_pdf
from app.core.index_store import chunks
from app.models.schemas import UploadResponse

router = APIRouter()

UPLOAD_DIR = Path("data/uploaded_docs")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as f:
        f.write(await file.read())

    index_pdf(str(file_path))

    return UploadResponse(
        message=f"{file.filename} indexed successfully",
        total_chunks=len(chunks)
    )
