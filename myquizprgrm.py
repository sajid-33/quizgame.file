def run_quiz(questions):
    score = 0
    for question in questions:
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == question["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer was {question['answer']}.")
    print(f"\n🎉 You got {score} out of {len(questions)} correct.")

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. Guido van Rossum", "C. James Gosling", "D. Linus Torvalds"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Computer Personal Unit", "C. Central Processing Unit", "D. Control Processing Unit"],
        "answer": "C"
    }
]

if __name__ == "__main__":
    run_quiz(questions)
