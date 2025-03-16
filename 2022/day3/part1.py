total = 0

with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:

        # Seperate into in half, eg two compartments
        comp1 = line[:len(line) // 2]
        comp2 = line[len(line) // 2:]
        
        # Iterate through comp1, find which item is in comp2
        for item in comp1:
            if item in comp2:

                # Calculate item score, then add to total
                # Upercase A is ASCII val 65, or priority 27. -38 to give priority
                if item.isupper():
                    total += ord(item) - 38
                
                # Lowercase a is ASCII val 97, or priority 1. -96 to give priorty
                elif item.islower():
                    total += ord(item) - 96

                # Only need to find the first duplicate
                break

print(total)