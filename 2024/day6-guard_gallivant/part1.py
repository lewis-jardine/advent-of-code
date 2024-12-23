from typing import Literal

type GuardDirections = Literal["^", ">", "v", "<"]
type Map = list[list[str]]

# INPUT = "test_input.txt"
INPUT = "input.txt"
GUARD_DIRECTIONS: list[GuardDirections] = ["^", ">", "v", "<"]


def find_guard(map: Map) -> tuple[int, int, GuardDirections]:
    """Get x and y of guard"""
    for y, row in enumerate(map):
        for x, symbol in enumerate(row):
            if symbol in GUARD_DIRECTIONS:
                return x, y, symbol
    raise ValueError("Guard not found")


def move_guard(map: Map) -> bool:
    """
    Attempt to move guard one space in current direction on supplied map.
    Turn right if obstacle encountered, fill in previous spot with 'x'

    Return True if move completed sucesfully, else False if moved off map
    """
    curr_x, curr_y, curr_symbol = find_guard(map)

    new_x, new_y = curr_x, curr_y
    match curr_symbol:
        case "^":
            new_y -= 1
        case ">":
            new_x += 1
        case "v":
            new_y += 1
        case "<":
            new_x -= 1

    # Check if new spot is on map before getting idx error on new spot lookup
    if not 0 <= new_y < len(map) or not 0 <= new_x < len(map[0]):
        return False

    new_symbol = map[new_y][new_x]
    if new_symbol == "." or new_symbol == "x":
        map[curr_y][curr_x] = "x"
        map[new_y][new_x] = curr_symbol
    elif new_symbol == "#":
        curr_symbol_idx = GUARD_DIRECTIONS.index(curr_symbol)
        # Next symbol in lookup will be a right turn
        map[curr_y][curr_x] = GUARD_DIRECTIONS[(curr_symbol_idx + 1) % 4]
    else:
        raise ValueError(f"Unknown symbol ({new_symbol}) at: {new_x}, {new_y}")
    return True


def count_visited_positions(map: Map) -> int:
    """A visited position is one with 'x' on map. Also include current position"""
    total = 0
    for row in map:
        for position in row:
            if position == "x" or position in GUARD_DIRECTIONS:
                total += 1
    return total


def display_map(map: Map) -> None:
    display_map = ["".join(row) for row in map]
    for row in display_map:
        print(row)
    print("\n")


def main():
    with open(INPUT) as file:
        # file is in format ['..#', '.^.', '#..']
        # Where . = free postion, # = occupied postion and ^ = guard position
        lines = file.readlines()
        # Strip removes final \n, split is required to allow letter in row to be changed
        map: Map = [list(line.strip()) for line in lines]

    while True:
        success = move_guard(map)
        if success == False:
            break

    print(count_visited_positions(map))


if __name__ == "__main__":
    main()
