class Product:
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price, quantity_in_stock=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock


if __name__ == "__main__":
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity_in_stock)
