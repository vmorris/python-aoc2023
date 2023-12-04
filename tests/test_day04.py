from aoc2023.day04 import solution
from aoc2023.util import get_input


input_data = get_input("tests/testinput.day04")


def test_solve_part1():
    expected = 13
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 30
    actual = solution.solve_part2(input_data)
    assert expected == actual