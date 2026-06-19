import streamlit as st
import re

from pdf_reader import extract_text_from_pdf
from summarizer import summarize_text
from flashcard_generator import generate_flashcards
from quiz_generator import generate_quiz


# ---------------- TEXT CLEANING ----------------

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\x00-\x7F]+", " ", text)
    return text.strip()


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Study Buddy",
    layout="wide"
)

# ---------------- HEADER ----------------

st.title("🧠 AI Study Buddy")
st.write(
    "Upload your study notes and generate AI-powered summaries, flashcards, and quizzes."
)

# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.header("About")
    st.write(
        "AI Study Buddy helps students quickly understand study materials using Gemini AI."
    )

# ---------------- FILE UPLOAD ----------------

pdf_file = st.file_uploader(
    "📂 Upload PDF",
    type=["pdf"]
)

# ---------------- FEATURE SELECTION ----------------

st.subheader("⚙️ Choose Features")

summary_selected = st.checkbox(
    "📄 Generate Summary",
    value=True
)

flashcards_selected = st.checkbox(
    "🧾 Generate Flashcards",
    value=True
)

quiz_selected = st.checkbox(
    "❓ Generate Quiz",
    value=True
)

# ---------------- PROCESS BUTTON ----------------

if pdf_file is not None:

    if st.button("🚀 Generate"):

        if not (
            summary_selected
            or flashcards_selected
            or quiz_selected
        ):
            st.warning("Please select at least one feature.")
            st.stop()

        with st.spinner("Processing PDF..."):

            # Save uploaded PDF temporarily
            with open("temp.pdf", "wb") as f:
                f.write(pdf_file.read())

            # Extract text
            text = extract_text_from_pdf("temp.pdf")

            if text.startswith("Error"):
                st.error(text)
                st.stop()

            # Clean extracted text
            text = clean_text(text)

            # Generate summary
            summary = summarize_text(text[:10000])

            if summary.startswith("ERROR:"):
                st.error(summary)
                st.stop()

            # ---------------- SUMMARY ----------------

            if summary_selected:
                st.subheader("📄 Summary")
                st.write(summary)

            # ---------------- FLASHCARDS ----------------

            if flashcards_selected:

                flashcards = generate_flashcards(summary)

                st.subheader("🧾 Flashcards")

                if flashcards:
                    for i, (q, a) in enumerate(
                        flashcards,
                        start=1
                    ):
                        with st.expander(f"Flashcard {i}"):
                            st.markdown(
                                f"**Question:** {q}"
                            )
                            st.markdown(
                                f"**Answer:** {a}"
                            )
                else:
                    st.warning(
                        "No flashcards generated."
                    )

            # ---------------- QUIZ ----------------

            if quiz_selected:

                quiz = generate_quiz(summary)

                st.subheader("❓ Quiz")

                if quiz:
                    for i, q in enumerate(
                        quiz,
                        start=1
                    ):
                        st.markdown(
                            f"### Q{i}. {q['question']}"
                        )

                        for option in q["options"]:
                            st.write(option)

                        st.success(
                            f"Answer: {q['answer']}"
                        )

                        st.markdown("---")
                else:
                    st.warning(
                        "No quiz generated."
                    )

else:
    st.info(
        "Please upload a PDF to begin."
    )

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "Built by Murali Krishna using Streamlit and Gemini AI"
)