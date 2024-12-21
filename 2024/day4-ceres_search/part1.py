# INPUT = "test_input.txt"
INPUT = "input.txt"


def xmas_search(wordsearch: list[str], x: int, y: int) -> int:
    """count 'XMAS' that starts at the given wordsearch coordinates"""
    # XMAS must start with an X
    if wordsearch[x][y] != "X":
        return 0

    total = 0
    # Next search for M, counter-clockwise around coordinates
    # If M is found, search for A and S in the direction of M
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            # This is X, skip
            if x_offset == 0 and y_offset == 0:
                continue

            # Avoid x index error
            if x + x_offset * 3 < 0 or x + x_offset * 3 >= len(wordsearch):
                continue

            # Avoid y index error
            if y + y_offset * 3 < 0 or y + y_offset * 3 >= len(wordsearch[0]):
                continue

            if wordsearch[x + x_offset][y + y_offset] == "M":
                if wordsearch[x + x_offset * 2][y + y_offset * 2] == "A":
                    if wordsearch[x + x_offset * 3][y + y_offset * 3] == "S":
                        total += 1

    return total


def main():
    with open(INPUT) as file:
        wordsearch = file.readlines()

    total = 0
    for x, row in enumerate(wordsearch):
        for y in range(len(row)):
            total += xmas_search(wordsearch, x, y)

    print(total)


if __name__ == "__main__":
    main()
