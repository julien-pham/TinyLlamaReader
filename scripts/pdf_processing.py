import os
import fitz

def check_new_pdfs(pdf_folder: str, cache_file: str) -> bool:
    """
    Checks if there are new or updated PDF files since the last scan.
    
    Args:
        pdf_folder (str): Directory containing PDFs.
        cache_file (str): Path to the cache file with previous state.

    Returns:
        bool: True if there are new or updated files, else False.
    """

    current_state = [
        f"{f}|{os.path.getmtime(os.path.join(pdf_folder, f))}"
        for f in sorted(os.listdir(pdf_folder)) if f.endswith(".pdf")
    ]
    current_str = "\n".join(current_state)

    if not os.path.exists(cache_file):
        with open(cache_file, "w") as f:
            f.write(current_str)
        return True

    with open(cache_file, "r") as f:
        previous_state = f.read()

    if previous_state != current_str:
        with open(cache_file, "w") as f:
            f.write(current_str)
        return True

    return False

def extract_pdf_text(pdf_path: str) -> str:
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF.

    Returns:
        str: The extracted text.
    """

    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def convert_pdfs_to_txt(pdf_folder: str, txt_folder: str) -> None:
    """
    Converts all PDFs in a folder to .txt files.
    
    Args:
        pdf_folder (str): Directory with PDF files.
        txt_folder (str): Directory where TXT files will be saved.
    """

    os.makedirs(txt_folder, exist_ok=True)

    for f in os.listdir(txt_folder):
        if f.endswith(".txt"):
            os.remove(os.path.join(txt_folder, f))
    print("📄 Old .txt files removed.")

    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            text = extract_pdf_text(pdf_path)
            txt_name = os.path.splitext(pdf_file)[0] + ".txt"
            txt_path = os.path.join(txt_folder, txt_name)
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"✅ {pdf_file} processed and saved to {txt_path}.")