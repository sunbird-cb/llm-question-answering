import faiss
import numpy as np
from DocEnricher import preprocess_text, get_embeddings

def ingest_data_to_faiss(data):
    index = faiss.IndexFlatL2(300)
    embeddings = []

    for text in data:
        preprocessed_tokens = preprocess_text(text)
        embeddings.extend(get_embeddings(preprocessed_tokens))

    embeddings = np.array(embeddings)
    index.add(embeddings)

    return index

if __name__ == "__main__":
    # Test data
    data = [
        "The quick brown fox jumps over the lazy dog.",
        "Hello, how are you doing?",
        "I love natural language processing!",
    ]

    faiss_index = ingest_data_to_faiss(data)

    # You can now perform similarity searches with the index
    query_vector = get_embeddings(preprocess_text("How to process natural language?"))
    D, I = faiss_index.search(query_vector, k=2)  # Retrieve the 2 most similar vectors
    print("Similarity search results:")
    for distance, index in zip(D[0], I[0]):
        print(f"Distance: {distance}, Index: {index}")
