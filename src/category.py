from src.product import Product

from src.smartphone import Smartphone


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        products_out_str = ""
        for product in self.__products:
            products_out_str += f"{str(product)}\n"
        return products_out_str

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Переданный объект не является объектом или наследником класса Product")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_in_list(self):
        return self.__products

    def middle_price(self):
        try:
            return sum([product.price for product in self.products_in_list]) / len(self.products_in_list)
        except ZeroDivisionError:
            return 0


if __name__ == "__main__":
    # pass
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category.name)
    print(category.description)
    print(category.products)

    product4 = Product("Nokia 3310", "Just a phone", 5000, 20)

    category.add_product(product4)

    print(category.products)
    print(category.category_count)
    print(category.product_count)

    print(category)

    product5 = Smartphone("Nokia 3310", "Just a phone", 5000, 50, 90.3, "Note 11", 1024, "Синий")

    category.add_product(product5)

    print(category.products)
    print(category.category_count)
    print(category.product_count)

    print(category)

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 10000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 20000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 15000.0, 14)

    category3 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")

    print()
    print(category3.average_price_product())


