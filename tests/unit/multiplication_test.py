from src.helpers import strip
from src.polynomial.multiplication import multiply


def test_degree_1_example():
    f = [1, 4]
    g = [-5, 1]
    modulus = 3

    assert multiply(f, g, modulus) == [1, 2, 1]

    print(multiply(f, g, modulus))


def test_degree_3_example():
    f = [1, 4, 1, 1]
    g = [-5, 1]
    modulus = 3

    assert strip(multiply(f, g, modulus)) == [1, 2, 2, 2, 1]


def test_length_1():
    f = [4]
    g = [2]
    modulus = 17

    assert multiply(f, g, modulus) == [8]
