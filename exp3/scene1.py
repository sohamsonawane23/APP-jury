print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(f"Added {product.name} to cart")

    def remove_item(self, product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f"Removed {product_name} from cart")
                return
        print(f"{product_name} not found in cart")

    def calculate_total(self):
        return sum(item.price for item in self.items)  # generator expression

    def print_bill(self):
        print("---- Shopping Cart Bill ----")
        for item in self.items:
            print(f"{item.name:20} ${item.price:.2f}")
        print("---------------------------")
        print(f"Total: {'':14} ${self.calculate_total():.2f}")

# Example Usage
p1 = Product("Laptop", 999.99)
p2 = Product("Mouse", 25.75)
p3 = Product("Keyboard", 45.50)

cart = Cart()
cart.add_item(p1)
cart.add_item(p2)
cart.add_item(p3)
cart.print_bill()

cart.remove_item("Mouse")
cart.print_bill()
