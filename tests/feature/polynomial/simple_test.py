from tests.feature.assert_answer import assert_exercise


def test_addition():
    assert_exercise("simple", 0)


def test_subtraction():
    assert_exercise("simple", 1)


def test_multiplication():
    assert_exercise("simple", 2)


def test_long_division():
    assert_exercise("simple", 3)


def test_long_division():
    assert_exercise("simple", 4)


def test_extended_euclidean_algorithm():
    assert_exercise("simple", 5)


def test_extended_euclidean_algorithm():
    assert_exercise("simple", 6)


def test_irreducibility_check():
    assert_exercise("simple", 7)


def test_irreducibility_check():
    assert_exercise("simple", 8)


def test_irreducible_element_generation():
    assert_exercise("simple", 9)
