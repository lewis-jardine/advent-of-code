# INPUT = "test_input.txt"
INPUT = "input.txt"


def is_cross_mass(wordsearch: list[str], x: int, y: int) -> bool:
    """
    True if current coordinate is an A crossed with MAS. This appears as:

    M S
     A
    M S

    MAS can be either way round
    """
    # Must be centered on an A
    if wordsearch[x][y] != "A":
        return False

    # Must also be at least 1 off any side
    if not 1 <= x < len(wordsearch) - 1 or not 1 <= y < len(wordsearch[0]) - 1:
        return False

    top_left = wordsearch[x - 1][y - 1]
    top_right = wordsearch[x - 1][y + 1]
    bottom_left = wordsearch[x + 1][y - 1]
    bottom_right = wordsearch[x + 1][y + 1]

    # Top left and right must be M or S
    if top_left not in ("M", "S") or top_right not in ("M", "S"):
        return False

    # Top left and bottom right must be opposite
    if top_left == "M" and bottom_right != "S":
        return False
    elif top_left == "S" and bottom_right != "M":
        return False

    # Same with top right and bottom left
    if top_right == "M" and bottom_left != "S":
        return False
    elif top_right == "S" and bottom_left != "M":
        return False

    return True


def main():
    with open(INPUT) as file:
        wordsearch = file.readlines()

    total = 0
    for x, row in enumerate(wordsearch):
        for y in range(len(row)):
            if is_cross_mass(wordsearch, x, y):
                total += 1

    print(total)


if __name__ == "__main__":
    main()
