rows=int(input("Enter no of rows"))

for row in range(rows):
    for column in range (rows-row-1):
        print(" ",end="")
    for k in range(2*row+1):
        print('*',end="")
    print()

