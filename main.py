from typing import Any

from colorama import Fore

import products
from store import Store


def display_message(message: str, color: Any = Fore.LIGHTWHITE_EX) -> None:
    print(color + message + Fore.RESET)


def display_menu() -> None:
    menu = [
        "   1. Display all products",
        "   2. Display total quantity",
        "   3. Make an order",
        "   4. Exit"
    ]
    display_message("\n      <<   Store Menu   >>", Fore.LIGHTMAGENTA_EX)
    display_message("=" * 32, Fore.LIGHTYELLOW_EX)
    for item in menu:
        display_message(item, Fore.LIGHTWHITE_EX)
    display_message("=" * 32, Fore.LIGHTYELLOW_EX)


def start(store: Any) -> None:
    """
    Start the interactive store management application.

    Args:
        store (Store): An instance of the Store class containing available products.
    """
    menu_actions = {
        1: lambda: store.display_products(store.get_all_products()),
        2: lambda: display_total_quantity(store),
        3: lambda: make_order(store),
        4: exit_program
    }

    while True:
        display_menu()
        try:
            choice = int(input(Fore.LIGHTMAGENTA_EX + "       Enter your choice: "))
            action = menu_actions.get(choice)
            if action:
                action()
            else:
                display_message("Invalid choice. Please enter a number between 1 and 4.",
                                Fore.LIGHTRED_EX)
        except ValueError:
            display_message("Invalid input. Please enter a number.", Fore.LIGHTRED_EX)


def display_total_quantity(store: Any) -> None:
    store.display_products(store.get_all_products())
    total_amount = store.get_total_quantity()
    display_message("-" * 58, Fore.LIGHTCYAN_EX)
    display_message(
        f"Total of {Fore.LIGHTCYAN_EX}{total_amount}{Fore.LIGHTWHITE_EX} items in store!",
        Fore.LIGHTWHITE_EX)
    display_message("-" * 58, Fore.LIGHTCYAN_EX)
    input(Fore.LIGHTGREEN_EX + " <<   Press Enter to continue  >>")


def make_order(store: Any) -> None:
    store.display_products(store.get_all_products())
    new_shopping_list = store.new_shopping_list()
    try:
        total_price = store.new_order(new_shopping_list)
    except ValueError as e:
        display_message(str(e), Fore.LIGHTRED_EX)
        return
    #total_price = store.new_order(new_shopping_list)
    display_message("-" * 58)
    display_message(f"Order made! Total payment: ${total_price}", Fore.LIGHTMAGENTA_EX)
    display_message("-" * 58, Fore.LIGHTCYAN_EX)
    store.display_products(store.get_all_products())


def exit_program() -> None:
    display_message("-" * 35, Fore.LIGHTBLUE_EX)
    display_message(" <<   The program is finished!   >>", Fore.LIGHTBLUE_EX)
    exit()


def main():
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()