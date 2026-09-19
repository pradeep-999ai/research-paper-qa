# Research Paper Q&A (RAG)

A Retrieval-Augmented Generation app that answers questions about an uploaded
research paper, grounded in the paper's actual text with page citations.

## Setup

```bash
git clone https://github.com/<your-username>/research-paper-qa.git
cd research-paper-qa
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Set your OpenAI API key:

```bash
export OPENAI_API_KEY="sk-..."      # Windows: set OPENAI_API_KEY=sk-...
```

## Run

```bash
streamlit run app.py
```

Open the URL Streamlit prints (usually `http://localhost:8501`), upload a PDF,
and ask questions.

## Project structure

```
research-paper-qa/
├── app.py            # Streamlit UI
├── ingest.py         # PDF loading + chunking
├── index_store.py    # embeddings + FAISS index
├── qa_chain.py        # retrieval + grounded generation
├── requirements.txt
└── sample_papers/    # sample PDFs for demo
```
