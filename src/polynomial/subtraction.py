from itertools import zip_longest

# ----------------------------------------------------------------
# POLYNOMIAL SUBTRACTION
# ----------------------------------------------------------------

"""
Subtract multiple polynomials element-wise.

Args:
    *args (list[int]): The polynomials to subtract.
    modulus (int): The modulus to use for arithmetic operations.

Returns:
    list[int]: The resulting polynomial after subtraction.
"""
def subtract(*args: list[int], modulus: int) -> list[int]:
    return [((x[0] - sum(x[1:])) % modulus) for x in zip_longest(*args, fillvalue=0)]
