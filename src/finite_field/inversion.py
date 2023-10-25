from src.finite_field.modular_exponentation import modular_exponentiation
from src.polynomial.xgcd import xgcd


def inverse(f: list[int], integer_modulus: int, polynomial_modulus: list[int]):
    """
    Computes the inverse of a polynomial f in a finite field defined by integer_modulus and polynomial_modulus.

    Args:
        f (list[int]): The polynomial to invert.
        integer_modulus (int): The integer modulus of the finite field.
        polynomial_modulus (list[int]): The polynomial modulus of the finite field.

    Returns:
        list[int]: The inverse of f in the finite field.
    """
    _, x, _ = xgcd(f, polynomial_modulus, integer_modulus)

    return x
