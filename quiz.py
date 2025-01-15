class Quiz:
    def __init__(self,question_list):
        self.question_no=0
        self.list=question_list
        self.score=0
    def is_still_question(self):
        return self.question_no < len(self.list)
    def next_question(self):
        current_question=self.list[self.question_no]
        self.question_no +=1
        user_answer=input(f"Q.{self.question_no} {current_question.text} (true/false)")
        self.check_answer(user_answer,current_question.answer)
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("you got it right")
        else:
            print("That's wrong")
        print(f"The correct answer is {correct_answer}")
        print(f'your current score is {self.score}/{self.question_no}')
        print('\n')