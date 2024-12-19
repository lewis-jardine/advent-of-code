import re

# INPUT = "test_input2.txt"
INPUT = "input.txt"
REGEX_MUL = r"mul\((\d+),(\d+)\)"
REGEX_DO_DONT = r"(do\(\)|don't\(\))"


def sum_mul_matches(input: str) -> int:
    matches = re.finditer(REGEX_MUL, input)
    total = 0
    for match in matches:
        # 2 capture groups, one for each match
        x, y = match.groups()
        total += int(x) * int(y)
    return total


def main():
    with open(INPUT) as f:
        chars = f.read()

    # Split on do/dont so we have [aaa, do(), bbb, ccc, don't()]
    do_dont_parts = re.split(REGEX_DO_DONT, chars)

    total = 0
    # Initially start enabled
    enabled = True
    for part in do_dont_parts:
        if part == "do()":
            enabled = True
            continue
        elif part == "don't()":
            enabled = False
            continue

        if enabled:
            total += sum_mul_matches(part)

    print(total)


if __name__ == "__main__":
    main()
