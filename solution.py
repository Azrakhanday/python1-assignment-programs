# Write your code below this line 👇
# print("Hello world!")
book_inventory={"Abc":{"Author":"Azra","Quantity":4},
                "BCD":{"Author":"Mutakeen","Quantity":6},
                "EFG":{"Author":"Abrar","Quantity":9}
                }
def display():
    print("current inventory")
    for book,details in book_inventory.items():
        print(f"{book}by {details['Author']}:{details['Quantity']}")
def purchase_book(title):
    if title in book_inventory:
        if book_inventory[title]["Quantity"]>0:
            book_inventory[title]["Quantity"]-=1
            print(f"you can purchase this")
    else:
        print("book is out of stock")
def main():
    display()
    while True:
        title=input("Enter title")
        purchase_book(title)
        display()
main()