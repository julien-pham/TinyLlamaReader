import os
import pickle
import numpy as np
from typing import List, Tuple
from sentence_transformers import SentenceTransformer

def vectorize_chunks(chunks: List[str]) -> Tuple[np.ndarray, SentenceTransformer]:
    """
    Generates sentence embeddings from the text chunks using Sentence-BERT.

    Args:
        chunks (List[str]): The text chunks.

    Returns:
        Tuple[np.ndarray, SentenceTransformer]: The embeddings and the model.
    """

    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)
    return embeddings, model

def load_text_chunks(txt_folder: str, chunk_size: int = 1000) -> List[str]:
    """
    Loads all .txt files from a folder and splits them into fixed-size chunks.

    Args:
        txt_folder (str): Directory containing .txt files.
        chunk_size (int): Size of each chunk.

    Returns:
        List[str]: List of text chunks.
    """

    chunks = []
    for file in os.listdir(txt_folder):
        if file.endswith(".txt"):
            path = os.path.join(txt_folder, file)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
                chunks.extend(text[i:i + chunk_size] for i in range(0, len(text), chunk_size))
    return chunks

def save_vectors(chunks: List[str], embeddings: np.ndarray, folder: str) -> None:
    """
    Saves the text chunks and their embeddings to a folder.
    
    Args:
        chunks (List[str]): List of text chunks.
        embeddings (np.ndarray): Corresponding embeddings.
        folder (str): Directory to save the files.
    """

    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "chunks.pkl"), "wb") as f:
        pickle.dump(chunks, f)
    np.save(os.path.join(folder, "embeddings.npy"), embeddings)

def load_vectors(folder: str) -> Tuple[List[str], np.ndarray]:
    """
    Loads text chunks and embeddings from saved files.
    
    Args:
        folder (str): Directory where the files are saved.

    Returns:
        Tuple[List[str], np.ndarray]: The loaded chunks and their embeddings.
    """
    
    with open(os.path.join(folder, "chunks.pkl"), "rb") as f:
        chunks = pickle.load(f)
    embeddings = np.load(os.path.join(folder, "embeddings.npy"))
    return chunks, embeddings
