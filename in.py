# books={"The life":{"Author":"Azra","Quantity":80},
#        "Survive":{"Author":"Mutakeen","Quantity":70},
#        "Meeting":{"Author":"Gazala","Quantity":60}
# }
# def display():
#     for i ,details in books.items():
#         print(f'The book under name {i} written by Author {details["Author"]},and with Quantity {details["Quantity"]}')
#
# def purchase(title):
#     if title in books:
#         if books[title]['Quantity'] >=0:
#             books[title]['Quantity'] -= 1
#             print('you can purchase this book')
#     else:
#         print("sorry we are out of stock")
# def main():
#     display()
#     title=input("Enter the name of book you want to buy")
#     purchase(title)
#     display()
# main()
# import time
# seconds=int(input("enter no of seconds"))
# for i in range(seconds,0,-1):
#     print(f"you have{i}seconds left")
#     time.sleep(1)
# shopping_list=[]
# while True:
#     choice=input("enter your choice enter 'y' to add items to list and 'n' to view list")
#     if choice=='y':
#         x=input("Enter items you want to add")
#         shopping_list.append(x)
#     else:
#         y=input("please enter check out to view the list")
#         print(shopping_list)
# def track_expenses():
#  expenses=[]
#  while True:
#         print(" expenses")
#         print("1.Add expenses")
#         print("2.show expenses")
#         print("3.Quit")
#         choice=input("please enter your choice ")
#         if choice=='1':
#
#             amount_spend = int(input('Enter the amount you spend'))
#             description = input("Enter the description where you spend this amonut")
#             expense = {"Amount": amount_spend, "Description": description}
#             expenses.append(expense)
#         elif choice=='2':
#             for i,expense in enumerate (expenses,start=1):
#                 print(f"the item{i} and with {expense['Amount']},{expense['Description']}")
#                 sum(expense["Amount"]for expense in expenses)
#                 print(f"{sum}")
#         else:
#             print("inventory is empty")
# track_expenses()
# candidates={"Azra":0,"Mutakeen":0,"Gazala":0}
# total_votes=0
# while True:
#     print("1.add votes")
#     print("2.display")
#     print("3.Quit")
#     choice=input("please enter your choice")
#     if choice=='1':
#         for candidate in candidates:
#             print(candidates)
#             vote=input("please enter the name of candidate you want to vote")
#             if vote in candidates:
#                 candidates[vote]+=1
#                 total_votes+=1
#     elif choice=='2':
#         for i,items in candidates.items():
#             print(f"the candidate under name{i} and with votes{items['votes']}")
#             print(f"{total_votes}")
#     else:
#         choice=='3'
#         print('you are not elgible for voting')
# total_fare=int(input("enter the total fare"))
# people=int(input("How many people are splitting this fare"))
# pay=total_fare/people
# print(pay)
# hotel_room={"Large_room":1000,"Medium_room":500,"small_room":200}
#
#
# for room,price in hotel_room.items():
#     print(f"We have this room{room} under {price}/night")
# room_type = input("Enter the name of the room")
# nights_Spend = int(input("Enter for how many days you want to stay"))
# if room_type in hotel_room:
#     total_cost=hotel_room[room_type]*nights_Spend
#     print(total_cost)
# cars={"Bmw":500000,"Audi":800000,"Lambeorgini":20000000}
# for car,price in cars .items():
#     print(f"{car},{price}")
# car=input("Enter the name of the car you want to buy")
# days=int(input("How many days you want to rent this car"))
# if car in cars:
#     rental_price=cars[car]*days
#     print(rental_price)
# inventory={}
# while True:
#     print("1.To add iteam")
#     print("2.Remove")
#     print("3.display")
#     choice=input("Please enter your choice")
#     if choice=='1':
#         name=input("Enter name of the object you want to add")
#         Quantity=int(input("Enter the quantity"))
#         inventory[name]=inventory.get(name,0)+Quantity
#         print(f"Added {name},{Quantity}")
#     elif choice=='2':
#         name=input("enter the name of product you want to remove ")
#         Quantity=int(input("enter quantity"))
#         if name in inventory and inventory[name]>Quantity:
#             inventory[name]-=Quantity
#             print(f"{name}item removed")
#     elif choice=='3':
#         for name,Quantity in inventory.items():
#             print(f"{name},{Quantity}")
#     else:
#         print("Quit")
# balance=1000
# def deposit():
#     global balance
#     amount=int(input("enter the amount you want to debit"))
#     if amount<balance:
#         balance-=amount
#         print(balance)
#     else:
#         print("we are out of money")
# def credit():
#     global balance
#     amount=int(input("enter the amount you want to credit"))
#     balance+=amount
#     print(balance)
# def check_balance():
#     global balance
#     return balance
# while True:
#     print("1.Debit")
#     print("2.credit")
#     print("3.check_balance")
#     choice=input("Enter your choice")
#     if choice=='1':
#         deposit()
#     elif choice=='2':
#         credit()
#     elif choice=='3':
#         check_balance()
#     else:
#         print("sorry you don't know how to use an Atm go home and sleep")
# rows=int(input("enter no rows"))
# for i in range(rows):
#     for j in range(rows-i-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end="")
#     print()
# rows=int(input("enter no of rows"))
# for i in range(rows):
#     for j in range(rows-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()
# def sum_of_digits(num):
#     total=0
#     while num>0:
#         total+=num%10
#         num//10
#     return total
# def main():
#     num=int(input("please enter your number"))
#     result=sum_of_digits(num)
#     print(f"sum of {num} is {result}")
# main()
# def is_prime(num):
#     if num<=1:
#         return False
#     else:
#         for i in range(2,int(num**0.5)+1):
#             if num%i == 0:
#                 print(f"number{num} is not prime")
#             else:
#                 print("number is prime")
# def main():
#     num=int(input("Entr a number"))
#     is_prime(num)
# main()
# list=[]
# for i in range (5):
#     fruits=input("Please enter the name of fruits")
#     list.append(fruits)
# print(list)
# students={'azar':1,'mutakeen':2,"gazala":3}
# for name,i in students.items():
#     print(f"my name is {name} with enroll {i}")
# grocery_item={}
# for i in range(5):
#     things=input("enter the name of things")
#     price=int(input("enter price of things"))
#     grocery_item[things]=price
# total_bill=sum(grocery_item.values())
# print("Grocery items and prices")
# for item,price in grocery_item.items():
#     print(f"{item}:{price:.2f}")
#     print(f"Total bill{total_bill:.2f}")
# grocery_item={}
# for i in range(5):
#     things=input("enter the name of  things")
#     price=int(input("enter the price of things"))
#     grocery_item[things]=price
# Total_bill=sum(grocery_item.values())
# for item,price in grocery_item.items():
#     print(f"{item},{price}")
#     print(f"{Total_bill}")
# set1={"Apple","Banana","Mango","book"}
# set1.add('pen')
# print(set1)
# expenses={}
# for i in range(2):
#     item=input("enter name of item")
#     description=input("enter the descrption of item")
#     expenses[item]=description
# print(expenses)
# expenses=[]
# item=input("enter the name of item you want to take")
# description=input("enter the description of item")
# amount=int(input("enter the amount"))
# expense={"Amount":{amount},"description":{description}}
# expenses.append(expense)
# number=int(input("enter the number"))
# if number<=2:
#     print("number is invalid")
# elif (number%i!=0 for i in range(2,int(number**0.5)+1)):
#     print(f"{number}is prime number")
# else:
#     print(f"{number}is not prime")
# set={'apple','mango','oranage'}
# set.add("orange")
# print(set)

