from src.helpers import strip
from src.polynomial.multiplication import multiply
from src.polynomial.long_division import long_division
from src.integer.divisors import find_divisors
import random

#----------------------------------------------------------------
# CHECK PRIMITIVITY
#----------------------------------------------------------------

"""
Creates a table of powers of 2 a polynomial f upto a certain exponent
Example: maxExp = 8. we get f^1, f^2, f^4, f^8, f^16

Args:
    f (list[int]):      represents the polynomial that we will cube log(maxExp) times
    maxExp (int):       will go upto the closes power of 2 higher than maxExp
    poly_modulus (int): polynomial modulus of the field
    modulus (int):      modulus of the field

Returns:
    list[list[int]]: returns all powers of f that have a power of 2 in the exponent
"""
def power_table(f: list[int], maxExp: int, poly_modulus: list[int], modulus: int) -> list[list[int]]:
    exp = [strip(f)]
    while maxExp:
        temp_p = exp[-1]
        _, rem = long_division(multiply(temp_p, temp_p, modulus), poly_modulus, modulus)
        exp.append(rem)

        maxExp = maxExp >> 1

    return exp

"""
Uses a exponents_table to calculate the result of certain polynomial (f) to the power e
(f is implicitly defined by the table)

Args:
    exp_table (list[list[int]]):    all powers of f that have a power of 2 in the exponent (upto a certain value)
    e (int):                        the exponent
    poly_modulus:                   polynomial modulus of the field
    modulus (int):                  modulus of the field

Returns:
    list[int]: polynomial that represents f^e
"""
def power(exp_table: list[list[int]], e: int, poly_modulus: list[int], modulus: int) -> list[int]:
    num = [1]
    itr = 0
    while e:
        if e & 1:
            _, num = long_division(multiply(num, exp_table[itr], modulus), poly_modulus, modulus)
        e = e >> 1
        itr = itr + 1

    return num

"""
Checks if a certain polynomial f is a primitive in its field
Example: f is primitve -> True, f is not primitve -> False

Args:
    f (list[int]):          represents polynomial f
    poly_modulus (int):     polynomial modulus of the field
    modulus (int):          modulus of the field
    divisors (list[int]):   Optional argument, default = None, functions that call check_primitivity
                            many times with the same divisors can compute those themselves

Returns:
    bool: States if f is primitive
"""
def check_primitivity(f: list[int], poly_modulus: list[int], modulus: int, divisors: list[int] = None) -> bool:
    poly_modulus = strip(poly_modulus)

    order = modulus ** (len(poly_modulus) - 1)

    exp_table = power_table(f, (order - 1) // 2, poly_modulus, modulus)

    #We find all divisors instead of only prime divisors
    if divisors == None:
        divisors = find_divisors(order - 1)[1:-1]

    for e in divisors:
        if strip(power(exp_table, e, poly_modulus, modulus)) == [1]:
            return False

    return True

#----------------------------------------------------------------
# PRIMITIVE ELEMENT GENERATION
#----------------------------------------------------------------

"""
Generate random polynomial within a field
The polynomial modulus is implicitly roughly "defined" by the variable length

Args:
    modulus (int):  modulus of the field
    length (int):   desired length of the generated polynomial (length of polynomial modulus - 1)

Returns:
    list[int]: polynomial in the field randomly chosen
"""
def random_poly(modulus: int, length: int) -> list[int]:
    p = strip([random.randint(0, modulus - 1) for _ in range(length)])

    while p == [0] or p == [1]:
        p = strip([random.randint(0, modulus - 1) for _ in range(length)])

    return p

"""
Generates a primitive element in the field
Contains a seed value that can be set by the caller (mostly for testing purposes)

Args:
    poly_modulus (int):     polynomial modulus of the field
    modulus (int):          modulus of the field
    seed (int):             Optional value that sets the seed of the random function.
                            It determines how the randomly generated polynomials are chosen.

Returns:
    list[int]: representing a primitive polynomial in the field
"""
def generate_primitve(poly_modulus: list[int], modulus: int, seed: int=69) -> list[int]:
    poly_modulus = strip(poly_modulus)
    random.seed(seed)

    #Calculate divisors once
    order = modulus ** (len(poly_modulus) - 1)
    divisors = find_divisors(order - 1)[1:-1]

    random_f = random_poly(modulus, len(poly_modulus) - 1)
    while not check_primitivity(random_f, poly_modulus, modulus, divisors=divisors):
        random_f = random_poly(modulus, len(poly_modulus) - 1)

    return random_f
