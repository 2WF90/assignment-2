import sys
sys.path.append('/Users/christian/Dev/2WF90/assignment-2')

from src.polynomial.irreducibility import get_random_polynomial
from src.polynomial.multiplication import multiply

modulus = 509
polynomials_f = [get_random_polynomial(128, modulus) for _ in range(1000)]
polynomials_g = [get_random_polynomial(128, modulus) for _ in range(1000)]

def multiply_karatsuba():
    for i in range(len(polynomials_f)):
        f = polynomials_f[i]
        g = polynomials_g[i]

        multiply(f, g, modulus)

def multiply_primary():
    for i in range(len(polynomials_f)):
        f = polynomials_f[i]
        g = polynomials_g[i]

        multiply(f, g, modulus, using_karatsuba=False)

__benchmarks__ = [
    (multiply_primary, multiply_karatsuba, "Multiplying using Karatsuba over primary school method")
]
