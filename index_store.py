"""
index_store.py
Embeds chunks and stores them in a FAISS vector index for
semantic similarity search. Uses Google Gemini's free embedding API.
"""

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings


def build_index(chunks, embedding_model="models/gemini-embedding-001"):
    """
    chunks: list of {'text': ..., 'page': ...} from ingest.load_pdf_chunks
    Returns a FAISS index that supports similarity_search().
    """
    embeddings = GoogleGenerativeAIEmbeddings(model=embedding_model)

    texts = [c["text"] for c in chunks]
    metadatas = [{"page": c["page"]} for c in chunks]

    return FAISS.from_texts(texts, embeddings, metadatas=metadatas)


def save_index(index, path="faiss_index"):
    index.save_local(path)


def load_index(path="faiss_index", embedding_model="models/gemini-embedding-001"):
    embeddings = GoogleGenerativeAIEmbeddings(model=embedding_model)
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)
