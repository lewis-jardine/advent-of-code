from itertools import combinations, chain

TARGET = 150

with open("input.txt") as f:
    lines = f.readlines()

containers = []
for line in lines:
    containers.append(int(line.strip()))

# Get all possible combinations of containers of any length (aka powerset)
container_combinations = chain.from_iterable(
    combinations(containers, r) for r in range(len(containers) + 1)
)

# Combinations are ordered by len, once combination found at len, all future lens are discarded
min_containers = 0
count = 0
for combination in container_combinations:
    if TARGET == sum(combination):
        # Signifies that smallest combination has been found and next len combinations has been reached
        if min_containers and len(combination) > min_containers:
            break
        min_containers = len(combination)
        count += 1

print(count)
