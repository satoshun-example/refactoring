## Before
def calculate_price(price, num, tax):
    base = price * 10
    total = base * num * tax
    discount_value = 0.9

    discount = False
    if total >= 1000:
        discount = True

    if discount:
        total = total * discount_value
    return int(total)

## After

class CaluculatePrice(object):
    __discount_value = 0.9

    def __init__(self, price, num, tax):
        self.__price = price
        self.__num = num
        self.__tax = tax

    def compute(self):
        if self.__is_discount():
            return self.__total() * self.__discount_value
        return self.__total()

    def __is_discount(self):
        return self.__total() >= 1000

    def __total(self):
        return self.__base_price() * self.__num * self.__tax
    
    def __base_price(self):
        return self.__price * 10

if __name__ == '__main__':
    c = CaluculatePrice(100, 10, 1.1)
    assert c.compute() == calculate_price(100, 10, 1.1)

    c1 = CaluculatePrice(3, 20, 1.5)
    assert c1.compute() == calculate_price(3, 20, 1.5)
