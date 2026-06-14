from summarizer import summarize_text
from flashcard_generator import generate_flashcards
from quiz_generator import generate_quiz
from history import save_history

while True:

    print("\n===== AI STUDY BUDDY =====")
    print("1. Summarize Notes")
    print("2. Generate Flashcards")
    print("3. Generate Quiz")
    print("4. View History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        text = input("\nEnter a paragraph:\n")

        summary = summarize_text(text)
        save_history("Generated Summary")

        print("\n===== SUMMARY =====")
        print(summary)

        with open("summary.txt", "w", encoding="utf-8") as file:
            file.write(summary)

        print("\nSummary saved to summary.txt")

    elif choice == "2":

        topic = input("\nEnter a topic: ")

        flashcards = generate_flashcards(topic)
        save_history("Generated Flashcards")

        print("\n===== FLASHCARDS =====")

        with open("flashcards.txt", "w", encoding="utf-8") as file:

            for i, (question, answer) in enumerate(flashcards, start=1):

                print(f"\nQ{i}: {question}")
                print(f"A{i}: {answer}")

                file.write(f"Q{i}: {question}\n")
                file.write(f"A{i}: {answer}\n\n")

        print("\nFlashcards saved to flashcards.txt")

    elif choice == "3":

        topic = input("\nEnter a topic: ")

        quiz = generate_quiz(topic)
        save_history("Generated Quiz")

        print("\n===== QUIZ =====")

        for i, q in enumerate(quiz, start=1):

            print(f"\nQ{i}: {q['question']}")

            for option in q["options"]:
                print(f"- {option}")

            print(f"Answer: {q['answer']}")

    elif choice == "4":

        try:
            with open("history.txt", "r", encoding="utf-8") as file:
                print("\n===== HISTORY =====")
                history = file.read()

                if history.strip():
                    print(history)
                else:
                    print("No history available.")

        except FileNotFoundError:
            print("No history found.")

    elif choice == "5":

        print("\nThank you for using AI Study Buddy!")
        break

    else:

        print("\nInvalid choice. Try again.")