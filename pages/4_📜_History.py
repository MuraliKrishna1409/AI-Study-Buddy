import streamlit as st

from history import (
    read_history,
    clear_history
)

st.title("📜 History")

history = read_history()

if history:

    for item in reversed(history):

        st.write(
            item.strip()
        )

else:
    st.info(
        "No history found."
    )

if st.button(
    "🗑 Clear History"
):

    clear_history()

    st.rerun()