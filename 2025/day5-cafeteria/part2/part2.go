package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

type Range struct {
	start int
	end   int
}

func main() {
	idRanges := readInput("../input.txt")
	solution := solve(idRanges)
	fmt.Println(solution)
}

/*
Input file is split into two parts seperated by blank line:
 1. 'range' two ints split by hyphen
 2. 'id' a single int
*/
func readInput(inputPath string) (idRanges []Range) {
	f, err := os.Open(inputPath)
	checkErr(err)
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()

		// Only read until end of id ranges
		if line == "" {
			break
		}

		idRange, err := parseIdRange(line)
		if err != nil {
			panic(err)
		}
		idRanges = append(idRanges, idRange)
	}

	if err := scanner.Err(); err != nil {
		checkErr(err)
	}

	return idRanges
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

func solve(idRanges []Range) (total int) {
	// Merge intersecting ranges first so we don't double count ids
	idRanges = mergeRanges(idRanges)
	for _, idRange := range idRanges {
		total += countRange(idRange)
	}
	return total
}

func mergeRanges(idRanges []Range) (merged []Range) {
	// Must be ordered for algorithm to work
	orderRanges(idRanges)
	for _, r := range idRanges {
		if len(merged) == 0 {
			merged = append(merged, r)
		} else {
			last := &merged[len(merged)-1]
			if rangesIntersect(*last, r) {
				// Merge into last
				if r.start < last.start {
					last.start = r.start
				}
				if r.end > last.end {
					last.end = r.end
				}
			} else {
				merged = append(merged, r)
			}
		}
	}
	return merged
}

// Orders slice of ranges in place
func orderRanges(ranges []Range) {
	slices.SortFunc(ranges, func(a, b Range) int {
		// Order first by starts then by ends
		startCmp := a.start - b.start
		if startCmp == 0 {
			return a.end - b.end
		}
		return startCmp
	})
}

func rangesIntersect(range1 Range, range2 Range) bool {
	return range1.start <= range2.end && range1.end >= range2.start
}

func countRange(idRange Range) (count int) {
	return idRange.end - idRange.start + 1
}

func checkErr(e error) {
	if e != nil {
		panic(e)
	}
}
