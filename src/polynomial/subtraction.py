from src.helpers import equalize_array_length, remove_leading_zeros


def subtract(modulus: int, f: list[int], g: list[int]) -> list[int]:
    if modulus <= 0:
        raise ValueError('Modulus must be > 0')

    equalize_array_length(f, g)

    result = [(x - g[i]) % modulus for i, x in enumerate(f)]

    return result

