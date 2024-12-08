INPUT = "input.txt"


def report_safe(report: list[int]) -> bool:
    """
    Test report for safety, it is safe if both:
        - Any two adjacent levels differ by at least one and at most three.
        - The levels are either all increasing or all decreasing.

    example report: [1, 4, 3] (not safe)
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
            return False

        # Then find if decrease/ increase pattern holds. First run ignores this check
        if increasing is None:
            increasing = n < next_n
            continue

        next_increasing = n < next_n
        if increasing != next_increasing:
            return False
    return True


def main():
    with open(INPUT) as f:
        lines = f.readlines()

    safe_reports: int = 0
    for line in lines:
        # Each report in format "8 1 4 2\n"
        report = line.strip().split()
        report = [int(n) for n in report]

        if report_safe(report):
            safe_reports += 1

    print(safe_reports)


if __name__ == "__main__":
    main()
