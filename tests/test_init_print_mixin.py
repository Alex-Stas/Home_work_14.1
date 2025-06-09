from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


def test_init_print_mixin_task(capsys):

    Product("Nokia 7730", "Best phone ever", 9800, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Nokia 7730, Best phone ever, 9800, 5)"

    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
