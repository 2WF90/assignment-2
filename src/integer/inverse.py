def extended_gcd(a: int, b: int):
    if a == 0:
        return (b, 0, 1)

    gcd, x, y = extended_gcd(b % a, a)

    return (gcd, y - (b // a) * x, x)


def integer_inverse(x: int, modulus: int):
    gcd, a_inverse, _ = extended_gcd(x, modulus)

    if gcd != 1:
        raise ValueError("Modular inverse does not exist")

    return a_inverse % modulus
