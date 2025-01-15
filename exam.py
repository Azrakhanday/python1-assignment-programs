# num=int(input("enter your number"))
# temp=num
# sum=0
# while (temp!=0):
#     digit=temp%10
#     sum+=digit
#     temp=temp//10
# print(sum)
list=[[1,2,3],
      [3,4,5],
      [6,7,8]]
print(len(list))

n=len(list)
for i in range(n):
    for j in range(n):
        if i==j:
            print(list[i][j])

