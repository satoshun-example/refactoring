from zope.interface import (
    Interface,
    Attribute,
    implementer
    )


## Before
class Ball(object):
    __slots__ = ['__speed', '__amount_of_change']

    def __init__(self, speed, amount_of_change):
        self.__speed = speed
        self.__amount_of_change = amount_of_change

    @property
    def power(self):
        return self.__speed * self.__amount_of_change


class Bat(object):
    def hit(self, ball):
        """safe or out"""
        if ball.power <= 300:
            return True
        return False


class BaseBallPlayer(object):
    __slots__ = ['__bat']

    def __init__(self, bat):
        self.__bat = bat

    def hit(self, ball):
        return self.__bat.hit(ball)


## After
class IHitItem(Interface):
    power = Attribute("This item have power")


@implementer(IHitItem)
class Ball2(object):
    __slots__ = ['__speed', '__amount_of_change']

    def __init__(self, speed, amount_of_change):
        self.__speed = speed
        self.__amount_of_change = amount_of_change

    @property
    def power(self):
        return self.__speed * self.__amount_of_change


class IUseBaseballPlayerItem(Interface):
    def hit(ball):
        """Return:
        type boolean, True or False"""


@implementer(IUseBaseballPlayerItem)
class Bat2(object):
    def hit(self, ball):
        """safe or out"""
        if ball.power <= 300:
            return True
        return False


if __name__ == '__main__':
    player = BaseBallPlayer(Bat())
    player2 = BaseBallPlayer(Bat2())

    ball = Ball(100, 2.0)
    ball2 = Ball2(100, 2.0)
    assert player.hit(ball) == player2.hit(ball2)

    ball = Ball(100, 4.0)
    ball2 = Ball2(100, 4.0)
    assert player.hit(ball) == player2.hit(ball2)
