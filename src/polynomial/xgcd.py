from src.helpers import get_lead_coeff, strip
from src.integer.inverse import integer_inverse
from src.polynomial.long_division import long_division
from src.polynomial.subtraction import subtract
from src.polynomial.multiplication import multiply


"""
Computes the greatest common divisor of 2 polynomials

Param:
    a: list of integers, represents the first polynomial
    b: list of integers, represent the second polynomial
    modulus: integer, represent the modulus of both polynomial

Returns:
    list of integers, represents the greatest common divisor of a and b (monic polynomial)
"""


def gcd(a: list[int], b: list[int], modulus: int) -> list[int]:
    b = strip(b)

    while len(b) > 1 or b[0] != 0:
        _, rem = long_division(a, b, modulus)
        a = b
        b = rem

    lc = get_lead_coeff(a)

    if lc != 1:
        gcd_inverse = integer_inverse(lc, modulus)
        a = multiply(a, [gcd_inverse], modulus)

    return a


"""
Computes the greatest common divisors and polynomials x and y such that ax + by = gcd(a, b)
(Extended euclidian algorithm)

WARNING, this function heavily relies on the implementations of long_division, subtract and multiply
If at any point these functions change their input as a side effect then the whole thing breaks

Param:
    a: list of integers, represents the first polynomial
    b: list of integers, represent the second polynomial
    modulus: integer, represent the modulus of both polynomial

Returns:
    tuple of 3 list of integers, represents the gcd of a and b, x and y
"""


def xgcd(
    a: list[int], b: list[int], modulus: int
) -> tuple[list[int], list[int], list[int]]:
    b = strip(b)
    x, v, y, u = [1], [1], [0], [0]

    while b != [0]:
        # gcd part
        quot, rem = long_division(a, b, modulus)
        a = b
        b = rem

        # extended part
        x_temp = x
        y_temp = y
        x = u
        y = v
        u = subtract(x_temp, strip(multiply(quot, u, modulus)), modulus=modulus)
        v = subtract(y_temp, strip(multiply(quot, v, modulus)), modulus=modulus)

    lc = get_lead_coeff(a)

    if lc != 1:  # gcd is not monic
        gcd_inverse = integer_inverse(lc, modulus)
        a = multiply(a, [gcd_inverse], modulus)
        x = multiply(x, [gcd_inverse], modulus)
        y = multiply(y, [gcd_inverse], modulus)

    return a, x, y
