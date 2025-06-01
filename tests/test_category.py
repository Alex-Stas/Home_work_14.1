from src.category import Category
from src.product import Product


def test_category_init(first_category, second_category):
    assert first_category.name == "Игровые приставки"
    assert first_category.description == "Игровые приставки от лидеров рынка"
    assert len(first_category.products_in_list) == 4


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


def test_products_property(second_category):
    assert second_category.products == (
        "Sony Trinitron 29 дюймов, 5000 руб. Остаток: 1 шт.\n"
        "Samsung Super Flat 109 дюймов, 164000 руб. Остаток: 20 шт.\n"
        "LG Axel 49 дюймов, 35000 руб. Остаток: 4 шт.\n"
    )


def test_category_add_product_setter(second_category, product):
    assert len(second_category.products_in_list) == 3
    second_category.add_product(product)
    assert len(second_category.products_in_list) == 4


def test_category_add_product_incorrect_data(capsys, first_category):
    first_category.add_product("product")
    message = capsys.readouterr()
    assert message.out.strip() == "Переданный объект не является объектом класса Product"


def test_category_str(second_category):
    assert str(second_category) == "Телевизоры, количество продуктов: 25 шт."
