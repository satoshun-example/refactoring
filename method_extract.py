#Before

class PriceCalculator(object):
    def __init__(self, unit_price, num):
        self.unit_price = unit_price
        self.num = num

    @property
    def price(self):
        """Returns: total price, total price is
        tanka * num * tax(1.1)
        """
        return int(self.unit_price * self.num * 1.1)

#After

class PriceCalculator2(object):
    def __init__(self, unit_price, num):
        self.unit_price = unit_price
        self.num = num

    @property
    def price(self):
        """Returns: total price, total price is
        tanka * num * tax(1.1)
        """
        return self.add_tax(self.unit_price * self.num)

    def add_tax(self, total):
        """extract"""
        return int(total * 1.1)


if __name__ == '__main__':
    b = PriceCalculator(100, 10)
    b2 = PriceCalculator2(100, 10)

    assert b.price == b2.price
