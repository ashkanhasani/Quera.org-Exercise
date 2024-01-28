import math


def square(x):
    return x ** 2


def triangle(x, h):
    return x * h * 0.5


def rectangle(a, b):
    return a * b


def circle(r):
    return math.pi * (r ** 2)


def get_func(ls: list):
    result = []
    for i in ls:
        if i == 'square':
            j = square
            result.append(j)
        elif i == 'circle':
            j = circle
            result.append(j)
        elif i == 'rectangle':
            j = rectangle
            result.append(j)
        elif i == "triangle":
            j = triangle
            result.append(j)
        else:
            raise Exception
    return result