# square=[x**2 for x in range (1,11)]
# print(square)
# num=[x for x in range(1,21) if x%2==0 ]
# print(num)
# first_word=[word[0] for word in ['Apple','Banana','Orange'] ]
# print(first_word)
# num=[x for x in range(1,31) if x%3==0]
# print(num)
# num=[(x,x**2)for x in range(1,30)]
# print(num)
# num=[x for x in range(1,7)]
# print(num)
# com=[word for word in 'The quick brown fox jumps over a lazy dog'.split() if len(word)>4]
# print(com)
# list=[x if x%2!=0 else "Even" for x in range(1,10)]
# print(list)
# number=int(input("enter a number "))
# quotient=number
# while quotient>0:
#     new_number=quotient%10
#     reminder=new_number
#
#     quotient//=10
#     print(reminder)
# coordinates=(1,2,3)
# x,y,z=coordinates
# print(x)
# items=[]
# prices=[]
# total_bill=0
# for i in range(5):
#     item=input('enter the name of item')
#     price=int(input("enter the price of item"))
#     items.append(items)
#     prices.append(price)
#     total_bill+=price
# print(total_bill)
# amount=int(input("enter the amount"))
# tip=0.1
# total_amount=amount+tip
# print(total_amount)

# marks=[]
# total=0
# for i in range(3):
#     mark=int(input("please enter the marks of 3 subjects"))
#     marks.append(mark)
#     total+=mark
# average=total/3*100
# print(average)
# if average>=100 and average>=90:
#     print("you got a A")
# elif average>=89 and average>=80:
#     print("you got a B")
# else:
#     print("sorry you fail the exam")
# inventory={
#             'Apple':{"price":20,"quantity":9},
#             'Mango':{"price":30,"quantity":40}
# }
# highest_price=max(item['price'] for item in inventory.values())
# print(f"Highest price:{highest_price}")
# set1={1,2,3,4,5}
# set2={6,7,8,9,10}
# result={x+y for x in set1 for y in  set2}
# print(result)
# value=max(set1)
#
# print(value)
# tuple1=(1,2,3,4)
# tuple2=(5,6,7,8)
# result=tuple(x+y for x,y in zip(tuple1,tuple2))
# print(result)
# list1=['Apple','Mango','orange']
# word_count={}
# for fruit in list1:
#     word_count[fruit]=word_count.get(fruit,0)+1
# print(word_count)
# inventory={"Laptop":{'price':30,'quantity':4},"Lenova":{'price':50,'quantity':7},"HP":{'price':80,'quantity':6}}
# highest_price=max(item['quantity']for item in inventory.values())
# print(highest_price)
# inventory={"Apple":10,"MAngo":30,"orange":40}
# highest_price=max(inventory.values())
# print(highest_price)
# num=int(input("enter no you want to get multiple of"))
# for i in range(10,0,-1):
#     mul=num*i
#     if i==5:
#         continue
#     elif i==7:
#         continue
#     print(mul)
# class Car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
# car1=Car("BMW","2","2020")
# print(car1.make,car1.year,car1.model)
# class Book:
#     def __init__(self,title,author,pages):
#         self.title=title
#         self.author=author
#         self.pages=pages
#     def display(self):
#         print(f"The book with title{self.title},and is written by{self.author},with pages {self.pages}")
#
# book=Book("Abc","Azra","101")
# book.display()
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def introduce(self):
#         print(f'Hi my name is {self.name} and i am {self.age} years old')
# per=Person('Azra','23')
# per.introduce()
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def parameter(self,area):
        parameter=2*(self.length+self.width)
rec=Rectangle(10,20)
rec.area()
print(rec.area())

























































