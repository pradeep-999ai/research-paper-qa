# Research Paper Q&A (RAG)

A Retrieval-Augmented Generation notebook that answers questions about an
uploaded research paper, grounded in the paper's actual text with page
citations.

Repo: https://github.com/pradeep-999ai/research-paper-qa

## How it works

1. Upload a research paper (PDF)
2. The paper is split into overlapping text chunks and embedded
3. When you ask a question, the most relevant chunks are retrieved
4. An LLM generates an answer using **only** those retrieved chunks — with
   the source page numbers cited, and an explicit "not covered" response if
   the answer isn't in the paper

## Run it (Google Colab)

1. Open **`Research_Paper_QA_Colab.ipynb`** in this repo, then click
   **"Open in Colab"** (or go to
   [colab.research.google.com](https://colab.research.google.com) → File →
   Open notebook → GitHub tab → paste this repo's URL)
2. Run each cell in order (Shift+Enter)
3. When prompted, paste a free Gemini API key — get one at
   [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
   (no credit card required)
4. Upload a research paper PDF when prompted
5. Ask questions in the last cell — re-run it as many times as you like

## Notes

- Google renames/retires Gemini model IDs fairly often. If a cell errors
  with a 404 "model not found", the error message itself names the current
  replacement — update the `model=` value in the relevant cell and re-run.
- The free tier has daily/per-minute rate limits. If you hit a 429 error,
  wait a bit and retry, or switch to a lighter model variant (e.g. a
  "flash-lite" model) if one is available.

## Tech stack

- **PDF text extraction:** PyMuPDF
- **Chunking:** LangChain `RecursiveCharacterTextSplitter`
- **Embeddings:** Google Gemini (`gemini-embedding-001`)
- **Vector store:** FAISS
- **Generation:** Google Gemini API
- **Interface:** Google Colab notebook
