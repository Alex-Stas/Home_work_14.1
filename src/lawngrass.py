from src.product import Product


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


if __name__ == "__main__":
    # pass

    # Testing data below to be cleared in final release

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    # grass_sum = grass1 + grass2
    # print(grass_sum)

    grass2.price = -25
    grass2.price = 9800
    print(grass2.price)

    grass_dict = {"name": "Газонная трава 3", "description": "Лучшая трава", "price": 1000, "quantity": 5, "country": 'New Zeland', 'germination_period': '4 дня', 'color': 'hobbiton green'}

    grass3 = LawnGrass.new_product(grass_dict)

    print(grass3.name)
    print(grass3.description)
    print(grass3.price)
    print(grass3.quantity)
    print(grass3.country)
    print(grass3.germination_period)
    print(grass3.color)