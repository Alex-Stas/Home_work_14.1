from src.category import Category
from src.product import Product


def test_category_init(first_category, second_category):
    assert first_category.name == "Игровые приставки"
    assert first_category.description == "Игровые приставки от лидеров рынка"
    assert len(first_category.products) == 4


def test_category_counters():

    assert Category.category_count == 2
    assert Category.product_count == 7

    new_product_1 = Product("Nokia 3110", "nothing but phone", 1800.0, 15)
    new_product_2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    new_product_3 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [new_product_1, new_product_2, new_product_3],
    )

    assert Category.category_count == 3
    assert Category.product_count == 10
