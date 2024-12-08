INPUT = "input.txt"
# INPUT = "test_input.txt"


def unsafe_level(report: list[int]) -> int | None:
    """
    Find idx of first unsafe level in report or None if report is safe.
    Report is safe if both:
        - Any two adjacent levels differ by at least one and at most three.
        - The levels are either all increasing or all decreasing.

    example report: [1, 4, 3] (idx 1 not safe)
    """
    increasing: bool | None = None
    for idx, n in enumerate(report):
        # Don't compare last to avoid value error
        if len(report) == idx + 1:
            break
        next_n = report[idx + 1]

        # Find level dif first
        dif = abs(n - next_n)
        if dif < 1 or dif > 3:
            return idx

        # Then find if decrease/ increase pattern holds. First run ignores this check
        if increasing is None:
            increasing = n < next_n
            continue

        next_increasing = n < next_n
        if increasing != next_increasing:
            return idx

    return None


def main():
    with open(INPUT) as f:
        lines = f.readlines()

    safe_reports: int = 0
    for line in lines:
        # Each report in format "8 1 4 2\n"
        report = line.strip().split()
        report = [int(n) for n in report]

        idx = unsafe_level(report)
        if idx is None:
            safe_reports += 1
            # print("safe")
            continue

        # Try remove the failed level and the next level in two different lists
        # This accounts for last number being the one that should be removed
        copy_report = report.copy()
        del report[idx]
        del copy_report[idx + 1]
        if unsafe_level(report) is None or unsafe_level(copy_report) is None:
            # print("safe by removing ", level)
            safe_reports += 1
        # else:
        #     print("unsafe: ", orig_report, " tried removing ", idx)

    print(safe_reports)


if __name__ == "__main__":
    main()
