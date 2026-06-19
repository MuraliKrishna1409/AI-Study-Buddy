from gemini_helper import ask_gemini


def generate_flashcards(text):

    prompt = f"""
You are an expert educator.

Generate exactly 10 high-quality flashcards from the study material.

Rules:
- Focus on concepts, not memorization.
- Questions should help students revise for exams.
- Answers should be short and precise.
- Format strictly:

Q: Question
A: Answer

Study Material:

{text}
"""

    response = ask_gemini(prompt)

    flashcards = []

    lines = response.split("\n")

    question = None

    for line in lines:

        if line.startswith("Q:"):
            question = line.replace("Q:", "").strip()

        elif line.startswith("A:") and question:
            answer = line.replace("A:", "").strip()
            flashcards.append((question, answer))
            question = None

    return flashcards