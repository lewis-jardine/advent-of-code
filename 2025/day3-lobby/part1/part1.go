package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	// input := readInput("../test.txt")
	input := readInput("../input.txt")
	solution := solve(input)
	fmt.Println(solution)
}

// Input file is lines of strings, made up of digits
func readInput(inputPath string) []string {
	f, err := os.Open(inputPath)
	checkErr(err)
	defer f.Close()

	scanner := bufio.NewScanner(f)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		checkErr(err)
	}

	return lines
}

func solve(input []string) int {
	total := 0
	for _, joltages := range input {
		n := maxJoltage(joltages)
		total += n
	}
	return total
}

// Find two digits in string that combine to give the highest number
func maxJoltage(joltages string) int {
	// First, find highest digit in string
	highest1, highestIdx1 := '0', 0
	for idx, joltage := range joltages {
		// Stop one before the end so theres spaced to find the second digit
		if idx+1 == len(joltages) {
			break
		}
		if joltage > highest1 {
			highest1 = joltage
			highestIdx1 = idx
		}
	}
	// Then, starting from that index find the next highest
	highest2 := '0'
	for _, joltage := range joltages[highestIdx1+1:] {
		if joltage > highest2 {
			highest2 = joltage
		}
	}
	out, err := strconv.Atoi(string(highest1) + string(highest2))
	checkErr(err)
	return out
}

func checkErr(e error) {
	if e != nil {
		panic(e)
	}
}
