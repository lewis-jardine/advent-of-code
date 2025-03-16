with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0
for line in lines:

    # Split into list delimited by 'x'
    dimensions = line.strip().split('x')

    # Turn list into ints, then sort list by asc to get smallest sides
    dimensions = [int(x) for x in dimensions]
    dimensions.sort()
    
    # l and w are smalles sides
    l, w, h = dimensions

    area = 2*l*w + 2*w*h + 2*h*l
    area += l * w

    total += area

print(total)