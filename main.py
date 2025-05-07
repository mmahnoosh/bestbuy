import products
import store
from store import Store


bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)

# instance of a store
best_buy = Store([bose, mac])

pixel = products.Product("Google Pixel 7", price=500, quantity=250)
best_buy.add_product(pixel)
print (best_buy.show_all())