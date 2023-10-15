from itertools import zip_longest
# Note ask if we can use itertools library (they will say yes just dont forget to ask)

#----------------------------------------------------------------
# ADDITION AND SUBTRACTION, POLYNOMIAL
#----------------------------------------------------------------

# Adds polynomial A and B mod the modulus
#
# Args:
#   a: list of integers, representing polynomial A
#   b: list of integers, representing polynomial B
#   modulus: integer, modulus of resulting polynomial
#
# Returns: list of integers, representing the new polynomial

def addition(a: list[int], b: list[int], modulus: int) -> list[int]:

    return [(n + m) % modulus for n, m in zip_longest(a, b, fillvalue=0)]


# Subtracts polynomial A and B mod the modulus
#
# Args:
#   a: list of integers, representing polynomial A
#   b: list of integers, representing polynomial B
#   modulus: integer, modulus of resulting polynomial
#
# Returns: list of integers, representing the new polynomial

def subtraction(a: list[int], b: list[int], modulus: int) -> list[int]:
    
    return [(n - m) % modulus for n, m in zip_longest(a, b, fillvalue=0)]


#----------------------------------------------------------------
# ADDITION AND SUBTRACTION, FINITE FIELD
#----------------------------------------------------------------