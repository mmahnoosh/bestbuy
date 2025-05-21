from typing import List

from products import Product
from color import Color as c

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

        self.products.append(product)

    def remove_product(self, product):
        """
        Remove a product from the store inventory.
        Args:
            product (Product): The product to remove.
        Raises:
            ValueError: If the product is not found in the store.
        """
        try:
            self.products.remove(product)
        except ValueError:
            print(f"Product {product} not found in the store.")

    def get_total_quantity(self) -> int:
        """
            Calculate the total quantity of all products in the store.
            Returns:
                int: The total quantity of all products in the store.
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
            if product.is_active():
                activ_products.append(product)
        return activ_products


    def order(self, shopping_list):
        """
           Process a new order based on a shopping list.
            Args:
                shopping_list (List[tuple[Product, int]]): A list of product-quantity pairs.
            Returns:
                float: The total price of the order.
            Raises:
                    TypeError: If the shopping list contains invalid data.
                    ValueError: If the requested quantity is not available.
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
            try:
                total_price += product.buy(quantity)
            except ValueError as error:
                return f"Error while making order: {error}"

        return f"{c.white}Total order price:{c.cyan} {total_price}{c.white}."



