from color import Color as c


def get_order_product(product_list):
    while True:
        product_number = (
            input(c.white + "Which product # do you want? "))
        if not product_number:
            return product_number
        if not product_number.isdigit():
            print(c.red + "Error. Please enter a whole number" + c.reset)
            continue
        product_number = int(product_number)
        if 0 < product_number <= len(product_list):
            return product_number
        print(c.red + f"Error. Please enter a number between 1 - {len(product_list)}" + c.reset)


def get_order_quantity():
    while True:
        product_quantity = (
            input(c.white + "what amount do you want? "))
        if not product_quantity:
            return product_quantity
        if not product_quantity.isdigit():
            print(c.red + "Error. Please enter a whole number" + c.reset)
            continue
        return int(product_quantity)
