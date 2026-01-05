def read_map(map_path: str) -> list[list[int]]:
    with open(map_path) as f:
        trail_map = f.read().splitlines()
    # get into list of lists so that [y][x] = x,y
    return [[int(y) for y in x] for x in trail_map]


def count_trailhead_scores(trail_map: list[list[int]]) -> int:
    total = 0
    for y, row in enumerate(trail_map):
        for x, tile in enumerate(row):
            if tile == 0:
                total += traverse_trailhead(trail_map, (y, x), set())
    return total


def traverse_trailhead(
    trail_map: list[list[int]],
    start_tile: tuple[int, int],
    ends_store: set[tuple[int, int]],
) -> int:
    total = 0
    # Check tiles up (+1, 0), right (0, +1), down (-1,0) left (0, -1)
    offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    start_tile_value = trail_map[start_tile[0]][start_tile[1]]
    for offset in offsets:
        new_tile = (start_tile[0] + offset[0], start_tile[1] + offset[1])
        # Check new tile within map bounds
        if not (
            0 <= new_tile[0] < len(trail_map) and 0 <= new_tile[1] < len(trail_map[0])
        ):
            continue
        new_tile_value = trail_map[new_tile[0]][new_tile[1]]
        # Trail end found, add 1 to total if it is a new end, add to store for future checks
        if new_tile_value == 9:
            if new_tile in ends_store:
                return total
            ends_store.add(new_tile)
            return total + 1
        # Next tile has been found, traverse to it and repeat
        elif new_tile_value == start_tile_value + 1:
            traverse_trailhead(trail_map, new_tile, ends_store)
        # No valid trail path, continue to next tile
    return total


def main():
    print("success")


if __name__ == "__main__":
    main()
