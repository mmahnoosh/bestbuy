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