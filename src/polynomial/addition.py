from src.helpers import zip_longest

# Note ask if we can use itertools library (they will say yes just dont forget to ask)

# ----------------------------------------------------------------
# POLYNOMIAL ADDITION
# ----------------------------------------------------------------

"""
Adds together multiple polynomials with coefficients in Z_modulus.

Args:
    *args: Variable length argument list of lists of integers representing the coefficients of the polynomials to be added.
    modulus: An integer representing the modulus to be used in the addition operation.

Returns:
    A list of integers representing the coefficients of the resulting polynomial.
"""
def add(*args: list[int], modulus: int) -> list[int]:
    return [sum(x) % modulus for x in zip_longest(*args, fillvalue=0)]
