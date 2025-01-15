car_model={"Abc":1000,"Bcd":2000,"Def":3000}
def display():
    for car,price in car_model.items():
        print(f"{car},{price}")
def buy():
    display()
    sum=0
    car=input("enter name of car you want to buy")
    days=int(input("enter no days you want to take the car"))
    if car in car_model:
        sum=car_model[car]*days
        print(f"{sum}")
    else:
        print("car is not available")
buy()



