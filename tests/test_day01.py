from aoc2023.day01 import solution
from aoc2023.util import get_input


input_data = get_input("tests/testinput.day01")


def test_solve_part1():
    expected = 142
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    pass
