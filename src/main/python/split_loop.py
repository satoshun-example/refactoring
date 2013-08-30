class Product(object):
    __slots__ = ['__name', '__price', '__size']

    def __init__(self, name, price, size):
        self.__name = name
        self.__price = price
        self.__size = size

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size


#Before
class SuperMarket(object):
    __slots__ = ['products']

    def __init__(self, *products):
        self.products = products

    def product_summary(self):
        d = {'total': 0, 'product_names': [], 'size': 0}

        for product in self.products:
            d['total'] += product.price
            d['product_names'].append(product.name)
            d['size'] += product.size
        return d

#After
class SuperMarket2(object):
    __slots__ = ['products']

    def __init__(self, *products):
        self.products = products

    def product_summary(self):
        d = {'total': 0, 'product_names': [], 'size': 0}

        for product in self.products:
            d['total'] += product.price
    
        for product in self.products:
            d['product_names'].append(product.name)

        for product in self.products:
            d['size'] += product.size

        return d


if __name__ == '__main__':
    s = SuperMarket(Product('meat', 100, 5),
        Product('vegitable', 300, 10),
        Product('deodorant', 500, 3))

    s2 = SuperMarket2(Product('meat', 100, 5),
        Product('vegitable', 300, 10),
        Product('deodorant', 500, 3))
    assert s.product_summary() == s2.product_summary()
