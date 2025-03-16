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

count = 0
for combination in container_combinations:
    if TARGET == sum(combination):
        count += 1

print(count)
