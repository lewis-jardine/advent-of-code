import numpy as np
from itertools import permutations
"""
Read in happiness vals as 2D array in form:
    [[0, -2, 60], [81, 39, 112], [32, 39, 141]]
Value x is source person, y is target person.
eg. Alice (source) would lose 2 happiness units by sitting next to Bob (target)

This can be created in multiple passes
1. Assign ID to each person, store in lookup table 
2. Init 2D array with size n_persons * n_persons
3. Assign happiness val as item in array with index of each person

Once happiness array has been created, find all permutations of n_persons numbers
For each number look up both neighbours happiness by array[number][neighbour]
Add to total, highest permutation wins.
"""
with open("input2.txt") as f:
    lines = f.readlines()

# Happiness matrix creation
# Step 1: Assign person ID in lookup table
n = 0
person_idx = {}

for line in lines:
    line = line.split()
    person = line[0]
    if person not in person_idx:
        person_idx[person] = n
        n += 1

# Step 2, init 2d array with size n * n
happiness_arr = np.zeros((n, n), int)

# Step 3, assign distance val for each city as item in array
for line in lines:
    line = line.split()
    # Strip last char from target as its '.'
    source, sign, happiness, target = line[0], line[2], int(line[3]), line[10][:-1]
    if sign == "lose":
        happiness *= -1
    happiness_arr[person_idx[source]][person_idx[target]] = happiness

# Find person seatign permutation with greatest happiness
best_happiness = None
paths = permutations(person_idx.values(), n)

for path in paths:
    happiness = 0
    for idx, person in enumerate(path):
        if idx == 0:
            happiness += happiness_arr[person][path[-1]]
            happiness += happiness_arr[person][path[1]]
        elif idx == len(path) - 1:
            happiness += happiness_arr[person][path[idx - 1]]
            happiness += happiness_arr[person][path[0]]
        else:
            happiness += happiness_arr[person][path[idx - 1]]
            happiness += happiness_arr[person][path[idx + 1]]
    if best_happiness is None or best_happiness < happiness:
        best_happiness = happiness

print(best_happiness)