package main

import (
	"reflect"
	"testing"
)

func TestFindStart(t *testing.T) {
	grid := &Grid{
		tiles: [][]Tile{
			{empty, start, empty},
		},
	}
	outRow, outCol, err := grid.FindStart()
	expRow, expCol := 0, 1

	if outRow != expRow || outCol != expCol {
		t.Errorf("expected: %v, %v	recieved: %v, %v", expRow, expCol, outRow, outCol)
	}
	if err != nil {
		t.Errorf("Expected no error but received: %v", err)
	}
}

func TestFindError(t *testing.T) {
	grid := &Grid{
		tiles: [][]Tile{
			{empty, splitter, empty},
		},
	}
	_, _, err := grid.FindStart()

	if err == nil {
		t.Errorf("Recieved no error when one expected")
	}
}

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

func TestGridSimulateParticle(t *testing.T) {
	grid := &Grid{
		tiles: [][]Tile{
			{empty, empty, empty, empty},
			{empty, empty, splitter, empty},
			{empty, empty, empty, empty},
			{empty, splitter, empty, empty},
			{empty, empty, empty, empty},
		},
	}

	exp := []Direction{left, left}
	out, err := grid.SimulateParticle(0, 2)

	if !reflect.DeepEqual(out, exp) {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
	if err != nil {
		t.Errorf("Expected no error but received: %v", err)
	}
}
func TestGridSimulateParticleEmpty(t *testing.T) {
	grid := &Grid{
		tiles: [][]Tile{
			{empty, empty, empty},
			{empty, splitter, empty},
			{empty, empty, empty},
		},
	}

	out, err := grid.SimulateParticle(0, 0)

	if out != nil {
		t.Errorf("expected: %v	recieved: %v", nil, out)
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

func TestDirectionsAllRightTrue(t *testing.T) {
	out := directionsAllRight([]Direction{right, right})
	exp := true

	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}

func TestDirectionsAllRightFalse(t *testing.T) {
	out := directionsAllRight([]Direction{left, right})
	exp := false

	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}
