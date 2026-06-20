import streamlit as st

from flashcard_generator import generate_flashcards
from history import save_history

st.title("🃏 Flashcards")

summary = st.session_state.get(
    "summary",
    ""
)

if not summary:
    st.warning(
        "Generate a summary first."
    )
    st.stop()

if st.button(
    "Generate Flashcards"
):

    flashcards = generate_flashcards(
        summary
    )

    st.session_state.flashcards = flashcards

    save_history(
        "Flashcards generated"
    )

flashcards = st.session_state.get(
    "flashcards",
    []
)

if flashcards:

    text_output = ""

    for i, (q, a) in enumerate(
        flashcards,
        start=1
    ):

        with st.expander(
            f"Flashcard {i}"
        ):

            st.write(
                f"Q: {q}"
            )

            st.write(
                f"A: {a}"
            )

        text_output += (
            f"Q: {q}\nA: {a}\n\n"
        )

    st.download_button(
        "⬇ Download Flashcards",
        text_output,
        file_name="flashcards.txt"
    )