"""
qa_chain.py
Retrieves relevant chunks for a question and generates a
context-grounded answer using Google Gemini's free API.
"""

import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))


def build_prompt(question, docs):
    context = "\n\n".join(
        f"[Page {d.metadata['page']}] {d.page_content}" for d in docs
    )
    return f"""Answer ONLY using the context below.
If the answer is not in the context, say "This is not covered in the paper."

Context:
{context}

Question: {question}
Answer:"""


def answer_question(index, question, k=4, model="gemini-3.6-flash"):
    """
    Returns (answer_text, set_of_source_pages)
    """
    docs = index.similarity_search(question, k=k)
    if not docs:
        return "This is not covered in the paper.", set()

    prompt = build_prompt(question, docs)

    gemini_model = genai.GenerativeModel(model)
    response = gemini_model.generate_content(prompt)

    answer = response.text
    pages = {d.metadata["page"] for d in docs}
    return answer, pages
