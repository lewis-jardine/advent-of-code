from itertools import combinations

# INPUT = "test_input.txt"
INPUT = "input.txt"

type Map = list[str]
type Location = tuple[int, int]
type AntennaLocations = dict[str, list[Location]]


def _load_map(input_path: str) -> Map:
    with open(input_path) as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


def _get_antenna_locations(map: Map) -> AntennaLocations:
    """x, y of each antenna on map, organised by frequency in dict"""
    locations: AntennaLocations = {}
    for row_idx, row in enumerate(map):
        for col_idx, cell in enumerate(row):
            # Any non "." on map is an antenna
            if cell == ".":
                continue
            if cell in locations:
                locations[cell].append((row_idx, col_idx))
            else:
                locations[cell] = [(row_idx, col_idx)]
    return locations


def _find_unique_antinodes(antenna_locations: AntennaLocations) -> set[Location]:
    antinodes: set[Location] = set()
    for locations in antenna_locations.values():
        for pair in combinations(locations, 2):
            antinodes.update(_calculate_antinode_pairs(pair))
    return antinodes


def _calculate_antinode_pairs(
    antenna_pair: tuple[Location, Location],
) -> tuple[Location, Location]:
    """Find both antinodes of a set of two antenna"""
    antenna1, antenna2 = antenna_pair
    # First find the vector from antenna 1 to 2
    row_diff, col_diff = antenna2[0] - antenna1[0], antenna2[1] - antenna1[1]
    # Antinode 1 is inverted vector applied to 1 and antinode 2 is vector applied to 2
    antinode1 = (antenna1[0] - row_diff, antenna1[1] - col_diff)
    antinode2 = (antenna2[0] + row_diff, antenna2[1] + col_diff)
    return antinode1, antinode2


def main():
    map = _load_map(INPUT)
    antenna_locations = _get_antenna_locations(map)
    antinode_locations = _find_unique_antinodes(antenna_locations)

    # Filter to just locations within map bounds then count
    map_height, map_width = len(map), len(map[0])
    antinodes = 0
    for row, col in antinode_locations:
        if 0 <= row < map_height and 0 <= col < map_width:
            antinodes += 1
    print(antinodes)


if __name__ == "__main__":
    main()
