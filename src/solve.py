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

from src.polynomial.addition import add
from src.polynomial.subtraction import subtract


"""
Polynomial arithmetic:
1. addition (-), subtraction (-), reduction (--), multiplication (-)
2. long_division (++)
3. xgcd (++)
4. irreducibily_check (++)
5. irreducible_element_generation (+)

Finite field arithmetic:
6. inversion (+)
7. division (-)
8. primitivity_check (++)
9. primitive_element_generation (+)
"""

def solve(exercise: object):
    exercise_type = exercise["type"]
    exercise_task = exercise["task"]
    integer_modulus = exercise["integer_modulus"]


    if integer_modulus <= 0:
        return {"answer": None}

    if exercise_type == "polynomial_arithmetic":
        if exercise_task == "addition":
            return {"answer": add(integer_modulus, exercise["f"], exercise["g"])}

        elif exercise_task == "subtraction":
            return {"answer": subtract(integer_modulus, exercise["f"], exercise["g"])}

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
