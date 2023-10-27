def extended_gcd(a: int, b: int):
    """
    Computes the xgcd using algorithm 2.2 from the Number Theory lecture notes.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        Tuple[int, int, int]: A tuple containing the GCD of a and b, and the Bezout coefficients x and y.
    """
    # Step 1
    a_prime = a # Step 1.1
    b_prime = b
    x_1, x_2, y_1, y_2 = 1, 0, 0, 1 # Step 1.2 and 1.3

    # step 2
    while b_prime > 0: # Step 2.1
        q = a_prime // b_prime # Step 2.2
        r = a_prime - q * b_prime

        a_prime = b_prime # Step 2.3
        b_prime = r

        x_3 = x_1 - q * x_2 # Step 2.4
        y_3 = y_1 - q * y_2

        x_1, x_2 = x_2, x_3 # Step 2.5
        y_1, y_2 = y_2, y_3 # Step 2.6

    d = a_prime # Step 3.1

    x = x_1 if a >= 0 else -x_1 # Step 3.2
    y = y_1 if b >= 0 else -y_1 # Step 3.3

    return d, x, y # Step 3.4


def integer_inverse(x: int, modulus: int):
    gcd, a_inverse, _ = extended_gcd(x, modulus)

    if gcd != 1:
        raise ValueError("Modular inverse does not exist")

    return a_inverse % modulus
