package main

import (
	"reflect"
	"testing"
)

func TestParseLine(t *testing.T) {
	out := parseLine("..@@.@")
	exp := []bool{false, false, true, true, false, true}
	if !reflect.DeepEqual(out, exp) {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}

func TestCountAdjTrue(t *testing.T) {
	input := [][]bool{{false, false, true}, {true, true, false}, {false, false, true}}
	out := isAccessible(input, 1, 1)
	exp := true
	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}

func TestCountAdjFalse(t *testing.T) {
	input := [][]bool{{true, false, true}, {true, true, false}, {false, false, true}}
	out := isAccessible(input, 1, 1)
	exp := false
	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}

// Check logic still works on corner (OOB handling works)
func TestCountAdjCorner(t *testing.T) {
	input := [][]bool{{true, false, true}, {true, true, false}, {false, false, true}}
	out := isAccessible(input, 0, 2)
	exp := true
	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}
