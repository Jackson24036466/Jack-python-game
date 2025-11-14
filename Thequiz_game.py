#the quiz assignemt
# at the end a calculator will score your quiz and display the percentage score

from tkinter import*

questions = ("Which animal is a fish?: ",
            "which country is in africa?: ",
            "which animal has two legs? ",)

options = (("A. Whale", "B. Crocodile", "C. Lion", "D. Dog"),
            ("A. German", "B. UK", "C. Malawi", "D. France"),
            ("A. Dog", "B. Chicken","C. Lizard", "D, Donkey"),)

answers = ("A", "C", "B",)
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("whaalaaa you are right!")
    else:
        print("Wrong....!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

#Score Calculator at the end of the quiz

score = int(score / len(questions) * 100)

print(f"Your score is: {score}%")

