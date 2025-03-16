"""Store directory structure as in dict:
    structure: {
        dir1: {
            size: (total size of files in dir),
            up: (reference to dict object of dir that is one level up),
            dir3: {
                size: ...,
                up: dir1
            }
        },
        dir2: {
            size: ...,
            up: structure
        },
        size: ...,
        """
structure = {
    "size": 0,
    "up": "root"
}
# Creates a dict reference to the current dir
current_dir = {}

with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:

        # Split into list for easier referencing by logic below
        line = line.strip().split(' ')

        # User inputted command
        if line[0] == "$":

            # Change into dir
            if line[1] == "cd":
                
                # Root
                if line[2] == "/":
                    current_dir = structure

                # Up one level, 
                elif line[2] == "..":
                    current_dir = current_dir["up"]

                # Down one level into specified dir
                else:
                    dir_name = line[2]
                    current_dir = current_dir[dir_name]

        # Terminal ouptut
        else:

            # Details dir info, add to structure
            if line[0] == "dir":
                
                dir_name = line[1]
                current_dir[dir_name] = {
                    "size": 0,
                    "up": current_dir
                }
                
            
            # Other output must be file
            else:

                file_size= int(line[0])

                # Iterate through parents dirs until root is reached.
                # Add size to each
                parent_dir = current_dir

                while parent_dir != "root":
                    parent_dir["size"] += file_size
                    parent_dir = parent_dir["up"]

current_size = structure["size"]
space_remaining = 70000000 - current_size
space_required = 30000000 - space_remaining

# Iterate through all dicts in structure, add dir with size > required_space to list
def count_sizes(d): 
    ret = []
    stack = list(d.items()) 
    while stack: 
        k, v = stack.pop() 
        if isinstance(v, dict): 
            if k != "up":
                stack.extend(v.items()) 
        else: 
            print("%s: %s" % (k, v)) 
            if k == "size" and v >= space_required:
                ret.append(v)
    
    return ret

possible_dirs = count_sizes(structure)
possible_dirs.sort()

print(possible_dirs[0])