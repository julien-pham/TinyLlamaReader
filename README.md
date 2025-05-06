
# 🧠 LLM Assistant for PDF Analysis

This project lets you interact with the content of your own PDF files by asking questions. It uses a local language model (TinyLlama) combined with semantic search based on sentence embeddings to retrieve relevant context and generate accurate, context-aware answers. All without relying on external APIs or internet access.


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
git clone ...
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the TinyLlama model
- Go to the [TinyLlama model page](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- Download the `.gguf` file (e.g., `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf`)
- Place it in `data/models/`

### 4. Add your PDFs
- Place your PDFs in `data/doc_pdf`

### 5. Run the main.py script

---

## 🛠️ Usage

```
📁 Checking PDF state...
✅ PDFs are up to date. Loading existing vectors...
📂 Loading vectors from C:\Users\...
🔄 Loading SentenceTransformer model...
🤖 Assistant is ready to answer your questions based on the PDFs you provided !
❓ Ask your question (or type 'exit' to quit): what options are available for histograms on sas?

🧠 Answer:
In addition to the general options, there are three options specific to histograms on SAS: direction, transparency, and bin range.

Direction:
Direction specifies whether the bars are vertical or horizontal.

Transparency:
Transparency specifies the amount of transparency for the bars.

Bi-range:
Bi-range specifies how the boundaries of the bin ranges are determined.

For example, when setting direction, the user can choose between "vertical" or "horizontal". With vertical, the bars are vertical, extending from the minimum value to the maximum value. With horizontal, the bars are horizontal, extending from the minimum value to the maximum value, but with some extra space in between the ranges.

For transparency, the user can choose between "system-determined values" or "rounding of boundaries". "System-determined values" might place the boundaries at rounded values, while "rounding of boundaries" might extend the boundaries a bit more.

Bin range:
Bin range specifies how the boundaries of the bin ranges are determined. The user can choose between "system-determined values" or "rounding of boundaries". "System-determined values" might place the boundaries at rounded values, while "rounding of boundaries" might extend the boundaries a bit more.

Specifying options in the Options panes of the SAS can customize the histogram to match the specific data values and requirements.
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
- [TinyLlama](https://github.com/jzhang38/TinyLlama) for the pre-trained language model.
- [Sentence Transformers](https://www.sbert.net/) for providing the embedding model used for semantic search.
- Developed by Julien PHAM, as part of a personal project using local LLMs and semantic search for document understanding.
