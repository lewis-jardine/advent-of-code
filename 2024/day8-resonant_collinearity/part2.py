# import math
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


def _find_unique_antinodes(
    antenna_locations: AntennaLocations, row_limit: int, col_limit: int
) -> set[Location]:
    antinodes: set[Location] = set()
    for locations in antenna_locations.values():
        for pair in combinations(locations, 2):
            antinodes.update(_calculate_antinodes(pair, row_limit, col_limit))
    return antinodes


def _calculate_antinodes(
    antenna_pair: tuple[Location, Location], row_limit: int, col_limit: int
) -> list[Location]:
    """Antinodes occur at every position in line of antenna"""
    antenna1, antenna2 = antenna_pair
    # First find the vector from antenna 1 to 2
    row_diff, col_diff = antenna2[0] - antenna1[0], antenna2[1] - antenna1[1]

    # Keep applying vector positivly from antenna 1 until limit is reached
    antinodes: list[Location] = []
    new_antinode = antenna1
    while True:
        new_antinode = (new_antinode[0] + row_diff, new_antinode[1] + col_diff)
        if not 0 <= new_antinode[0] < row_limit or not 0 <= new_antinode[1] < col_limit:
            break
        antinodes.append(new_antinode)
    # Then repeat negatively from antenna 2
    new_antinode = antenna2
    while True:
        new_antinode = (new_antinode[0] - row_diff, new_antinode[1] - col_diff)
        if not 0 <= new_antinode[0] < row_limit or not 0 <= new_antinode[1] < col_limit:
            break
        antinodes.append(new_antinode)
    return antinodes


def main():
    map = _load_map(INPUT)
    antenna_locations = _get_antenna_locations(map)
    antinodes = _find_unique_antinodes(antenna_locations, len(map), len(map[0]))
    print(len(antinodes))


if __name__ == "__main__":
    main()
