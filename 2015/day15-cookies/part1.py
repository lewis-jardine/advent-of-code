from itertools import combinations
from math import prod

QUANTITY_INGREDIENTS = 100
INPUT_PATH = "input.txt"


with open(INPUT_PATH) as f:
    lines = f.readlines()

# Read in ingredient properties
ingredients = []
for line in lines:
    line = line.split()
    # [:-1] is required to strip last char from certain fields
    ingredients.append(
        {
            "capacity": int(line[2][:-1]),
            "durability": int(line[4][:-1]),
            "flavor": int(line[6][:-1]),
            "texture": int(line[8][:-1]),
            "calories": int(line[10]),
        }
    )


def partitions(n, k):
    """generate all permutations of k ints of val up to n"""
    for c in combinations(range(n + k - 1), k - 1):
        yield [b - a - 1 for a, b in zip((-1,) + c, c + (n + k - 1,))]


ratios = partitions(QUANTITY_INGREDIENTS, len(ingredients))

# Get score of each ingredient ratio
high_score = 0
for ratio in ratios:
    score = {"capacity": 0, "durability": 0, "flavor": 0, "texture": 0}
    for ingredient_id, quantity in enumerate(ratio):
        for property in score:
            score[property] += ingredients[ingredient_id][property] * quantity
    # Calculate total score of that ratio only if all scores are positive
    if all([val > 0 for val in score.values()]):
        total_score = prod(score.values())
    else:
        total_score = 0
    if total_score > high_score:
        high_score = total_score

print(high_score)
