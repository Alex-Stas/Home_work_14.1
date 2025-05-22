def test_category_init(first_category, second_category):
    assert first_category.name == "Игровые приставки"
    assert first_category.description == "Игровые приставки от лидеров рынка"
    assert len(first_category.products) == 4

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 7
    assert second_category.product_count == 7
