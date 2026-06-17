from gemini_helper import ask_gemini
import re


def generate_quiz(text):

    prompt = f"""
    Generate 5 MCQs.

    Format EXACTLY:

    Question: ...

    A) ...
    B) ...
    C) ...
    D) ...

    Answer: A

    Text:
    {text[:10000]}
    """

    result = ask_gemini(prompt)

    quiz = []

    blocks = result.split("Question:")

    for block in blocks[1:]:

        lines = [line.strip() for line in block.splitlines() if line.strip()]

        if len(lines) < 6:
            continue

        question = lines[0]

        options = []

        answer = ""

        for line in lines[1:]:

            if line.startswith(("A)", "B)", "C)", "D)")):
                options.append(line)

            elif line.startswith("Answer:"):
                answer = line.replace("Answer:", "").strip()

        quiz.append({
            "question": question,
            "options": options,
            "answer": answer
        })

    return quiz