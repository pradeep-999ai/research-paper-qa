# Research Paper Q&A (RAG)

A Retrieval-Augmented Generation app that answers questions about an uploaded
research paper, grounded in the paper's actual text with page citations.

Repo: https://github.com/pradeep-999ai/research-paper-qa

## Setup

```bash
git clone https://github.com/pradeep-999ai/research-paper-qa.git
cd research-paper-qa
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Set your Google Gemini API key (free, no billing required — get one at
[aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)):

```bash
export GOOGLE_API_KEY="AI..."      # Windows: $env:GOOGLE_API_KEY="AI..."
```

## Run

```bash
streamlit run app.py
```

Open the URL Streamlit prints (usually `http://localhost:8501`), upload a PDF,
and ask questions.

## Notes

- Google's Gemini model names change fairly often. If you hit a "model not
  found" error, the error message itself names the current replacement —
  update the `model=` value in `qa_chain.py` / `index_store.py` accordingly.
- The free tier is rate-limited (~100 embedding requests/minute). Larger
  papers may need a short wait/retry if you hit that limit.

## Project structure

```
research-paper-qa/
├── app.py            # Streamlit UI
├── ingest.py         # PDF loading + chunking
├── index_store.py    # embeddings + FAISS index (Gemini)
├── qa_chain.py        # retrieval + grounded generation (Gemini)
├── requirements.txt
└── sample_papers/    # sample PDFs for demo
```
