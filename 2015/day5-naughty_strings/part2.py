with open("input.txt", "r") as f:
    lines = f.readlines()

nice_count = 0
for line in lines:
    line = line.strip()
    # Iterate through each char in line, store it and next two chars.
    # Store each pair as key in dict, with value idx of second char.
    # Check if first and third char equal.
    pairs = False
    pair_store = {}
    repeat = False
    for idx, i in enumerate(line):
        # Prevent idx errors
        if idx + 1 != len(line):
            j = line[idx + 1]

            # Try store i + j as key in dict with val idx + 1
            # If already exists and val != idx, then pair
            if i + j in pair_store:
                if pair_store[i + j] != idx:
                    pairs = True

            else:
                pair_store[i + j] = idx + 1


            if idx + 2 != len(line):
                k = line[idx + 2]

                # Check for repeat char
                if i == k:
                    repeat = True

    if pairs and repeat:
        nice_count += 1

print(nice_count)