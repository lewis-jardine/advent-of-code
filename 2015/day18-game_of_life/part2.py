STEPS = 100
INPUT = "input.txt"


def assign_state(lines: list[str]) -> list[list[bool]]:
    """
    Light state will be stored in 2D matrix where on is True and off is False:

        state = [[True, True, False], [True, False, False], [False, False, False]]

    Individual light state can be accessed by state[y][x], where 0, 0 is top left
    So light furthest right on top level will be accessed by state[0][2]
    """
    state = []
    for line in lines:
        row = []
        for light in line.strip():
            if light == "#":
                row.append(True)
            else:
                row.append(False)
        state.append(row)
    state = turn_on_corners(state)
    return state


def animate_step(state: list[list[bool]]) -> list[list[bool]]:
    # Create copy of new state to return to avoid side effects
    new_state = [row[:] for row in state]
    for light_y, row in enumerate(state):
        for light_x, light in enumerate(row):
            neighbours = get_lights_neighbours(state, light_x, light_y)
            # print(f"{light_x=} {light_y=} {neighbours=} {light=}")
            if light:
                if neighbours != 2 and neighbours != 3:
                    new_state[light_y][light_x] = False
            else:
                if neighbours == 3:
                    new_state[light_y][light_x] = True
            # print(f"{light} to {state[light_y][light_x]} {neighbours} neighbours")
    # Corners may have been changed, they should not have been
    new_state = turn_on_corners(new_state)
    return new_state


def get_lights_neighbours(state: list[list[bool]], light_x: int, light_y: int) -> int:
    """Find number of given lights neighbours that are on"""
    neighbours = 0
    for offset_y in range(-1, 2):
        # x and y are the coords of neighbour light currently being checked
        y = offset_y + light_y
        for offset_x in range(-1, 2):
            x = offset_x + light_x
            # Avoid index error by skipping neighbour if outside array
            outside_array = y < 0 or x < 0 or y >= len(state) or x >= len(state[0])
            # Also discount self as neighbour
            if outside_array or (offset_x == 0 and offset_y == 0):
                continue
            if state[y][x]:
                neighbours += 1
    return neighbours


def turn_on_corners(state: list[list[bool]]):
    """*Part2 exclusive* change state of all array 'corners' to True"""
    new_state = [row[:] for row in state]
    new_state[0][0] = True
    new_state[-1][0] = True
    new_state[0][-1] = True
    new_state[-1][-1] = True
    return new_state


def count_lights_on(state: list[list[bool]]) -> int:
    """Count total number of lights currently on"""
    count = 0
    for row in state:
        for light in row:
            if light:
                count += 1
    return count


if __name__ == "__main__":
    with open(INPUT) as f:
        lines = f.readlines()
    state = assign_state(lines)
    for step in range(STEPS):
        print(f"step {step}: {count_lights_on(state)}")
        state = animate_step(state)
    print(f"step {STEPS}: {count_lights_on(state)}")
