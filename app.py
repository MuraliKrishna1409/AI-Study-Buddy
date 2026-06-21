import streamlit as st

st.write("API Key Exists:", "GEMINI_API_KEY" in st.secrets)

st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Study Buddy")

st.markdown("""
### AI-Powered Learning Assistant

Upload study materials and instantly generate:

✅ Smart Summaries

✅ Interactive Flashcards

✅ Practice Quizzes

✅ Study History

Built using:
- Python
- Streamlit
- Google Gemini AI
- PyPDF2
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Summary", "✓")

with col2:
    st.metric("Flashcards", "✓")

with col3:
    st.metric("Quiz", "✓")

st.success("Use the sidebar to begin.")