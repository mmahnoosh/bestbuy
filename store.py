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
            if product.active:
                activ_products.append(product)
        return activ_products


    def get_shopping_list(self):

        shopping_list = []
        print(Fore.LIGHTGREEN_EX + " \n<<  When you want to finish order, enter -> '0'. >>")
        while True:
            try:
                product_index = int(
                    input(Fore.LIGHTWHITE_EX + "Which product # do you want? ")) - 1
                if product_index == -1:
                    break

                product = self.products[product_index]
                if not product.is_active():
                    print(Fore.LIGHTRED_EX + "This product is inactive and cannot be ordered.")
                    continue
                quantity = int(input(Fore.LIGHTWHITE_EX + "What amount do you want? "))
                if not isinstance(quantity, int) or quantity < 1:
                    raise ValueError("Quantity must be a positive integer!")
                if product.quantity < quantity:
                    raise ValueError(
                        f"{Fore.LIGHTRED_EX}Error while making order! {Fore.LIGHTYELLOW_EX}Quantity larger than what exists."
                        f"{Fore.LIGHTWHITE_EX} Available: {Fore.LIGHTGREEN_EX}{product.quantity}, "
                        f"{Fore.LIGHTYELLOW_EX}Requested: {Fore.LIGHTRED_EX}{quantity}")
                print(Fore.LIGHTCYAN_EX + "-" * 58)
                shopping_list.append((product, quantity))

            except (ValueError, IndexError):
                print(Fore.LIGHTRED_EX + "Invalid input. Please try again.")

        return shopping_list

    def order(self,  shopping_list):
        total_price = 0
        for item in shopping_list:
            product, quantity = item
            total_price += product.price * quantity
            product.quantity -= quantity

        return total_price

    def display_products(self, items):
        print(Fore.LIGHTCYAN_EX + "Available Products:")
        print("-" * 58)
        for i, product in enumerate(items, start=1):
            print(
                f"{Fore.LIGHTWHITE_EX}{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
        print(Fore.LIGHTCYAN_EX + "-" * 58)
