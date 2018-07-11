# vertli 2018
from question_bank import QuestionBank
import random

q = QuestionBank()
q.file_open("test1.txt")  # 4 questions
q.file_open("test2.txt")  # 1 question
q.file_open("test3.txt")  # this will give you an error message!
total = len(q)
valid_ans = ["A", "B", "C", "D", "E"]

while total > 0:

    index = random.randrange(0, total)

    print("Question: ", q.get_question(index))
    print(q.get_choice_a(index))
    print(q.get_choice_b(index))
    print(q.get_choice_c(index))
    print(q.get_choice_d(index))
    print(q.get_choice_e(index))
    guess = input("Please enter your answer: ").upper()
    answer = q.get_answer(index)

    while guess not in valid_ans:
        print("Invalid input! Please enter again: ")
        guess = input("Please enter your answer: ").upper()
    if guess == answer:
        print("Correct")
    else:
        print("Wrong!!!! The answer is", answer)
    print()
