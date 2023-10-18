from src.helpers import *


def test_get_degree_and_coefficient():
    assert (3, 1) == get_degree_and_leading_coefficient([1, 9, 2, 1])
    assert (0, 0) == get_degree_and_leading_coefficient([0, 0, 0, 0])
    assert (0, 1) == get_degree_and_leading_coefficient([1])
    assert (6, 4) == get_degree_and_leading_coefficient([1, 2, 3, 9, 45, 5, 4, 0, 0, 0])
    assert (0, 0) == get_degree_and_leading_coefficient([0, 0, 0, 0, 0, 0, 0])
