from typing import List, Tuple
from llama_cpp import Llama
import numpy as np
from sentence_transformers import SentenceTransformer
from .semantic_search import search_semantic_answer

def combine_llm_and_semantic_response(
    question: str,
    chunks: List[str],
    embeddings: np.ndarray,
    model: SentenceTransformer,
    model_path: str,
    chat_history: List[Tuple[str, str]] = None  # optional list of (user, assistant) pairs
) -> str:
    """
    Combines a direct LLM answer with a semantic search result to provide a better response.
    Includes conversational history to maintain context.

    Args:
        question (str): The user question.
        chunks (List[str]): The list of text chunks from the documents.
        embeddings (np.ndarray): Embeddings of the chunks.
        model (SentenceTransformer): Sentence-BERT model used for encoding.
        model_path (str): Path to the TinyLlama model.
        chat_history (List[Tuple[str, str]], optional): Conversation history as (user, assistant) pairs.

    Returns:
        str: A final rewritten and combined answer.
    """
    llm = Llama(model_path=model_path, n_ctx=2048, n_threads=4, n_gpu_layers=0, verbose=False)

    # Format the conversation history (if any)
    history_prompt = ""
    if chat_history:
        for user_msg, assistant_msg in chat_history:
            history_prompt += f"<|user|>\n{user_msg}\n</s>\n<|assistant|>\n{assistant_msg}\n</s>\n"

    # Step 1: Direct LLM response
    prompt_llm_direct = (
        "<|system|>\nYou are a SAS Visual Analytics assistant.\n</s>\n" +
        history_prompt +
        f"<|user|>\n{question}\n</s>\n<|assistant|>\n"
    )
    direct_response = llm(prompt=prompt_llm_direct, max_tokens=512, stop=["</s>"])["choices"][0]["text"].strip()

    # Step 2: Semantic search
    semantic_responses = search_semantic_answer(question, chunks, embeddings, model, top_k=1)
    semantic_context = semantic_responses[0]

    # Step 3: Combine everything
    prompt_combined = (
        "<|system|>\nYou are a helpful assistant for SAS Visual Analytics.\n</s>\n" +
        history_prompt +
        f"<|user|>\nHere is a question: {question}\n\n"
        f"Draft answer:\n\"\"\"\n{direct_response}\n\"\"\"\n\n"
        f"Context:\n\"\"\"\n{semantic_context}\n\"\"\"\n\n"
        "Please combine both in a clear, concise response.\n</s>\n<|assistant|>\n"
    )
    final_response = llm(prompt=prompt_combined, max_tokens=512, stop=["</s>"])
    return final_response["choices"][0]["text"].strip()
