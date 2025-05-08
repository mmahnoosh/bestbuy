from typing import List
from colorama import Fore
from products import Product


class Store:

    def __init__(self, products=None):
        if not isinstance(products, list):
            raise TypeError("Expected a list of product!")
        if products is None:
            products = []
        self.products = products

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Expected instance of product!")
        # if not hasattr(product, 'name') or not hasattr(product, 'price') or not hasattr(product,'quantity'):
        # raise TypeError("Product must have 'name', 'price', and 'quantity' attributes")
        self.products.append(product)

    def remove_product(self, product):
        try:
            self.products.remove(product)
        except ValueError:
            print(f"Product {product} not found in the store.")

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self) -> List[Product]:
        activ_products = []
        for product in self.products:
            if product.active:
                activ_products.append(product)
        return activ_products

    """def show_all(self):

        for product in self.products:
            print(f'"{product.name}, Price: {product.price}, Quantity: {product.quantity}"')
        #return f'"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Status: {status}"'
"""

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
                    f"{Fore.LIGHTRED_EX}Not enough stock for {product.name}.{Fore.LIGHTWHITE_EX} Available: {product.quantity}, "
                    f"{Fore.LIGHTRED_EX}Requested: {quantity}")

            total_price += product.price * quantity
            product.quantity -= quantity

        return total_price
