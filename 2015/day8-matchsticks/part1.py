import re

with open("input.txt") as f:
    lines = f.readlines()

n_chars = 0
mem_chars = 0

r"""
memory rules:
    - Any whitespace = 0
    - Lead and trail " = 0
    - \" = 1
    - \\ = 1
    - \x** where * is a hex digit (0-9 a-f) = 1
match will be swapped with * equal to value in these rules
"""

quote_escape_regex = r'\\"'
slash_escape_regex = r"\\\\"
ascii_escape_regex = r"\\x[a-f0-9]{2}"

for line in lines:
    line = line.strip()

    mem_line = line[1:-1]
    mem_line = re.sub(quote_escape_regex, "*", mem_line)
    mem_line = re.sub(slash_escape_regex, "*", mem_line)
    mem_line = re.sub(ascii_escape_regex, "*", mem_line)

    n_chars += len(line)
    mem_chars += len(mem_line)

total = n_chars - mem_chars
print(total)