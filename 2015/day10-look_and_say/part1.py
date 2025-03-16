puzzle_input = "1113222113"
iterations = 40

for i in range(iterations):
    output = ""
    char_count = 1
    for idx, char in enumerate(puzzle_input):
        if idx + 1 < len(puzzle_input):
            next_char = puzzle_input[idx + 1]
        else:
            next_char = None
        if next_char == char:
            char_count += 1
        else:
            output += f"{char_count}{char}"
            char_count = 1
    puzzle_input = output

print(len(puzzle_input))