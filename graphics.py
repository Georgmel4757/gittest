gufrom matplotlib import pyplot as plt


def linear_eq(k=1, b=0):
    x = [i for i in range(-10, 11)]
    y = [k * element + b for element in x]
    plt.plot(x, y)
    plt.title(f'График функции {k}x+{b}')
    plt.show()


def quadratic_eq():
    x = [i for i in range(-10, 11)]
    y = [el * el for el in x]
    plt.plot(x, y)
    plt.title('График функции x^2')
    plt.show()


if __name__ == '__main__':
    linear_eq(2, 5)
    quadratic_eq()
