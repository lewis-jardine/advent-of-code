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
list1: list[int] = []
list2: list[int] = []
appearances: dict[int, int] = {}
for line in lines:
    x, y = line.split()
    list1.append(int(x))

    # We also need to store how often each number in list 2 appears
    y = int(y)
    if y in appearances:
        appearances[y] += 1
    else:
        appearances[y] = 1
    list2.append(y)

# Find appearances of each val in list1 to add to similarity. If not there, 0 similarity
similarity = 0
for n in list1:
    if n in appearances:
        similarity += n * appearances[n]

print(similarity)
