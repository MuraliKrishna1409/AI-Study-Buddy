from gemini_helper import ask_gemini
import re


def generate_flashcards(text):

    prompt = f"""
    Generate 10 flashcards.

    Format EXACTLY like:

    Q: question
    A: answer

    Q: question
    A: answer

    Text:
    {text[:10000]}
    """

    result = ask_gemini(prompt)

    flashcards = []

    pattern = r"Q:\s*(.*?)\nA:\s*(.*?)(?=\nQ:|\Z)"

    matches = re.findall(pattern, result, re.DOTALL)

    for q, a in matches:
        flashcards.append(
            (q.strip(), a.strip())
        )

    return flashcards