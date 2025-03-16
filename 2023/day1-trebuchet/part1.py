with open("input.txt") as f:
    lines = f.readlines()

total = 0
for line in lines:
    # Remove all non-digits from string (aka list of chars)
    digits = [x for x in line if x.isdigit()]
    # Concatenate first and last digits together (same digit if len 1)
    n = int(digits[0] + digits[-1])
    total += n

print(total)
