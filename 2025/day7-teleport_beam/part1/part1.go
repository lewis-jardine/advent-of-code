package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	input := readInput("../input.txt")
	// input := readInput("../test.txt")
	solution := solve(input)
	fmt.Println(input, solution)
}

func readInput(inputPath string) *Grid {
	grid := &Grid{}
	f, err := os.Open(inputPath)
	checkErr(err)
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		if err := grid.addLine(scanner.Text()); err != nil {
			panic(err)
		}
	}
	return grid
}

// Representation of the 2D array puzzle input.
type Grid struct {
	tiles [][]Tile
}

func (g *Grid) Height() int {
	return len(g.tiles)
}

func (g *Grid) Width() int {
	if len(g.tiles) == 0 {
		return 0
	}
	return len(g.tiles[0])
}

// Check if a coordinate (row, col) is out of bounds of the grid
func (g *Grid) coordOOB(row, col int) bool {
	return row < 0 || row >= g.Height() || col < 0 || col >= g.Width()
}

func (g *Grid) Get(row, col int) (Tile, error) {
	if g.coordOOB(row, col) {
		return empty, fmt.Errorf("Grid: Get: Coordinate OOB")
	}
	return g.tiles[row][col], nil
}

func (g *Grid) Set(row, col int, tile Tile) error {
	if g.coordOOB(row, col) {
		return fmt.Errorf("Grid: Set: Coordinate OOB")
	}
	g.tiles[row][col] = tile
	return nil
}

// Add new line of tiles to the grid
func (g *Grid) addLine(line string) error {
	parsed, err := parseLine(line)
	if err != nil {
		return err
	}
	g.tiles = append(g.tiles, parsed)
	return nil
}

func (g *Grid) String() (out string) {
	for _, row := range g.tiles {
		for _, tile := range row {
			out += tile.String()
		}
		out += "\n"
	}
	return out
}

func (g *Grid) Simulate() error {
	// We set other tiles to beam based on the current tile value
	// Ignore the last row to avoid idx err
	for row, rowTiles := range g.tiles[:g.Height()-1] {
		for col, tile := range rowTiles {
			switch tile {
			case start, beam:
				// Set tile below to beam if empty
				if err := g.setBeam(row+1, col); err != nil {
					return fmt.Errorf("Simulate: %w", err)
				}
			case splitter:
				// Set tiles left, right on level and one tile down from splitter
				if err := g.setBeam(row, col-1); err != nil {
					return fmt.Errorf("Simulate: %w", err)
				}
				if err := g.setBeam(row+1, col-1); err != nil {
					return fmt.Errorf("Simulate: %w", err)
				}
				if err := g.setBeam(row, col+1); err != nil {
					return fmt.Errorf("Simulate: %w", err)
				}
				if err := g.setBeam(row+1, col+1); err != nil {
					return fmt.Errorf("Simulate: %w", err)
				}
			}
		}
	}
	return nil
}

// Sets a tile to beam ONLY if that tile is empty. Don't alert if not empty
func (g *Grid) setBeam(row, col int) error {
	tile, err := g.Get(row, col)
	if err != nil {
		return fmt.Errorf("SetBeam: %w", err)
	}

	if tile == empty {
		if err := g.Set(row, col, beam); err != nil {
			return fmt.Errorf("SetBeam: %w", err)
		}
	}
	return nil
}

func parseLine(line string) ([]Tile, error) {
	out := make([]Tile, len(line))

	for i, field := range line {
		var tile Tile
		switch field {
		case '.':
			tile = empty
		case 'S':
			tile = start
		case '^':
			tile = splitter
		default:
			return nil, fmt.Errorf("parseLine: %v is not a valid tile", field)
		}
		out[i] = tile
	}
	return out, nil
}

type Tile int

const (
	empty Tile = iota
	start
	splitter
	beam
)

var tileToString = map[Tile]string{
	empty:    ".",
	start:    "S",
	splitter: "^",
	beam:     "|",
}

func (tile Tile) String() string {
	return tileToString[tile]
}

func solve(g *Grid) (total int) {
	g.Simulate()
	// Count splitters with a beam above (aka beam has been split here)
	for row, rowTiles := range g.tiles {
		if row == 0 { // Avoid row OOB from tileAbove get
			continue
		}
		for col, tile := range rowTiles {
			tileAbove, err := g.Get(row-1, col)
			if err != nil {
				panic(fmt.Errorf("solve: %w", err))
			}
			if tile == splitter && tileAbove == beam {
				total++
			}
		}
	}
	return total
}

func checkErr(e error) {
	if e != nil {
		panic(e)
	}
}
