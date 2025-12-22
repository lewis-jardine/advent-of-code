package main

import (
	"testing"
)

// func parseIdRange()
func TestParseIdRangeValid(t *testing.T) {
	out, err := parseIdRange("1234-5678")
	exp := Range{start: 1234, end: 5678}
	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
	if err != nil {
		t.Errorf("recieved error: %v", err)
	}
}

func TestParseIdRangeInvalid(t *testing.T) {
	_, err := parseIdRange("1234-5678-6475")
	if err == nil {
		t.Error("expected error but recieved none")
	}
}

var idRanges []Range = []Range{{start: 1, end: 3}, {start: 5, end: 6}}

// func isFresh()
func TestIsFreshTrue(t *testing.T) {
	out := isFresh(3, idRanges)
	exp := true
	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}

func TestIsFreshFalse(t *testing.T) {
	out := isFresh(4, idRanges)
	exp := false
	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}
