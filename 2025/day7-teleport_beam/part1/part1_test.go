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

func TestGridSimulate(t *testing.T) {
	grid := &Grid{
		tiles: [][]Tile{
			{empty, start, empty},
			{empty, empty, empty},
			{empty, splitter, empty},
			{empty, empty, empty},
		},
	}

	exp := [][]Tile{
		{empty, start, empty},
		{empty, beam, empty},
		{beam, splitter, beam},
		{beam, empty, beam},
	}

	err := grid.Simulate()

	if !reflect.DeepEqual(grid.tiles, exp) {
		t.Errorf("expected: \n%v	recieved: \n%v", &Grid{exp}, grid)
	}
	if err != nil {
		t.Errorf("Expected no error but received: %v", err)
	}
}

func TestSetBeamEmpty(t *testing.T) {
	grid := &Grid{
		tiles: [][]Tile{
			{empty, start},
			{empty, empty},
		},
	}

	exp := [][]Tile{
		{beam, start},
		{empty, empty},
	}

	err := grid.setBeam(0, 0)

	if !reflect.DeepEqual(grid.tiles, exp) {
		t.Errorf("expected: \n%v	recieved: \n%v", &Grid{exp}, grid)
	}
	if err != nil {
		t.Errorf("Expected no error but received: %v", err)
	}
}

func TestSetBeamFilled(t *testing.T) {
	grid := &Grid{
		tiles: [][]Tile{
			{splitter, start},
			{empty, empty},
		},
	}

	exp := [][]Tile{
		{splitter, start},
		{empty, empty},
	}

	err := grid.setBeam(0, 0)

	if !reflect.DeepEqual(grid.tiles, exp) {
		t.Errorf("expected: \n%v	recieved: \n%v", &Grid{exp}, grid)
	}
	if err != nil {
		t.Errorf("Expected no error but received: %v", err)
	}
}
