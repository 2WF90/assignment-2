def extended_gcd(a: int, b: int):
    a_prime = a
    b_prime = b
    x_1, x_2, y_1, y_2 = 1, 0, 0, 1

    while b_prime > 0:
        q = a_prime // b_prime
        r = a_prime - q * b_prime

        a_prime = b_prime
        b_prime = r

        x_3 = x_1 - q * x_2
        y_3 = y_1 - q * y_2

        x_1, x_2 = x_2, x_3
        y_1, y_2 = y_2, y_3

    d = a_prime

    x = x_1 if a >= 0 else -x_1
    y = y_1 if b >= 0 else -y_1

    return d, x, y


def integer_inverse(x: int, modulus: int):
    gcd, a_inverse, _ = extended_gcd(x, modulus)

    if gcd != 1:
        raise ValueError("Modular inverse does not exist")

    return a_inverse % modulus
