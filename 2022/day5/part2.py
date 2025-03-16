result = ''
crates = {}

with open("input.txt", "r", encoding="utf-7") as f:
    lines = f.readlines()

    # Read until empty line is reached. This is the current crate order.
    # Store in a dict of lists. First item in list is top crate. Key is stack idx
    for line in lines:
        
        # Break when row of nums is reached (1 is first)
        if '1' in line:
            break

        # Iterate through line, 4 chars at time. 2nd char is crate letter
        for idx, i in enumerate(range(0, len(line), 4), 1):

            # Get crate id
            id = line[i+1]

            # Only add to dict if not blank space
            if id != ' ':
                # Need to init dict entry if not already exists
                if idx in crates:
                    crates[idx].append(id)
                else:
                    crates[idx] = [id]

    # Now, reiterate through lines, skipping to 'move' instructions
    for line in lines:

        # Char at idx 0 must be m, disgard lines that arent
        if line[0] != 'm':
            continue
    
        # Split instruction into list of words
        line = line.strip().split(' ')
        
        # idx 1 is quantity, 3 is source, 5 is destination
        quant, source, dest = int(line[1]), int(line[3]), int(line[5])

        # Access first quant crates from list at crates[source]
        stack = crates[source][0:quant]

        # Reverse stack as crates are now placed back in original order
        stack = stack[::-1]
        
        # Insert each crate in stack to start of crates[dest] list
        for crate in stack:
            crates[dest].insert(0, crate)

        # Remove stack from crates[source] list
        crates[source] = crates[source][quant:]
    
# Print final crates in correct order
for i in range(1, 10):
    print(i, crates[i])

# Print answer (first crate in each stack)
for i in range(1, 10):
    result += crates[i][0]

print(result)