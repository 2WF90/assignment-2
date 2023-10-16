from src.helpers import reduce_int_modulus
from src.polynomial.long_division import long_division
from src.polynomial.multiplication import multiply


def modular_exponentiation(f: list[int], power: int, integer_modulus: int, polynomial_modulus: list[int] = None) -> list[int]:
    """
    Computes the modular exponentiation of a polynomial f raised to a power, modulo a given modulus, using left-to-right
    binary exponentiation.

    Args:
        f (list[int]): The polynomial to be raised to a power.
        power (int): The power to which the polynomial is to be raised.
        modulus (int): The modulus with respect to which the result is to be computed.

    Returns:
        list[int]: The result of raising the polynomial f to the power power, modulo the modulus.
    """
    if power == 0:
        return [1]

    if power == 1:
        return f

    result = [1]


    for bit in bin(power)[2:]:
        result = multiply(result, result, integer_modulus)

        if bit == "1":
            result = multiply(result, f, integer_modulus)

        result = reduce_int_modulus(result, integer_modulus)

        if polynomial_modulus is not None:
            result = long_division(result, polynomial_modulus, integer_modulus)[1]

    return result
