book_inventory={"How to make wrong choices":{"Author":"Azra","Quantity":7},
       "How to survive fights":{"Author":"Mutakeen","Quantity":8},
        "How to get out of relation":{"Author":"Gazala","Quantity":9}
      }
def display():
    for title,details in book_inventory.items():
        print(f"{title},{details['Author']},{details['Quantity']}")
def purchase_book(title):
    if title in book_inventory:
        if book_inventory[title]["Quantity"]>=0:
            book_inventory[title]["Quantity"]-=1
            print("book purchased")
    else:
        print("book is out of stock")
def main():
    display()
    title=input("enter name of book")
    purchase_book(title)
    display()
main()




