__all__ = ['Vector2', 'add', 'sub', 'mul', 'div', 'fibonacci']


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def fibonacci(n):
    if n > 0:
        a, b = 0, 1
        while n > 1:
            a, b = b, a + b
            n -= 1
        return a
    return None
