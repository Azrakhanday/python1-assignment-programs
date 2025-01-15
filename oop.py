# class Student:
#     def __init__(self,fullname,roll_no):
#         self.name=fullname
#         self.roll_no=roll_no
#
# s1=Student("Azra Khanday",3)
# print(s1.name)
# print(s1.roll_no)
# s2=Student("mutakeen nissar",7)
# print(s2.name)
# print(s2.roll_no)
# class Marks:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
#         for value in self.marks:
#             sum+=value
#         print("hi",self.name,"your average marks is",sum/3)
# s1=Marks("Azra",[99,98,76])
# # s1.get_avg()
# class Account:
#     def __init__(self,bal,acc):
#         self.balance=bal
#         self.account_no=acc
#     def debit(self,amount):
#         self.balance-=amount
#         print("rs.",amount,"was debited")
#         print("total balnce",self.get_balance())
#         self.balance+=amount
#         print("rs.",amount,"was credited")
#         print("total balance =",self.get_balance())
#     def get_balance(self):
#         return self.t(1000,123454)
# print(acc1.balance)
#
# print(acc1.account_no)
# acc1.debit(1000)
# acc1.credit(2000)balance

# class Product:
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
#     def get_total_price(self):
#         return self.price*self.quantity
#     def __str__(self):
#         return f"{self.name}-{self.price}*{self.quantity}"
# object=Product("Apple",20,4)
# print(object.name)
# print(object.get_total_price())
# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
information=[]
while True:
    print("1.add")
    print("2.dispaly")
    print("3.quite")
    choice=input("enter your choice")
    if choice=='1':
        amount=int(input("ente your amount"))
        description=int(input("enter descrption"))
        expense={"Amount":amount,"Descrption":description}
        information.append(expense)
        print("expense added sucessfuly")
    elif choice=="2":
        if information:
            print("expense summary")
        for i ,expense in enumerate(information,start=1):

            print(f"{i}, Amount:{expense['Amount']}/description{expense['description']}")
        sum(expense['Amount'] for expense in information )
        print(f"{sum}")
    elif choice=='3':
        print("quit")
    else:
        print("inventory is empty")





