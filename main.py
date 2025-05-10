from colorama import Fore, init

import products
from store import Store

init()
prompt = (
    f"{Fore.LIGHTYELLOW_EX}|{Fore.LIGHTWHITE_EX} 1. List all products in store  {Fore.LIGHTYELLOW_EX}|\n"
    f"|{Fore.LIGHTWHITE_EX} 2. Show total amount in store  {Fore.LIGHTYELLOW_EX}|\n"
    f"|{Fore.LIGHTWHITE_EX} 3. Make an order               {Fore.LIGHTYELLOW_EX}|\n"
    f"|{Fore.LIGHTWHITE_EX} 4. Quit                        {Fore.LIGHTYELLOW_EX}|")


def start(store):
    """
        Start the interactive store management application.

        Args:
            store (Store): An instance of the Store class containing available products.
        """
    while True:
        print(Fore.LIGHTMAGENTA_EX + "\n      <<   Store Menu   >>")
        print(Fore.LIGHTYELLOW_EX + "", "=" * 32)
        print(prompt)
        print(Fore.LIGHTYELLOW_EX + "", "=" * 32)
        try:
            choice = int(input(Fore.LIGHTMAGENTA_EX + "       Enter your choice: "))
        except ValueError:
            print(Fore.LIGHTRED_EX + "Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            items = store.get_all_products()
            store.display_products(items)
            input(Fore.LIGHTGREEN_EX + " <<   Press Enter to continue  >>")

        elif choice == 2:
            total_amount = store.get_total_quantity()
            print(Fore.LIGHTCYAN_EX + "-" * 58)
            print(
                f"{Fore.LIGHTWHITE_EX}>>> Total of {Fore.LIGHTGREEN_EX}{total_amount}{Fore.LIGHTWHITE_EX} items in store!")
            print(Fore.LIGHTCYAN_EX + "-" * 58)
            input(Fore.LIGHTGREEN_EX + " <<   Press Enter to continue  >>")

        elif choice == 3:
            print(store.get_shoping_list())
            #store.order(shoping_list)
            continue
            """shopping_list = []
            items = store.get_all_products()
            display_products(items)
            print(Fore.LIGHTGREEN_EX + " \n<<  When you want to finish order, enter -> '0'. >>")
"""
            while True:
                try:
                    product_index = int(
                        input(Fore.LIGHTWHITE_EX + "Which product # do you want? ")) - 1
                    if product_index == -1:
                        break
                    product = store.products[product_index]

                    if not product.is_active():
                        print(Fore.LIGHTRED_EX + "This product is inactive and cannot be ordered.")
                        continue

                    quantity = int(input(Fore.LIGHTWHITE_EX + "What amount do you want? "))
                    print(Fore.LIGHTCYAN_EX + "-" * 58)
                    shopping_list.append((product, quantity))

                except (ValueError, IndexError):
                    print(Fore.LIGHTRED_EX + "Invalid input. Please try again.")

            try:
                total_price = store.order(shopping_list)
                print("-" * 58)
                print(
                    f"{Fore.LIGHTWHITE_EX}Order made! Total payment: ${Fore.LIGHTMAGENTA_EX}{total_price}")
                print()
                print(Fore.LIGHTCYAN_EX + "-" * 58)
                display_products(items)
            except Exception as e:
                print(f"{Fore.RED}Order failed: {e}")

        elif choice == 4:
            print(Fore.LIGHTBLUE_EX+ "-" * 35)
            print(Fore.LIGHTBLUE_EX + " <<   The program is finish!   >>")
            exit()

        else:
            print(Fore.LIGHTRED_EX + "Invalid choice. Please enter a number between 1 and 4.")

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