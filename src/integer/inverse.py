def extended_gcd(a: int, b: int):
    if a == 0:
        return (b, 0, 1)

    gcd, x, y = extended_gcd(b % a, a)

    return (gcd, y - (b // a) * x, x)


def modular_inverse(a: int, modulus: int):
    gcd, x, _ = extended_gcd(a, modulus)

    if gcd != 1:
        raise ValueError("Modular inverse does not exist")

    return x % modulus
