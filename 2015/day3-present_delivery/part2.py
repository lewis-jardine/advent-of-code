"""
Assume start is 0,0. Up and right is positive, down and left negative.
Record already visited houses in nested dicts. 
First level key is x, value is dict with second level key y and bool:
houses = {
    0: {
        0: True,
        1: True,
        2: True
    },
    1: {
        2: True
    }
}
"""
with open("input.txt", "r") as f:
    moves = f.read()

# Starts at (0,0 so thatl always be filled
total = 1
houses = {
    0: {
        0: True
    }
}

# Split moves into santas and robo santas
santa_moves = []
robo_moves = []
count = 0
for move in moves:
    # If even
    if count % 2 == 0:
        santa_moves.append(move)
    else:
        robo_moves.append(move)
    count += 1


def deliver_presents(moves, houses):
    pres_count = 0
    pos = [0, 0]
    for move in moves:

        # Move up, +1 y
        if move == "^":
            pos[1] += 1
        # Move right, +1 x
        if move == ">":
            pos[0] += 1
        # Move down, -1 y
        if move == "v":
            pos[1] -= 1
        # Move left, -1 x
        if move == "<":
            pos[0] -= 1
            
        # Prevent key error as first level may not be filled
        if pos[0] not in houses:
            houses[pos[0]] = {}
        # Check if house has not been visited, add to tracker if so
        if pos[1] not in houses[pos[0]]:
            houses[pos[0]][pos[1]] = True
            pres_count += 1
        
    return pres_count, houses

# Run deliver function twice, once for santa, once for robo santa
santa_total, houses = deliver_presents(santa_moves, houses)
robo_total, houses = deliver_presents(robo_moves, houses)
total += santa_total + robo_total
print(total)