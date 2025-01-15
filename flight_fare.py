def k(fare,people):
    split=fare/people
    return split
def main():
    fare=int(input("enter total fare"))
    people=int(input("enter how many people splits the bill"))
    bill=k(fare,people)
    print(bill)
main()