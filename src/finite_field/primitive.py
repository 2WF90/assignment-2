from src.helpers import strip
from src.polynomial.multiplication import multiply
from src.polynomial.long_division import long_division
from src.integer.divisors import find_divisors

def power_table(f: list[int], maxExp: int, modulus: int, poly_modulus: list[int]) -> list[list[int]]:
    exp = [strip(f)]
    while maxExp:
        temp_p = exp[-1].copy() #not sure if multiplication changes input as side effect
        _, rem = long_division(multiply(temp_p, temp_p, modulus), poly_modulus, modulus)
        exp.append(rem)

        maxExp = maxExp >> 1
    
    return exp

def power(exp_table: list[list[int]], e: int, modulus: int, poly_modulus: list[int]) -> list[int]:
    num = [1]
    itr = 0
    while e:
        if e & 1:
            _, num = long_division(multiply(num, exp_table[itr], modulus), poly_modulus, modulus)
        e = e >> 1
        itr = itr + 1
    
    return num

def check_primitivity(f: list[int], poly_modulus: list[int], modulus: int) -> bool:
    poly_modulus = strip(poly_modulus)

    order = modulus ** len(poly_modulus)

    exp_table = power_table(f, (order - 1) // 2, modulus, poly_modulus)
    
    #We find all divisors instead of only prime divisors
    for e in find_divisors(order - 1)[1:-1]:
        if strip(power(exp_table, e, modulus, poly_modulus)) == [1]:
            return False
    
    return True
