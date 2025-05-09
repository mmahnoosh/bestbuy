from typing import List

from colorama import Fore

from products import Product


class Store:
    """
        A class to represent a store that manages products and processes orders.
        Attributes:
            products (List[Product]): A list of Product instances available in the store.
    """

    def __init__(self, products=None):
        """
        Initialize the Store with a list of products.
        Args:
            products (List[Product], optional): A list of products to initialize the store. Defaults to an empty list.
        Raises:
            TypeError: If the provided products are not in a list.
        """
        if not isinstance(products, list):
            raise TypeError("Expected a list of product!")
        if products is None:
            products = []
        self.products = products

    def add_product(self, product):
        """
        Add a product to the store inventory.
        Args:
            product (Product): The product to add.
        Raises:
            TypeError: If the provided product is not an instance of Product.
        """
        if not isinstance(product, Product):
            raise TypeError("Expected instance of product!")
        # if not hasattr(product, 'name') or not hasattr(product, 'price') or not hasattr(product,'quantity'):
        # raise TypeError("Product must have 'name', 'price', and 'quantity' attributes")
        self.products.append(product)

    def remove_product(self, product):
        """
        Remove a product from the store inventory.
        Args:
            product (Product): The product to remove.
        Prints:
            Error message if the product is not found in the store.
        """
        try:
            self.products.remove(product)
        except ValueError:
            print(f"Product {product} not found in the store.")

    def get_total_quantity(self) -> int:
        """
            Calculate the total quantity of all products in the store.
            Returns:
                int: The total quantity of all products.
            """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self) -> List[Product]:
        """
        Retrieve a list of all active products in the store.
        Returns:
                List[Product]: A list of active products.
        """
        activ_products = []
        for product in self.products:
            if product.active:
                activ_products.append(product)
        return activ_products

    def order(self, shopping_list) -> float:
        """
            Processes an order based on a list of (Product, quantity) tuples.

            Args:
                shopping_list (list of tuples): A list where each tuple contains
                                                a Product instance and the desired quantity.

            Returns:
                float: The total cost of the order.

            This method checks for input validity, ensures that the requested quantity is available,
            updates the product stock accordingly, and calculates the total order cost.
            """
        total_price = 0
        for item in shopping_list:
            if not isinstance(item, tuple) or len(item) != 2:
                raise TypeError("Expected a tuple of (Product, quantity)!")

            product, quantity = item
            if not isinstance(product, Product):
                raise TypeError("First element of tuple must be an instance of Product!")
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError("Quantity must be a positive integer!")
            if product.quantity < quantity:
                raise ValueError(
                    f"{Fore.LIGHTRED_EX}Error while making order! {Fore.LIGHTYELLOW_EX}Quantity larger than what exists."
                    f"{Fore.LIGHTWHITE_EX} Available: {Fore.LIGHTGREEN_EX}{product.quantity}, "
                    f"{Fore.LIGHTYELLOW_EX}Requested: {Fore.LIGHTRED_EX}{quantity}")

            total_price += product.price * quantity
            product.quantity -= quantity

        return total_price
