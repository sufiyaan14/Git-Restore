def quiz_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
            "answer": "B"
        },
        {
            "question": "Which language is used for web apps?",
            "options": ["A) Python", "B) Java", "C) JavaScript", "D) All of the above"],
            "answer": "D"
        },
        {
            "question": "What is 5 + 3 * 2?",
            "options": ["A) 16", "B) 13", "C) 11", "D) 10"],
            "answer": "C"
        }
    ]

    score = 0

    print("\n===== Welcome to the Quiz Game! =====")
    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}: {q['question']}")
        for opt in q["options"]:
            print(opt)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}")

    print("\n===== Quiz Over! =====")
    print(f"Your score: {score}/{len(questions)}")
    if score == len(questions):
        print("🏆 Excellent! You got all correct!")
    elif score > len(questions) // 2:
        print("Good job!")
    else:
        print("Keep practicing!")

if __name__ == "__main__":
    quiz_game()
