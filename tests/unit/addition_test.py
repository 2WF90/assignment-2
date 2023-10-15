from src.helpers import strip
from src.polynomial.addition import addition


def test_addZero():
    a = [0]
    b = [0, 0]
    m = 2

    r = addition(a, b, m)

    assert [0] == strip(r)


def test_addNegative():
    a = [-1, -3, -4]
    b = [-2, -25, -6]
    m = 13

    r = addition(a, b, m)

    assert [10, 11, 3] == strip(r)


def test_addDifferentLen():
    a = [34, 56, 12, 98, 5, 4, 76, 6, 1]
    b = [2, 103]
    m = 53

    r = addition(a, b, m)

    assert [36, 0, 12, 45, 5, 4, 23, 6, 1] == strip(r)


def test_addArbitrary():
    a = [1, 2, -4, 4, 0, 3, 1, -2]
    b = [0, 0, 4, 2, -3, 4, 0, 1, -3, 0, 2]
    m = 5

    r = addition(a, b, m)

    assert [1, 2, 0, 1, 2, 2, 1, 4, 2, 0, 2] == strip(r)
