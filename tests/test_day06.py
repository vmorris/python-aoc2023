from aoc2023.day06 import solution
from aoc2023.util import get_input


input_data = get_input("tests/testinput.day06")


def test_solve_part1():
    expected = 288
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 71503
    actual = solution.solve_part2(input_data)
    assert expected == actual
