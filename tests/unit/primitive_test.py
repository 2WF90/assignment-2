from src.finite_field.primitive import *

#----------------------------------------------------------------
# CHECK PRIMITIVITY
#----------------------------------------------------------------

# example from lecture notes
def test_primitivity_check_bin():
    f = [0, 1]
    poly_modulus = [1, 1, 1]
    modulus = 2

    assert check_primitivity(f, poly_modulus, modulus)

# also example from lecture notes
def test_primitivity_check_tri():
    f = [0, 1]
    poly_modulus = [1, 0, 1]
    modulus = 3

    assert not check_primitivity(f, poly_modulus, modulus)

#----------------------------------------------------------------
# PRIMITIVE ELEMENT GENERATION
#----------------------------------------------------------------

def primitve_equivalence(f: list[int], answer: list[int], poly_mod: list[int], modulus: int) -> bool:
    poly_mod = strip(poly_mod)
    poly_temp = [1]
    for _ in range(modulus ** (len(poly_mod) - 1)):
        _, poly_temp = long_division(multiply(poly_temp, f, modulus), poly_mod, modulus)
        if poly_temp == answer:
            return True
    return False

def test_generate_primitive_simple():
    modulus = 2
    poly_modulus = [1, 1, 1]
    right_answer = [1, 1]
    result = generate_primitve(poly_modulus, modulus)
    assert primitve_equivalence(result, right_answer, poly_modulus, modulus)

def test_generate_primitve_realistic():
    modulus = 5
    poly_modulus = [4, 1, 2, 1]
    right_answer = [3, 1]
    result = generate_primitve(poly_modulus, modulus)
    assert primitve_equivalence(result, right_answer, poly_modulus, modulus)
