class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def get_total_price(self):
        return self.price*self.quantity
    def __str__(self):
        return f"{self.name}-${self.price}*{self.quantity}"

class ShoppingCart:
    def __init__(self):
        self.cart_items=[]
    def add_product(self,product):
        self.cart_items.append(product)
    def remove_product(self,product_name):
        self.cart_items=[item for item in self.cart_items if item.name!=product_name ]
    def calculate_total(self):
        return sum(item.get_total_price()for item in self.cart_items)
    def show_cart(self):
        if not self.cart_items:

            return "your shopping cart is empty"
        cart_content="\n".join(str(item)for item in self.cart_items)
        return f"your cart:{cart_content}\n Total:${self.calculate_total()}"
apple=Product("Apple",0.99,3)
cart=ShoppingCart()
cart.add_product(apple)
print(cart.show_cart())
cart.remove_product(apple)
print(cart.show_cart())
