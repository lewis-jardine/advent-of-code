package main

import (
	"reflect"
	"testing"
)

// func parseLine()
func TestParseLineValid(t *testing.T) {
	out, err := parseLine(".S^.")
	exp := []Tile{empty, start, splitter, empty}

	if !reflect.DeepEqual(out, exp) {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
	if err != nil {
		t.Errorf("Expected no error but received: %v", err)
	}
}

func TestParseLineInvalid(t *testing.T) {
	_, err := parseLine(".Sa.")

	if err == nil {
		t.Error("Expected error but recieved nil")
	}
}
