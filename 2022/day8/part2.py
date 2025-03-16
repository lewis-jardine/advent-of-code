with open("input.txt", "r") as f:
    lines = f.readlines()

# lines = [
#     '30373',
#     '25512',
#     '65332',
#     '33549',
#     '35390'
# ]
# Store grid in 2d array of nested lists
# [0][0] is top left tree, [0][1] is one to right of that etc.
trees = []
highscore = 0
for line in lines:
    line = line.strip() 
    # Convert string to list of ints
    line = [int(x) for x in line]
    trees.append(line)

# For each tree, store its value, iterate over all above, below and either side
# Iterate score until tree with height > curr tree height is reached
# Repeat with all other trees. 
right_tree_idx = len(trees) - 1
bottom_tree_idx = len(trees[0]) - 1
for tree_y, row in enumerate(trees):
    for tree_x, tree in enumerate(row):
        # Start from tree, move left until grid edge (-1) is reached
        score_left = 0
        x = tree_x
        while x != 0:
            x -= 1
            score_left += 1
            # Grab current tree value, check against tree height
            if trees[tree_y][x] >= tree:
                # Tree blocking view, break loop
                break

        # Check from tree up to top grid edge
        score_up = 0
        y = tree_y
        while y != 0:
            y -= 1
            score_up += 1
            if trees[y][tree_x] >= tree:
                break

        # Check from tree to right grid edge
        score_right = 0
        x = tree_x
        while x != right_tree_idx:
            x += 1
            score_right += 1
            if trees[tree_y][x] >= tree:
                break
        
        # Check from tree to bottom grid edge
        score_down = 0
        y = tree_y
        while y != bottom_tree_idx:
            y += 1
            score_down += 1
            if trees[y][tree_x] >= tree:
                break
        
        score = score_left * score_up * score_right * score_down
        if score > highscore:
            highscore = score

print(highscore)