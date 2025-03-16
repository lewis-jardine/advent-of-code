marker = 0

with open("input.txt", "r", encoding="utf-8") as f:
    input = f.readline()

    # Iterate through input str, get substring of 14 chars and find repitions
    for i in range(len(input)):
        substr = input[i:i+14]

        # Convert to set, if set is still 14 then no duplicates
        if len(set(substr)) == 14:
            marker = i + 14
            break

print(substr, marker)