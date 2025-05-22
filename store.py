from typing import List

from color import Color as c
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
        for product in products:
            if not isinstance(product, Product):
                raise TypeError("All elements of the list need to be a Product class object!")
        self.products = products

    def add_product(self, product):
        """
        Adds a new product to the store inventory.
        Checks for type correctness and ensures the product does not already exist
            based on its name.
        Args:
            product (Product): The product to be added to the store.

        Raises:
            TypeError: If the provided object is not an instance of Product.
            ValueError: If a product with the same name already exists in the store.
        """
        if not isinstance(product, Product):
            raise TypeError("Expected instance of product!")
        for store_product in self.products:
            if store_product.name == product.name:
                raise ValueError("Product already exists in the store!")
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store inventory.

        The product is identified by its name. If no matching product is found,
        an error is raised.

        Args:
            product (Product): The product to remove.

         Raises:
            ValueError: If the product is not found in the store inventory.
        """
        for store_product in self.products:
            if store_product.name == product.name:
                self.products.remove(store_product)
        raise ValueError("Product does not exist in the store!")

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
            Processes a new order based on a list of product-quantity pairs.
        Args:
            shopping_list (List[tuple[Product, int]]):
            A list where each element is a tuple containing a Product instance
            and the quantity to be purchased.

        Returns:
            str: A formatted string indicating the total price of the order,
             or an error message if the order fails.

        Raises:
        TypeError: If an item in the shopping list is not a (Product, int) tuple.
        ValueError: If the quantity is not a positive integer or if the requested
                    quantity is unavailable.
        """
        total_price = 0
        order_list = []

        for item in shopping_list:
            if not isinstance(item, tuple) or len(item) != 2:
                raise TypeError("Expected a tuple of (Product, quantity)!")
            product, quantity = item
            # Add product and quantity before the purchase to get original quantity
            order_list.append((product, product.get_quantity()))

            if not isinstance(product, Product):
                raise TypeError("First element of tuple must be an instance of Product!")
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError("Quantity must be a positive integer!")
            try:
                total_price += product.buy(quantity)
            except ValueError as error:
                restored_products = []
                for product, quantity in order_list[:-1]:
                    # Ensures only the quantity before the first purchase is restored
                    if product not in restored_products:
                        # Resets quantity to before the first purchase of the particular product
                        product.set_quantity(quantity)
                        restored_products.append(product)
                return f"Error while making order: {error}"

        return f"{c.white}Total order price:{c.cyan} {total_price}{c.white}."
