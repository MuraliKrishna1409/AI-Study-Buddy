import streamlit as st

from quiz_generator import generate_quiz
from history import save_history

st.title("❓ Quiz")

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
    "Generate Quiz"
):

    quiz = generate_quiz(
        summary
    )

    st.session_state.quiz = quiz

    save_history(
        "Quiz generated"
    )

quiz = st.session_state.get(
    "quiz",
    []
)

if quiz:

    output = ""

    for i, q in enumerate(
        quiz,
        start=1
    ):

        st.markdown(
            f"### Q{i}. {q['question']}"
        )

        st.radio(
            "Choose",
            q["options"],
            key=f"quiz_{i}"
        )

        st.success(
            f"Answer: {q['answer']}"
        )

        output += (
            f"{q['question']}\n"
        )

        for option in q["options"]:
            output += (
                option + "\n"
            )

        output += (
            f"Answer: {q['answer']}\n\n"
        )

    st.download_button(
        "⬇ Download Quiz",
        output,
        file_name="quiz.txt"
    )