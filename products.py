class Product:
    """
    A class to represent a product with a name, price, quantity, and activation status.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The available quantity of the product.
        active (bool): The activation status of the product.
    """

    def __init__(self, name, price, quantity):
        """
        Initialize a new product instance.
        Args:
            name (str): The name of the product.
            price (float): The price of the product. Must be non-negative.
            quantity (int): The quantity of the product. Must be non-negative.
        Raises:
            ValueError: If name is empty or if price/quantity is negative.
        """
        if not name:
            raise ValueError("Invalid input: name must not be empty")
        if price < 0 or quantity < 0:
            raise ValueError("Invalid input: price and quantity must be non-negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Get the current quantity of the product.
        Returns:
            int: The available quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Set the quantity of the product and update its active status.
        Args:
            quantity (int): The new quantity of the product.
        """
        self.quantity = quantity
        if quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        """
        Check if the product is active.
        Returns:
            bool: True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activate the product, setting its status to active.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivate the product, setting its status to inactive.
        """
        self.active = False

    def show(self) -> str:
        """
        Display the product's details as a formatted string.
        Returns:
            str: A string representation of the product, including name, price, quantity, and status.
        """
        status = "Active" if self.active else "Inactive"
        return f'"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Status: {status}"'

    def buy(self, quantity) -> float:
        """
        Purchase a specified quantity of the product.
        Args:
            quantity (int): The quantity to purchase. Must be positive and less than or equal to available stock.
        Returns:
            float: The total cost of the purchase.
        Raises:
            ValueError: If quantity is non-positive or exceeds available stock.
        """
        if quantity <= 0:
            raise ValueError("Invalid input: quantity must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock: there is not enough product available.")

        total_price = quantity * self.price
        self.quantity -= quantity
        return total_price
