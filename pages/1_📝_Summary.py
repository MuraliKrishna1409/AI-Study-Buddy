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

text = ""
if pdf_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(pdf_file.read())

    text = extract_text_from_pdf("temp.pdf")

if st.button("Generate Summary"):
    with st.spinner("Generating Summary..."):
        try:
            if not text:
                st.error("Please upload a PDF file first.")
            else:
                st.write("✅ PDF extracted")

                cleaned_text = clean_text(text[:10000])

                st.write(f"✅ Text Length: {len(cleaned_text)}")

                summary = summarize_text(cleaned_text)

                st.write("✅ Gemini returned response")

                st.session_state["summary"] = summary

                save_history("Summary generated")

                st.success("Summary Generated Successfully")
        except Exception as e:
            st.error(f"Error: {e}")

if "summary" in st.session_state:
    st.subheader("Summary")
    st.write(st.session_state["summary"])
    st.download_button(
        label="⬇ Download Summary",
        data=st.session_state["summary"],
        file_name="summary.txt",
        mime="text/plain"
    )
