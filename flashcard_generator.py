def generate_flashcards(text):
    """
    Generates conceptual flashcards from summary text.
    """

    sentences = text.split(".")
    flashcards = []

    for s in sentences:
        s = s.strip()

        if len(s) > 40:
            question = "What is the concept of: " + s[:40] + "?"
            answer = s
            flashcards.append((question, answer))

    if not flashcards:
        flashcards.append(("No flashcards generated", "Try better input text"))

    return flashcards