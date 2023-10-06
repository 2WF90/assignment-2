from src.polynomial import Polynomial
from itertools import zip_longest
# Note ask if we can use itertools library (they will say yes just dont forget to ask)

#----------------------------------------------------------------
# ADDITION AND SUBTRACTION, POLYNOMIAL
#----------------------------------------------------------------

# Both functions use practically the same logic
# They iterate over the exponents in the polynomials and either subtract or add them
# zip_longest tulpes the elements of the 2 lists, 
# if one is longer than the other the short one is automatically padded with 0

def additionPoly(a: Polynomial, b: Polynomial, modulus: int) -> Polynomial:
    exp = list()

    for n, m in zip_longest(a, b, fillvalue=0):
        exp.append((n + m) % modulus)
    
    return Polynomial(exponents=exp)


def subtractionPoly(a: Polynomial, b: Polynomial, modulus: int) -> Polynomial:
    exp = list()

    for n, m in zip_longest(a, b, fillvalue=0):
        exp.append((n - m) % modulus)
    
    return Polynomial(exponents=exp)


#----------------------------------------------------------------
# ADDITION AND SUBTRACTION, FINITE FIELD
#----------------------------------------------------------------