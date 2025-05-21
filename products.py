class Product:
    """
    A class to represent a product with a name, price, quantity, and activation status.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The available quantity of the product.
        active (bool): The activation status of the product.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a new product instance.
        Args:
            name (str): The name of the product.
            price (float): The price of the product. Must be non-negative.
            quantity (int): The quantity of the product. Must be non-negative.
        Raises:
            ValueError: If the name is empty or if price/quantity is negative.
        """
        if not name:
            raise ValueError("Invalid input: name must not be empty")
        if price < 0 or quantity < 0:
            raise ValueError("Invalid input: price and quantity must be non-negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

    def get_quantity(self) -> int:
        """
        Get the current quantity of the product.

        Returns:
            int: The available quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Update the quantity of the product and adjust its active status accordingly.
        Args:
            quantity (int): The new quantity of the product. Must be a non-negative integer.
        Raises:
            ValueError: If the quantity is not a non-negative integer.
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()
        elif not self.active:
            self.activate()

    def is_active(self) -> bool:
        """
        Check if the product is currently active.
        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Set the product's status to active.
        Note:
            The product can only be activated if the quantity is greater than zero.
        """
        if self.quantity > 0:
            self.active = True

    def deactivate(self):
        """
        Set the product's status to inactive.
        Note:
            Deactivation occurs when the product quantity reaches zero.
        """
        self.active = False

    def show(self) -> str:
        """
        Generate a formatted string representing the product's details.
        Returns:
            str: A formatted string including the product's name, price, quantity, and status.
        """
        if self.is_active():
            return f'"{self.name}, Price: {self.price}, Quantity: {self.quantity}"'
        return ""

    def buy(self, quantity):
        if not self.is_active():
            raise ValueError("Product inactive!")
        if self.get_quantity() < quantity:
            raise ValueError("Quantity larger then what exists!")
        self.set_quantity(self.get_quantity() - quantity)
        return quantity * self.price
