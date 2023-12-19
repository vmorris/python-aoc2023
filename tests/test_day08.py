from aoc2023.day08 import solution
from aoc2023.util import get_input


input_data_1 = get_input("tests/testinput.day08.1")
input_data_2 = get_input("tests/testinput.day08.2")


def test_solve_part1():
    expected = 2
    actual = solution.solve_part1(input_data_1)
    assert expected == actual


def test_solve_part2():
    expected = 6
    actual = solution.solve_part2(input_data_2)
    assert expected == actual