# strip removes all the zero elements at the end of the list
# upto the first nonzero element.
#
# Args:
#   l: list of integers
#
# Returns: stripped list of integers
def strip(l: list[int]) -> list[int]:
    # reverse iterate over l
    for i in range(len(l) - 1, -1, -1):
        if l[i] != 0:
            return l[: i + 1]

    return list([0])


def match_length(f: list[int], g: list[int]) -> tuple[list[int], list[int], int]:
    """
    Pads the input lists with zeros to ensure they have the same length, and returns the padded lists and their length.

    Args:
        f (list[int]): The first list to be padded.
        g (list[int]): The second list to be padded.

    Returns:
        tuple[list[int], list[int], int]: A tuple containing the padded lists and their length.
    """
    f_length = len(f)
    g_length = len(g)
    max_length = max(f_length, g_length)

    padded_f = f + [0] * (max_length - f_length)
    padded_g = g + [0] * (max_length - g_length)

    return padded_f, padded_g, max_length


def get_degree_and_leading_coefficient(f: list[int]):
    """
    Returns the degree of the polynomial `f`.
    For example, the polynomial 3x^2 + 2x + 1 represented as the list `[1, 2, 3]` has a degree of 2.

    Args:
    - f: A list of integers representing the coefficients of a polynomial.

    Returns:
    - An integer representing the degree of the polynomial.
    """
    for degree, coefficient in reversed(list(enumerate(f))):
        if coefficient != 0:
            return degree, coefficient
    return 0, 0


def reduce_int_modulus(f: list[int], modulus: int):
    """
    Reduces each element in the given list `f` modulo `modulus`.

    Args:
        modulus (int): The modulus to reduce each element of `f` by.
        f (list[int]): The list of integers to reduce.

    Returns:
        list[int]: A new list containing the reduced elements of `f`.
    """
    return [x % modulus for x in f]


#----------------------------------------------------------------
# ITERTOOLS
#----------------------------------------------------------------

# We were not allowed to use the itertools library because "it was to large"
# So I just copied the source code of these 2 specific functions (https://docs.python.org/3/library/itertools.html)
# In my opinion this falls under fair use since this does not make the assingment significantly easier,
# it just makes our code a bit cleaner readable.
# I checked the Python license and this should be fine.

def repeat(object, times=None):
    # repeat(10, 3) --> 10 10 10
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object

def zip_longest(*args, fillvalue=None):
    # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    iterators = [iter(it) for it in args]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for i, it in enumerate(iterators):
            try:
                value = next(it)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iterators[i] = repeat(fillvalue)
                value = fillvalue
            values.append(value)
        yield tuple(values)