from models.product import Product


for product in Product.load_product():
    print(product.name)