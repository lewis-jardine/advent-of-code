package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Range struct {
	Start int
	End   int
}

func main() {
	// input := readInput("../test.txt")
	input := readInput("../input.txt")
	solution := solve(input)
	fmt.Println(solution)
}

// Read file, split by commas and then hyphens to denote ranges (0:start,1:end)
func readInput(inputPath string) []Range {
	f, err := os.Open(inputPath)
	checkErr(err)
	defer f.Close()

	// Only one line
	scanner := bufio.NewScanner(f)
	scanner.Scan()
	line := scanner.Text()
	splitLine := strings.Split(line, ",")

	var finalLine []Range
	for _, i := range splitLine {
		splitI := strings.Split(i, "-")

		// Split should always be len 2
		if len(splitI) != 2 {
			panic(fmt.Sprintf("%s should be length 2", splitI))
		}

		start, err := strconv.Atoi(splitI[0])
		checkErr(err)

		end, err := strconv.Atoi(splitI[1])
		checkErr(err)

		rangeItem := Range{
			Start: start,
			End:   end,
		}
		finalLine = append(finalLine, rangeItem)
	}
	return finalLine
}

func solve(input []Range) int {
	total := 0
	for _, idRange := range input {
		for id := idRange.Start; id <= idRange.End; id++ {
			if isIdInvalid(id) {
				total += id
			}
		}
	}
	return total
}

// Check if ID invalid (made up of repeating digits)
func isIdInvalid(id int) bool {
	strId := strconv.Itoa(id)
	lenId := len(strId)

	// Iterate through each repeat digit possibility
	// A repeat runs out of room if > half total length of id
	for i := 1; i <= lenId/2; i++ {
		// A repeat also must fit exactly into the id 'n' times
		if lenId%i != 0 {
			continue
		}
		// Create repeat match by extending sequence to length of id
		repeatStr := strings.Repeat(strId[:i], lenId/i)
		if strId == repeatStr {
			return true
		}
	}
	return false
}

func checkErr(e error) {
	if e != nil {
		panic(e)
	}
}
