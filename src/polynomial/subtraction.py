from itertools import zip_longest

# ----------------------------------------------------------------
# POLYNOMIAL SUBTRACTION
# ----------------------------------------------------------------


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
