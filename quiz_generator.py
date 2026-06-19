from gemini_helper import ask_gemini
import re


def generate_quiz(text):

    prompt = f"""
You are an expert examiner.

Generate exactly 5 multiple-choice questions.

Rules:
- Questions should test understanding.
- Avoid trivial facts.
- Provide 4 options.
- Mark the correct answer.

Format exactly:

Q: Question

A) Option
B) Option
C) Option
D) Option

Answer: A

Study Material:

{text}
"""

    response = ask_gemini(prompt)

    questions = []

    blocks = response.split("Q:")

    for block in blocks[1:]:

        lines = [
            line.strip()
            for line in block.strip().split("\n")
            if line.strip()
        ]

        try:

            question = lines[0]

            options = [
                lines[1],
                lines[2],
                lines[3],
                lines[4]
            ]

            answer = lines[5].replace(
                "Answer:",
                ""
            ).strip()

            questions.append(
                {
                    "question": question,
                    "options": options,
                    "answer": answer
                }
            )

        except:
            continue

    return questions