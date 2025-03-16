with open("input.txt", "r") as f:
    lines = f.readlines()

# Store light states in 2d 1000 x 1000 array (true is on, false is off)
lights = [[False for x in range(1000)] for y in range(1000)]

for line in lines:
    
    # Seperate line into command, start coords, end coords
    line = line.strip().split()
    
    # 'turn' means command to turn off or on, also changes pos start, end coords
    if line[0] == 'turn':
        command = line[1]
        start_coords = line[2].split(',')
        end_coords = line[4].split(',')
    
    # 'toggle' is only other command
    else:
        command = 'toggle'
        start_coords = line[1].split(',')
        end_coords = line[3].split(',')
    
    # Iterate through all lights in coords range
    x = int(start_coords[0])
    while x <= int(end_coords[0]):
        y = int(start_coords[1])
        while y <= int(end_coords[1]):
            if command == 'on':
                lights[x][y] = True
            elif command == 'off':
                lights[x][y] = False
            else:
                lights[x][y] = not lights[x][y]
            y += 1
        x += 1

# Now, iterate through lights and count how many are on (true)
lit_count = 0
for row in lights:
    for light in row:
        if light:
            lit_count += 1

print(lit_count)