# 📚 AI Study Buddy v1.0

AI Study Buddy is a Generative AI-powered learning assistant that helps students convert study materials into concise summaries, revision flashcards, and interactive quizzes.

Built using Python, Streamlit, and Google's Gemini API, the application simplifies studying by automatically extracting information from PDF documents and generating personalized learning resources.

---

## 🚀 Features

### 📄 PDF Upload & Text Extraction

* Upload study materials in PDF format.
* Automatically extract and process text content.
* Supports document-based learning workflows.

### 📝 AI-Powered Summarization

* Generate concise summaries from lengthy study materials.
* Focus on key concepts and important information.
* Improve revision efficiency.

### 🎴 Flashcard Generation

* Automatically create question-answer flashcards.
* Designed for active recall and spaced repetition.
* Useful for quick revision sessions.

### ❓ Quiz Generation

* Generate multiple-choice questions from study content.
* Interactive quiz interface using Streamlit.
* Hidden answer reveal option for self-assessment.

### 🕒 History Tracking

* Records user activities with timestamps.
* Tracks generated summaries, flashcards, and quizzes.
* Provides a history page for reviewing past actions.

### 💾 Download Support

* Download generated summaries.
* Download flashcards for offline study.
* Download quizzes and answer keys.

---

## 🏗️ Project Architecture

```text
AI-Study-Buddy/
│
├── app.py
├── gemini_helper.py
├── pdf_reader.py
├── summarizer.py
├── flashcard_generator.py
├── quiz_generator.py
├── history.py
├── requirements.txt
│
├── pages/
│   ├── Summary.py
│   ├── Flashcards.py
│   ├── Quiz.py
│   └── History.py
│
└── README.md
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & NLP

* Google Gemini API

### Libraries

* PyPDF2
* python-dotenv

### Version Control

* Git
* GitHub

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone <repository-url>
cd AI-Study-Buddy
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📖 How to Use

1. Launch the Streamlit application.
2. Upload a PDF document.
3. Generate a summary of the content.
4. Create flashcards for revision.
5. Generate quiz questions for self-assessment.
6. Download generated study materials.
7. Review activity history from the History page.

---

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Python Application Development
* Generative AI Integration
* Prompt Engineering
* Streamlit Web Applications
* PDF Processing
* Session State Management
* Modular Software Design
* Git & GitHub Workflow
* API Integration
* Educational Technology Development

---

## 🔮 Future Improvements

* Multi-language support
* Advanced quiz scoring system
* User authentication
* Cloud database integration
* OCR support for scanned PDFs
* Personalized learning analytics
* Difficulty-based quiz generation

---

## 👨‍💻 Author

**S. Murali Krishna**

Computer Science Engineering Student

### Project

AI Study Buddy v1.0

### Academic Year

2025–2026

---

## 📄 License

This project is intended for educational and learning purposes.
