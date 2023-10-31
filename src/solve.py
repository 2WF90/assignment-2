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
from src.finite_field.division import division
from src.finite_field.inversion import inverse
from src.helpers import strip

from src.polynomial.addition import add
from src.polynomial.long_division import long_division
from src.polynomial.multiplication import multiply
from src.polynomial.subtraction import subtract
from src.polynomial.xgcd import xgcd
from src.polynomial.irreducibility import (
    generate_irreducible_polynomial,
    is_irreducible,
)
from src.finite_field.primitive import check_primitivity, generate_primitve


def solve(exercise: object):
    exercise_type = exercise["type"]
    exercise_task = exercise["task"]
    integer_modulus = exercise["integer_modulus"]

    try:
        if integer_modulus < 2:  # disallowed as per definition of assingment
            raise ValueError("Integer modulus must be at least 2")

        if exercise_type == "polynomial_arithmetic":
            if exercise_task == "addition":
                a = exercise["f"]
                b = exercise["g"]
                result = add(a, b, modulus=integer_modulus)
                return {"answer": strip(result)}

            if exercise_task == "subtraction":
                a = exercise["f"]
                b = exercise["g"]
                result = subtract(a, b, modulus=integer_modulus)
                return {"answer": strip(result)}

            if exercise_task == "multiplication":
                f = exercise["f"]
                g = exercise["g"]
                result = multiply(f, g, integer_modulus)
                return {"answer": strip(result)}

            if exercise_task == "long_division":
                f = exercise["f"]
                g = exercise["g"]

                try:
                    q, r = long_division(f, g, integer_modulus)
                    return {"answer-q": strip(q), "answer-r": strip(r)}
                except:
                    return {"answer-q": None, "answer-r": None}

            if exercise_task == "extended_euclidean_algorithm":
                f = exercise["f"]
                g = exercise["g"]

                try:
                    gcd, x, y = xgcd(f, g, integer_modulus)

                    return {
                        "answer-a": strip(x),
                        "answer-b": strip(y),
                        "answer-gcd": strip(gcd),
                    }
                except:
                    return {"answer-a": None, "answer-b": None, "answer-gcd": None}

            if exercise_task == "irreducibility_check":
                f = exercise["f"]
                return {"answer": is_irreducible(f, modulus=integer_modulus)}

            if exercise_task == "irreducible_element_generation":
                modulus = exercise["integer_modulus"]
                degree = exercise["degree"]
                return {"answer": generate_irreducible_polynomial(degree, modulus)}

        elif exercise_type == "finite_field_arithmetic":
            polynomial_modulus = exercise["polynomial_modulus"]

            if exercise_task == "addition":
                f = exercise["f"]
                g = exercise["g"]
                result = add(f, g, modulus=integer_modulus)
                _, rem = long_division(result, polynomial_modulus, integer_modulus)
                return {"answer": strip(rem)}

            if exercise_task == "subtraction":
                f = exercise["f"]
                g = exercise["g"]
                result = subtract(f, g, modulus=integer_modulus)
                _, rem = long_division(result, polynomial_modulus, integer_modulus)
                return {"answer": strip(rem)}

            if exercise_task == "multiplication":
                f = exercise["f"]
                g = exercise["g"]
                result = multiply(f, g, integer_modulus)
                _, rem = long_division(result, polynomial_modulus, integer_modulus)
                return {"answer": strip(rem)}

            if exercise_task == "inversion":
                f = exercise["f"]
                result = inverse(f, integer_modulus, polynomial_modulus)
                _, rem = long_division(result, polynomial_modulus, integer_modulus)
                return {"answer": strip(rem)}

            if exercise_task == "division":
                f = exercise["f"]
                g = exercise["g"]
                result = division(f, g, polynomial_modulus, integer_modulus)
                return {"answer": strip(result)}

            if exercise_task == "primitivity_check":
                f = exercise["f"]
                poly_mod = exercise["polynomial_modulus"]
                modulus = exercise["integer_modulus"]
                return {"answer": check_primitivity(f, poly_mod, modulus)}

            if exercise_task == "primitive_element_generation":
                poly_mod = exercise["polynomial_modulus"]
                modulus = exercise["integer_modulus"]
                return {"answer": generate_primitve(poly_mod, modulus)}

        raise ValueError("Invalid exercise type or task")
    except:
        return {"answer": None}


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
