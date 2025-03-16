from itertools import permutations
import numpy as np

"""
Read in city pairs with distance as array in form:
    [[65, 28, 60], [81, 39, 112], [32, 39, 141]]

This can be created in multiple passes
1. Create lookup table of each city with int 
2. Init 2D array with size n_cities * n_cities
3. Assign distance val as item in array with index of each city
    - This will add two vals to array, as cities can be either way round
        eg. 0 to 2 = 55, array[0][2] = 55 and array[2][0] = 55
    - Item with index x = y is the distance of city to itself
        eg. array[2][2] = 0

Once distance matrix generated, find all n length permutations of cities.
Get total distance of each permutation, store greatest and return.
"""

with open("input.txt") as f:
    lines = f.readlines()

# Distance matrix creation
# Step 1, create loookup table of city idx pair
n = 0
city_idx = {}

for line in lines:
    line = line.split()
    cities = (line[0], line[2])
    for city in cities:
        if city not in city_idx:
            city_idx[city] = n
            n += 1

# Step 2, init 2d array with size n * n
distances = np.zeros((n, n), int)

# Step 3, assign distance val for each city as item in array
for line in lines:
    line = line.split()
    city1, city2, distance = line[0], line[2], int(line[4])
    distances[city_idx[city1]][city_idx[city2]] = distance
    distances[city_idx[city2]][city_idx[city1]] = distance

# Find city path permutation with greatest distance
best_distance = None
paths = permutations(city_idx.values(), n)

for path in paths:
    distance = 0
    prev_city = None
    for city in path:
        if prev_city is not None:
            distance += distances[prev_city][city]
        prev_city = city
    if best_distance is None or best_distance < distance:
        best_distance = distance

print(best_distance)