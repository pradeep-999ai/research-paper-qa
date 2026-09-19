"""
app.py
Streamlit interface for the Research Paper QA system.
Run with: streamlit run app.py
"""

import os
import tempfile
import streamlit as st

from ingest import load_pdf_chunks
from index_store import build_index
from qa_chain import answer_question

st.set_page_config(page_title="Research Paper Q&A", page_icon="📄")
st.title("📄 Research Paper Q&A")
st.caption("Upload a research paper and ask questions grounded in its actual text.")

if "index" not in st.session_state:
    st.session_state.index = None
if "indexed_filename" not in st.session_state:
    st.session_state.indexed_filename = None

uploaded = st.file_uploader("Upload a paper (PDF)", type=["pdf"])

# Re-index whenever a NEW file is uploaded (not just the first time)
if uploaded and uploaded.name != st.session_state.indexed_filename:
    with st.spinner("Reading and indexing the paper..."):
        tmp_path = None
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded.read())
                tmp_path = tmp.name

            chunks = load_pdf_chunks(tmp_path)

            if not chunks:
                st.error(
                    "No text could be extracted from this PDF. "
                    "It may be a scanned/image-only document — try a different file."
                )
                st.session_state.index = None
                st.session_state.indexed_filename = None
            else:
                st.session_state.index = build_index(chunks)
                st.session_state.indexed_filename = uploaded.name
                st.success(f"Indexed {len(chunks)} chunks. Ask away!")
        finally:
            if tmp_path and os.path.exists(tmp_path):
                os.remove(tmp_path)

if st.session_state.index:
    question = st.text_input("Ask a question about the paper")
    if question:
        with st.spinner("Thinking..."):
            answer, pages = answer_question(st.session_state.index, question)
        st.write(answer)
        if pages:
            st.caption(f"Source page(s): {sorted(pages)}")

if st.button("Reset"):
    st.session_state.index = None
    st.session_state.indexed_filename = None
    st.rerun()
