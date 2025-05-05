
# 🧠 LLM Assistant for PDF Analysis (SAS Visual Analytics)

This project allows you to ask questions about a collection of SAS Visual Analytics PDF documents using a local language model (TinyLlama) combined with semantic search.

---

## 🚀 Features

- 🔍 Extracts text from PDF documents
- 🧱 Splits text into chunks and generates embeddings
- 🔎 Uses `sentence-transformers` for semantic search
- 🤖 Generates final answers using a local TinyLlama model
- 💾 Automatically caches data to avoid redundant processing

---

## 📁 Project Structure

    .
    ├── data/                                 # Contains the input PDFs, text files, embeddings, and models
    │   ├── doc_pdf/                          # Input PDFs
    │   ├── doc_txt/                          # Extracted text files
    │   ├── models/                           # TinyLlama GGUF model
    │   ├── vectors/                          # Saved embeddings
    │   └── pdf_state.txt                     # Tracks processed PDFs
    │
    ├── scripts/                              # Contains Python scripts for processing
    │   ├── pdf_processing.py                 # Handles PDF extraction and text processing
    │   ├── vectors_chunks_processing.py      # Processes chunks and embeddings
    │   ├── llm_interaction.py                # Interfaces with TinyLlama for answering questions
    │   └── semantic_search.py                # Performs semantic search on text
    │
    ├── main.py                               # Main entrypoint for running the assistant
    ├── requirements.txt                      # Lists required Python libraries
    ├── LICENSE                               # Project license file
    └── README.md                             # Project documentation

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/projet_llm.git
cd projet_llm
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the TinyLlama model
- Go to the [TinyLlama model page](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- Download the `.gguf` file (e.g., `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf`)
- Place it in `data/models/`

---

## 🛠️ Usage

1. Place your SAS Visual Analytics PDF files in the `data/doc_pdf/` folder.

2. Run the assistant:
```bash
python main.py
```

3. Ask questions about the content. Type `exit` to quit the assistant.

Example:
```text
blablabla
```

---

## 🧠 How It Works

1. **Text Extraction**: Converts each PDF to text using `PyMuPDF`.
2. **Chunking**: Splits the text into manageable parts.
3. **Vectorization**: Embeds chunks with `sentence-transformers`.
4. **Semantic Search**: Finds the most relevant chunk(s) for a question.
5. **LLM Interaction**: Uses TinyLlama to generate and refine the final answer.

---

## 📝 License

This project is licensed under the **Apache 2.0 License**.  
It uses the [TinyLlama model](https://huggingface.co/cmp-nct/TinyLlama-1.1B-Chat-v1.0) which is also under the Apache 2.0 License.

---

## 🙌 Acknowledgments
- [SAS Visual Analytics](https://go.documentation.sas.com/doc/en/vacdc/7.5/homeapp/titlepage.htm) for the official documentation PDFs.
- [TinyLlama](https://github.com/jzhang38/TinyLlama) for the pre-trained language model.
- [Sentence Transformers](https://www.sbert.net/) for providing the embedding model used for semantic search.
