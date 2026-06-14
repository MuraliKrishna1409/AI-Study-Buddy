def generate_quiz(topic):

    quiz = [
        {
            "question": f"What does {topic} stand for?",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "answer": "Option A"
        },
        {
            "question": f"Why is {topic} important?",
            "options": [
                "Entertainment",
                "Problem Solving",
                "Decoration",
                "Gaming"
            ],
            "answer": "Problem Solving"
        }
    ]

    return quiz