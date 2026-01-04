package main

import (
	"reflect"
	"testing"
)

// solveProblem
func TestSolveProblemMultiply(t *testing.T) {
	out := solveProblem(Problem{multiply, []int{3, 5}})
	exp := 15

	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}

func TestSolveProblemAdd(t *testing.T) {
	out := solveProblem(Problem{add, []int{3, 5}})
	exp := 8

	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}

// Parser
func TestParser(t *testing.T) {
	parser := &Parser{}
	err := parser.parseLine("10  20 ")
	err = parser.parseLine("5 15")
	err = parser.parseLine("+  *")

	exp := []Problem{{add, []int{10, 5}}, {multiply, []int{20, 15}}}

	if !reflect.DeepEqual(parser.problems, exp) {
		t.Errorf("expected %v, got %v", exp, parser.problems)
	}
	if err != nil {
		t.Errorf("Expected no error but received: %v", err)
	}
}

// func parseOperands()
func TestParseOperandsValid(t *testing.T) {
	out, err := parseOperands([]string{"8", "17", "451"})

	exp := []int{8, 17, 451}
	if !reflect.DeepEqual(out, exp) {
		t.Errorf("expected %v, recieved %v", exp, out)
	}

	if err != nil {
		t.Errorf("Expected no error but received: %v", err)
	}
}
func TestParseOperandsInvalid(t *testing.T) {
	_, err := parseOperands([]string{"8", "+", "451"})

	if err == nil {
		t.Error("Expected error but recieved nil")
	}
}

// func parseOperators()
func TestParseOperatorsValid(t *testing.T) {
	out, err := parseOperators([]string{"+", "*", "+"})

	exp := []Operator{add, multiply, add}
	if !reflect.DeepEqual(out, exp) {
		t.Errorf("expected %v, recieved %v", exp, out)
	}
	if err != nil {
		t.Errorf("Expected no error but received: %v", err)
	}
}
func TestParseOperatorsInvalid(t *testing.T) {
	_, err := parseOperators([]string{"+", "451", "+"})

	if err == nil {
		t.Error("Expected error but recieved nil")
	}
}

func TestBuildProblemsValid(t *testing.T) {
	out, err := buildProblems([]Operator{add, multiply}, [][]int{{8, 3}, {98, 10}})
	exp := []Problem{{add, []int{8, 98}}, {multiply, []int{3, 10}}}

	if !reflect.DeepEqual(out, exp) {
		t.Errorf("expected %v, recieved %v", exp, out)
	}
	if err != nil {
		t.Errorf("Expected no error but received: %v", err)
	}
}

func TestBuildProblemsLengthMismatch(t *testing.T) {
	_, err := buildProblems([]Operator{add, multiply, multiply}, [][]int{{8, 3}, {98, 10}})

	if err == nil {
		t.Error("Expected error but recieved nil")
	}
}

func TestBuildProblemsInsufficientOperands(t *testing.T) {
	_, err := buildProblems([]Operator{add, multiply}, [][]int{})

	if err == nil {
		t.Error("Expected error but recieved nil")
	}
}
