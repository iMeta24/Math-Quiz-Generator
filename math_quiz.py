# math_quiz.py

import random

def math_quiz():
    score = 0
    for _ in range(5):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 + num2
        user_answer = int(input(f"What is {num1} + {num2}? "))
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print(f"Your score: {score}/5")

# Run the quiz
math_quiz()
