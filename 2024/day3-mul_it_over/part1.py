import re

# INPUT = "test_input.txt"
INPUT = "input.txt"
REGEX = r"mul\((\d+),(\d+)\)"


def main():
    with open(INPUT) as f:
        chars = f.read()

    matches = re.finditer(REGEX, chars)

    total = 0
    for match in matches:
        # 2 capture groups, one for each match
        x, y = match.groups()
        total += int(x) * int(y)

    print(total)


if __name__ == "__main__":
    main()
