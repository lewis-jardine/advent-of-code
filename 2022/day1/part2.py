total = 0
totals = []

# Open input file, read each line in as an int
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
    
        # Add to current elfs total, unless line break which signifies new elf
        if line != '\n':
            line = int(line)
            total += line

        else:
            totals.append(total)
            total = 0

# Sort totals desc then slice to get three highest. Add those all up
totals.sort(reverse=True)
totals = totals[:3]
sum_totals = sum(totals)



print(sum_totals)