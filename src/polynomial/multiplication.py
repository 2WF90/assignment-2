# Implement karatsuba and use primary method within karatsuba when n < 32 (experiment maybe with this threshold)


from src.helpers import match_length

from src.polynomial.addition import addition
from src.polynomial.subtraction import subtraction


def multiply(f: list[int], g: list[int], modulus: int) -> list[int]:
    """
    Multiplies two polynomials f and g using the Karatsuba algorithm.

    Args:
        f (list[int]): The first polynomial represented as a list of coefficients.
        g (list[int]): The second polynomial represented as a list of coefficients.
        modulus (int): The modulus to be used in the arithmetic operations.

    Returns:
        list[int]: The resulting polynomial represented as a list of coefficients.
    """
    f_padded, g_padded, n = match_length(f, g)

    if n < 64:
        return multiply_primary(f_padded, g_padded, modulus)

    if n & 1:
        f_padded.append(0)
        g_padded.append(0)
        n += 1

    half_n = n >> 1

    x_lo, x_hi = f_padded[half_n:], f_padded[:half_n]
    y_lo, y_hi = g_padded[half_n:], g_padded[:half_n]

    z_2 = multiply(x_hi, y_hi, modulus)
    z_0 = multiply(x_lo, y_lo, modulus)
    z_1 = subtraction(
        subtraction(
            multiply(
                addition(x_hi, x_lo, modulus), addition(y_hi, y_lo, modulus), modulus
            ),
            z_0,
            modulus,
        ),
        z_2,
        modulus,
    )

    return addition(addition([0] * n + z_0, [0] * half_n + z_1, modulus), z_2, modulus)


def multiply_primary(f: list[int], g: list[int], modulus: int) -> list[int]:
    """
    Multiplies two polynomials f and g using the primary school method.

    Args:
        f (list[int]): The coefficients of the first polynomial.
        g (list[int]): The coefficients of the second polynomial.
        modulus (int): The modulus to use for the coefficients.

    Returns:
        list[int]: The coefficients of the resulting polynomial.
    """
    n = len(f)

    result = [0] * ((n << 1) - 1)

    for i in range(n):
        for j in range(n):
            index = i + j
            result[index] += f[i] * g[j]
            result[index] = result[index] % modulus

    return result
