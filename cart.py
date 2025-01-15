def add_items():
    shopping_cart=[]
    while True:
        print("shopping cart meanu")
        print("1.Add iteam to cart")
        print("2.checkout")
        print("3.quit")
        choice=input("please enter your choice")
        if choice=="1":
           item=input("enter iteam you want to add")
           shopping_cart.append(item)
           print(f"iteam added{item}")
        elif choice=="2":
            if shopping_cart:
                print("your cart")
                for i,item in enumerate(shopping_cart,start=1):
                    print(f"{i}.{item}")
            else:
                print("cart is empty")
        elif choice=="3":
            print("good bye")
            break
        else:
            print("invalid choice")
add_items()