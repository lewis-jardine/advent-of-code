with open("input.txt", "r") as f:
    input = f.read()

floor = 0
basement = 0

for idx, i in enumerate(input, 1):
    if i == "(":
        floor += 1
    elif i == ")":
        floor -= 1

    if floor < 0:
        basement = idx
        break

print(basement)