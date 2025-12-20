package main

import (
	"reflect"
	"testing"
)

// func parseLine()
func TestParseLine(t *testing.T) {
	out := parseLine("..@@.@")
	exp := []bool{false, false, true, true, false, true}
	if !reflect.DeepEqual(out, exp) {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}

// func removeRolls()
func TestRemoveRolls(t *testing.T) {
	input := [][]bool{{true, true, true}, {true, true, true}, {true, true, true}}
	out := removeRolls(input)
	exp := 4
	transformedInput := [][]bool{{false, true, false}, {true, true, true}, {false, true, false}}
	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
	if !reflect.DeepEqual(input, transformedInput) {
		t.Errorf("expected: %v	recieved: %v", transformedInput, input)
	}
}

// func isAccessible()
func TestIsAccessibleTrue(t *testing.T) {
	input := [][]bool{{false, false, true}, {true, true, false}, {false, false, true}}
	out := isAccessible(input, 1, 1)
	exp := true
	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}

func TestIsAcccesibleFalse(t *testing.T) {
	input := [][]bool{{true, false, true}, {true, true, false}, {false, false, true}}
	out := isAccessible(input, 1, 1)
	exp := false
	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}

// Check logic still works on corner (OOB handling works)
func TestIsAccesibleCorner(t *testing.T) {
	input := [][]bool{{true, false, true}, {true, true, false}, {false, false, true}}
	out := isAccessible(input, 0, 2)
	exp := true
	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}
