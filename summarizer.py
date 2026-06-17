from gemini_helper import ask_gemini


def summarize_text(text):

    prompt = f"""
    Summarize the following study material.

    Include:

    1. Short Summary
    2. Key Points
    3. Important Exam Notes

    Text:
    {text[:10000]}
    """

    return ask_gemini(prompt)