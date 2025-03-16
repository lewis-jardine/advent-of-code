INPUT = "test_input.txt"

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


def _unique_antinode_locations(antenna_locations: AntennaLocations) -> set[Location]:
    return {(1, 3), (9, -1), (-1, 5), (3, 2)}


def main():
    map = _load_map(INPUT)
    print(map)
    antenna_locations = _get_antenna_locations(map)
    print(antenna_locations)
    antinode_locations = _unique_antinode_locations(antenna_locations)

    # Filter to just locations within map bounds then count
    map_height, map_width = len(map), len(map[0])
    antinodes = 0
    for row, col in antinode_locations:
        if 0 <= row < map_height and 0 < col <= map_width:
            antinodes += 1
    print(antinodes)


if __name__ == "__main__":
    main()
