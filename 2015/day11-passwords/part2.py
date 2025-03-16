input = "hxbxwxba"
password_count = 2

# Array of ascii value for each input char
# a: 97, z: 122
ascii_input = []
for char in input:
    ascii_input.append(ord(char))


def next_password(input: list[int]) -> list[int]:
    """Get next iterated password"""
    reversed = input[::-1]
    for idx, i in enumerate(reversed):
        if i < 122:
            reversed[idx] += 1
            break
        else:
            reversed[idx] = 97
    return reversed[::-1]


# Continue until password requirements are satisfied
n = 0
while n < password_count:
    pass1 = False
    pairs = []
    ascii_input = next_password(ascii_input)
    for idx, i in enumerate(ascii_input):

        # Requirement 1: 3 letter straight of increasing value
        if idx >= 2:
            if ascii_input[idx - 2] == (ascii_input[idx -1] - 1) == i - 2:
                pass1 = True
        
        # Requirement 2: cannot contain i, o, l
        if i in [ord("i"), ord("o"), ord("l")]:
            break
        
        # Requirement 3: two different letter pairs
        if idx >= 1:
            if i == ascii_input[idx - 1] and i not in pairs:
                pairs.append(i)
    
    # No outright fails as loop completed
    else:
        if pass1 and len(pairs) > 1:
            n += 1


# Turn back into string from ascii array
output = ""
for i in ascii_input:
    output += chr(i)

print(output)

