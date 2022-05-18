from question import Question
from data import question_d
from quizgame import Quiz

question_bank = []
for i in range(len(question_d)):
    question_bank.append(Question(question_d[i]["question"], question_d[i]["correct_answer"]))

user = Quiz(question_bank)
for _ in range(len(question_bank)):
    user.next_question()
print("You have completed your quiz")
print(f"Your final score is {user.score} / 10")
