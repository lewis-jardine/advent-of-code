package main

import "testing"

func TestMaxJoltage(t *testing.T) {
	out := maxJoltage("987654321111111", 12)
	exp := 987654321111
	if out != exp {
		t.Errorf("expected: %d	recieved: %d", exp, out)
	}
}

// Greatest joltage is the last digit, ensure not picked as first digit
func TestMaxJoltageEnd(t *testing.T) {
	out := maxJoltage("811111111111119", 12)
	exp := 811111111119
	if out != exp {
		t.Errorf("expected: %d	recieved: %d", exp, out)
	}
}
