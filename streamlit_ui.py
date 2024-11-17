import streamlit as st
from pdf_processor import process_pdf

def upload_pdfs():
    uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)
    if uploaded_files:
        pdf_contents = [process_pdf(file) for file in uploaded_files]
        st.session_state['knowledge_base'] = pdf_contents
        st.success("PDFs uploaded successfully!")
