import streamlit as st
import re

from pdf_reader import extract_text_from_pdf
from summarizer import summarize_text
from history import save_history


def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()


st.title("📝 Summary Generator")

pdf_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if pdf_file:

    with open("temp.pdf", "wb") as f:
        f.write(pdf_file.read())

    text = extract_text_from_pdf("temp.pdf")

    if st.button("Generate Summary"):

        with st.spinner("Generating Summary..."):

            summary = summarize_text(
                clean_text(text[:10000])
            )

            st.session_state.summary = summary

            save_history(
                "Summary generated"
            )

if "summary" in st.session_state:

    st.subheader("Summary")

    st.write(
        st.session_state.summary
    )

    st.download_button(
        "⬇ Download Summary",
        st.session_state.summary,
        file_name="summary.txt"
    )