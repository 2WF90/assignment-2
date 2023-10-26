from src.helpers import get_degree_and_leading_coefficient
from subtraction import subtract
from xgcd import gcd

#used to make X^q^t
def polynomial_coefficients(a: int)-> list[int]:
    coefficients = [0] * (a + 1)
    coefficients[-1] = 1
    return coefficients

# print(polynomial_coefficients(3**2))
def irreducibility_check(
        modulus: int, f: list[int]
) -> bool:
    
    # Ensure n > 1
    degree = get_degree_and_leading_coefficient(f)
    if degree <= 1:
        return False
    t = 1
    X = [0,1]

    # X^1 = [0,1] X^3 = [0,0,0,1] X^9 =[0,0,0,0,0,0,0,0,0,1]
    # 1 = 1 * X^0 = [1]


    while gcd(f, subtract((polynomial_coefficients(degree**t), X, modulus)), modulus)==[1]:
        t=t+1
    if t == degree:
        return True
    else:
        return False