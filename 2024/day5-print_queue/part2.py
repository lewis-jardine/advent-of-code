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


def get_failed_page_idx(
    pages: list[int], order_following_pages: PageOrder
) -> int | None:
    """Return idx of first unordered page, else None if all pages are correctly ordered"""
    # Record previous pages, check that they are not also in the following page order
    prev_pages: set[int] = set()
    for idx, page in enumerate(pages):
        if page in order_following_pages:
            if not prev_pages.isdisjoint(order_following_pages[page]):
                return idx
        prev_pages.add(page)
    return None


def reorder_pages(
    pages: list[int], order_following_pages: PageOrder, failed_page_idx: int
) -> list[int]:
    """Reorder pages so that the failed page abides by page order rules"""
    failed_page = pages[failed_page_idx]
    # Incorrectly ordered pages, in appearance order to preserve the correct ordering
    out_of_order_pages = [
        page
        for page in pages[:failed_page_idx]
        if page in order_following_pages[failed_page]
    ]
    # Put out of order pages just after the failed page
    reordered = (
        pages[: failed_page_idx + 1] + out_of_order_pages + pages[failed_page_idx + 1 :]
    )
    # Remove will only delete the first occurence of the value- aka the unordered page(s)
    for page in out_of_order_pages:
        reordered.remove(page)
    return reordered


def get_middle_failed_page(line: str, order_following_pages: PageOrder) -> int:
    """
    Get number of middle page IF NOT correctly ordered, re-order if required
    Return 0 if not valid pages/ correctly ordered
    """
    pages = line.split(",")
    if len(pages) <= 1:
        return 0

    pages = [int(page) for page in pages]

    failed = False
    while True:
        failed_page_idx = get_failed_page_idx(pages, order_following_pages)
        if failed_page_idx is None:
            break
        failed = True
        pages = reorder_pages(pages, order_following_pages, failed_page_idx)

    # Must now be correctly ordered, find middle page
    return pages[len(pages) // 2] if failed else 0


def main():
    with open(INPUT) as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    order_following_pages = read_page_order(lines)

    total = 0
    for line in lines:
        total += get_middle_failed_page(line, order_following_pages)

    print(total)


if __name__ == "__main__":
    main()
