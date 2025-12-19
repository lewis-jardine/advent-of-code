package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const DigitCount int = 12

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
		n := maxJoltage(joltages, DigitCount)
		total += n
		// fmt.Printf("joltages: %v\n", joltages)
		// fmt.Printf("n: %v\n", n)
		// fmt.Println()
	}
	return total
}

// Find n digits in string that combine to give the highest number
func maxJoltage(joltages string, nDigits int) int {
	// fmt.Println(joltages)
	// Next idx to be searched
	nextIdx := 0
	outStr := ""
	// n = within how many digits can I get to the end?
	// if closer than n, then not enough room to find rest of joltage digits
	for n := nDigits - 1; n >= 0; n-- {
		// fmt.Printf("n: %v\n", n)
		highestJoltage := rune(0)
		joltageRange := joltages[nextIdx : len(joltages)-n]
		// fmt.Printf("joltageRange: %v\n", joltageRange)
		// Highest idx internal to joltageRange will be different to overall highestIdx
		// Due to joltageRange being sliced
		rangeHighestIdx := 0
		// Search for next highest joltage after last
		for idx, joltage := range joltageRange {
			if joltage > highestJoltage {
				highestJoltage = joltage
				rangeHighestIdx = idx
			}
		}
		if highestJoltage == 0 {
			panic("Next Joltage could not be found")
		}
		// Advance one idx at minimum
		nextIdx += rangeHighestIdx + 1
		outStr += string(highestJoltage)
		// fmt.Printf("outStr: %v\n", outStr)

	}
	out, err := strconv.Atoi(outStr)
	checkErr(err)
	return out
}

func checkErr(e error) {
	if e != nil {
		panic(e)
	}
}
