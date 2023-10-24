from src.helpers import get_degree_and_leading_coefficient, match_length
from subtraction import subtract

#used to make X^q^t
def polynomial_coefficients(degree)-> list[int]:
    coefficients = [0] * (degree + 1)
    coefficients[-1] = 1
    return coefficients

def irreducibility_check(
        integer_modulus: int, f: list[int]
) -> bool:
    
    # Ensure n > 1
    degree = get_degree_and_leading_coefficient(f)
    if degree <= 1:
        return False
    t = 1
    #integer mod = 3 then X^3, X^9, X^27, 
    # X^1 = [0,1] X^3 = [0,0,0,1] X^9 =[0,0,0,0,0,0,0,0,0,1]


    while xgcd(f, subtract(match_length(polynomial_coefficients(degree**t), [0,1]), integer_modulus))[2] == [1]:
        t=t+1
    if t == degree:
        return True
    else:
        return False

    