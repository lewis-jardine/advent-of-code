import math

with open("input.txt", "r") as f:
    lines = f.readlines()
lines = [
    'R 5',
    'U 8',
    'L 8',
    'D 3',
    'R 17',
    'D 10',
    'L 25',
    'U 20'
]

# Store points tails visited in dict with key [x, y] and val true or false
visited = {(0, 0): True}
visited_count = 1

# Store head to tail positions in list with idx 0 through 9
pos = [[0, 0] for _ in range(10)]

for line in lines:

    # Get direction and number of moves
    line = line.strip().split()
    direction = line[0]
    n_moves = int(line[1])

    for n in range(n_moves):

        # Move each segment in turn until no more moves are necessary
        # First move head
        match direction:
            case "U":
                pos[0][1] += 1
            case "D":
                pos[0][1] -= 1
            case "R":
                pos[0][0] += 1
            case "L":
                pos[0][0] -= 1
        
        # Move each segment as well if required
        for i in range(1, len(pos)):

            # Calculate distance from previous section
            dist = [x - y for x, y in zip(pos[i - 1], pos[i])]

            # Check which (if any dist is 2),
            # Change that to a 1, add both to pos 
            if abs(dist[0]) == 2:
                pos[i][0] += dist[0] // 2
                pos[i][1] += dist[1]
            elif abs(dist[1]) == 2:
                pos[i][0] += dist[0]
                pos[i][1] += dist[1] // 2
            else:
                break

            # Record point as visited by section 9 only
            if i == 9:
                if tuple(pos[9]) not in visited:
                    visited[tuple(pos[9])] = True
                    visited_count += 1

print(visited_count)