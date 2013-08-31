## Before
class Calculator(object):
    __slots__ = ['__values']

    def __init__(self, *args):
        self.__values = args

    def compute(self):
        total = sum(self.__values)
        if self.is_over_thousand(total):
            total = 1000
        return total

    def is_over_thousand(self, value):
        return value >= 1000

## After
class Calculator2(object):
    """ Method is_over_thousand move in inline code"""
    __slots__ = ['__values']

    def __init__(self, *args):
        self.__values = args

    def compute(self):
        total = sum(self.__values)
        if total >= 1000:
            total = 1000
        return total


if __name__ == '__main__':
    calculator = Calculator(1, 5, -10, 2, 100)
    calculator2 = Calculator2(1, 5, -10, 2, 100)

    assert calculator.compute() == calculator2.compute()
