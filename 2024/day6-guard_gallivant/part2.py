from typing import Generator, Literal

type Map = list[list[str]]
type GuardDirections = Literal["^", ">", "v", "<"]
type GuardPosition = tuple[int, int, GuardDirections]

# INPUT = "test_input.txt"
INPUT = "input.txt"
GUARD_DIRECTIONS: list[GuardDirections] = ["^", ">", "v", "<"]


def _find_guard(map: Map) -> GuardPosition:
    """Search map for guard, get x, y and direction"""
    for y, row in enumerate(map):
        for x, symbol in enumerate(row):
            if symbol in GUARD_DIRECTIONS:
                return x, y, symbol
    raise ValueError("Guard not found")


def _guard_positions(
    map: Map, init_guard_position: GuardPosition
) -> Generator[GuardPosition, None, None]:
    """Generate all guard positions in map, until guard has left map"""
    x, y, direction = init_guard_position

    while True:
        next_x, next_y = x, y
        match direction:
            case "^":
                next_y -= 1
            case ">":
                next_x += 1
            case "v":
                next_y += 1
            case "<":
                next_x -= 1

        # Stop iterating only if guard has left the map
        if not 0 <= next_y < len(map) or not 0 <= next_x < len(map[0]):
            break

        # Rotate if wall has been hit, use current x, y as guard can't move into wall
        if map[next_y][next_x] == "#":
            curr_symbol_idx = GUARD_DIRECTIONS.index(direction)
            # Next symbol in lookup is equivalent to turning right
            direction = GUARD_DIRECTIONS[(curr_symbol_idx + 1) % 4]
        else:
            # We can move to the next position
            x, y = next_x, next_y

        yield x, y, direction


def _is_guard_stuck(
    map: Map, init_guard_position: GuardPosition, limit: int = 10000
) -> bool:
    """
    Return True if guard is stuck in an infite loop
    Error if no loop detected after limit iterations
    """
    # Previous guard movement states stored here
    # Guard is stuck in a loop if a repeat value is found
    previous_positions: set[GuardPosition] = set()
    for counter, position in enumerate(_guard_positions(map, init_guard_position)):
        if counter > limit:
            raise RuntimeError(f"Guard movement limit of {limit} exceeded")

        if position in previous_positions:
            return True
        previous_positions.add(position)

    # Reached edge of map without getting stuck in loop
    return False


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

    guard_position = _find_guard(map)

    total_stuck = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            # Must be a free space
            if map[y][x] != ".":
                continue
            map[y][x] = "#"
            if _is_guard_stuck(map, guard_position):
                total_stuck += 1
                print(total_stuck)
            # Deepcopy could be used so we don't have to cleanup, though memory inefficient
            map[y][x] = "."

    print("Final: ", total_stuck)


if __name__ == "__main__":
    main()
