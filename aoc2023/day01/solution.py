from aoc2023.util import get_input


def solve_part1(entries):
    result = 0
    for code in entries:
        digits = "".join(list(filter(lambda i: i.isdigit(), code)))
        first = digits[0]
        last = digits[-1]
        final = "".join([first, last])
        result += int(final)
    return result


def solve_part2(entries):
    new_codes = []
    for code in entries:
        new_codes.append(
            code.replace("zero", "z0o")
            .replace("one", "o1e")
            .replace("two", "t2o")
            .replace("three", "t3e")
            .replace("four", "f4r")
            .replace("five", "f5e")
            .replace("six", "s6x")
            .replace("seven", "s7n")
            .replace("eight", "e8t")
            .replace("nine", "n9e")
        )
    return solve_part1(new_codes)


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2023/day01/input")
    #    print(solve_part1(entries))
    print(solve_part2(entries))
