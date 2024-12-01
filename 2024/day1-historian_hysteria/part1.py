"""
input format:
3   4
4   3
2   5
1   3
3   9
3   3
"""

with open("input.txt") as f:
    lines = f.readlines()

# Split each line into 2x numbers, append each to a seperate list
list1 = []
list2 = []
for line in lines:
    x, y = line.split()
    list1.append(int(x))
    list2.append(int(y))

# Sort so that equivalent numbers can be compared
list1.sort()
list2.sort()

# Get distance (abs value) at each idx
distance = 0
for idx in range(len(list1)):
    distance += abs((list1[idx] - list2[idx]))

print(distance)
