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
