package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	input := readInput("../input.txt")
	// input := readInput("../test.txt")
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

// Parser will build problems out of 1+ single character wide columns of operands and 1 line
// of whitespace seperated operators. The problems slice will only be built when the parser
// is provided an operator line and valid operands have been provided. As operands are built
// with each line, they will be stored as strings for easy concatenation until build.
type Parser struct {
	problems    []Problem
	colOperands []string
}

// Feed lines of operands or operators into parser. Build problems if an operator line is provided.
func (p *Parser) parseLine(line string) error {

	// The operator line always starts with an operator (not whitespace/ digit)
	// if _, err := strconv.Atoi(string(trimmedLine[0])); err == nil {
	switch line[0] {
	case '+', '*':
		// Operator line found
		operators, err := parseOperators(line)
		if err != nil {
			return fmt.Errorf("parseLine: %w", err)
		}

		// Operators line is last, we have parsed everything. Build the problems.
		problems, err := buildProblems(operators, p.colOperands)
		if err != nil {
			return fmt.Errorf("parseLine: %w", err)
		}
		p.problems = problems

	default:
		// Operand line found - concat digit found at each idx to the digits found at that
		// same idx in other lines.
		if p.colOperands == nil {
			// Assume all lines are equal to the first.
			p.colOperands = make([]string, len(line))
		}
		for i, val := range line {
			// Only concat if a digit
			if _, err := strconv.Atoi(string(val)); err == nil {
				p.colOperands[i] += string(val)
			}
		}
	}
	return nil
}

// Operands are displayed vertically.
// func parseOperands(line string) ([]int, error) {
// 	operands := make([]int, len(line))
// 	for i, val := range line {
// 		intVal, err := strconv.Atoi(val)
// 		if err != nil {
// 			return nil, fmt.Errorf("parseOperands: %w", err)
// 		}
// 		operands[i] = intVal
// 	}
// 	return operands, nil
// }

// Convert slice of string-format operators into Operator type. Error if invalid.
func parseOperators(line string) ([]Operator, error) {
	splitLine := strings.Fields(line)

	operators := make([]Operator, len(splitLine))
	for i, val := range splitLine {
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
func buildProblems(operators []Operator, operands []string) ([]Problem, error) {
	// Validate >1 operands
	if len(operands) == 0 {
		return nil, fmt.Errorf("buildProblems: Operands cannot be empty")
	}

	// Group operands by problem (one operator per problem), demarcating by empty values (whitespace col in input)
	var groupOperands = make([][]int, len(operators))
	problemCount := 0
	for i, operand := range operands {

		// Empty string marks a new problem
		if operand == "" {
			problemCount++
			if problemCount >= len(operators) {
				return nil, fmt.Errorf("buildProblems: Could not find an operator for problem starting col %v", i)
			}
			continue
		}

		intOperand, err := strconv.Atoi(operand)
		if err != nil {
			return nil, fmt.Errorf("buildProblems: %w", err)
		}
		groupOperands[problemCount] = append(groupOperands[problemCount], intOperand)
	}

	problems := make([]Problem, len(operators))
	for i, operator := range operators {
		problems[i] = Problem{operator, groupOperands[i]}
	}

	return problems, nil
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

func checkErr(e error) {
	if e != nil {
		panic(e)
	}
}
