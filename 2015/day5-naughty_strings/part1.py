with open("input.txt", "r") as f:
    lines = f.readlines()

vowels = ['a', 'e', 'i', 'o', 'u']
banned_strings = ['ab', 'cd', 'pq', 'xy']

nice_count = 0
for line in lines:
    line = line.strip()
    # Iterate through each char in line, store it and next char.
    # Count vowels, check consecutive chars, check not disallowed string
    vowel_count = 0
    consecutive = False
    for idx, i in enumerate(line):

        # Ensure not last letter, get next letter as well
        if idx + 1 != len(line):
            j = line[idx + 1]

            # Check if string naughty, break if so
            if i + j in banned_strings:
                break

            # Check if same letter
            if i == j:
                consecutive = True

        # Check if vowel
        if i in vowels:
            vowel_count += 1
    
    # Loop would break if naughty, so wouldnt reach else
    else:
        # Check at least 3 vowels and 1 consecutive letter
        if vowel_count >= 3 and consecutive:
            nice_count += 1


print(nice_count)