from src.helpers import strip, get_degree_and_leading_coefficient
from src.integer.inverse import integer_inverse
from src.polynomial.long_division import long_division
from src.polynomial.subtraction import subtract
from src.polynomial.multiplication import multiply

def divide_coefficients(f: list[int], num: int, modulus: int) -> list[int]:
    inv = integer_inverse(num, modulus)

    return strip([(n * inv) % modulus for n in f])


def gcd(a: list[int], b: list[int], modulus: int) -> list[int]:
    b = strip(b)

    while len(b) > 1 or b[0] != 0:
        _, rem = long_division(a, b, modulus)
        a = b
        b = rem
    
    _, lc = get_degree_and_leading_coefficient(a)
    return divide_coefficients(a, lc, modulus)

# WARNING, this function heavily relies on the implementations of long_division, subtract and multiply
# If at any point these functions change their input as a side effect then the whole thing breaks
def xgcd(a: list[int], b: list[int], modulus: int) -> tuple[list[int], list[int], list[int]]:
    b = strip(b) 
    x, v, y, u = [1], [1], [0], [0]

    while len(b) > 1 or b[0] != 0:
        #gcd part
        quot, rem = long_division(a, b, modulus)
        a = b
        b = rem

        #extended part
        x_temp = x
        y_temp = y
        x = u
        y = v
        u = subtract(x_temp, multiply(quot, u, modulus), modulus=modulus)
        v = subtract(y_temp, multiply(quot, v, modulus), modulus=modulus)

    _, lc = get_degree_and_leading_coefficient(a)
    return divide_coefficients(a, lc, modulus), divide_coefficients(x, lc, modulus), divide_coefficients(y, lc, modulus)