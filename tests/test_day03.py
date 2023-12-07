from aoc2023.day03 import solution
from aoc2023.util import get_input


input_data = get_input("tests/testinput.day03", type="char-matrix")


def test_solve_part1():
    expected = 4361
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 467835
    actual = solution.solve_part2(input_data)
    assert expected == actual
