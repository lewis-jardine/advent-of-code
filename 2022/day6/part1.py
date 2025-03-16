marker = 0

with open("input.txt", "r", encoding="utf-8") as f:
    input = f.readline()

    # Iterate through input str, get substring of 4 chars and find repitions
    for i in range(len(input)):
        substr = input[i:i+4]

        # Convert to set, if set is still 4 then no duplicates
        if len(set(substr)) == 4:
            marker = i + 4
            break

print(substr, marker)