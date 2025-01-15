

inventory={}
while True:
    print("1.Add iteam")

    print("2.remove iteam")
    print("3.print inventory")
    choice=input("enter your choice 1,2 ")
    if choice=='1':
        name=input("enter your name you want to add")
        quantity=int(input("enter quantity"))
        inventory[name]=inventory.get(name,0)+quantity
        print(f"Added {quantity}{name}")
    elif choice=='2':
        name=input("enter name of iteam")
        quantity=int(input("enter quantity"))
        if name in inventory and inventory[name]>quantity:
            inventory[name]-=quantity
            print(f"removed {quantity}{name}")
    elif choice=='3':
        print("current inventory")
        for iteam,quantity in inventory.iteams():
            print(f"{iteam}:{quantity}")
    else:
        print("invalid choice.please try again.")


