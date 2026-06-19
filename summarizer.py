from gemini_helper import ask_gemini


def summarize_text(text):

    prompt = f"""
You are an expert study assistant.

Summarize the following study material.

Requirements:
- Maximum 300 words.
- Use clear bullet points.
- Focus only on important concepts.
- Remove repetitive information.
- Highlight key definitions.
- Highlight important terms, services, formulas, or concepts.
- Make it useful for exam revision.
- Use simple student-friendly language.

Study Material:

{text}
"""

    return ask_gemini(prompt)