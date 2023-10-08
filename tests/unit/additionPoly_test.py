from src.polynomial import Polynomial
from src.basicOperations import additionPoly

def test_addZero():
    a = Polynomial(exponents=[0])
    b = Polynomial(exponents=[0, 0])
    m = 2

    r = additionPoly(a, b, m)

    assert [] == r.get_sanitized() #Is this [0] or just an empty list???

def test_addNegative():
    a = Polynomial(exponents=[-1, -3, -4])
    b = Polynomial(exponents=[-2, -25, -6])
    m = 13

    r = additionPoly(a, b, m)

    assert [10, 11, 3] == r.get_sanitized()

def test_addDifferentLen():
    a = Polynomial(exponents=[34, 56, 12, 98, 5, 4, 76, 6, 1])
    b = Polynomial(exponents=[2, 103])
    m = 53

    r = additionPoly(a, b, m)

    assert [36, 0, 12, 45, 5, 4, 23, 6, 1] == r.get_sanitized()

def test_addArbitrary():
    a = Polynomial(exponents=[1, 2, -4, 4, 0, 3, 1, -2])
    b = Polynomial(exponents=[0, 0, 4, 2, -3, 4, 0, 1, -3, 0, 2])
    m = 5

    r = additionPoly(a, b, m)

    assert [1, 2, 0, 1, 2, 2, 1, 4, 2, 0, 2] == r.get_sanitized()
