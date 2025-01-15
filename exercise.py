Exercises={"Running":20,"cycling":30,"swimming":50}
def exercise():
    calories_burn=0
    exercise=input("enter you exercise you want to perform")
    min=int(input("Enter your minutes"))
    if exercise in Exercises:
        calories_burn=Exercises[exercise]*min
        print(f"you burn {calories_burn} in a day")
    else:
        print("you choose a wrong exercise")
exercise()
