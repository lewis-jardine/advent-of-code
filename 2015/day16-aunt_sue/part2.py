TARGET = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

with open("input.txt") as f:
    lines = f.readlines()

sues = {}
for line in lines:
    line = line.split()
    # [:-1] strips last char. Always : or , except prop3Value which has none
    id = int(line[1][:-1])
    prop1Key, prop1Value = line[2][:-1], int(line[3][:-1])
    prop2Key, prop2Value = line[4][:-1], int(line[5][:-1])
    prop3Key, prop3Value = line[6][:-1], int(line[7])
    sues[id] = {prop1Key: prop1Value, prop2Key: prop2Value, prop3Key: prop3Value}

for id, props in sues.items():
    for key, value in props.items():
        if key == "cats" or key == "trees":
            if value <= TARGET[key]:
                break
        elif key == "pomeranians" or key == "goldfish":
            if value >= TARGET[key]:
                break
        else:
            if value != TARGET[key]:
                break
    # Only runs if loop completes unbroken eg. all sue props = TARGET props
    else:
        print(id)
        break
