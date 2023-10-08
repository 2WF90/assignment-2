from src.polynomial import Polynomial
from src.basicOperations import subtractionPoly

def test_subZero():
    a = Polynomial(exponents=[0])
    b = Polynomial(exponents=[0, 0])
    m = 2

    r = subtractionPoly(a, b, m)

    assert [] == r.get_sanitized() #Is this [0] or just an empty list???

def test_subNegative():
    a = Polynomial(exponents=[13, 5, 7, 9, 0, 1])
    b = Polynomial(exponents=[-1, -3, -4, -14, -2, -10])
    m = 17

    r = subtractionPoly(a, b, m)

    assert [14, 8, 11, 6, 2, 11] == r.get_sanitized()

def test_subDifferentLen():
    a = Polynomial(exponents=[5, 6, 0, 2])
    b = Polynomial(exponents=[3, 0, 0, 7, 1, 3, 0, 4])
    m = 8

    r = subtractionPoly(a, b, m)

    assert [2, 6, 0, 3, 7, 5, 0, 4] == r.get_sanitized()

def test_subArbitrary():
    a = Polynomial(exponents=[-3, -13, -3, 27, 23, 15, 6, 0, 0, 1, 9])
    b = Polynomial(exponents=[-6, 0, 5, 9, 13, -18, 17, 16])
    m = 29

    r = subtractionPoly(a, b, m)

    assert [3, 16, 21, 18, 10, 4, 18, 13, 0, 1, 9] == r.get_sanitized()