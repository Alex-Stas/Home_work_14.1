from src.product import Product


class Category:
    name: str
    description: str
    products_list: list
    category_count = 0
    all_products_count = 0

    def __init__(self, name, description, products_list=None):
        self.name = name
        self.description = description
        self.products_list = products_list if products_list else []
        Category.category_count += 1
        Category.all_products_count += len(products_list) if products_list else 0


if __name__ == "__main__":

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
    print(category.products_list)

    print(category.category_count)
    print(category.all_products_count)
