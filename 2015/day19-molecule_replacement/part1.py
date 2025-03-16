INPUT = "input.txt"


def read_replacements(lines: list[str]) -> dict[str, list[str]]:
    """
    Each replacement read in format 'molecule => replaced' eg 'Al => ThF'
    One molecule may have multiple replacements
    Will be returned as dict in format:
        replacements = {molecule: [replaced1, replaced2]}
    eg. All replacements of molecule i can be access by replacements[i]
    """
    replacements = {}
    for line in lines:
        line = line.strip().split()
        molecule, replacement = line[0], line[2]
        if molecule in replacements:
            replacements[molecule].append(replacement)
        else:
            replacements[molecule] = [replacement]
    return replacements


def count_replacements(replacements: dict[str, list[str]], target: str) -> int:
    """Count number of unique replacements that can be made in target molecule"""
    found_replacements = set()
    for idx, molecule in enumerate(target):
        # Molecules can be up to len 2, combined includes next in chain too
        combined_molecule = ""
        if idx + 1 < len(target):
            combined_molecule = molecule + target[idx + 1]
        if molecule in replacements:
            # One molecule could have multiple replacements
            for replacement in replacements[molecule]:
                # print(idx, molecule, replacement)
                new_target = target[:idx] + replacement + target[idx + 1 :]
                # print(target[:idx], replacement, target[idx + 1 :])
                found_replacements.add(new_target)
        if combined_molecule in replacements:
            for replacement in replacements[combined_molecule]:
                new_target = target[:idx] + replacement + target[idx + 2 :]
                found_replacements.add(new_target)
    return len(found_replacements)


if __name__ == "__main__":
    with open(INPUT) as f:
        lines = f.readlines()
    # Target molecule is last line only
    TARGET = lines[-1].strip()
    # Replacements are all but last two lines (newline and target)
    replacements = read_replacements(lines[:-2])
    count = count_replacements(replacements, TARGET)
    print(count)
