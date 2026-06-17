import streamlit as st
import re

from pdf_reader import extract_text_from_pdf
from summarizer import summarize_text
from flashcard_generator import generate_flashcards
from quiz_generator import generate_quiz

# ---------------- TEXT CLEANING ----------------

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    return text.strip()

# ---------------- UI SETUP ----------------

st.set_page_config(
    page_title="AI Study Buddy",
    layout="wide"
)

st.title("🧠 AI Study Buddy")
st.write("Upload a PDF and generate Summary, Flashcards, and Quiz")

with st.sidebar:
    st.header("About")
    st.write(
        "Upload study notes and generate AI-powered summaries, flashcards, and quizzes."
    )

# ---------------- FILE UPLOAD ----------------

pdf_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

# ---------------- MAIN LOGIC ----------------

if pdf_file is not None:
    if st.button("🚀 Generate"):
        with st.spinner("Processing PDF..."):
            # Save temporary PDF
            with open("temp.pdf", "wb") as f:
                f.write(pdf_file.read())

            # Extract text
            text = extract_text_from_pdf("temp.pdf")

            if text.startswith("Error"):
                st.error(text)
                st.stop()

            # Clean text
            text = clean_text(text)

            # Generate summary
            final_summary = summarize_text(text[:10000])

            if final_summary.startswith("ERROR:"):
                st.error(final_summary)
                st.stop()

            # Generate flashcards
            flashcards = generate_flashcards(final_summary)

            # Generate quiz
            quiz = generate_quiz(final_summary)

            # ---------------- SUMMARY ----------------
            st.subheader("📄 Summary")
            st.write(final_summary)

            # ---------------- FLASHCARDS ----------------
            st.subheader("🧾 Flashcards")

            if flashcards:
                for i, (q, a) in enumerate(flashcards, 1):
                    with st.expander(f"Q{i}: {q}"):
                        st.write(a)
            else:
                st.warning("No flashcards generated.")

            # ---------------- QUIZ ----------------
            st.subheader("❓ Quiz")

            if quiz:
                for i, q in enumerate(quiz, 1):
                    st.markdown(f"**Q{i}: {q['question']}**")
                    for opt in q["options"]:
                        st.write("-", opt)
                    st.success(f"Answer: {q['answer']}")
            else:
                st.warning("No quiz generated.")
else:
    st.info("Please upload a PDF file to begin.")

st.markdown("---")
st.caption(
    "Built by Murali Krishna using Streamlit and Gemini AI"
)
