# book_inventory={"wrong choice":{"Author":"Azra","quantity":23},
#       "Beautiful thoughts":{"Author":"Mutakeen","quantity":65},
#       "Cde":{"Author":"Gazala","quantity":79}}
# def display():
#       for title,details in book_inventory.items():
#             print(f" {title} by {details['Author']} with quantity:{details['quantity']}")
#
# display()
# def purchase(title,how):
#
#       if title in book_inventory:
#             if book_inventory[title]["quantity"]>0:
#                   book_inventory[title]["quantity"]-=how
#                   print("you have purchased the book")
#       else:
#             print("we are out of stock")
# def main():
#       display()
#       title=input("enter your iteam you want to buy")
#       how=int(input("enter quantity"))
#       purchase(title,how)
#       display()
# main()
# class Employee:
#       def __init__(self,name,age):
#             self.name=name
#             self.age=age
#       def __str__(self):
#             return f"My name is {self.name},Age is {self.age}"
#
# emp=Employee("Azra",23)
#
# print(str(emp))
# class Student:
#       def __init__(self,name):
#             self.name=name
#             self.grades=[]
#       def add_grades(self,grade):
#             self.grades.append(grade)
#       def sum_average(self):
#             return sum(self.grades)/len(self.grades)
# stu=Student("Azra")
# stu.add_grades(20)
# stu.add_grades(30)
# print(stu.sum_average())
# class Flower:
#       @staticmethod
#       def flower():
#            print("i want to buy a flower")
# class Rose(Flower):
#
#       def __init__(self,color):
#             self.color=color
# class Lily(Rose):
#       def __init__(self,price,color):
#             self.price=price
#             super().__init__("color")
#
# flower1=Lily("20","red")
# print(flower1.price)
# print(flower1.flower())
# import cart


# class Shopping_Cart:
#       def __init__(self):
#
#             self.add_cart=[]
#       def add_iteam(self,product):
#             self.add_cart.append(product)
#       def remove_iteam(self,product):
#             if product in self.add_cart:
#                   self.add_cart.remove(product)
#       def display_list(self):
#             print("current list:")
#             for product in self.add_cart:
#                   print(product)
#             print()

# cart1=Shopping_Cart()
# cart1.add_iteam("apple")
# cart1.add_iteam("banana")


# cart1.add_iteam("mango")
# cart1.remove_iteam("apple")
# print(cart1.display_list())
# class Person:
#       def __init__(self,name):
#             self.name=name
#       @property
#       def name(self):
#             return self.name
# p1=Person("azra")
# print(p1.name)
# p1.name("mutakeen")
# print(p1.name)
# class Person:
#       def __init__(self,name,age):
#             self.name=name
#             self.age=age
#       @classmethod
#       def from_birth_year(cls,name,birth_year):
#             age=2024-birth_year
#             return cls(name,age)
# p1=Person("Azra",23)
# print(p1.name,p1.age)
# p2=Person.from_birth_year("azra",2000)
# print(p2.name,p2.age)
# class Person:
#       def __init__(self,name,age):
#             self.name=name
#             self.age=age
#       @classmethod
#       def name(cls,name,current_year,birth_year):
#             age=current_year-birth_year
#             return cls(name,age)
# p2=Person.name("Azra",2024,2000)
# print(p2.name,p2.age)

