from aoc2023.util import get_input


class CustomMapping:
    def __init__(self, source, destination, length):
        self.source = source
        self.destination = destination
        self.length = length
        self.delta = destination - source

    def __repr__(self):
        return f"<CustomMap: s:{self.source} d:{self.destination} l:{self.length}>"


class Map:
    def __init__(self, name):
        self.name = name
        self.custom_maps = []

    def add_custom_map(self, custom_map):
        dest = custom_map[0]
        source = custom_map[1]
        length = custom_map[2]
        self.custom_maps.append(CustomMapping(source, dest, length))

    def __repr__(self):
        return f"<{self.name} custom_maps: {self.custom_maps}>"


def build_map(mapping):
    _map = Map(mapping.pop(0))
    for m in mapping:
        _map.add_custom_map(list(map(int, m.split())))
    return _map


def use_map(_map: Map, source):
    use_cm = None
    for cm in _map.custom_maps:
        if source >= cm.source and source < cm.source + cm.length:
            use_cm = cm
            # print(f"in use_map - found cm to use: {cm}")
            break
    if use_cm:
        result = source + cm.delta
    else:
        result = source
    return result


def solve_part1(entries):
    seeds = list(map(int, entries[0][0].split(":")[1].split()))
    seed_to_soil_map = build_map(entries[1])
    soil_to_fertilizer_map = build_map(entries[2])
    fertilizer_to_water_map = build_map(entries[3])
    water_to_light_map = build_map(entries[4])
    light_to_temperature_map = build_map(entries[5])
    temparature_to_humidity_map = build_map(entries[6])
    humidity_to_location_map = build_map(entries[7])
    """
    print(f"seeds: {seeds}")
    print(f"{seed_to_soil_map}")
    print(f"{soil_to_fertilizer_map}")
    print(f"{fertilizer_to_water_map}")
    print(f"{water_to_light_map}")
    print(f"{light_to_temperature_map}")
    print(f"{temparature_to_humidity_map}")
    print(f"{humidity_to_location_map}")
    """
    min_location = 0
    for seed in seeds:
        # print(f"seed: {seed}")
        seed_to_soil = use_map(seed_to_soil_map, seed)
        # print(f" - soil: {seed_to_soil}")
        soil_to_fertilizer = use_map(soil_to_fertilizer_map, seed_to_soil)
        # print(f" - fert: {soil_to_fertilizer}")
        fertilizer_to_water = use_map(fertilizer_to_water_map, soil_to_fertilizer)
        # print(f" - watr: {fertilizer_to_water}")
        water_to_light = use_map(water_to_light_map, fertilizer_to_water)
        # print(f" - lght: {water_to_light}")
        light_to_temperature = use_map(light_to_temperature_map, water_to_light)
        # print(f" - temp: {light_to_temperature}")
        temparature_to_humidity = use_map(
            temparature_to_humidity_map, light_to_temperature
        )
        # print(f" - hmdt: {temparature_to_humidity}")
        humidity_to_location = use_map(
            humidity_to_location_map, temparature_to_humidity
        )
        # print(f" - locn: {humidity_to_location}")
        if min_location == 0 or humidity_to_location < min_location:
            min_location = humidity_to_location
    return min_location


def use_map2(_map: Map, intervals):
    # sort our custom mappings
    _map.custom_maps.sort(key=lambda x: x.source)
    result_intervals = []
    for interval in intervals:
        for cm in _map.custom_maps:
            if interval[0] < cm.source:  # less than lowest custom map start
                result_intervals.append(range(interval[0], cm.source))
                result_intervals.append(range(cm.source, cm.source + cm.delta))
            ## keep going ... how do we
    return result_intervals


"""
    use_cm = None
    for cm in _map.custom_maps:
        if source >= cm.source and source < cm.source + cm.length:
            use_cm = cm
            # print(f"in use_map - found cm to use: {cm}")
            break
    if use_cm:
        result = source + cm.delta
    else:
        result = source
    return result
"""


def solve_part2(entries):
    seeds = list(map(int, entries[0][0].split(":")[1].split()))
    seed_to_soil_map = build_map(entries[1])
    soil_to_fertilizer_map = build_map(entries[2])
    fertilizer_to_water_map = build_map(entries[3])
    water_to_light_map = build_map(entries[4])
    light_to_temperature_map = build_map(entries[5])
    temparature_to_humidity_map = build_map(entries[6])
    humidity_to_location_map = build_map(entries[7])
    min_location = 0
    for i, k in zip(seeds[0::2], seeds[1::2]):
        _seeds = range(i, i + k)
        print(f"seed_range: {_seeds}")
        seed_to_soil_ranges = use_map2(
            seed_to_soil_map,
            [_seeds],
        )
        print(f" - soil: {seed_to_soil_ranges}")
        soil_to_fertilizer_ranges = use_map2(
            soil_to_fertilizer_map,
            seed_to_soil_ranges,
        )
        print(f" - fert: {soil_to_fertilizer_ranges}")
        """
        fertilizer_to_water = use_map(fertilizer_to_water_map, soil_to_fertilizer)
        # print(f" - watr: {fertilizer_to_water}")
        water_to_light = use_map(water_to_light_map, fertilizer_to_water)
        # print(f" - lght: {water_to_light}")
        light_to_temperature = use_map(light_to_temperature_map, water_to_light)
        # print(f" - temp: {light_to_temperature}")
        temparature_to_humidity = use_map(
            temparature_to_humidity_map, light_to_temperature
        )
        # print(f" - hmdt: {temparature_to_humidity}")
        humidity_to_location = use_map(
            humidity_to_location_map, temparature_to_humidity
        )
        # print(f" - locn: {humidity_to_location}")
        if min_location == 0 or humidity_to_location < min_location:
            min_location = humidity_to_location
        """
    return min_location


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2023/day05/input", type="nlnl")
    print(solve_part1(entries))
    print(solve_part2(entries))
