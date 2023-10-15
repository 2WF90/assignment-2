from src.helpers import strip
from src.polynomial.subtraction import subtraction


def test_subZero():
    a = [0]
    b = [0, 0]
    m = 2

    r = subtraction(a, b, m)

    assert [0] == strip(r)


def test_subNegative():
    a = [13, 5, 7, 9, 0, 1]
    b = [-1, -3, -4, -14, -2, -10]
    m = 17

    r = subtraction(a, b, m)

    assert [14, 8, 11, 6, 2, 11] == strip(r)


def test_subDifferentLen():
    a = [5, 6, 0, 2]
    b = [3, 0, 0, 7, 1, 3, 0, 4]
    m = 8

    r = subtraction(a, b, m)

    assert [2, 6, 0, 3, 7, 5, 0, 4] == strip(r)


def test_subArbitrary():
    a = [-3, -13, -3, 27, 23, 15, 6, 0, 0, 1, 9]
    b = [-6, 0, 5, 9, 13, -18, 17, 16]
    m = 29

    r = subtraction(a, b, m)

    assert [3, 16, 21, 18, 10, 4, 18, 13, 0, 1, 9] == strip(r)
