""" Before

inheritance list class
"""
class NewList(list):
    def increase(self):
        for i in range(len(self)):
            self[i] += 1

    def decrease(self):
        for i in range(len(self)):
            self[i] -= 1


""" After

delegate list class
"""
class ListManipulation(object):
    def __init__(self, iterator):
        self.value = list(iterator)

    def increase(self):
        for i in range(len(self.value)):
            self.value[i] += 1

    def decrease(self):
        for i in range(len(self.value)):
            self.value[i] -= 1

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    ## Before
    print('-' * 10)
    l = NewList([1, 2, 3])
    print(l)
    l.increase()
    print(l)
    l.decrease()
    print(l)
    print('-' * 10)

    l2 = ListManipulation([1, 2, 3])
    print(l2)
    l2.increase()
    print(l2)
    l2.decrease()
    print(l2)
    print('-' * 10)
