# INPUT = "test_input.txt"
INPUT = "input.txt"

type Equation = tuple[int, list[int]]


def _load_equations(lines: list[str]) -> list[Equation]:
    """Split each line into tuple with answer idx 0, list of factors idx 1"""
    equations: list[Equation] = []
    for line in lines:
        split_line = line.strip().split(":")
        answer = int(split_line[0])
        factors = [int(n) for n in split_line[1].strip().split()]
        equations.append((answer, factors))
    return equations


def _calculate_combinations(factors: list[int]) -> list[int]:
    """Return a list of results of  + or * or concat for each factor"""
    combinations = [factors[0]]
    for factor in factors[1:]:
        add_combinations = [n + factor for n in combinations]
        multiply_combinations = [n * factor for n in combinations]
        concat_combinations = [int(str(n) + str(factor)) for n in combinations]
        combinations = add_combinations + multiply_combinations + concat_combinations
    return combinations


def _equation_correct(equation: Equation) -> bool:
    """Return True if combination of factors can be added/multiplied to answer"""
    answer, factors = equation
    possible_answers = _calculate_combinations(factors)
    return answer in possible_answers


def main():
    with open(INPUT) as file:
        lines = file.readlines()
    equations = _load_equations(lines)

    total = 0
    for equation in equations:
        if _equation_correct(equation):
            total += equation[0]
    print(total)


if __name__ == "__main__":
    main()
