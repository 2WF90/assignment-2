from src.helpers import strip
from src.finite_field.modular_exponentation import modular_exponentiation


def test_power_2():
    f = [1, 0, 1, 1]

    assert strip(modular_exponentiation(f, 2, 2)) == [1, 0, 0, 0, 1, 0, 1]


def test_power_40():
    f = [1, 0, 1, 1]

    assert strip(modular_exponentiation(f, 10, 2)) == [
        1,
        0,
        0,
        0,
        1,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        0,
        0,
        1,
        0,
        1,
    ]


def test_ff():
    f = [1, 4, 1]
    polynomial_modulus = [1, 1, 0, 1]

    assert strip(modular_exponentiation(f, 40, 5, polynomial_modulus)) == [0, 3, 1]
