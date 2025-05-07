class Store:

    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products

    def add_product(self, product):
        if not hasattr(product, 'name') or not hasattr(product, 'price') or not hasattr(product,
                                                                                        'quantity'):
            raise TypeError("Product must have 'name', 'price', and 'quantity' attributes")
        self.products.append(product)

