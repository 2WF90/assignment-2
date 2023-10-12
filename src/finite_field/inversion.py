

from src.helpers import remove_leading_zeros


def inverse(x: list[int], integer_modulus: int, polynomial_modulus: list[int]):
    # By fermat's little theorem, a^(p-1) = 1 mod p, so from that, we can derive that a^(p-2) = a^-1 mod p
    remove_leading_zeros(x)

    p = integer_modulus

    # compute x^(p-2) mod p using modular exponentiation

    return
