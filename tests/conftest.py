import pytest

from src.category import Category
from src.product import Product
from src.product_iteration import ProductIterator
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


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


@pytest.fixture
def product2():
    return Product("Nokia 7730", "Best phone ever", 9800, 5)


@pytest.fixture
def product_iterator(first_category):
    return ProductIterator(first_category)


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawngrass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

@pytest.fixture
def category_without_products():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
