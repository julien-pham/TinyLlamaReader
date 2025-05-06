import numpy as np
from typing import List
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def search_semantic_answer(question: str, chunks: List[str], embeddings: np.ndarray,
                           model: SentenceTransformer, top_k: int = 1) -> List[str]:
    """
    Performs semantic search to find the most relevant text chunks for a question.

    Args:
        question (str): The user's question.
        chunks (List[str]): List of text chunks.
        embeddings (np.ndarray): Embeddings of the chunks.
        model (SentenceTransformer): Sentence-BERT model.
        top_k (int): Number of most similar chunks to return.

    Returns:
        List[str]: Top matching chunks.
    """
    question_embedding = model.encode([question])
    similarities = cosine_similarity(question_embedding, embeddings)
    top_indices = np.argsort(similarities[0])[::-1][:top_k]
    return [chunks[i] for i in top_indices]
