from tests.feature.assert_answer import assert_exercise


def test_addition():
    assert_exercise("simple", 10)


def test_subtraction():
    assert_exercise("simple", 11)


def test_multiplication():
    assert_exercise("simple", 12)


def test_division_1():
    assert_exercise("simple", 13)


def test_division_2():
    assert_exercise("simple", 14)


def test_inversion():
    assert_exercise("simple", 15)


def test_primitivity_check():
    assert_exercise("simple", 16)


def test_primitive_element_generation():
    assert_exercise("simple", 17)
