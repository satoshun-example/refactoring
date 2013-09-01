## Before

"""
    Customer
        |
     -------
    |       |
   Shop - Product
"""

class Customer(object):
    """ depend Shop, Product class"""
    def __init__(self, shop, product):
        self.__shop = shop
        self.__product = product

    def get_shop(self):
        return self.__shop

    def get_product(self):
        return self.__product


class Shop(object):
    def __init__(self, product=None):
        self.__product = product

    def get_product(self):
        return self.__product

    def set_product(self, product):
        self.__product = product


class Product(object):
    def __init__(self, shop=None):
        self.__shop = shop

    def get_shop(self):
        return self.__shop

    def set_shop(self, shop):
        self.__shop = shop


## After
"""
    Customer2
        |
      Shop2
        |
     Product2
"""

class Customer2(object):
    """ depend Shop class"""
    def __init__(self, shop):
        self.__shop = shop

    def get_shop(self):
        return self.__shop


class Shop2(object):
    def __init__(self, product=None):
        self.__product = product

    def get_product(self):
        return self.__product

    def set_product(self, product):
        self.__product = product


class Product2(object):
    pass


if __name__ == '__main__':
    ##Before
    shop = Shop()
    product = Product(shop)
    shop.set_product(product)

    customer = Customer(shop, product)
    print(customer.get_shop())
    print(customer.get_product())

    ##After
    product2 = Product2()
    shop2 = Shop2(product2)
    customer2 = Customer2(shop2)
    print(customer2.get_shop())
    print(customer2.get_shop().get_product())
