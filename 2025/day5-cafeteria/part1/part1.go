package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Range struct {
	start int
	end   int
}

func main() {
	idRanges, ids := readInput("../input.txt")
	solution := solve(idRanges, ids)
	fmt.Println(solution)
}

/*
Input file is split into two parts seperated by blank line:
 1. 'range' two ints split by hyphen
 2. 'id' a single int
*/
func readInput(inputPath string) (idRanges []Range, ids []int) {
	f, err := os.Open(inputPath)
	checkErr(err)
	defer f.Close()

	reachedIds := false
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		// Change logic to parse for ids once blank line is hit
		if line == "" {
			reachedIds = true
			continue
		}

		if !reachedIds {
			idRange, err := parseIdRange(line)
			if err != nil {
				panic(err)
			}
			idRanges = append(idRanges, idRange)
		} else {
			id, err := strconv.Atoi(line)
			if err != nil {
				panic(err)
			}
			ids = append(ids, id)
		}
	}

	if err := scanner.Err(); err != nil {
		checkErr(err)
	}

	return idRanges, ids
}

// Parse string of two ints seperated by a hyphen into a valid Range
// Return error if string is not a valid idRange
func parseIdRange(inStr string) (outRange Range, outErr error) {
	splitLine := strings.Split(inStr, "-")
	if len(splitLine) != 2 {
		return outRange, fmt.Errorf("idRange should be two items only: %v", splitLine)
	}

	startId, err := strconv.Atoi(splitLine[0])
	if err != nil {
		return outRange, fmt.Errorf("parseIdRange: failed to convert first item in %v to int: %w", splitLine, err)
	}

	endId, err := strconv.Atoi(splitLine[1])
	if err != nil {
		return outRange, fmt.Errorf("parseIdRange: failed to convert second item in %v to int: %w", splitLine, err)
	}

	return Range{start: startId, end: endId}, nil
}

func solve(idRanges []Range, ids []int) int {
	total := 0
	for _, id := range ids {
		fresh := isFresh(id, idRanges)
		if fresh {
			total++
		}
	}
	return total
}

// Check if ingredient is fresh (id is in at least one id range)
func isFresh(id int, idRanges []Range) bool {
	for _, idRange := range idRanges {
		if id >= idRange.start && id <= idRange.end {
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
