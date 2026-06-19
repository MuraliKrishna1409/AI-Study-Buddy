import streamlit as st
import re

from pdf_reader import extract_text_from_pdf
from summarizer import summarize_text
from flashcard_generator import generate_flashcards
from quiz_generator import generate_quiz

from history import (
    save_history,
    read_history,
    clear_history
)


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


# ---------------- SESSION STATE ----------------

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "flashcards" not in st.session_state:
    st.session_state.flashcards = []

if "quiz" not in st.session_state:
    st.session_state.quiz = []


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

    st.markdown("---")

    st.subheader("Recent History")

    history = read_history()

    if history:

        for item in reversed(history[-10:]):
            st.text(item.strip())

    else:
        st.write("No history available.")

    st.markdown("---")

    if st.button("🗑 Clear History"):
        clear_history()
        st.rerun()


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


# ---------------- GENERATE BUTTON ----------------

if pdf_file is not None:

    if st.button("🚀 Generate"):

        if not (
            summary_selected
            or flashcards_selected
            or quiz_selected
        ):
            st.warning(
                "Please select at least one feature."
            )
            st.stop()

        with st.spinner("Processing PDF..."):

            with open("temp.pdf", "wb") as f:
                f.write(pdf_file.read())

            text = extract_text_from_pdf(
                "temp.pdf"
            )

            if text.startswith("Error"):
                st.error(text)
                st.stop()

            text = clean_text(text)

            summary = summarize_text(
                text[:10000]
            )

            if summary.startswith("ERROR:"):
                st.error(summary)
                st.stop()

            st.session_state.summary = summary

            if summary_selected:
                save_history(
                    "Summary generated"
                )

            if flashcards_selected:

                flashcards = generate_flashcards(
                    summary
                )

                st.session_state.flashcards = (
                    flashcards
                )

                save_history(
                    "Flashcards generated"
                )

            if quiz_selected:

                quiz = generate_quiz(
                    summary
                )

                st.session_state.quiz = quiz

                save_history(
                    "Quiz generated"
                )


# ---------------- SUMMARY ----------------

if (
    summary_selected
    and st.session_state.summary
):

    st.subheader("📄 Summary")

    st.write(
        st.session_state.summary
    )

    st.download_button(
        label="⬇ Download Summary",
        data=st.session_state.summary,
        file_name="summary.txt",
        mime="text/plain"
    )


# ---------------- FLASHCARDS ----------------

if (
    flashcards_selected
    and st.session_state.flashcards
):

    st.subheader("🧾 Flashcards")

    for i, (q, a) in enumerate(
        st.session_state.flashcards,
        start=1
    ):

        with st.expander(
            f"Flashcard {i}"
        ):

            st.markdown(
                f"**Question:** {q}"
            )

            st.markdown(
                f"**Answer:** {a}"
            )


# ---------------- QUIZ ----------------

if (
    quiz_selected
    and st.session_state.quiz
):

    st.subheader("❓ Quiz")

    for i, q in enumerate(
        st.session_state.quiz,
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


# ---------------- EMPTY STATE ----------------

if pdf_file is None:

    st.info(
        "Please upload a PDF to begin."
    )


# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "Built by Murali Krishna using Streamlit and Gemini AI"
)