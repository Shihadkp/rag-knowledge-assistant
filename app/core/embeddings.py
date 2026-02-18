import ollama

def embed_texts(texts: list[str]) -> list[list[float]]:
    embeddings = []

    for text in texts:
        response = ollama.embeddings(
            model="nomic-embed-text",
            prompt=text
        )
        embeddings.append(response["embedding"])

    return embeddings
