import operator
import sys
from functools import reduce
from typing import Callable

Problem = tuple[list[str], Callable[[int, int], int]]


def p2(problems: list[Problem]) -> int:
    return sum(reduce(op, map(int, col)) for col, op in problems)


def p1(problems: list[Problem]):
    answers: list[int] = []
    for column, op in problems:
        cols: list[list[str]] = list(map(list, zip(*column)))
        numbers = [int("".join(r)) for r in cols]
        answers.append(reduce(op, numbers))

    return sum(answers)


def parse_columns_and_operators(filename: str) -> list[Problem]:
    lines = open(filename).read().strip().split("\n")
    operators = [operator.add if o == "+" else operator.mul for o in lines[-1].split()]

    problem_columns: list[list[str]] = []
    digit_columns: list[str] = []
    for col in map(list, zip(*lines[:-1])):
        number = "".join(col)
        if not number.strip():
            problem_columns.append(digit_columns)
            digit_columns = []
        else:
            digit_columns.append(number)

    problem_columns.append(digit_columns)
    return list(zip(problem_columns, operators))


def run(filename: str):
    problems = parse_columns_and_operators(filename)
    print(p1(problems))
    print(p2(problems))


filename = sys.argv[1] if len(sys.argv) > 1 else "test"
run(filename)
