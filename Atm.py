balance=1000
def with_draw():
    global balance
    amount=int(input("enter your amount you want to put"))
    balance-=amount
    print(f"your account is debited by {amount} your balance is {balance} ")
def deposit():
    global balance
    amount=int(input("enter your amount you want to deposit"))
    balance+=amount
    print(f"your account is credited by {amount} your balance is {balance}")
def main():
    choice=(input("enter your choice"))
    if choice=='1':
        deposit()
    elif choice=='2':
        with_draw()
    elif choice=='3':
        quit
    else:
        print("you have entered an invalid amount")
main()



