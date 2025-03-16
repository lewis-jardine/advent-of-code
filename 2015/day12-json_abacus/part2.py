import json


def recurse_sum(x) -> int:
    """recursivly find sum of input and all its children"""
    total = 0
    if isinstance(x, dict):
        for key, val in x.items():
            # "red" negates entire dict
            if val == "red":
                return 0
            total += recurse_sum(val)
    elif isinstance(x, list):
        for val in x:
            total += recurse_sum(val)
    elif isinstance(x, int):
        total = x
    return total


if __name__ == "__main__":
    with open("input.json") as f:
        json_input = json.load(f)
    
    total = recurse_sum(json_input)
    print(total)
