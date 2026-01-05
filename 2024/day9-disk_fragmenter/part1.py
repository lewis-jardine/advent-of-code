import cProfile
import pstats

INPUT = "input.txt"
# INPUT = "test_input.txt"
# INPUT = "test_input2.txt"


def load_disk_map(filename: str) -> str:
    """
    output: digits alternate between indicating the length of a file and the length of
    free space
    """
    with open(filename) as f:
        line = f.readline().strip()
    return line


def parse_disk_map(disk_map: str) -> str:
    """
    output: block id's where data is present and '.' in free space
    """
    parsed_disk_map = ""
    free_block = False
    idx = 0
    for block in disk_map:
        if not block.isdigit():
            raise ValueError(f"block '{block}' in disk_map is not a valid number")
        block = int(block)
        if not free_block:
            parsed_disk_map += str(idx) * block
            idx += 1
        else:
            parsed_disk_map += "." * block
        free_block = not free_block
    return parsed_disk_map


def compact_disk_map(disk_map: str) -> str:
    """
    input: disk_map in format "00...1.222..."

    output: disk_map with blocks re-arranged so that all space on left is filled, from
    rightmost block first
    """
    while True:
        next_free_idx = disk_map.find(".")
        print(next_free_idx, "/", len(disk_map))
        if next_free_idx == -1:  # No free space is found
            break
        last_full_idx = find_last_digit_idx(disk_map)
        # None idx = no digits present, full idx < free idx = disk compacted
        if last_full_idx is None or last_full_idx < next_free_idx:
            break
        disk_map = (
            disk_map[:next_free_idx]
            + disk_map[last_full_idx]
            + disk_map[next_free_idx + 1 : last_full_idx]
            + "."
            + disk_map[last_full_idx + 1 :]
        )
    return disk_map


def find_last_digit_idx(disk_map: str) -> int | None:
    """
    input: disk_map in format "00...1.222..."

    output: idx of last digit in disk_map (e.g. 9 in input example) or
    None if no digits in disk_map
    """
    for idx in range(len(disk_map) - 1, -1, -1):
        if disk_map[idx] != ".":
            # disk_map is reversed, need to get idx of opposing side instead
            return idx
    return None


def calculate_checksum(disk_map: str) -> int:
    """
    checksum is calculated by adding up the result of multiplying each of the
    blocks' position with the file ID number it contains
    """
    total = 0
    for idx, block in enumerate(disk_map):
        if block.isdigit():
            total += idx * int(block)
    return total


def main():
    disk_map = load_disk_map(INPUT)
    parsed_disk_map = parse_disk_map(disk_map)
    compacted_disk_map = compact_disk_map(parsed_disk_map)
    checksum = calculate_checksum(compacted_disk_map)
    print(checksum)


if __name__ == "__main__":
    with cProfile.Profile() as profiler:
        main()
    stats = pstats.Stats(profiler)
    stats.sort_stats(pstats.SortKey.TIME)  # Sort by time spent
    stats.print_stats(10)  # Print the top 10 slowest functions
    # main()
