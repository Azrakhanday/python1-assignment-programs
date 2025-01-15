# num=int(input("enter a number"))
# if num%2==0:
#     print("num is even")
# else:
#     print("num is odd")
# numbers=[1,2,3,4,5]
# print(len(numbers))
# n=len(numbers)
# sum=0
# for i in range(n):
#     sum+=i
# print(sum)
# numbers=[1,2,3,4,5]
# sum=0
# for i in numbers:
#     sum+=i
# print(sum)
list=[]
for i in range(5):

    num=int(input("enter a number"))

    list.append(num)
print(list)
sum=0
for i in list:
    if num%2!=0 and num in list:
        sum+=i
print(sum)
if sum<=30 and sum<=40:
    print(f'{sum} is in this range')
else:
    print("out of range")






