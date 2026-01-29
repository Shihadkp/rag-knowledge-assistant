#!/bin/bash

echo "🚀 Bootstrapping RAG project structure..."

# Create directories
mkdir -p experiments
mkdir -p app/api app/core app/models
mkdir -p data/uploaded_docs

# Create __init__.py files
touch app/api/__init__.py
touch app/core/__init__.py
touch app/models/__init__.py

# Create experiment notebooks
touch experiments/01_pdf_loader.ipynb
touch experiments/02_chunking.ipynb
touch experiments/03_embeddings.ipynb
touch experiments/04_similarity_search.ipynb
touch experiments/05_rag_pipeline.ipynb

# Create application files
touch app/main.py
touch app/api/upload.py
touch app/api/chat.py

touch app/core/loader.py
touch app/core/chunker.py
touch app/core/embeddings.py
touch app/core/vector_store.py
touch app/core/rag.py

touch app/models/schemas.py
touch app/config.py
touch app/utils.py

echo "✅ Project structure created successfully!"
