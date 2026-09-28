import streamlit as st
import requests
from utils.formatter import format_docx, format_pdf
from utils.sanitizer import sanitize_text

BACKEND_URL = "http://127.0.0.1:8000/generate"

st.title("LegalEase - AI Legal Document Generator")

doc_type = st.text_input("Document Type")
parties = st.text_area("Parties Involved")
terms = st.text_area("Terms (separate with ;) ")
date = st.text_input("Effective Date")

if st.button("Generate Document"):
    payload = {
        "document_type": doc_type,
        "parties": parties,
        "terms": terms,
        "date": date
    }

    response = requests.post(BACKEND_URL, json=payload)

    if response.status_code == 200:
        doc_text = sanitize_text(response.json()["document"])
        edited_text = st.text_area("Edit Document", doc_text, height=300)

        st.download_button("Download TXT", edited_text, file_name="document.txt")

        if st.button("Download DOCX"):
            file = format_docx(edited_text)
            with open(file, "rb") as f:
                st.download_button("Download File", f, file_name="document.docx")

        if st.button("Download PDF"):
            file = format_pdf(edited_text)
            with open(file, "rb") as f:
                st.download_button("Download File", f, file_name="document.pdf")
