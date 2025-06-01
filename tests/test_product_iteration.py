import pytest

def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "XBox - 1"
    assert next(product_iterator).name == "XBox - 3"
    assert next(product_iterator).name == "Playstation 3"
    assert next(product_iterator).name == "Playstation 5"
    with pytest.raises(StopIteration):
        next(product_iterator)
    iter(product_iterator)
    assert next(product_iterator).name == "XBox - 1"