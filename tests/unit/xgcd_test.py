from src.polynomial.xgcd import *
from src.polynomial.addition import add
from src.polynomial.multiplication import multiply
from src.helpers import strip
import pytest

#----------------------------------------------------------------
# DIVIDE COEFFICIENTS
#----------------------------------------------------------------

def test_coeff_zero():
    with pytest.raises(ValueError):
        f = [1, 3, 5]
        num = 0
        modulus = 10
        divide_coefficients(f, num, modulus)

def test_coeff():
    f = [4, 5, 3, 5]
    num = 4
    modulus = 7
    
    assert divide_coefficients(f, num, modulus) == [1, 3, 6, 3]

#----------------------------------------------------------------
# GCD
#----------------------------------------------------------------

def test_gcd_b_divisor_a():
    a = [0, 1, 1]
    b = [0, 1, 0, 0, 1]
    modulus = 2
    assert [0, 1, 1] == gcd(a, b, modulus)

def test_gcd_bin():
    a = [0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
    b = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]
    modulus = 2
    assert [0, 0, 1, 0, 1] == gcd(a, b, modulus)
    
#----------------------------------------------------------------
# XGCD
#----------------------------------------------------------------

def test_xgcd_b_divisor_a():
    a = [0, 1, 1]
    b = [0, 1, 0, 0, 1]
    modulus = 2
    assert ([0, 1, 1], [1], [0]) == xgcd(a, b, modulus)

def test_xgcd_bin():
    a = [0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
    b = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]
    modulus = 2
    assert ([0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 1]) == xgcd(a, b, modulus)

def test_xgcd_axby_is_gcd_1():
    a = [1, 3, 7, 5, 0, 5]
    b = [9, 1, 8, 4, 6]
    modulus = 11
    div, x, y = xgcd(a, b, modulus)

    assert div == strip(add(multiply(a, x, modulus), multiply(b, y, modulus), modulus=modulus))

def test_xgcd_axby_is_gcd_1():
    a = [4, 3, 5, 3, 1, 4, 6, 4, 4, 1]
    b = [6, 5, 1, 3, 3, 1, 6, 3, 1, 5, 0, 6, 3, 1]
    modulus = 7
    div, x, y = xgcd(a, b, modulus)

    assert div == strip(add(multiply(a, x, modulus), multiply(b, y, modulus), modulus=modulus))

"""
#Stress test, this is what it should be able to handle according to the assingment
def test_xgcd_axby_is_gcd_1():
    a = [340, 164, 283, 94, 162, 4, 398, 361, 380, 426, 218, 38, 502, 245, 32, 178, 372, 294, 61, 428, 497, 
         96, 500, 451, 459, 287, 201, 335, 100, 18, 191, 103, 109, 102, 464, 391, 457, 21, 386, 496, 431, 
         249, 424, 225, 70, 107, 488, 267, 302, 487, 266, 390, 89, 207, 208, 208, 321, 80, 97, 192, 142, 
         250, 129, 456, 2, 95, 462, 262, 83, 456, 454, 383, 94, 175, 131, 472, 99, 22, 392, 251, 187, 151, 
         148, 147, 31, 488, 474, 362, 178, 97, 32, 249, 90, 494, 94, 504, 126, 315, 284, 318, 449, 222, 475, 
         408, 475, 351, 151, 159, 359, 295, 13, 114, 410, 4, 240, 69, 99, 118, 14, 2, 205, 241, 230, 327, 
         262, 278, 318, 68, 144, 261, 174, 131, 32, 232, 206, 164, 273, 457, 192, 34, 52, 135, 503, 74, 126, 
         486, 28, 227, 253, 184, 154, 223, 206, 78, 456, 267, 339, 5, 43, 236, 73, 201, 445, 153, 171, 317, 
         136, 293, 402, 483, 352, 268, 374, 300, 6, 186, 291, 250, 485, 85, 491, 467, 208, 362, 336, 475, 87, 
         439, 319, 461, 215, 229, 29, 497, 293, 248, 234, 14, 111, 236, 421, 372, 466, 351, 113, 381, 429, 
         281, 264, 50, 70, 9, 317, 1, 508, 372, 229, 395, 324, 446, 257, 460, 304, 374, 221, 480, 247, 198, 
         388, 340, 3, 405, 108, 446, 149, 480, 370, 439, 31, 116, 98, 95, 489, 189, 291, 225, 346]
    b = [57, 143, 231, 202, 81, 448, 8, 111, 245, 65, 494, 41, 209, 455, 202, 473, 460, 505, 62, 87, 219, 224, 
         497, 373, 360, 68, 104, 455, 103, 166, 480, 372, 494, 494, 406, 132, 262, 367, 136, 210, 266, 251, 10, 
         454, 155, 41, 209, 62, 76, 367, 44, 473, 239, 413, 322, 265, 329, 175, 480, 267, 346, 253, 255, 342, 
         351, 20, 154, 54, 137, 304, 75, 90, 83, 457, 183, 299, 364, 505, 463, 254, 300, 315, 26, 232, 503, 384, 
         381, 22, 113, 47, 157, 250, 367, 442, 92, 339, 336, 468, 489, 94, 334, 101, 338, 423, 370, 183, 125, 258, 
         194, 466, 28, 310, 150, 225, 237, 139, 416, 68, 422, 470, 421, 10, 408, 40, 248, 418, 116, 321, 475, 408, 
         293, 101, 154, 120, 359, 503, 44, 184, 251, 32, 211, 238, 426, 501, 0, 1, 400, 448, 100, 418, 78, 441, 496, 
         11, 181, 382, 18, 289, 103, 20, 11, 251, 496, 65, 161, 25, 333, 315, 46, 95, 376, 448, 409, 13, 103, 180, 
         202, 210, 474, 381, 24, 349, 77, 2, 286, 126, 78, 307, 50, 186, 75, 499, 215, 318, 158, 256, 375, 123, 304, 
         197, 228, 482, 277, 138, 60, 137, 318, 412, 109, 108, 242, 233, 101, 250, 489, 359, 313, 260, 204, 65, 104, 
         497, 114, 118, 345, 123, 312, 148, 83, 8, 183, 213, 83, 130, 330, 69]

    modulus = 509
    div, x, y = xgcd(a, b, modulus)

    assert div == strip(add(multiply(a, x, modulus), multiply(b, y, modulus), modulus=modulus))
"""