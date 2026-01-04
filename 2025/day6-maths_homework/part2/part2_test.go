package main

import (
	"reflect"
	"testing"
)

// Parser
func TestParserColOperands(t *testing.T) {
	parser := &Parser{}
	err := parser.parseLine("123 328")
	err = parser.parseLine(" 45 64 ")

	exp := []string{"1", "24", "35", "", "36", "24", "8"}

	if !reflect.DeepEqual(parser.colOperands, exp) {
		t.Errorf("expected %v, got %v", exp, parser.problems)
	}
	if err != nil {
		t.Errorf("Expected no error but received: %v", err)
	}
}

func TestParserProblems(t *testing.T) {
	parser := &Parser{}
	err := parser.parseLine("123 328")
	err = parser.parseLine(" 45 64 ")
	err = parser.parseLine("*   +  ")

	exp := []Problem{{multiply, []int{1, 24, 35}}, {add, []int{36, 24, 8}}}

	if !reflect.DeepEqual(parser.problems, exp) {
		t.Errorf("expected %v, got %v", exp, parser.problems)
	}
	if err != nil {
		t.Errorf("Expected no error but received: %v", err)
	}
}

// func parseOperators()
func TestParseOperatorsValid(t *testing.T) {
	out, err := parseOperators("+  *  +")

	exp := []Operator{add, multiply, add}
	if !reflect.DeepEqual(out, exp) {
		t.Errorf("expected %v, recieved %v", exp, out)
	}
	if err != nil {
		t.Errorf("Expected no error but received: %v", err)
	}
}

func TestParseOperatorsInvalid(t *testing.T) {
	_, err := parseOperators("+ 451  +")

	if err == nil {
		t.Error("Expected error but recieved nil")
	}
}

// func buildProblems()
func TestBuildProblemsValid(t *testing.T) {
	out, err := buildProblems([]Operator{add, multiply}, []string{"1", "24", "", "36", "24"})
	exp := []Problem{{add, []int{1, 24}}, {multiply, []int{36, 24}}}

	if !reflect.DeepEqual(out, exp) {
		t.Errorf("expected %v, recieved %v", exp, out)
	}
	if err != nil {
		t.Errorf("Expected no error but received: %v", err)
	}
}

func TestBuildProblemsInsufficientOperands(t *testing.T) {
	_, err := buildProblems([]Operator{add, multiply}, []string{})

	if err == nil {
		t.Error("Expected error but recieved nil")
	}
}

// func solveProblem()
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
