from src.polynomial.long_division import long_division


def test_simple_case():
    f = [3, 2, 1, 0, 3]  # Represents 3 + 2x + x^2 + 3x^4
    g = [1, 0, 1, 0, 1]  # Represents 1 + x^2 + x^4

    assert ([3], [0, 2, 17]) == long_division(f, g, 19)


def test_divisor_larger_than_dividend():
    f = [3, 2, 1, 0, 3]
    g = [1, 0, 1, 0, 1, 1]

    assert ([0], f) == long_division(f, g, 19)


def test_case():
    f = [0, 0, 0, 0, 1, 1]
    g = [1, 9, 0, 0, 1]

    assert ([1, 1], [9, 0, 1]) == long_division(f, g, 10)


def test_another():
    f = [1, 9, 0, 0, 1]
    g = [9, 0, 1]

    assert ([1, 0, 1], [2, 9]) == long_division(f, g, 10)


def test_inverse_leading_coefficient():
    f = [9, 0, 1]
    g = [2, 9]

    assert ([8,9], [3]) == long_division(f, g, 10)
