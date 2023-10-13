from src.helpers import remove_leading_zeros


def inverse(x: list[int], integer_modulus: int, polynomial_modulus: list[int]):
    # By fermat's little theorem, a^(p^n-1) = 1 mod p, so from that, we can derive that a^(p^n-2) = a^-1 mod p
    remove_leading_zeros(x)

    q = integer_modulus ** len(polynomial_modulus)  # compute p^n

    # compute x^(q-2) mod p using modular exponentiation

    return
