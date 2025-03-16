total = 0

with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:

        # Split line into two pairs by comma
        pair1, pair2 = line.strip().split(',')

        # Split each pair by - to give range, convert to ints
        pair1 = [int(n) for n in pair1.split('-')]
        pair2 = [int(n) for n in pair2.split('-')]

        # Find if either pair overlaps
        # Max val of 1 must be greater than or equal to min val of 2
        if pair1[1] >= pair2[0] and pair1[0] <= pair2[1]:
            total += 1
        
print(total)