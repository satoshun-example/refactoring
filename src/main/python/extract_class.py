#Before
class Person(object):
    __slots__ = ['__name', '__age', '__telephone']

    def __init__(self, name, age, telephone):
        self.__name = name
        self.__age = age
        self.__telephone = telephone

    @property
    def telephone(self):
        telephone_str = str(self.__telephone)
        return str(telephone_str[0:4]) + '-' + str(telephone_str[4:])


#After
class Person2(object):
    __slots__ = ['__name', '__age', '__telephone']

    def __init__(self, name, age, telephone):
        self.__name = name
        self.__age = age
        self.__telephone = Telephone(telephone)

    @property
    def telephone(self):
        return str(self.__telephone)


class Telephone(object):
    __slots__ = ['__telephone']

    def __init__(self, telephone):
        self.__telephone = telephone

    def __str__(self):
        telephone_str = str(self.__telephone)
        return str(telephone_str[0:4]) + '-' + str(telephone_str[4:])


if __name__ == '__main__':
    person = Person('Ken', 30, 12345678)
    print(person.telephone)

    person2 = Person2('Ken', 30, 12345678)
    print(person2.telephone)
