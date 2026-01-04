package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// input := readInput("../input.txt")
	input := readInput("../test.txt")
	solution := solve(input)
	fmt.Println(input, solution)
}

func readInput(inputPath string) []Problem {
	parser := &Parser{}
	f, err := os.Open(inputPath)
	checkErr(err)
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		err := parser.parseLine(scanner.Text())
		if err != nil {
			panic(err)
		}
	}
	return parser.problems
}

func solve(problems []Problem) (total int) {
	for _, problem := range problems {
		total += solveProblem(problem)
	}
	return total
}

// Apply operator to all operands in problem.
func solveProblem(problem Problem) int {
	total := problem.operands[0]
	for i := 1; i < len(problem.operands); i++ {
		if problem.operator == add {
			total += problem.operands[i]
		} else {
			total *= problem.operands[i]
		}
	}
	return total
}

// Problem describes a mathematical formula found in each column of the input file.
// Operands are all transformed based on the operator.
type Problem struct {
	operator Operator
	operands []int
}

// Operator is an enum of possible operators in a problem.
type Operator int

const (
	add Operator = iota
	multiply
)

var operatorLookup = map[Operator]string{
	add:      "+",
	multiply: "*",
}

func (operator Operator) String() string {
	return operatorLookup[operator]
}

// Parser will build problems out of 1+ lines of whitespace seperated operands and 1 line
// of whitespace seperated operators. The problems slice will only be built when the parser
// is provided an operator line and valid operands have been provided.
type Parser struct {
	problems    []Problem
	allOperands [][]int
}

// Feed lines of operands or operators into parser. Build problems if an operator line is provided.
func (p *Parser) parseLine(line string) error {
	splitLine := strings.Fields(line)

	// Identify whether line contains operators or operands by trying to convert to int
	if _, err := strconv.Atoi(splitLine[0]); err == nil {
		// Able to convert to int - must be operands
		operands, err := parseOperands(splitLine)
		if err != nil {
			return fmt.Errorf("parseLine: %w", err)
		}
		p.allOperands = append(p.allOperands, operands)

	} else {
		// Cannot convert to int - should be operators
		operators, err := parseOperators(splitLine)
		if err != nil {
			return fmt.Errorf("parseLine: %w", err)
		}

		// Operators line is last, we have parsed everything. Build the problems.
		problems, err := buildProblems(operators, p.allOperands)
		if err != nil {
			return fmt.Errorf("parseLine: %w", err)
		}
		p.problems = problems
	}
	return nil
}

// Convert slice of string-format operands into ints. Error if invalid.
func parseOperands(input []string) ([]int, error) {
	operands := make([]int, len(input))
	for i, val := range input {
		intVal, err := strconv.Atoi(val)
		if err != nil {
			return nil, fmt.Errorf("parseOperands: %w", err)
		}
		operands[i] = intVal
	}
	return operands, nil
}

// Convert slice of string-format operators into Operator type. Error if invalid.
func parseOperators(input []string) ([]Operator, error) {
	operators := make([]Operator, len(input))
	for i, val := range input {
		switch val {
		case add.String():
			operators[i] = add
		case multiply.String():
			operators[i] = multiply
		default:
			err := fmt.Errorf("parseOperators: Invalid operator %q was found. Valid operators are %q and %q", val, add.String(), multiply.String())
			return nil, err
		}
	}
	return operators, nil
}

// Build problems slice from one operators slice and at least one operands slice.
func buildProblems(operators []Operator, operands [][]int) ([]Problem, error) {
	// Validate >1 operands
	if len(operands) == 0 {
		return nil, fmt.Errorf("buildProblems: Operands cannot be empty")
	}
	// Validate all lines are equal length
	for i, operandLine := range operands {
		if len(operators) != len(operandLine) {
			return nil, fmt.Errorf("buildProblems: Operand line %v is a different length from operators", i)
		}
	}

	problems := make([]Problem, len(operators))
	for i, operator := range operators {

		columnOperands := make([]int, len(operands))
		for j, operandLine := range operands {
			columnOperands[j] = operandLine[i]
		}
		problems[i] = Problem{operator, columnOperands}
	}

	return problems, nil
}

func checkErr(e error) {
	if e != nil {
		panic(e)
	}
}
