from typing import TypeVar


def equalize_array_length(f: list[int], g: list[int]):
    """
    This function takes two lists of integers as input and modifies them in-place to have the same length by adding leading
    zeros to the shorter list. It returns the length of the resulting lists.

    Args:
        f (list[int]): The first list of integers.
        g (list[int]): The second list of integers.

    Returns:
        int: The length of the resulting lists.
    """
    f_length = len(f)
    g_length = len(g)
    max_length = max(f_length, g_length)

    # Add leading zeros to the shorter list, making changes in-place.
    f.extend([0] * (max_length - f_length))
    g.extend([0] * (max_length - g_length))

    return max_length


def remove_leading_zeros(array: list[int]):
    """
    Removes leading zeros from a given array of integers in place.

    Args:
        array (list[int]): The array to remove leading zeros from.

    Returns:
        None. The function modifies the input array in place.
    """
    i = len(array) - 1

    while i >= 0 and array[i] == 0:
        i -= 1

    array[:] = array[:i + 1] if i >= 0 else [0]


def get_degree_and_leading_coefficient(f: list[int]):
    """
    Returns the degree of the polynomial `f`.
    For example, the polynomial 3x^2 + 2x + 1 represented as the list `[1, 2, 3]` has a degree of 2.

    Args:
    - f: A list of integers representing the coefficients of a polynomial.

    Returns:
    - An integer representing the degree of the polynomial.
    """
    # for i in range(len(f) - 1, -1, -1):
    #     if f[i] != 0:
    #         return i, f[i]

    # return 0, 0

    for degree, coefficient in reversed(list(enumerate(f))):
        if coefficient != 0:
            return degree, coefficient
    return 0, 0


def reduce_modulus(modulus: int, f: list[int]):
    """
    Reduces each element in the given list `f` modulo `modulus`.

    Args:
        modulus (int): The modulus to reduce each element of `f` by.
        f (list[int]): The list of integers to reduce.

    Returns:
        list[int]: A new list containing the reduced elements of `f`.
    """
    return [x % modulus for x in f]
