import math

with open("input.txt", "r") as f:
    lines = f.readlines()

# Store points tails visited in dict with key [x, y] and val true or false
visited = {(0, 0): True}
visited_count = 1

# Store current head and tail positions as [x, y]
head_pos = [0, 0]
tail_pos = [0, 0]

for line in lines:

    # Get direction and number of moves
    line = line.strip().split()
    direction = line[0]
    n_moves = int(line[1])

    # Move head then tail n_moves in direction
    for n in range(n_moves):
        last_head_pos = head_pos.copy()

        # First move head
        match direction:
            case "U":
                head_pos[1] += 1
            case "D":
                head_pos[1] -= 1
            case "R":
                head_pos[0] += 1
            case "L":
                head_pos[0] -= 1
        
        # Then if tail is at least 2 units away,
        # Move it to the last head pos 
        if math.dist(head_pos, tail_pos) >= 2:
            tail_pos = last_head_pos

            # Record point as visited by tail
            if tuple(tail_pos) not in visited:
                visited[tuple(tail_pos)] = True
                visited_count += 1

print(visited_count)