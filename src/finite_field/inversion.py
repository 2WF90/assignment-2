from src.finite_field.modular_exponentation import modular_exponentiation
from src.helpers import strip


def inverse(f: list[int], integer_modulus: int, polynomial_modulus: list[int]):
    # By fermat's little theorem, a^(p^n-1) = 1 mod p, so from that, we can derive that a^(p^n-2) = a^-1 mod p
    q = integer_modulus ** (len(polynomial_modulus) - 1)  # compute p^n

    # compute x^(q-2) mod p using modular exponentiation
    result = modular_exponentiation(f, q - 2, integer_modulus, polynomial_modulus)

    return result
