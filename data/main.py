import json
import os

def load_questions():
    file_path = os.path.join("data", "questions.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def run_quiz():
    questions = load_questions()
    score = 0
    
    print("Welcome to the Vocabulary Quiz!")
    print("-------------------------------\n")

    for q in questions:
        print(f"Q{q['id']}: {q['question']}")
        for key, value in q['options'].items():
            print(f"  ({key}) {value}")
        
        user_answer = input("\nYour answer (A/B/C/D): ").upper().strip()
        
        if user_answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer was ({q['answer']})\n")

    print(f"Quiz Finished! You scored {score}/{len(questions)}.")

if __name__ == "__main__":
    run_quiz()