# class Person:
#       def __init__(self,name=""):
#             self._name=name
#       """here property is a getter gives acess to object outside the class"""
#       @property
#       def name(self):
#             return self._name
#       """setter sets the value of class"""
#       @name.setter
#       def name(self,name):
#             self._name=name
# p1=Person("azra")
# print(p1._name)
# p1.name="mutakeen"
# print(p1.name)
# def my_decorator(func):
#       def wrapper():
#             print("doing something before function ")
#             func()
#             print("doing something after function")
#             return wrapper
#       @my_decorator
#       def say_hello():
#        print("hello")
#      say_hello()
# class Animal:
#     def __init__(self,name):
#         self.name=name
# class Dog(Animal):
#     def __init__(self,color,name):
#         self.color=color
#         super().__init__(name)
# p1=Dog('buddy','green')
# print(p1.name,p1.color)
# class Engine:
#     def start(self):
#
#         print("engine started")
# class Car:
#     def __init__(self):
#         self.engine=Engine()
#     def start(self):
#         self.engine.start()
# car1=Engine()
# bmw=Car()
# bmw.start()
# class Battery:
#     def charge(self):
#         print("battery charging ")
# class Laptop:
#     def __init__(self,battery):
#         self.battery=battery
#     def power_on(self):
#         self.battery.charge()
#         print("laptop is on ")
#
# battery=Battery()
# laptop=Laptop(battery)
# # laptop.power_on()
# class Salary:
#     def __init__(self,pay,bonus):
#         self.pay=pay
#         self.bonus=bonus
#     def annual_salary(self):
#         return (self.pay*12)+self.bonus
# class Employee:
#     def __init__(self,name,age,pay,bonus):
#         self.name=name
#         self.age=age
#         self.obect_salary=Salary(pay,bonus)
#     def total_salary(self):
#         return self.obect_salary.annual_salary()
#  emp=Employee('max',25,15000,1000)
#  print(emp.total_salary())
# class Book:
#     def __init__(self,title,author,pages):
#         self.title=title
#         self.author=author
#         self.pages=pages
#     def display(self):
#         print(f"you have a book under name{self.title},with author{self.author}and having with pages{self.pages}")
# book1=Book("choices","azra","101")
# book1.display()
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(f"Hi my name is {self.name} and I'm {self.age}years old")
# student1=Person("azra",23)
# student1.display()
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#          return self.length*self.width
#     def parameter(self):
#         return 2*self.length+self.width
#
# traingle=Rectangle(4,5)
# print(traingle.area())
#  print(traingle.parameter())
# class Employee:
#     def __init__(self,name="",salary=""):
#         self._name=name
#         self._salary=salary
#     @property
#     def name(self):
#         return self._name
#
#     def salary(self):
#         return self._salary
#
#
#
#     @name.setter
#     def name(self,new_name):
#          self._name=new_name
#
#     def salary(self,salary):
#         self._salary=salary
#
#
# Emp=Employee("azra",100000000)
# print(Emp._name)
# Emp.name="Mutakeen"
# Emp.salary=20000
# print(Emp.salary)
#  print(Emp.name)
# class Patient:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
#     @property
#     def name(self):
#         return self._name
#     @property
#     def age(self):
#         return self._age
#     @name.setter
#     def name(self,new_name):
#         self._name=new_name
#     @age.setter
#     def age(self,new_age):
#         self._age=new_age
# p1=Patient("Abc",45)
# print(p1._name)
# p1.name="Bcd"
# print(p1._name)
# print(p1._age)
# p1.age=55
# print(p1._age)
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print(f"{self.name}makes this sound")
#
# class Dog(Animal):
#     def __init__(self,name,breed):
#
#         super().__init__(name)
#         self.breed = breed
#     def speak(self):
#         print(f"{self.name} makes this sound")
# class Cat(Animal):
#     def __init__(self,name,color):
#         super().__init__(name)
#         self.color=color
# animal1=Animal("dog")
# p1=Dog("tyson","bull_dog")
# print(p1.name)
# p1.speak()
# class Vechicle:
#     def __init__(self,name):
#         self.name=name
# class Car(Vechicle):
#     def __init__(self,name,model):
#         super().__init__(name)
#         self.model=model
# class Bike(Car):
#     def __init__(self,name,model,make):
#         super().__init__(name)
#         super().__init__(model)
#         self.make=make
# c1=Vechicle("BMw")
# c1=Car("Bmw",2019)
# c1=Bike("Abc",2016,"Honda")
# class Student:
#     def __init__(self,name,roll_no):
#         self.name=name
#         self.roll_no=roll_no
#     def __str__(self):
#         return f"my name is {self.name} under rollno{self.roll_no}"
# stu=Student("azra",23)
# print(stu)
# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def __str__(self):
#         return f"we want to buy a product under name{self.name}with price{self.price}"
# p1=Product("apple",20)
# print(p1)
# class Math_operations:
#     @staticmethod
#     def add(a,b):
#         return a+b
#
#
#
# num1=Math_operations.add(5,6)
# print(num1)
# class Person:
#     populatiom=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         Person.populatiom+=1
#     @classmethod
#     def get_population(cls):
#         return cls.populatiom
#
# p=Person("azra",24)
# p1=Person("Mutakeen",23)
# print("Total population",Person.get_population())
# class Temperature:
#     def __init__(self,celsius=0):
#         self._celsius=celsius
#     @property
#     def celsius(self):
#         return self._celsius
#     @celsius.setter
#     def celsius(self,new_value):
#         self._celsius=new_value
#     def __str__(self):
#         return f"the temperature of this room is {self.celsius}"
#     def farenheit(self):
#         return f"{self.celsius*9/5+32}"
# temp1=Temperature()
# temp1.celsius=30
# print(temp1.farhait())
# print(temp1)

