# Legacy CLI version.
# Active development continues in Streamlit app (app.py).


from summarizer import summarize_text
from flashcard_generator import generate_flashcards
from quiz_generator import generate_quiz
from history import save_history
from pdf_reader import extract_text_from_pdf


def split_text(text, max_words=300):
    words = text.split()
    return [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)]


def process_pdf(file_path):

    text = extract_text_from_pdf(file_path)

    if text.startswith("Error"):
        return text, None, None

    chunks = split_text(text)

    chunk_summaries = []

    for chunk in chunks:
        chunk_summaries.append(summarize_text(chunk))

    final_summary = summarize_text(" ".join(chunk_summaries))

    flashcards = generate_flashcards(final_summary)
    quiz = generate_quiz(final_summary)

    return final_summary, flashcards, quiz


while True:

    print("\n===== AI STUDY BUDDY =====")
    print("1. Summarize Notes")
    print("2. Generate Flashcards")
    print("3. Generate Quiz")
    print("4. Process PDF (SMART MODE 🚀)")
    print("5. View History")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        text = input("Enter text:\n")

        summary = summarize_text(text)
        save_history("Summary generated")

        print("\n--- SUMMARY ---")
        print(summary)

        with open("summary.txt", "w", encoding="utf-8") as f:
            f.write(summary)


    elif choice == "2":

        topic = input("Enter topic: ")

        flashcards = generate_flashcards(topic)
        save_history("Flashcards generated")

        for i, (q, a) in enumerate(flashcards, 1):
            print(f"\nQ{i}: {q}")
            print(f"A{i}: {a}")


    elif choice == "3":

        topic = input("Enter topic: ")

        quiz = generate_quiz(topic)
        save_history("Quiz generated")

        for i, q in enumerate(quiz, 1):
            print(f"\nQ{i}: {q['question']}")
            for opt in q["options"]:
                print("-", opt)
            print("Answer:", q["answer"])


    elif choice == "4":

        path = input("Enter PDF path: ")

        summary, flashcards, quiz = process_pdf(path)

        if flashcards is None:
            print(summary)
        else:

            print("\n--- SUMMARY ---")
            print(summary)

            print("\n--- FLASHCARDS ---")
            for i, (q, a) in enumerate(flashcards, 1):
                print(f"\nQ{i}: {q}")
                print(f"A{i}: {a}")

            print("\n--- QUIZ ---")
            for i, q in enumerate(quiz, 1):
                print(f"\nQ{i}: {q['question']}")
                for opt in q["options"]:
                    print("-", opt)
                print("Answer:", q["answer"])

            save_history("Full PDF processed")


    elif choice == "5":

        try:
            with open("history.txt", "r", encoding="utf-8") as f:
                print(f.read())
        except:
            print("No history found")


    elif choice == "6":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")