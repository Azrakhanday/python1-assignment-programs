# Write your code below this line 👇
book_inventory = {"How to make wrong choices": {"Author": "Azra", "Quantity":5},
                  "How to survive fights": {"Author": "Mutakeen", "Quantity": 6},
                  "How to get out of relation": {"Author": "Gazala", "Quantity": 8}
                  }


def display():
    print("current inventory")
    for book, details in book_inventory.items():
        print(f"{book},{details['Author']},{details['Quantity']}")


def purchase_book(title):
    if title in book_inventory:
        if book_inventory[title]['Quantity'] > 0:
            book_inventory[title]["Quantity"] -= 1
        print("you can purchase  this book")
    else:
        print("out of stock")


def main():
    display()
    while True:
        title = input("enter the title of book you want to purchase")
        purchase_book(title)
        display()


main()


