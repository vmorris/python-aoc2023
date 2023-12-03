from aoc2023.day02 import solution
from aoc2023.util import get_input


input_data = get_input("tests/testinput.day02")


def test_solve_part1():
    expected = 8
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 2286
    actual = solution.solve_part2(input_data)
    assert expected == actual
