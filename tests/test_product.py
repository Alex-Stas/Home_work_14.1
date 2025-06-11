from src.product import Product
import pytest


def test_product_init(product):

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_create():
    product_dict = {"name": "Nokia 7730", "description": "Best phone ever", "price": 10000, "quantity": 5}
    product2 = Product.new_product(product_dict)
    assert product2.name == "Nokia 7730"
    assert product2.description == "Best phone ever"
    assert product2.price == 10000
    assert product2.quantity == 5


def test_price_update(capsys, product):
    assert product.price == 180000
    product.price = -1
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    product.price = 9800
    assert product.price == 9800


def test_product_str(product):
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product, product2):
    assert product + product2 == 949000


def test_init_product_zero_quantity():
    with pytest.raises(ValueError) as exc_info:
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)
        assert exc_info == "Товар с нулевым количеством не может быть добавлен"
