# cart={"iteam1":{"price":5,"Quantity":9},
#        "iteam2":{"price":7,"Quantity":8},
#       "iteam3":{"price":8,"Quantity":2}}
# sum=0
# for i in cart.values():
#
#     price=i["Quantity"]
#     sum+=price
# print(sum)
# def is_prime(num):
#     if num<=1:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#
#     return True
# def sum(num):
#     total=0
#     for i in range(2,num+1):
#         if is_prime(i):
#             total+=i
#     return total
# num=sum(int(input("enter a number")))
# print(num)
# def is_prime(num):
#     if num<=1:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#     return True
# def sum(num):
#     total=0
#     for i in range(2,num+1):
#         if is_prime(num):
#             total+=i
#     return total
# def main():
#     n=sum(int(input("enter a number")))
#
#     print(f"sum of num is{n}")
# main()
# students=[[1,2,3],
#           [4,5,6]]
# for row in students:
#     for column in row:
#         coordinates=(123,456)
#         print(coordinates[1])
# sum=0
# number=int(input("enter your number"))
# temp=number
# while(temp!=0):
#     digit=temp%10
#     sum+=digit
#     temp=temp//10
#     print(temp)
# print(sum)
# fruits=["apple","mango","plum","kiwi"]
# fruits.sort()
# word_count={}
# for fruit in fruits:
#     word_count[fruit]=word_count.get(fruit,0)+1
# print(word_count)
# matrix=[[1,2,3],
#         [2,4,5],
#         [6,7,8]]
# print(len(matrix))
# n=len(matrix)
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(matrix[i][j])
# class Book:
#     def __init__ (self,name="kashmir",author="azra",price="18"):
#         self.name=name
#         self.author=author
#         self.price=price
#     def display(self):
#         print(self.name,self.author,self.price)
# book1=Book()
# book1.display()
# def gredding(func):
#     def wrapper():
#         print("good morning")
#         func()
#         print("thanks for using this function")
#     return wrapper
#
# @gredding
# def hello():
#     print("hello world")
#
# hello()
# class Account:
#     def __init__(self):
#         self.balance=1000
#     def debit(self,amount):
#         self.balance-=amount
#         print(f"rs {amount} is debited ")
#         print("you have ", self.get_balance())
#     def credit(self,amount):
#         self.balance+=amount
#         print(f"your account is credited by {amount}")
#         print(f"you have {self.get_balance()}")
#     def get_balance(self):
#         return self.balance
#
# account1=Account()
# # account1.debit(100)
# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def __str__(self):
#         return f"{self.name}${self.price}"
#
#
#
# class Cart:
#
#     def __init__(self):
#
#
#         self.items=[]
#     def add_product(self,product):
#         self.items.append(product)
#     def remove_product(self,product):
#         if product in self.items:
#             self.items.remove(product)
#
#     def calculate(self):
#         total=0
#         for item in self.items:
#             total+=item.price
#         return total
#     def display(self):
#         print("Cart")
#         for item in self.items:
#             print(item)
#         print(f"price {self.calculate()}")
#
#
#
#
# product1=Product("apple",20)
# item=Cart()
# item.add_product(product1)
# item.display()
# class Person:
#     population=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         Person.population+=1
#     @classmethod
#     def get_population(cls):
#         return cls.population
#
# p1=Person("Azra",23)
# p2=Person("mutakeen",23)
# print("total Population",Person.get_population())
# class Student:
#     def __init__(self,acc_pass):
#         self.__account_pass=acc_pass
#     def reset_pass(self):
#         print(self.__account_pass)
# s1=Student(9435)
# print(s1.reset_pass())
# class Student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.marks=marks
#         self.a=age
#     @classmethod
#     def change_name(cls,new_name):
#         Student.name=new_name
#
# s1=Student("azra",12,40)
# print(s1.name)
# s1.change_name("mutaken")
# print(Student.name)
# class Person:
#     name="anonymous"
#     def change_name(self,name):
#         self.__class__.name=name
# p1=Person()
# p1.change_name("azra")
# print(p1.name)
# # print(Person.name)
# candidates={"Azra":0,"Mutakeen":0,"Gazala":0}
# vote_count=0
# total_votes=0
# while True:
#     print("1.add vote")
#     print("2.display list")
#     print("3.quit")
#     choice=input("enter your choice")
#     if choice=='1':
#         for candidate in candidates:
#             print(candidates)
#             name=input("enter name of the candidate you want to vote")
#             if name in candidates:
#                 candidates[name]+=1
#
#                 total_votes+=1
#     elif choice=='2':
#         for name,vote in candidates.items():
#             print(f"{name},{vote} votes")
#             print(f"total votes {total_votes}")
#     elif choice=='3':
#         print("you quit")
#
#     else:
#         print("you already enter your vote")
# hotel_room={"large room":1000,"medium room":500,"small room":200}
# total_price=0
# while True:
#     print("1.Display list")
#     print("2.book room")
#     choice=input("please enter your choice ")
#     if choice=='1':
#         for room,amount in hotel_room.items():
#             print(f"{room},{amount}/night")
#     elif choice=='2':
#         room=input("please enter your room choicve that you want to book")
#         night_spend=int(input("enter no of days you want to spend"))
#         if room in hotel_room:
#             total_price=hotel_room[room]*night_spend
#             print(total_price)
#     else:
#         print("room is not available")
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __str__(self):
        return f"{self.name},{self.price}"
class Cart:
    def __init__(self):
        self.items=[]
    def add_items(self,product):
        self.items.append(product)
    def remove_items(self,product):
        self.items.remove(product)
    def calculate_total(self):
        total=0
        for i in self.items:
            total+=i.price
        return total
    def show_cart(self):
        print("cart")
        for item in self.items:
            print(item)
        print(f"{self.calculate_total()}")
product1=Product("apple",20)
cart=Cart()
cart.add_items(product1)
cart.show_cart()
















