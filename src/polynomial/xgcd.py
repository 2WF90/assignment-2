from src.helpers import strip, get_degree_and_leading_coefficient
from src.integer.inverse import integer_inverse
from src.polynomial.long_division import long_division
from src.polynomial.subtraction import subtract
from src.polynomial.multiplication import multiply

"""
Devides every coefficient in a polynomial f by a given number

Param:
    f: list of integers, represents the polynomial
    num: integer, represents the number to devide with
    modulus: integer, represents the modulus of the polynomial

Returns:
    list of integers, represent the resulting polynomial
"""
def divide_coefficients(f: list[int], num: int, modulus: int) -> list[int]:
    if num == 0:
        raise ValueError("Can not devide by zero")

    inv = integer_inverse(num, modulus)

    return strip([(n * inv) % modulus for n in f])

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

    _, lc = get_degree_and_leading_coefficient(a)
    return divide_coefficients(a, lc, modulus)


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
def xgcd(a: list[int], b: list[int], modulus: int) -> tuple[list[int], list[int], list[int]]:
    b = strip(b)
    x, v, y, u = [1], [1], [0], [0]

    while b != [0]:
        #gcd part
        quot, rem = long_division(a, b, modulus)
        a = b
        b = rem

        #extended part
        x_temp = x
        y_temp = y
        x = u
        y = v
        u = subtract(x_temp, strip(multiply(quot, u, modulus)), modulus=modulus)
        v = subtract(y_temp, strip(multiply(quot, v, modulus)), modulus=modulus)

    if a[-1] != 1: # gcd is not monic
        gcd_inverse = integer_inverse(a[-1], modulus)
        a = multiply(a, [gcd_inverse], modulus)
        x = multiply(x, [gcd_inverse], modulus)
        y = multiply(y, [gcd_inverse], modulus)
    
    return a, x, y
