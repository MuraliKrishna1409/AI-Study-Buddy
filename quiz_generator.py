import random

def generate_quiz(text):
    """
    Generates simple MCQ-style quiz from summary text.
    """

    sentences = [s.strip() for s in text.split(".") if len(s.strip()) > 40]
    quiz = []

    for s in sentences[:5]:

        correct = s

        # fake options (simple distractors)
        options = [
            correct,
            "Not related concept",
            "Opposite idea",
            "Unrelated statement"
        ]

        random.shuffle(options)

        quiz.append({
            "question": "What does the following describe?",
            "options": options,
            "answer": correct
        })

    if not quiz:
        quiz.append({
            "question": "No quiz generated",
            "options": ["N/A"],
            "answer": "N/A"
        })

    return quiz