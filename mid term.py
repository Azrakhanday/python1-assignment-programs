# import time
# seconds=int(input("enter second you want to count down"))
# for i in range(seconds,0,-1):
#     print(f"{i} seconds remaining")
#     time.sleep(1)
# print("time is up")
# print("hello world")
# car={"Abc":3000,"Bcd":4000,"Def":9000}
# for i,(car,price) in enumerate(car,start=1):
#     print(f"{i}.{car}:{price}")
# car_model=input("enter the name of the model")
# days=int(input("for how many days you want to rent this"))
# if car_model in car:
#
#         total=car[car_model]*days
#         print(f"total price is {total}")
# expenses=[]
# while True:
#     print("1.Display")
#     print("2.add iteams")
#     print("3.quit")
#     choice=int(input("please enter your choice"))
#     if choice=='1':
#         for i ,(expense,
# Exercises={"cycling":20,"Running":40,"swimming":100}
# for i,(exercise,calories) in enumerate(Exercises.items(),start=1):
#     print(f"{i}.{exercise}:{calories}")
# exercise=input("enter the name of exercise you want to perform")
# mins=int(input("for how many minutes you want to perform"))
# if exercise in Exercises:
#     total=Exercises[exercise]*mins
#     print(total)
# store={"apple":30,"Mango":80,"Banana":20}
# for i,price in store.items():
#     print(f"The items available in store are{i}and with the quantity{price}")
# while True:
#     print("1.Add items")
#     print("2.Remove items")
#     print("3.exit")
#     choice=input("please enter your choice")
#     if choice=='1':
#         item=input("enter your item you want to add")
#         quantity=int(input("enter quantity of this item"))
#         store[item]=store.get(item,0)+quantity
#         for i, price in store.items():
#             print(f"The items available in store are{i}and with the quantity{price}")
#     elif choice=='2':
#         item=input("enter your item")
#         quantity=int(input("enter quantity of item"))
#         if item in store and store[item] >=quantity:
#             store[item]-=quantity
#         else:
#             print("insufficient quantity")
#     elif choice=='3':
#         break
#     else:
#         print("invalid choice")
# balance=1000
# def withdraw(amount):
#     global balance
#     balance-=amount
#     check_balance()
#
# def credit(amount):
#     global balance
#     balance+=amount
#     check_balance()
# def check_balance():
#     print(f"{balance} is left in your account")
# amount1=int(input("enter amount you want to withdraw"))
# withdraw(amount1)
# temperatures=[]
# for i in range(1,8):
#     temperature=int(input("enter temperature"))
#     temperatures.append(temperature)
# average=sum(temperatures)/len(temperatures)
# print(temperatures)
# print(average)
# budget=int(input("enter total budget of your trip"))
# expenses={}
# flights=int(input("enter your flight fare"))
# expenses["flight"]=flights
# accommodation=int(input("enter your expense for accomadation"))
# expenses["accommodation"]=accommodation
# food=int(input("enter your expense for food"))
# expenses["food"]=food
# transport=int(input("enter your expense for transport"))
# expenses["transport"]=transport
# print(expenses)
# balance=budget-sum(expenses.values())
# print(balance)
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=Person("Azra","23")
# print(p1.name,p1.age)
# class Car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
#     def start(self):
#         return f"engine of {self.brand},{self.model} is running"
# c1=Car("BMW","SuV",2023)
# print(c1.brand,c1.model,c1.year)
# print(c1.start())
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def get_age(self):
#         return self.__age
# p1=Person("Azra",20)
# print(p1.get_age())
# print(p1.name)
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def sound(self):
#         return f"{self.name} makes this sound"
# class Dog(Animal):
#     def sound(self):
#         return f"{self.name} barks"
# class Cat(Animal):
#     def sound(self):
#         return f"{self.name} meow"
# animal1=Dog("tyson")
# print(animal1.name)
# print(animal1.sound())
# animal2=Cat("kutu")
# print(animal2.name)
# print(animal2.sound())
# class Bank_account:
#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder
#         self.__balance=balance
#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance-=amount
#         print(f"this {amount} debited from your account")
#         print(f"your balance is {self.balance()}")
#     def credit(self,amount):
#         self.__balance+=amount
#         print(f"this {amount} get credited in your account")
#         print(f"the balance ion your accont is {self.balance()}")
#     def balance(self):
#         return self.__balance
# acc1=Bank_account("Azra Qadir Khanday",1000)
# acc1.credit(1000)
# class Parent:
#     def greeding(self):
#         print("hello from papa")
# class Child(Parent):
#     def greeding(self):
#         print("hello from child")
# person1=Child()
# person1.greeding()
# class MathOperations:
#     def add(self,a,b,c=0):
#         return a+b+c
# addition=MathOperations()
# print(addition.add(2,3))
# print(addition.add(1,2,3))
# class Product:
#     def __init__(self,price):
#         self.__price=price
#     def get_price(self):
#         return self.__price
#     def set_price(self,new_price):
#         if new_price>0:
#             self.__price=new_price
# item1=Product(1000)
# print(item1.get_price())
# item1.set_price(2000)
# print(item1.get_price())
# class Utility:
#     @staticmethod
#     def add(a,b):
#         return a+b
# print(Utility.add(2,3))
# class Employee:
#     count=0
#     def __init__(self,name):
#         self.name=name
#         Employee.count+=1
#     @classmethod
#     def get_employee_count(cls):
#         return cls.count
# employee1=Employee("azra")
# employee2=Employee("mutakeen")
# print(Employee.get_employee_count())

# class Book:
#     def __init__(self,book,author):
#         self.name=book
#         self.author=author
#     def __str__(self):
#         return f"{self.name} by author {self.author}"
#     def __repr__(self):
#         return f"{self.name} by author {self.author}"
# book1=Book("Bcd","azra")
# print(book1)
# print(repr(book1))
# class Product:
#     def __init__(self,price):
#         self.__price=price
#     @property
#     def price(self):
#         return self.__price
#     @price.setter
#     def price(self,new_value):
#         if new_value>=0:
#             self.__price=new_value
#         else:
#             print("plese enter a valid amount")
# product1=Product(1000)
# print(product1.price)
# product1.price=200000
# print(product1.price)
# class Engine:
#     def start(self):
#         print("engine started")
# class Car:
#     def __init__(self):
#         self.engine=Engine()
#     def drive(self):
#         self.engine.start()
#         print("car is moving")
# car1=Car()
# car1.drive()
# class Animal:
#     def sound(self):
#         pass
# class Dog():
#     def sound(self):
#         print("bark")
# class Cat():
#     def sound(self):
#         print("meow")
# animal1=[Dog(),Cat()]
# for animal in animal1:
#     animal.sound()
# number=int(input("enter a number"))
# count=0
# new_number=0
# quotient=number
# while quotient!=0:
#     count+=1
#     last_number=quotient%10
#     new_number=new_number*10+last_number
#     print(last_number)
#     quotient//=10
# print(quotient)
# print(count)
# class Engine:
#     def start(self):
#         print( "car started")
# class Car:
#     def __init__(self,name):
#         self.name=name
#         self.engine=Engine()
#     def drive(self):
#         self.engine.start()
#         print("car is moving")
# car1=Car("bmw")
# car1.drive()
class Book:
    # def __init__(self,name,author):
    #     self.name=name
    #     self.author=author
    def dispaly(self):
        print(f"the name of this book is ")
    def author(self):
        print(f"the book under this name is written by author")
class Library:
    def __init__(self,name):
        self.name=name
        self.aut1= Book()
    def run(self):
        self.aut1.author()
book1=Library("rumi library")
book1.run()

















