from maths import add, sub, mul, div


def test_add():
    assert add(1, 2) == 3
    assert add(2, 0) == 2
    assert add(0, 2) == 2
    assert add(0, 0) == 0
    assert add(-11, 2) == -9
    assert add(11, -2) == 9
    assert add(-11, -2) == -13


def test_sub():
    assert sub(2, 1) == 1
    assert sub(2, 0) == 2
    assert sub(0, 2) == -2
    assert sub(0, 0) == 0
    assert sub(-11, 2) == -13
    assert sub(11, -2) == 13
    assert sub(-11, -2) == -9


def test_mul():
    assert mul(2, 1) == 2
    assert mul(1, 2) == 2
    assert mul(2, 0) == 0
    assert mul(0, 2) == 0
    assert mul(0, 0) == 0
    assert mul(-11, 2) == -22
    assert mul(11, -2) == -22
    assert mul(-11, -2) == 22


def test_div():
    assert div(2, 1) == 2
    assert div(1, 2) == 0.5
    assert div(0, 2) == 0
    assert div(-11, 2) == -5.5
    assert div(11, -2) == -5.5
    assert div(-11, -2) == 5.5


if __name__ == "__main__":
    test_add()
    test_sub()
    test_mul()
    test_div()
    print('Testing has ended')
