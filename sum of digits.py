def sum_of_digits(n):
    total=0
    while n>0:
        total+=n%10
        n//=10
    return total
def main():
    num=int(input("enter a number"))

    result=sum_of_digits(num)
    print(f"sum of {num} is {result}")
main()


