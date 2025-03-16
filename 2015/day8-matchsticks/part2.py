with open("input.txt") as f:
    lines = f.readlines()

r"""
To encode:
    1. Add \ before each \
    2. Add \ before each "
    3. Add " to start and end of string
"""

orig_chars = 0
encode_chars = 0
for line in lines:
    line = line.strip()

    encoded_line = line.replace("\\", "\\\\")
    encoded_line = encoded_line.replace(r'"', r'\"')
    encoded_line = fr'"{encoded_line}"'
    
    orig_chars += len(line)
    encode_chars += len(encoded_line)

result = encode_chars - orig_chars
print(result)