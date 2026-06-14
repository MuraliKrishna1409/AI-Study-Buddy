def summarize_text(text):

    sentences = text.split(".")

    summary = ".".join(sentences[:2])

    return summary