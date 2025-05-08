import products
from store import Store
from colorama import Fore, init

init()
prompt = (f"{Fore.LIGHTYELLOW_EX }|{Fore.LIGHTWHITE_EX } 1. List all products in store  {Fore.LIGHTYELLOW_EX }|\n"
          f"|{Fore.LIGHTWHITE_EX } 2. Show total amount in store  {Fore.LIGHTYELLOW_EX }|\n"
          f"|{Fore.LIGHTWHITE_EX } 3. Make an order               {Fore.LIGHTYELLOW_EX }|\n"
          f"|{Fore.LIGHTWHITE_EX } 4. Quit                        {Fore.LIGHTYELLOW_EX }|")


def start(store):
    # products = Store.get_all_products()
    while True:
        print(Fore.LIGHTYELLOW_EX + "\n", "=" * 32)
        print(prompt)
        print(Fore.LIGHTYELLOW_EX + "", "=" * 32)
        try:
            choice = int(input(Fore.LIGHTMAGENTA_EX + "       Enter your choice: "))
        except ValueError:
            print(Fore.LIGHTRED_EX + "Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            print(Fore.LIGHTCYAN_EX + "Available Products:" )
            print("-" * 58)
            products = store.get_all_products()
            for i, product in enumerate(products, start=1):
                print(f"{Fore.LIGHTWHITE_EX }{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
            print(Fore.LIGHTCYAN_EX + "-" * 58)
            input(Fore.LIGHTGREEN_EX + " <<   Press Enter to continue  >>")

        elif choice == 2:
            total_amount = store.get_total_quantity()
            print(Fore.LIGHTCYAN_EX + "-" * 58)
            print(f"{Fore.LIGHTWHITE_EX}>>> Total of {Fore.LIGHTGREEN_EX}{total_amount}{Fore.LIGHTWHITE_EX} items in store!")
            print(Fore.LIGHTCYAN_EX + "-" * 58)
            input(Fore.LIGHTGREEN_EX + " <<   Press Enter to continue  >>")

        elif choice == 3:
            shopping_list = []
            print(Fore.LIGHTCYAN_EX + "Available Products:")
            print("-" * 58)
            products = store.get_all_products()
            for i, product in enumerate(products, start=1):
                print(
                    f"{Fore.LIGHTWHITE_EX}{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
            print(Fore.LIGHTCYAN_EX + "-" * 58)
            print(Fore.LIGHTGREEN_EX + " \n<<  When you want to finish order, enter -> '0'. >>")

            while True:
                try:
                    product_index = int(input("Which product # do you want? ")) - 1
                    if product_index == -1:
                        break
                    quantity = int(input("What amount do you want? "))

                    product = store.products[product_index]

                    shopping_list.append((product, quantity))
                    print(Fore.LIGHTCYAN_EX + "-" * 58)
                    print("Product added to list!")
                except (ValueError, IndexError):
                    print(Fore.LIGHTRED_EX + "Invalid input. Please try again.")

            try:
                total_price = store.order(shopping_list)
                print("-" * 58)
                print(f"{Fore.LIGHTWHITE_EX}Order made! Total payment: ${Fore.LIGHTMAGENTA_EX}{total_price}")
                print("-" * 58)
                print(Fore.LIGHTCYAN_EX + "Available Products:")
                print("-" * 58)
                products = store.get_all_products()
                for i, product in enumerate(products, start=1):
                    print(
                        f"{Fore.LIGHTWHITE_EX}{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
                print(Fore.LIGHTCYAN_EX + "-" * 58)

            except Exception as e:
                print(f"Order failed: {e}")


        elif choice == 4:
            print(" <<   The program is finish!   >>")
            exit()

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = Store(product_list)
start(best_buy)
