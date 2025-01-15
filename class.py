# class Person:
#     name="john"
#     age="25"
# p1=Person()
# print(p1.name)
# print(p1.age)
# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
# b1=Book("my bad choices","azra")
# print(b1.title,b1.author)
# class Laptop:
#     def __init__(self,brand,price):
#         self.brand_name=brand
#         self.price=price
# laptop1=Laptop("Dell","$800")
# print(laptop1.brand_name,laptop1.price)
# laptop2=Laptop("Apple","$1200")
# print(laptop2.brand_name,laptop2.price)
# class Phone:
#     price="500"
#     def __init__(self,Model):
#         self.Model=Model
#
# phone1=Phone("iphone")
# print(phone1.Model,phone1.price)
# phone2=Phone("Samsung Galaxy")
# print(phone2.Model,phone2.price)
# class Student():
#     def __init__(self,name,Grade):
#         self.name=name
#         self.grade=Grade
# student1=Student("Azra","A")
# print(f"Name:{student1.name}")
# print(f"Grade:{student1.grade}")
#
# student2=Student("mutakeen","A++")
# print(f"Name:{student2.name}")
# print(f"Grade:{student2.grade}")
# class Movie:
#     def __init__(self,title,director,year):
#         self.title=title
#         self.director=director
#         self.year=year
# movie1=Movie("7 shades of life","Azra and mutakeen",2024)
# print(movie1.title,movie1.director,movie1.year)
class Car:
    def __init__(self,make,model,year,color):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
    @staticmethod
    def start(cls):

        print("car started")

class Car1(Car):
    pass
car1=Car("BMW","X5",2021,"Black")

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)
car2=Car1("Toyoto","corolia",2020,"black")
print(car2.make)
print(car2.model)
print(car2.year)
print(car1.start())










