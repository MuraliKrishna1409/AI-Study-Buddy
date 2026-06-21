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

    answer_key = "\n\n===== ANSWER KEY =====\n\n"

    for i, q in enumerate(
        quiz,
        start=1
    ):

        st.markdown(
            f"### Q{i}. {q['question']}"
        )

        st.radio(
            "Choose your answer:",
            q["options"],
            key=f"quiz_{i}"
        )

        with st.expander(
            "Show Answer"
        ):
            st.write(
                q["answer"]
            )

        output += (
            f"Q{i}. {q['question']}\n"
        )

        for option in q["options"]:
            output += (
                option + "\n"
            )

        output += "\n"

        answer_key += (
            f"Q{i}: {q['answer']}\n"
        )

    output += answer_key

    st.download_button(
        "⬇ Download Quiz",
        output,
        file_name="quiz.txt"
    )