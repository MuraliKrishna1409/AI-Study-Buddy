def summarize_text(text):
    """
    Simple extractive-style summarizer (safe fallback version).
    Works for both small and chunked inputs.
    """

    sentences = text.split(".")
    sentences = [s.strip() for s in sentences if len(s.strip()) > 30]

    # Take top meaningful sentences (simple heuristic)
    summary = ". ".join(sentences[:5])

    if not summary:
        return "Unable to generate summary."

    return summary