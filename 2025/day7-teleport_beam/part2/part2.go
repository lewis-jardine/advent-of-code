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

func (g *Grid) FindStart() (row, col int, err error) {
	for row, rowTiles := range g.tiles {
		for col, tile := range rowTiles {
			if tile == start {
				return row, col, nil
			}
		}
	}
	return -1, -1, fmt.Errorf("Grid: no start tile found")
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

// Simulate one particle, starting at a given coordinate and always going left
func (g *Grid) SimulateParticle(row, col int) (directions []Direction, err error) {
	// Continue down until first splitter is encoutered
	// Iterate through each row in grid (starting from one below current) until bottom reached
	for i := row + 1; i < g.Height(); i++ {
		tile, err := g.Get(i, col)
		if err != nil {
			return nil, fmt.Errorf("SimulateParticle: %w", err)
		}

		// Record new direction and shift beam to the left
		if tile == splitter {
			directions = append(directions, left)
			col--
		}
	}
	return directions, nil
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

// Coordinates of a splitter and the direction previously taken at that splitter
type SplitterDecision struct {
	row       int
	col       int
	direction Direction
}

type Direction int

const (
	left Direction = iota
	right
)

var directionToString = map[Direction]string{
	left:  "left",
	right: "right",
}

func (direction Direction) String() string {
	return directionToString[direction]
}

/*
We want to find the number of unique beam paths
A beam ends when it reaches the bottom of the grid

Store whether we went left or right at each splitter - start with all left
Store run then change the last splitter to right, appending new splitters as reached
Continue until all decisions are right
*/
func solve(g *Grid) (total int) {
	// Simulate one run from the start to give the first batch of splitter directions
	row, col, err := g.FindStart()
	if err != nil {
		panic(err)
	}

	for {
		directions, err := g.SimulateParticle(row, col)
		if err != nil {
			panic(err)
		}

		// nil == end of grid reached, full particle run simulated
		if directions == nil {
			total++
		}
	}

	return total
}

// Find if all directions are right
func directionsAllRight(directions []Direction) bool {
	for _, direction := range directions {
		if direction == left {
			return false
		}
	}
	return true
}

func checkErr(e error) {
	if e != nil {
		panic(e)
	}
}
