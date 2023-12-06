from aoc2023.util import get_input

from typing import Iterable


class Race:
    def __init__(self, race_number, duration, record):
        self.number = race_number
        self.duration = duration
        self.record = record

    def __repr__(self):
        return f"<Race {self.number}: {self.duration} ms, record: {self.record} mm>"


def parse_input1(input) -> Iterable[Race]:
    races = list()
    times = list(map(int, input[0].split(":")[1].split()))
    distances = list(map(int, input[1].split(":")[1].split()))
    for idx, race in enumerate(zip(times, distances)):
        races.append(Race(race_number=idx + 1, duration=race[0], record=race[1]))
    return races


def solve_part1(entries):
    races = parse_input1(entries)
    results = None
    for race in races:
        ways_to_win = 0
        for hold_time in range(1, race.duration):
            time_remaining = race.duration - hold_time
            distance_traveled = hold_time * time_remaining
            if distance_traveled > race.record:
                ways_to_win += 1
        if not results:
            results = ways_to_win
        else:
            results *= ways_to_win
    return results


def parse_input2(input) -> Race:
    duration = int("".join(input[0].split(":")[1].split()))
    record = int("".join(input[1].split(":")[1].split()))
    return Race(0, duration, record)


def solve_part2(entries):
    race = parse_input2(entries)
    shortest_hold_time = 0
    longest_hold_time = 0
    for hold_time in range(1, race.duration):
        # find the shortest hold time that wins
        time_remaining = race.duration - hold_time
        distance_traveled = hold_time * time_remaining
        if distance_traveled > race.record:
            shortest_hold_time = hold_time
            break
    for hold_time in range(race.duration, 0, -1):
        # find the longest hold time that wins
        time_remaining = race.duration - hold_time
        distance_traveled = hold_time * time_remaining
        if distance_traveled > race.record:
            longest_hold_time = hold_time
            break
    return longest_hold_time - shortest_hold_time + 1


if __name__ == "__main__":  # pragma: no cover
    races = get_input("aoc2023/day06/input")
    print(solve_part1(races))
    print(solve_part2(races))
