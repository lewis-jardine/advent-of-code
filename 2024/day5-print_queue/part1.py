# INPUT = "test_input.txt"
INPUT = "input.txt"

type PageOrder = dict[int, set[int]]


def read_page_order(lines: list[str]) -> PageOrder:
    """
    First n lines until empty line are page order cmds (47|64), output these as:
        {page: [list of pages that are ordered later than page]}
    """
    order_following_pages: PageOrder = {}
    for line in lines:
        if line == "":
            break
        x = int(line[0:2])
        y = int(line[3:5])
        if x not in order_following_pages:
            order_following_pages[x] = {y}
        else:
            order_following_pages[x].add(y)
    return order_following_pages


def get_middle_page(line: str, order_following_pages: PageOrder) -> int:
    """Get number of middle page if in correct order, otherwise 0"""
    pages = line.split(",")
    if len(pages) <= 1:
        return 0

    # Record previous pages, check that they are not also in the following page order
    prev_pages: set[int] = set()
    for page in pages:
        page = int(page)
        if page in order_following_pages:
            if not prev_pages.isdisjoint(order_following_pages[page]):
                return 0
        prev_pages.add(page)

    # Must be correctly ordered, find middle page
    middle = int(pages[len(pages) // 2])
    return middle


def main():
    with open(INPUT) as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    order_following_pages = read_page_order(lines)

    total = 0
    for line in lines:
        total += get_middle_page(line, order_following_pages)

    print(total)


if __name__ == "__main__":
    main()
