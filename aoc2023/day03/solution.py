from aoc2023.util import get_input


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __repr__(self):
        return f"<Point ({self.x}, {self.y})>"


def symbol_adjacent(schematic, symbols, part_num, location: Point):
    # print(f"{part_num}, {location}")
    part_num_length = len(part_num)
    prev_row = location.y - 1
    next_row = location.y + 1
    prev_col = location.x - 1
    next_col = location.x + part_num_length
    # print(f"    prev_row:{prev_row}, prev_col:{prev_col}")
    # print(f"    next_row:{next_row}, next_col:{next_col}")
    points_to_check = []
    if (
        prev_row >= 0
        and prev_col >= 0
        and next_row < len(schematic)
        and next_col < len(schematic[0])
    ):  # this part is not on an edge
        for i in range(prev_col, next_col + 1):
            points_to_check.append(Point(x=i, y=prev_row))
            points_to_check.append(Point(x=i, y=next_row))
        points_to_check.append(Point(x=prev_col, y=location.y))
        points_to_check.append(Point(x=next_col, y=location.y))
    ## handle the edge cases
    # are we on the top edge?
    elif prev_row < 0:
        # are we on the left edge?
        if prev_col < 0:
            # print("    - top left edge")
            for i in range(location.x, next_col + 1):
                points_to_check.append(Point(i, next_row))
            points_to_check.append(Point(next_col, location.y))
        # are we on the right edge?
        elif next_col >= len(schematic[0]):
            # print("    - top right edge")
            for i in range(prev_col, next_col):
                points_to_check.append(Point(i, next_row))
            points_to_check.append(Point(prev_col, location.y))
        else:
            # print("    - top middle edge")
            for i in range(prev_col, next_col + 1):
                points_to_check.append(Point(i, next_row))
            points_to_check.append(Point(prev_col, location.y))
            points_to_check.append(Point(next_col, location.y))
    # are we on the bottom edge?
    elif next_row >= len(schematic):
        # are we on the left edge?
        if prev_col < 0:
            # print("    - bottom left edge")
            for i in range(location.x, next_col + 1):
                points_to_check.append(Point(i, prev_row))
            points_to_check.append(Point(next_col, location.y))
        # are we on the right edge?
        elif next_col >= len(schematic[0]):
            # print("    - bottom right edge")
            for i in range(prev_col, next_col):
                points_to_check.append(Point(i, prev_row))
            points_to_check.append(Point(prev_col, location.y))
        else:
            # print("    - bottom middle edge")
            for i in range(prev_col, next_col + 1):
                points_to_check.append(Point(i, prev_row))
            points_to_check.append(Point(prev_col, location.y))
            points_to_check.append(Point(next_col, location.y))
    # not on the top or bottom, are we on the left edge?
    elif prev_col < 0:
        # print("    - left edge, middle")
        for i in range(location.x, next_col + 1):
            points_to_check.append(Point(i, prev_row))
            points_to_check.append(Point(i, next_row))
        points_to_check.append(Point(next_col, location.y))
    # not on the top or bottom, then we must be on the right edge..
    elif next_col >= len(schematic[0]):
        # print("    - right edge, middle")
        for i in range(prev_col, next_col):
            points_to_check.append(Point(i, prev_row))
            points_to_check.append(Point(i, next_row))
        points_to_check.append(Point(prev_col, location.y))
    else:
        print("don't know how you got here!")
    # print(f"to check: {points_to_check}")
    for point in points_to_check:
        if schematic[point.y][point.x] in symbols:
            return schematic[point.y][point.x]
    return None


def solve_part1(schematic):
    symbols = set()
    parts = []
    for y, row in enumerate(schematic):
        part_num = ""
        for x, char in enumerate(row):
            if char.isdigit():  # we found a part number
                if not part_num:
                    start_loc = Point(x, y)
                part_num += char
                # print(part_num)
                if (
                    x + 1 >= len(row) or not row[x + 1].isdigit()
                ):  # we are done parsing the part number
                    parts.append((part_num, start_loc))
                    part_num = ""
            if not char.isdigit() and char != ".":
                symbols.add(char)

    result = 0
    for part_num, location in parts:
        symbol = symbol_adjacent(schematic, symbols, part_num, location)
        # print(f"part: {part_num}; adjacent_symbol: {symbol}")
        if symbol:
            result += int(part_num)
    return result


class Part:
    def __init__(self, number, start_loc: Point):
        self.number = number
        self.start_loc = start_loc
        self.space = []
        for i in range(start_loc.x, start_loc.x + len(number)):
            self.space.append(Point(i, start_loc.y))

    def __eq__(self, other):
        if self.number == other.number and self.start_loc == other.start_loc:
            return True

    def __repr__(self):
        return f"<Part {self.number}; space: {self.space}>"


def is_gear(schematic, parts, gear_loc):
    prev_row = gear_loc.y - 1
    next_row = gear_loc.y + 1
    prev_col = gear_loc.x - 1
    next_col = gear_loc.x + 1
    adjacent_parts = []
    # search around the location and see if there are two part numbers
    if (
        prev_row >= 0
        and prev_col >= 0
        and next_row < len(schematic)
        and next_col < len(schematic[0])
    ):  # this gear is not on an edge
        # search the part locations to see if one is adjacent
        for part in parts:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if Point(gear_loc.x + i, gear_loc.y + j) in part.space:
                        # print(f"found adjacent part: {part}")
                        if part not in adjacent_parts:
                            adjacent_parts.append(part)
                        # todo: this may not be enough here.. might need to compare part space
    if len(adjacent_parts) >= 2:
        return adjacent_parts
    else:
        return []


def solve_part2(schematic):
    parts = []
    for y, row in enumerate(schematic):
        part_num = ""
        for x, char in enumerate(row):
            if char.isdigit():  # we found a part number
                if not part_num:
                    start_loc = Point(x, y)
                part_num += char
                # print(part_num)
                if (
                    x + 1 >= len(row) or not row[x + 1].isdigit()
                ):  # we are done parsing the part number
                    parts.append(Part(part_num, start_loc))
                    part_num = ""

    gear_ratio_sum = 0
    for y, row in enumerate(schematic):
        for x, char in enumerate(row):
            if char == "*":
                gear_loc = Point(x, y)
                # print(f"potential gear at {gear_loc}")
                adjacent_parts = is_gear(schematic, parts, gear_loc)
                if adjacent_parts:
                    ratio = 1
                    for part in adjacent_parts:
                        ratio *= int(part.number)
                    gear_ratio_sum += ratio
    return gear_ratio_sum


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2023/day03/input", type="char-matrix")
    print(solve_part1(entries))
    print(solve_part2(entries))
