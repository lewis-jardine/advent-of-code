total = 0
badge = ''

with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    # Iterate through lines, getting 3 at a time
    for i in range(0, len(lines), 3):
        line1, line2, line3 = lines[i: i + 3]

    # Iterate through rucksack 1, find item that occures in both others. That is the badge
        for item in line1:
            if item in line2 and item in line3:
                badge = item
                break

        # Calculate item score, then add to total
        # Upercase A is ASCII val 65, or priority 27. -38 to give priority
        if badge.isupper():
            total += ord(badge) - 38
        
        # Lowercase a is ASCII val 97, or priority 1. -96 to give priorty
        elif badge.islower():
            total += ord(badge) - 96


print(total)