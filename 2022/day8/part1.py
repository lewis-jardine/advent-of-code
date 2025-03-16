with open("input.txt", "r") as f:
    lines = f.readlines()

# Store grid in 2d array of nested lists
# [0][0] is top left tree, [0][1] is one to right of that etc.
trees = []
visible_count = 0
for line in lines:
    line = line.strip() 
    # Convert string to list of ints
    line = [int(x) for x in line]
    trees.append(line)

# For each tree, store its value, iterate over all above, below and either side
# If any value on these 4 seperate passes > its value, not visible. 
# Repeat with all other trees. 
right_tree_idx = len(trees) - 1
bottom_tree_idx = len(trees[0]) - 1
for tree_y, row in enumerate(trees):
    for tree_x, tree in enumerate(row):
        # Assume visible until higher tree reached 
        # Start from left grid edge, check until tree reached.
        x = 0
        while x != tree_x:
            # Grab current tree value, check against tree height
            if trees[tree_y][x] >= tree:
                # Tree invisble from left, break loop
                break
            x += 1
        # If loop completes, then tree must be visible
        else:
            visible_count += 1
            continue

        # Check from top grid down to tree
        y = 0
        while y != tree_y:
            if trees[y][tree_x] >= tree:
                break
            y += 1
        else:
            visible_count += 1
            continue

        # Check from right grid left to tree
        x = right_tree_idx
        while x != tree_x:
            if trees[tree_y][x] >= tree:
                break
            x -= 1
        else:
            visible_count += 1
            continue
        
        # Check from bottom grid up to tree
        y = bottom_tree_idx
        while y != tree_y:
            if trees[y][tree_x] >= tree:
                break
            y -= 1
        else:
            visible_count += 1
        

print(visible_count)