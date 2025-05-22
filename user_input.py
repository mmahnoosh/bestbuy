from color import Color as C


def get_order_product(product_list):
    """
    Prompts the user to select a product by its number from the product list.

    The function continuously asks the user for input until a valid product
    number is entered or the input is empty (to cancel the selection).

    Args:
        product_list (List): A list of available products.

    Returns:
        Optional[int or str]: The selected product number as an integer (1-based index),
                              or an empty string if the user cancels by pressing Enter.

    """
    while True:
        product_number = (
            input(C.white + "Which product # do you want? "))
        if not product_number:
            return product_number
        if not product_number.isdigit():
            print(C.red + "Error. Please enter a whole number" + C.reset)
            continue
        product_number = int(product_number)
        if 0 < product_number <= len(product_list):
            return product_number
        print(C.red + f"Error. Please enter a number between 1 - {len(product_list)}" + C.reset)


def get_order_quantity():
    """
        Prompts the user to enter the desired quantity of a product.

        The function repeatedly asks for input until a valid whole number is entered
        or the input is empty (to cancel the operation).

        Returns:
            Optional[int or str]: The entered quantity as an integer,
                                  or an empty string if the user presses Enter to cancel.
    """
    while True:
        product_quantity = (
            input(C.white + "what amount do you want? "))
        if not product_quantity:
            return product_quantity
        if not product_quantity.isdigit():
            print(C.red + "Error. Please enter a whole number" + C.reset)
            continue
        return int(product_quantity)
