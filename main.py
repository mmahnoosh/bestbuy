import products
from color import Color as c
from store import Store
from user_input import get_order_product, get_order_quantity


def display_menu() -> None:
    """
        Display the main menu options to the user.
    """
    menu = [
        "   1. Display all products",
        "   2. Display total quantity",
        "   3. Make an order",
        "   4. Exit"
    ]
    print(c.magenta + "\n      <<   Store Menu   >>")
    print(c.yellow + "=" * 32)
    for item in menu:
        print(c.white + item)
    print(c.yellow + "=" * 32 + c.reset)


def display_products(store):
    """
        Display the list of products with their details.
        Args:
            items (List[Product]): The list of products to display.
    """
    product_list = store.get_all_products()
    print(c.cyan + "Available Products:")
    print("-" * 58)
    for i, product in enumerate(product_list, start=1):
        print(f"{c.white}{i}. {product.show()}")
    print(c.cyan + "-" * 58)


def create_shopping_list(store):
    """
        Collect a shopping list from user input.
        Returns:
            List[tuple[Product, int]]: A list of product-quantity pairs.
    """
    shopping_list = []
    product_list = store.get_all_products()
    print(c.green + " \n<<  When you want to finish order, enter empty text. >>")
    while True:
        product_number = get_order_product(product_list)
        if not product_number:
            break
        quantity = get_order_quantity()
        if not quantity:
            break
        shopping_list.append((product_list[product_number - 1], quantity))
        print(c.magenta + "Product added to list!")
        print(c.cyan + "-" * 58)

    return shopping_list


def display_total_quantity(store) -> None:
    """
        Display the total quantity of items in the store along with all product details.
e
        Args:
            store (Any): An instance of the Store class containing available products.
    """
    total_amount = store.get_total_quantity()
    print(c.cyan + "-" * 58)
    print(f"{c.white} Total of {c.cyan}{total_amount} {c.white}items in store.")
    print(c.cyan + "-" * 58)
    input(c.green + " <<   Press Enter to continue  >>")


def make_order(store) -> None:
    """
        Create a new order and display the total price.

        Args:
            store (Any): An instance of the Store class containing available products.
    """
    display_products(store)
    shopping_list = create_shopping_list(store)
    try:
        print(c.cyan + "-" * 58)
        print(store.order(shopping_list))
        print(c.cyan + "-" * 58)
    except ValueError as e:
        print(c.red + str(e))


def exit_program() -> None:
    """
       Exit the program with a goodbye message.
    """
    print(c.blue + "-" * 35)
    print(c.blue + " <<   The program is finished!   >>")
    exit()


def start(store: Store) -> None:
    """
    Start the interactive store management application.

    Args:
        store (Store): An instance of the Store class containing available products.
    """
    menu_actions = {
        1: lambda: display_products(store),
        2: lambda: display_total_quantity(store),
        3: lambda: make_order(store),
        4: exit_program
    }

    while True:
        display_menu()
        try:
            choice = int(input(c.magenta + "       Enter your choice: "))
            action = menu_actions.get(choice)
            if action:
                action()
            else:
                print(c.red + "Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print(c.red + "Invalid input. Please enter a number.")


def main():
    """
        Initialize the store with initial products and start the application.
    """
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
