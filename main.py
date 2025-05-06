import os
from sentence_transformers import SentenceTransformer
from scripts.pdf_processing import check_new_pdfs, convert_pdfs_to_txt
from scripts.vectors_chunks_processing import vectorize_chunks, load_text_chunks, save_vectors, load_vectors
from scripts.llm_interaction import combine_llm_and_semantic_response

def main():
    """
    Main execution pipeline:
    - Check for new or modified PDFs
    - Convert them to text if needed
    - Chunk and vectorize the content
    - Continuously answer user questions using LLM and semantic search until 'exit' is typed
    """

    base_dir = os.path.join(os.getcwd(), "data")
    pdf_dir = os.path.join(base_dir, "doc_pdf")
    txt_dir = os.path.join(base_dir, "doc_txt")
    vector_dir = os.path.join(base_dir, "vectors")
    cache_file = os.path.join(base_dir, "pdf_state.txt")
    model_path = os.path.join(base_dir, "models", "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf")

    print("📁 Checking PDF state...")
    new_pdfs = check_new_pdfs(pdf_dir, cache_file)

    if new_pdfs:
        print("📄 New or modified PDFs detected.")
        
        print(f"🔄 Converting PDFs in {pdf_dir} to text files in {txt_dir}...")
        convert_pdfs_to_txt(pdf_dir, txt_dir)
        
        print(f"📂 Loading text chunks from {txt_dir}...")
        chunks = load_text_chunks(txt_dir)
        
        print(f"⚙️ Generating embeddings for the loaded text chunks...")
        embeddings, model = vectorize_chunks(chunks)

        print(f"💾 Saving vector data to {vector_dir}...")
        save_vectors(chunks, embeddings, vector_dir)
        
    else:
        print("✅ PDFs are up to date. Loading existing vectors...")

        print(f"📂 Loading vectors from {vector_dir}...")
        chunks, embeddings = load_vectors(vector_dir)

        print("🔄 Loading SentenceTransformer model...")
        model = SentenceTransformer('all-MiniLM-L6-v2')

    print("🤖 Assistant is ready to answer your questions on SAS Visual Analytics!")

    # ⏱️ Initialize chat history
    chat_history = []

    while True:
        question = input("❓ Ask your question (or type 'exit' to quit): ").strip()
        if question.lower() in ("exit", "quit"):
            print("👋 Thank you ! See you soon !")
            break

        response = combine_llm_and_semantic_response(
            question=question,
            chunks=chunks,
            embeddings=embeddings,
            model=model,
            model_path=model_path,
            chat_history=chat_history  # 🔁 Pass history
        )

        # 📝 Store interaction
        chat_history.append((question, response))

        print(f"\n🧠 Answer:\n{response}\n")

if __name__ == "__main__":
    main()
