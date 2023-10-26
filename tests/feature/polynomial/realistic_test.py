from tests.feature.assert_answer import assert_exercise


def test_long_division():
    assert_exercise("realistic", 2)


def test_subtraction():
    assert_exercise("realistic", 3)


# def test_irreducible_element_generation(): non-deterministic
#     assert_exercise("realistic", 4)


def test_irreducibility_check():
    assert_exercise("realistic", 6)


def test_long_division():
    assert_exercise("realistic", 9)


def test_extended_euclidean_algorithm():
    assert_exercise("realistic", 11)


def test_multiplication():
    assert_exercise("realistic", 13)


def test_irreducibility_check():
    assert_exercise("realistic", 14)


def test_addition():
    assert_exercise("realistic", 15)


def test_extended_euclidean_algorithm():
    assert_exercise("realistic", 16)
