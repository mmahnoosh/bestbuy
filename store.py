class Product:

    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError(
                "Invalid input: name must not be empty")
        if price < 0 or quantity < 0:
            raise ValueError(
                "Invalid input: price and quantity must be non-negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> int:
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity
        if quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self) -> str:
        status = "Active" if self.active else "Inactive"
        return f'"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Status: {status}"'

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Invalid input: quantity must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock: there is not enough product available.")

        total_price = quantity * self.price
        self.quantity -= quantity  # Shorter way of updating the quantity
        return total_price

product = Product("MacBook Air M2",1450, 100)
print(product.show())