# class Bank_Account:
#     def __init__(self,balance=0):
#         self._balance=balance
#     @property
#     def balance(self):
#         return self._balance
#     @balance.setter
#     def balance(self,new_value):
#         self._balance=new_value
#     def deposit(self,amount):
#         self._balance+=amount
#         print(f"This amount get debited{amount}")
#         print(f"you have {self.balance1()}")
#     def credit(self,amount):
#         self._balance+=amount
#         print(f"rs {amount}got credit ")
#         print(f"you have{self.balance1()}")
#     def balance1(self):
#         return self._balance
# user=Bank_Account()
# user.credit(1000)
# class Address:
#     def __init__(self,city,zipcode):
#         self.city=city
#         self.zipcode=zipcode
#     def __str__(self):
#         return f"{self.city},{self.zipcode}"
# class Person:
#     def __init__(self,name,city,zipcode):
#         self.name=name
#         self.address=Address(city,zipcode)
#
#     def __str__(self):
#         return f"my name is {self.name} i live in city{self.address} "
#
# p1=Person("azra","srinagar",00)
# print(p1)
#

# class Engine:
#     def __init__(self,horse_power):
#         self.horse_power=horse_power
#     # def __str__(self):
#     #     return f"{self.horse_"power}
#
# class Car:
#     def __init__(self,name,color,horse_power):
#         self.name=name
#         self.color=color
#         self.engine=Engine(horse_power)
#     def dispaly(self):
#         return f"{self.name},{self.color},{self.engine.horse_power}"
# c1=Car("BMw","black",500)
# print(c1.dispaly())
# class Employee:
#     def __init__(self,name):
#         self.name=name
# class Manager(Employee):
#     def __init__(self,name,id):
#         super().__init__(name)
#         self.id=id
#
# manager=Manager("azra","7654")
# print(manager.name,manager.id)
# class GrandParent:
#     def __init__(self,caste):
#         self.caste=caste
#
# class Parent(GrandParent):
#     def __init__(self,caste,name):
#
#         super().__init__(caste)
#         self.name=name
#
# class Grand_child(Parent):
#     def __init__(self,age,caste,name):
#
#         super().__init__(name,caste)
#         self.age=age
#
# gc=Grand_child(23,"azra","khanday")
# print(gc.age,gc.caste,gc.name)
# class Father:
#     def __init__(self,caste,occupation):
#         self.caste = caste
#         self.occupation=occupation
#     def dispaly(self):
#         return f"{self.caste},{self.occupation}"
#
#
# class Mother:
#     def __init__(self,name,caste,occupation):
#         super().__init__(caste,occupation)
#         self.name = name
#
#
#
#
# class Grand_child(Mother):
#     def __init__(self, age, caste, name,occupation):


#         super().__init__(caste,occupation,name)
#         self.age = age
#     def display(self):
#         return f"{self.age},{self.name},{self.occupation}"
#
#
#
# gc = Grand_child(23,"khanday","azra","student")
# print(gc.age, gc.caste,gc.name)

# class Father:
#     def __init__(self,father_name):
#         self.name=father_name
# class Mother:
#     def __init__(self,mothers_name):
#         self.mname=mothers_name
# class Child(Father,Mother):
#     def __init__(self,father_name,mother_name,child_name):
#         self.child = child_name
#         super().__init__(father_name)
#         Mother.__init__(self,mother_name)
#
# c1=Child("Qadir","parveen","azra")
# print(c1.child,c1.name,c1.mname)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class Teacher(Person):
#     def __init__(self,salary,name,age):
#
#         super().__init__(name,age)
#         self.salary = salary
#
# T1=Teacher("20000","kaisar khanday",60)
# print(T1.name)
# class Product:
    # def __init__(self,name):
    #     self.name=name
    #     self.items=[]
#     def add_book(self,product):
#         self.items.append(product)
#     def list_book(self):
#         return [f"{items.name} by {book.author}"for book in self.books]
# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
# library=Library("rumi library")
# book1=Book("abc","azra")
# library.add_book(book1)
# for book in library.list_book():
#     print(book)
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __str__(self):
        return f"{self.name},{self.price}"
class Cart:
    def __init__(self):
        self.cart_item=[]
    def add_item(self,product):
        self.cart_item.append(product)
    def remove_itme(self,product):
        if product in self.cart_item:
            self.cart_item.remove(product)
    def total(self):
        total=0
        for item in self.cart_item:
            total+=item.price
        return total
    def display(self):
        for item in self.cart_item:
            print(item)
        print(f"Total price is {self.total()}")
product1=Product("apple",30)
product2=Product("mango",10)
cart=Cart()
cart.add_item(product1)
cart.add_item(product2)
cart.display()




