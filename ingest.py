"""
ingest.py
Loads a PDF, extracts text page-by-page, and splits it into
overlapping chunks ready for embedding.
"""

import fitz  # PyMuPDF
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_pdf_chunks(path, chunk_size=1000, chunk_overlap=100):
    """
    Reads a PDF file and returns a list of dicts:
    [{'text': <chunk text>, 'page': <page number>}, ...]
    """
    doc = fitz.open(path)
    pages = [(i + 1, page.get_text()) for i, page in enumerate(doc)]
    doc.close()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    chunks = []
    for page_num, text in pages:
        if not text.strip():
            continue
        for piece in splitter.split_text(text):
            chunks.append({"text": piece, "page": page_num})

    return chunks


if __name__ == "__main__":
    # quick manual test: python ingest.py sample_papers/example.pdf
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "sample_papers/example.pdf"
    result = load_pdf_chunks(path)
    print(f"Extracted {len(result)} chunks from {path}")
    print(result[0] if result else "No text found")
