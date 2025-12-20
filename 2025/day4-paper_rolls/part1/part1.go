package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// input := readInput("../test.txt")
	input := readInput("../input.txt")
	solution := solve(input)
	fmt.Println(solution)
}

// Input file is lines with either '.' or '@', signifying if roll present or not
// Return as 2d slice of bool (true if roll present)
func readInput(inputPath string) [][]bool {
	f, err := os.Open(inputPath)
	checkErr(err)
	defer f.Close()

	scanner := bufio.NewScanner(f)
	var lines [][]bool
	for scanner.Scan() {
		lines = append(lines, parseLine(scanner.Text()))
	}

	if err := scanner.Err(); err != nil {
		checkErr(err)
	}

	return lines
}

func parseLine(line string) []bool {
	var parsedLine []bool
	for _, i := range line {
		parsedLine = append(parsedLine, i == '@')
	}
	return parsedLine
}

func solve(input [][]bool) int {
	total := 0
	for y, row := range input {
		for x, roll := range row {
			if roll && isAccessible(input, y, x) {
				total++
			}
		}
	}
	return total
}

// Check if roll is accesible at location x, y in input
// A roll is accesible if it has < 4 others ('true' values) adjacent
func isAccessible(input [][]bool, initY int, initX int) bool {
	// Check slice idxs aren't OOB
	lowerY, upperY := initY-1, initY+2
	if lowerY < 0 {
		lowerY = 0
	}
	if upperY > len(input) {
		upperY = len(input)
	}
	lowerX, upperX := initX-1, initX+2
	if lowerX < 0 {
		lowerX = 0
	}
	if upperX > len(input[0]) {
		upperX = len(input[0])
	}

	rollCount := 0
	for y := lowerY; y < upperY; y++ {
		for x := lowerX; x < upperX; x++ {
			// Remeber to ignore the central roll
			if input[y][x] && !(y == initY && x == initX) {
				rollCount++
			}
		}
	}
	return rollCount < 4
}

func checkErr(e error) {
	if e != nil {
		panic(e)
	}
}
