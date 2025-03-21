import random
python_questions = {
    "What is Python?": "programming Language",
    "How do you print in Python?": "print()",
    "How do you take user input?": "input()",
    "Which keyword defines a function?": "def",
    "What is a mutable sequence?": "list",
    "Which loop runs indefinitely?": "while",
    "How do you handle exceptions?": "try",
    "Which data type is immutable?": "tuple",
    "What stores key-value pairs?": "dict",
    "What keyword creates a class?": "class"
}
def python_trivia_game():
    print("WelCome to TRIVIA_GAME.\nYou have to Answer 5 questions. ")
    question_list=list(python_questions.keys())
    total_questions=5
    score=0
    selected_questions= random.sample(question_list,total_questions)
    try:    
        for idx, question in enumerate(selected_questions):
            print(f"{idx+1}. {question}")
            user_answer=input("Your answer: ").lower().strip()
            correct_answer =python_questions[question]
            if user_answer == correct_answer.lower():
                print("Correct!\n")
                score+=1
            else:
                print(f"Wrong. The correct answer is {correct_answer}.\n")
        print(f"Game over! Your final score is {score}/{total_questions}")
    except Exception as a:
        print("Invalid Input!, Please try again.")
if __name__=="__main__":
    python_trivia_game()    