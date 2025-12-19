package main

import "testing"

func TestMaxJoltage(t *testing.T) {
	out := maxJoltage("818181911112111")
	exp := 92
	if out != exp {
		t.Errorf("expected: %d	recieved: %d", exp, out)
	}
}

// Greatest joltage is the last digit, ensure not picked as first digit
func TestMaxJoltageEnd(t *testing.T) {
	out := maxJoltage("811111111111119")
	exp := 89
	if out != exp {
		t.Errorf("expected: %d	recieved: %d", exp, out)
	}
}
