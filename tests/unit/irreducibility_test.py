from src.polynomial.irreducibility import *


def test_simple_example():
    f = generate_irreducible_polynomial(2, 2)

    assert [1, 1, 1] == f


def test_random_gen():
    f = get_random_polynomial(3, 5)

    assert 4 == len(f)


def test_realistic_example():
    f = generate_irreducible_polynomial(5, 5)

    assert is_irreducible(f, 5)
    assert len(f) == 6
