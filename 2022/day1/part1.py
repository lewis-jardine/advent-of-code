highest = 0
total = 0

# Open input file, read each line in as an int
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
    
        # Add to current elfs total, unless line break which signifies new elf
        if line != '\n':
            line = int(line)
            total += line

            # Set new highest if total is greater than it
            if total > highest:
                highest = total
        
        else:
            total = 0

print(highest)