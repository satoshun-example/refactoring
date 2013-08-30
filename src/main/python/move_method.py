## Before

class Product(object):
    __slots__ = ['unit', 'num']

    def __init__(self, unit, num):
        self.unit = unit
        self.num = num


class Delivery(object):
    __slots__ = ['products']

    def __init__(self, *products):
        self.products = products

    def price(self, product):
        return product.unit * product.num * 1.10

    @property
    def total_price(self):
        total = 0
        for product in self.products:
            total += self.price(product)
        return int(total)


## After
## Move method

class Product2(object):
    __slots__ = ['__unit', '__num']

    def __init__(self, unit, num):
        self.__unit = unit
        self.__num = num

    def price(self):
        """move price method"""
        return self.__unit * self.__num * 1.10


class Delivery2(object):
    __slots__ = ['products']

    def __init__(self, *products):
        self.products = products

    @property
    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price()
        return int(total)


if __name__ == '__main__':
    delivery = Delivery(
        Product(100, 10),
        Product(10, 20))
    delivery2 = Delivery2(
        Product2(100, 10),
        Product2(10, 20))
    assert delivery.total_price == delivery2.total_price
