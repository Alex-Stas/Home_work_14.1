import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_category():
    return Category(
        name="Игровые приставки",
        description="Игровые приставки от лидеров рынка",
        products=[
            Product("XBox - 1", "Классическая игровая приставка, 8 Gb памяти", 24000, 2),
            Product("XBox - 3", "Новейшая игровая приставка, 32 Gb памяти", 64000, 20),
            Product("Playstation 3", "Еще актуальная, 16 Gb памяти, интернет-магазин приложений", 35000, 4),
            Product("Playstation 5", "Новая версия игровой приставки, 64 Gb памяти, 1 Tb жесткий диско", 92000, 8),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description="Телевизоры любых размеров и категорий",
        products=[
            Product("Sony Trinitron 29 дюймов", "Нестареющая классика для гаража", 5000, 1),
            Product(
                "Samsung Super Flat 109 дюймов",
                "Огромный экран, идеальные цвета, встроенный комплекс мультимедиа",
                164000,
                20,
            ),
            Product("LG Axel 49 дюймов", "Доступный телевизор для всех", 35000, 4),
        ],
    )


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
