from aoc2023.util import get_input

CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def solve_part1(entries):
    game_sum = 0
    for game in entries:
        game_no, game_results = game.split(":")
        game_no = game_no.split()[1]
        game_results = game_results.split(";")
        impossible_game = False
        for result in game_results:
            hand_cubes = result.split(",")
            for cubes in hand_cubes:
                cubes_no, color = cubes.split()
                if int(cubes_no) > CUBES[color]:
                    impossible_game = True
        if not impossible_game:
            game_sum += int(game_no)
    return game_sum

def solve_part2(entries):
    game_sum = 0
    for game in entries:
        game_no, game_results = game.split(":")
        game_no = game_no.split()[1]
        game_results = game_results.split(";")
        min_red = 0
        min_green = 0
        min_blue = 0
        for result in game_results:
            hand_cubes = result.split(",")
            for cubes in hand_cubes:
                cubes_no, color = cubes.split()
                if color == "red":
                    if min_red < int(cubes_no):
                        min_red = int(cubes_no)
                elif color == "green":
                    if min_green < int(cubes_no):
                        min_green = int(cubes_no)
                elif color == "blue":
                    if min_blue < int(cubes_no):
                        min_blue = int(cubes_no)
        game_power = min_red * min_green * min_blue
        game_sum += game_power
    return game_sum
            

if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2023/day02/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
