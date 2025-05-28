class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_with_arg):
        return cls(**dict_with_arg)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price < 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price


if __name__ == "__main__":
    pass

    # product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    #
    # print(product.name)
    # print(product.description)
    # print(product.price)
    # print(product.quantity)
    #
    # product_dict = {"name": "Nokia 7730", "description": "Best phone ever", "price": 10000, "quantity": 5}
    #
    # product2 = Product.new_product(**product_dict)
    #
    # print(product2.name)
    # print(product2.description)
    # print(product2.price)
    # print(product2.quantity)
    #
    # product2.price = -25
    # product2.price = 9800
    # print(product2.price)
