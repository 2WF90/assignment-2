##
# 2WF90 Algebra for Security -- Software Assignment 2
# Polynomial and Finite Field Arithmetic
# solve.py
#
#
# Group number:
# 21
#
# Author names and student IDs:
# Thijs Notten (1717219)
# Tom Nagel (1716042)
# Vincent Hoogendam (1440551)
# Christian Groothuis (1715534)
##
import json
from src.helpers import strip

from src.polynomial.addition import addition
from src.polynomial.multiplication import multiply
from src.polynomial.subtraction import subtraction

"""
Polynomial arithmetic:
1. addition (-), subtraction (-), reduction (--), multiplication (-)
2. long_division (++)
3. xgcd (++)
4. irreducibily_check (++)
5. irreducible_element_generation (+)
(6. modular_exponentiation (++))

Finite field arithmetic:
7. inversion (+)
8. division (-)
9. primitivity_check (++)
10. primitive_element_generation (+)
"""


def solve(exercise: object):
    exercise_type = exercise["type"]
    exercise_task = exercise["task"]
    integer_modulus = exercise["integer_modulus"]

    if integer_modulus < 2:  # disallowed as per definition of assingment
        return {"answer": None}

    if exercise_type == "polynomial_arithmetic":
        if exercise_task == "addition":
            a = exercise["f"]
            b = exercise["g"]
            result = addition(a, b, integer_modulus)
            return {"answer": strip(result)}

        if exercise_task == "subtraction":
            a = exercise["f"]
            b = exercise["g"]
            result = subtraction(a, b, integer_modulus)
            return {"answer": strip(result)}

        if exercise_task == "multiplication":
            f = exercise["f"]
            g = exercise["g"]
            result = multiply(f, g, integer_modulus)
            return {"answer": strip(result)}

        return {"answer": None}

    elif exercise_type == "finite_field_arithmetic":
        polynomial_modulus = exercise["polynomial_modulus"]


def solve_from_file(exercise_location: str):
    with open(exercise_location, "r") as exercise_file:
        exercise = json.load(exercise_file)

    return solve(exercise)


def save_answer_to_file(answer_location: str, answer: object):
    with open(answer_location, "w") as answer_file:
        json.dump(answer, answer_file, indent=4)


def solve_exercise(exercise_location: str, answer_location: str):
    answer = solve_from_file(exercise_location)

    save_answer_to_file(answer_location, answer)
