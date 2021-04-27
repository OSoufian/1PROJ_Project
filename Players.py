"""import pygame

players = {}

class players():"""


class Meta(type):
    def __new__(mcs, name, bases, dct):
        mcs.x = super().__new__(mcs, name, bases, dct)
        mcs.x.attr = 2000
        setattr(mcs.x, mcs.test.__name__, mcs.test)
        setattr(mcs.x, mcs.draw_pieces.__name__, mcs.draw_pieces)
        return mcs.x

    def test(cls):
        print(1000)

    def draw_pieces(cls):
        pass


class foo(metaclass=Meta):

    def __init__(self):
        x = 23


class foo2(metaclass=Meta):
    pass


print(foo().test())
