from random import randint

Easy_Level_attempts=10
Hard_Level_attempts=5
def number(user_guess,answer,turns):
    if user_guess>answer:
        print("too high")
        return turns-1
    elif user_guess<answer:
        print("too low")
        return turns-1
    else:
        print("you got it right")
def difficulty():
    choice=input("Enter your choice type 'easy' for Easy level 'hard' for diffucult level")
    if choice=='easy':
        return Easy_Level_attempts
    else:
        return Hard_Level_attempts


def game():
    print("welcome to guess game")
    print("i am thinking of a number between 1-100")
    answer=randint(1,100)
    print(f"pssst correct answer is {answer} ")
    turns=difficulty()
    guess=0
    while guess!=answer:
        print(f"you have {turns} left")
        guess=int(input("guess a number"))
        turns=number(guess,answer,turns)
        if turns==0:
            print("you've run out of guess,you lose.")
        elif guess != answer:
            print("Guess again.")
game()



