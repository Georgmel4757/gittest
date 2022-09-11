__all__ = ['add', 'sub', 'mul', 'div', 'fibonacci']


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
