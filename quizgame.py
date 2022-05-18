class Quiz:
    def __init__(self, qlist):
        self.question_Number = 0
        self.question_list = qlist
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_Number]
        self.question_Number += 1
        user_answer = input(f"Q:{self.question_Number} {current_question.text}? (True/False) ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("YAY! you got it right")
            self.score += 1
        else:
            print("That's a wrong answer")
        print(f"Correct Answer is {correct_answer}")
        print(f"Your Score is {self.score} / {self.question_Number}")
        print("")
