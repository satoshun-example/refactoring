## before

class BookStore(object):
    book_price = 100

    def __init__(self, num):
        self.num = num

    @property
    def price(self):
        """if price * num >= 1000 service price"""
        rate = 1.0
        base_price = self.num * self.__class__.book_price

        if base_price >= 1000:
            rate = 0.9
        return base_price * rate

## after

class BookStore2(object):
    book_price = 100

    def __init__(self, num):
        self.num = num

    @property
    def price(self):
        """if price * num >= 1000 service price"""
        rate = 1.0
        if self._base_price() >= 1000:
            rate = 0.9
        return self._base_price() * rate

    def _base_price(self):
        return self.num * self.__class__.book_price
        
## after2

class BookStore3(object):
    book_price = 100

    def __init__(self, num):
        self.num = num

    @property
    def price(self):
        """if price * num >= 1000 service price"""
        return self._base_price() * self._rate()

    def _rate(self):
        if self._base_price() >= 1000:
            return 0.9
        return 1.0

    def _base_price(self):
        return self.num * self.__class__.book_price


if __name__ == '__main__':
    b = BookStore(10)
    b2 = BookStore2(10)
    b3 = BookStore3(10)

    assert b.price == b2.price == b3.price
