import re

INPUT = "input.txt"
TARGET = "e"


def read_replacements(lines: list[str]) -> dict[str, str]:
    """
    Each replacement read in format 'replacement => molecule' eg 'Al => ThF'
    *Ignore arrow direction as replacements are reversed for part 2*
    Will be returned as dict in format:
        replacements = {molecule: replacement, molecule2: replacement2, molecule3: replacement3}
    eg. Replacement of molecule i can be access by replacements[i]
    Replacements is sorted by key length
    """
    replacements = {}
    for line in lines:
        line = line.strip().split()
        replacement, molecule = line[0], line[2]
        replacements[molecule] = replacement
    print(replacements)
    # Convert to list then sort by longest replacement then convert back to dict
    list_replacements = list(replacements.items())
    list_replacements.sort(key=lambda x: len(x[0]), reverse=True)
    sorted_replacements = {i[0]: i[1] for i in list_replacements}
    print(sorted_replacements)
    return sorted_replacements


def reduce_molecule(
    start: tuple[str, int],
    target: str,
    replacements: dict[str, str],
) -> tuple[str, int]:
    """
    Count steps required to reduce start molecule down to a target molecule.
    Steps and molecule will be stored in tuple (molecule, steps)
    Try largest substitution possible substitution first, if unable to substitute more
    then move back a step and try again with next possible substitution.
    """
    for molecule, replacement in replacements.items():
        replaced = start[0].replace(molecule, replacement, 1)
        if replaced == target:
            return replaced
        else:
            replaced = reduce_molecule(replaced, target, replacements)
    return start


def apply_replacements(replacements: dict[str, str], inital: str) -> set[str]:
    """Find all unique replacements that can be made in inital molecule"""
    new_molecules = set()
    # Find idxs of all occurences of each replacement in molecule
    for replacement, molecule in replacements.items():
        found_idxs = re.finditer(replacement, inital)
        for match in found_idxs:
            start, end = match.span()
            # Replace replacement with molecule
            new_molecule = inital[:start] + molecule + inital[end:]
            # print(inital, new_molecule)
            # print(f"{start=} {end=} {molecule=} {replacement=}")
            # print(f"{new_molecule=}")
            new_molecules.add(new_molecule)
    return new_molecules


if __name__ == "__main__":
    with open(INPUT) as f:
        lines = f.readlines()
    # Start molecule is last line only
    START = lines[-1].strip()
    # Replacements are all but last two lines (newline and target)
    REPLACEMENTS = read_replacements(lines[:-2])
    # steps = reduce_molecule(START, TARGET, REPLACEMENTS)
    # print(steps)
