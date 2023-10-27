from src.helpers import match_length
from src.polynomial.addition import add
from src.polynomial.subtraction import subtract


def multiply(
    f: list[int], g: list[int], modulus: int, using_karatsuba: bool = True
) -> list[int]:
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

    if not using_karatsuba:
        return primary_multiplication(f_padded, g_padded, modulus)

    if n < 80: # experimentally determined threshold
        return primary_multiplication(f_padded, g_padded, modulus)

    if n & 1:
        f_padded.append(0)
        g_padded.append(0)
        n += 1

    n_over_2 = n >> 1

    x_lo, x_hi = f_padded[n_over_2:], f_padded[:n_over_2]
    y_lo, y_hi = g_padded[n_over_2:], g_padded[:n_over_2]

    z_2 = multiply(x_hi, y_hi, modulus)
    z_0 = multiply(x_lo, y_lo, modulus)
    z_1 = subtract(
        multiply(
            add(x_lo, x_hi, modulus=modulus),
            add(y_lo, y_hi, modulus=modulus),
            modulus,
        ),
        z_2,
        z_0,
        modulus=modulus,
    )

    return add(([0] * n) + z_0, ([0] * n_over_2) + z_1, z_2, modulus=modulus)


def primary_multiplication(f: list[int], g: list[int], modulus: int) -> list[int]:
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
