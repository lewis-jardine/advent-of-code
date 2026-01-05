package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// input := readInput("../input.txt")
	input := readInput("../test.txt")
	// solution := solve(input)
	fmt.Println(input)
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

// func solve(problems [][]Tile) (total int) {
// 	for _, problem := range problems {
// 		total += solveProblem(problem)
// 	}
// 	return total
// }

// Parser will build problems out of 1+ lines of whitespace seperated operands and 1 line
// of whitespace seperated operators. The problems slice will only be built when the parser
// is provided an operator line and valid operands have been provided.
// type Parser struct {
// 	problems    []Problem
// 	allOperands [][]int
// }

// Feed lines of operands or operators into parser. Build problems if an operator line is provided.
// func (p *Parser) parseLine(line string) error {
// 	splitLine := strings.Fields(line)

// 	return nil
// }

func checkErr(e error) {
	if e != nil {
		panic(e)
	}
}
