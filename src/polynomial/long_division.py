from src.helpers import reduce_int_modulus, strip
from src.integer.inverse import modular_inverse


def long_division(
    f: list[int], g: list[int], integer_modulus: int
) -> tuple[list[int], list[int]]:
    """
    Divides two polynomials f and g modulo integer_modulus.
    Returns the quotient and remainder of the division.

    Args:
        f (list[int]): The dividend polynomial.
        g (list[int]): The divisor polynomial.
        integer_modulus (int): The integer modulus of the finite field.

    Returns:
        tuple[list[int], list[int]]: The quotient and remainder of the division.
    """
    f = strip(f)

    if f == [0]:
        return [0], [0]

    if g == [0]:
        raise ZeroDivisionError("Cannot divide by zero")

    remainder = f
    qoutient = [0] * (len(f) - len(g) + 1)

    while remainder != [0] and len(remainder) >= len(g):
        leading_coeff = (
            modular_inverse(g[-1], integer_modulus) * remainder[-1] % integer_modulus
        )

        qoutient[len(remainder) - len(g)] = leading_coeff

        for i in range(
            len(g)
        ):  # using subtract and multiply gave big loop on modular exponentiation test for some reason -> check
            remainder[-i - 1] -= leading_coeff * g[-i - 1] % integer_modulus

        remainder = reduce_int_modulus(strip(remainder), integer_modulus)

    if qoutient == []:
        qoutient = [0]

    return qoutient, remainder
