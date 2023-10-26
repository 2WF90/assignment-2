from tests.feature.assert_answer import assert_exercise


def test_division():
    assert_exercise("realistic", 0)


def test_subtraction():
    assert_exercise("realistic", 1)


def test_inversion():
    assert_exercise("realistic", 5)


def test_primitivity_check():
    assert_exercise("realistic", 7)


def test_division():
    assert_exercise("realistic", 8)


def test_addition():
    assert_exercise("realistic", 10)


def test_multiplication():
    assert_exercise("realistic", 12)


# def test_primitive_element_generation():
#     assert_exercise("realistic", 17)
