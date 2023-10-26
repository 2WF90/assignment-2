from src.finite_field.inversion import inverse
from src.helpers import strip
from src.polynomial.long_division import long_division
from src.polynomial.multiplication import multiply


def division(
    f: list[int], g: list[int], polynomial_modulus: list[int], integer_modulus: int
):
    """
    Divides two polynomials in a finite field.

    Args:
        f (list[int]): The dividend polynomial.
        g (list[int]): The divisor polynomial.
        polynomial_modulus (list[int]): The polynomial modulus.
        integer_modulus (int): The integer modulus.

    Returns:
        list[int]: The quotient polynomial.
    Raises:
        ZeroDivisionError: If the divisor polynomial is zero.
    """
    f = strip(f)

    if g == [0]:
        raise ZeroDivisionError("Cannot divide by zero")

    return long_division(
        multiply(f, inverse(g, integer_modulus, polynomial_modulus), integer_modulus),
        polynomial_modulus,
        integer_modulus,
    )[1]
