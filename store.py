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

    def order_alt(self, shopping_list) -> float:

        total_price = 0
        for item in shopping_list:
            if not isinstance(item, tuple) or len(item) != 2:
                raise TypeError("Expected a tuple of (Product, quantity)!")

            product, quantity = item
            if not isinstance(product, Product):
                raise TypeError("First element of tuple must be an instance of Product!")
            """if not isinstance(quantity, int) or quantity < 1:
                raise ValueError("Quantity must be a positive integer!")
            if product.quantity < quantity:
                raise ValueError(
                    f"{Fore.LIGHTRED_EX}Error while making order! {Fore.LIGHTYELLOW_EX}Quantity larger than what exists."
                    f"{Fore.LIGHTWHITE_EX} Available: {Fore.LIGHTGREEN_EX}{product.quantity}, "
                    f"{Fore.LIGHTYELLOW_EX}Requested: {Fore.LIGHTRED_EX}{quantity}")

            if not product.is_active():
                raise ValueError(f"Product '{product.name}' is inactive and cannot be ordered.")"""

            total_price += product.price * quantity
            product.quantity -= quantity

            if product.quantity == 0:
                product.deactivate()
            print("add item in order ----------")
        return total_price

    def get_shoping_list(self):
        self.display_products(self.get_all_products())

        shoping_list = []
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
                shoping_list.append((product, quantity))

            except (ValueError, IndexError):
                print(Fore.LIGHTRED_EX + "Invalid input. Please try again.")

        return shoping_list

    def order(self,  shoping_list):
        total_price = 0
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

        for item in shopping_list:
            if not isinstance(item, tuple) or len(item) != 2:
                raise TypeError("Expected a tuple of (Product, quantity)!")
                product, quantity = item
                total_price += product.price * quantity
                product.quantity -= quantity
            print("-" * 58)
            print(
                f"{Fore.LIGHTWHITE_EX}Order made! Total payment: ${Fore.LIGHTMAGENTA_EX}{total_price}")
            print()
            print(Fore.LIGHTCYAN_EX + "-" * 58)
            self.display_products(self.get_all_products())
        return total_price

    def display_products(self, items):
        print(Fore.LIGHTCYAN_EX + "Available Products:")
        print("-" * 58)
        for i, product in enumerate(items, start=1):
            print(
                f"{Fore.LIGHTWHITE_EX}{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
        print(Fore.LIGHTCYAN_EX + "-" * 58)
