with open("input.txt", "r") as f:
    input = f.read()

floor = 0

for i in input:
    if i == "(":
        floor += 1
    elif i == ")":
        floor -= 1

print(floor)