from turtle import *


def square():
    shape('turtle')
    speed(10000000)

    for i in range(120):
        for _ in range(4):
            forward(100)
            right(90)

        right(6)


square()
