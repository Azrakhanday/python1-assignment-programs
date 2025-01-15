# f=open('E:\\reta.txt','r' )
# print(f.read())
# # f=open('E:\\reta.txt','w')
# # f.write("hi my name is azra")
# # # f.close()
# # f=open('E:\\reta.txt','a')
# # f.write("i am doing mtec")
# # f=open('file.txt')
# # f.read()


# fruits=["orange",'grapes','mango']
# fruits.insert(0,'apple')
# print(fruits)
# coordinates=(1,2,3)
# x,y,z=coordinates
# print(x,y,z)
# indi={"name":"Azra","course":"mtec"}
# print(indi["name"])
# print(indi.get("type","Silver"))
# def user_name(name):
#     print(f"my name is {name}")
# name1=input("enter your name")
# user_name(name1)
# print(user_name(name1))
# try:
#     age=int(input("enter your age"))
#     income=int(input("enter your income"))
#     risk=income/age
#     print(risk)
# except ValueError:
#     print(("you entered a invalid number"))
# except ZeroDivisionError:
#     print(("you entered zero number plese enter a non zero"))
# class Duck:
#     def swim(self):
#         print("hi i am a duck and i can swim")
#     def sound(self):
#         print("i am doing quack quack")
# class Dog:
#     def swim(self):
#         print("hi i am a dog and i can swim")
#     def sound(self):
#         print("i do wouf wouf")
# def display(obj):
#     obj.swim()
#     obj.sound()
# c1=Dog()
# display(c1)
# class Parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Mother(Parent):
#     def __init__(self,name,age):
#         self.age=age
#         super.name=name
# def add(n1,n2):
#     return n1+n2
# def sub(n1,n2):
#     return n1-n2
# def multiple(n1,n2):
#     return n1*n2
# def div(n1,n2):
#     return n1/n2
# operations={"+":add,
#            "_":sub,
#            "*":multiple,
#            "/":div}
# def calculator():
#     acculumate = True
#     num1=float(input("enter your first number"))
#     while acculumate:
#         for symbol in operations:
#             print(symbol)
#         operation_symbol=input("pick a symbol")
#         num2=int(input("enter a number"))
#         answer=operations[operation_symbol](num1,num2)
#         print(f"{num1}{operation_symbol}{num2}={answer}")
#         choice=input("if you want to continue operation on this number pick 'y' for yes and'n' for no")
#         if choice=="y":
#             num1=answer
#         else:
#             acculumate=False
#             print("/n"*20)
#             calculator()
# calculator()
# import time
# seconds=int(input("Enter no of seconds"))
# for i in range(seconds,0,-1):
#     print(f"{i} seconds remaining")
#     time.sleep(1)
# print("Time's up!")
# shopping_cart=[]
#
# add=True
# while add:
#     items = input("enter name of items you want to add")
#     shopping_cart.append(items)
#     choice=input("enter 'checkout' to display all elements and 'n' to stop")
#     if choice=='checkout':
#
#             print(shopping_cart)
#     else:
#         print("there is no item available")
#         add=False
# Book_store={"Bad choice":{"Author":"azra","quantity":10},
#             "crying":{"Author":"mutt","quantity":20},
#             "play":{"Author":"gazal","quantity":30}
#             }
#
# def display():
#     for i,details in Book_store.items():
#         print(f"The book under name {i} and under quantity {details["quantity"]},and is written by {details['Author']}")
#
# def purchase(title):
#     if title in Book_store:
#         if Book_store[title]["quantity"]>0:
#             Book_store[title]["quantity"]-=1
#     else:
#         print("book is not available")
# def main():
#     display()
#     title=input("please enter the name of book you want to purchase")
#     purchase(title)
#     display()
# main()
import time
seconds=int(input("enter no of seconds"))
for i in range(seconds,0,-1):
    print(i)
    time.sleep(1)
print("time is up")












