import streamlit as st
from pdf_processor import extract_text_from_pdf
from knowledge_base import build_knowledge_base
from ai_chat import ask_question

st.title("AI Chat with Multiple PDFs")
uploaded_files = st.file_uploader("Upload PDFs", accept_multiple_files=True, type=["pdf"])

if uploaded_files:
    texts = [extract_text_from_pdf(file) for file in uploaded_files]
    knowledge_base = build_knowledge_base(texts)
    st.write("Knowledge base created!")

    question = st.text_input("Ask a question about the PDFs:")
    if question:
        response = ask_question(knowledge_base, question)
        st.write("AI Response:", response)
