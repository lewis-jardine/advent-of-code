import re

INPUT = "input.txt"
with open(INPUT) as f:
    lines = f.readlines()

NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

# Regex will match any overlapping values in NUMBERS dict
# Match will always be in capture group 1
numbers_regex = re.compile(f"(?=({'|'.join(NUMBERS.keys())}|\d))")

total = 0
for line in lines:
    # Finds all numbers (spelled or digit) in order
    digits = [m.group(1) for m in numbers_regex.finditer(line)]
    # Tranforms spelled numbers to digits
    digits = [NUMBERS[x] if x in NUMBERS else x for x in digits]
    # Concatenate first and last digits together (same digit if len 1)
    n = int(digits[0] + digits[-1])
    total += n

print(total)
