from gemini_helper import ask_gemini


def generate_quiz(text):

    prompt = f"""
You are an expert examiner.

Generate exactly 5 multiple-choice questions based on the study material.

Rules:
- Questions should test understanding.
- Avoid trivial facts.
- Each question must have exactly 4 options.
- Only one option should be correct.
- Mark the correct answer.
- Follow the format exactly.

Format:

Q: Question text

A) Option 1
B) Option 2
C) Option 3
D) Option 4

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

        except Exception:
            continue

    return questions