import random
from src.helpers import get_degree
from src.polynomial.xgcd import gcd


def is_irreducible(f: list[int], modulus: int) -> bool:
    """
    Determines whether the given polynomial f is irreducible over the field Z mod modulus.

    Args:
        f (list[int]): The coefficients of the polynomial f
        modulus (int): The modulus of the field Z mod modulus.

    Returns:
        bool: True if f is irreducible over Z mod modulus, False otherwise.
    """
    p = modulus
    t = 1

    while gcd(f, [0, -1] + [0] * (p**t - 2) + [1], modulus) == [
        1
    ]:  # check if gcd(f, X^(p^t) - X, modulus) == 1
        t = t + 1

    return t == get_degree(f)


def generate_irreducible_polynomial(degree: int, modulus: int) -> list[int]:
    """
    Generates a random irreducible polynomial of the given degree and modulus.

    Args:
        degree (int): The degree of the polynomial to generate.
        modulus (int): The modulus of the polynomial to generate.

    Returns:
        list[int]: A list of coefficients representing the generated polynomial.
    """
    f = get_random_polynomial(degree, modulus)

    while not is_irreducible(f, modulus):
        f = get_random_polynomial(degree, modulus)

    return f


def get_random_polynomial(degree: int, modulus: int) -> list[int]:
    """
    Returns a random polynomial of the given degree and modulus.

    Args:
        degree (int): The degree of the polynomial.
        modulus (int): The modulus of the polynomial.

    Returns:
        list[int]: A list of coefficients representing the polynomial.
    """
    leading_coefficient = random.randint(1, modulus - 1)
    non_leaning_coefficients = [random.randint(0, modulus - 1) for _ in range(degree)]

    return non_leaning_coefficients + [leading_coefficient]
