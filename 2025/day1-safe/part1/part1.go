package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const Input = "../input.txt"

// const Input = "../test.txt"

func main() {

	f, err := os.Open(Input)
	checkErr(err)
	defer f.Close()

	// Current position of dial and count of times dial has been at zero
	dial, zero_count := 50, 0

	scanner := bufio.NewScanner(f)
	for i := 0; scanner.Scan(); i++ {
		line := scanner.Text()

		if len(line) == 0 {
			continue
		}

		// Each line is made of 'L' or 'R' followed by n length integer
		direction := rune(line[0])
		amount, err := strconv.Atoi(line[1:])
		checkErr((err))

		switch direction {
		case 'L':
			amount *= -1
		case 'R':
			// Do nothing
		default:
			s := fmt.Sprintf("'L' or 'R' not found as first character of line %d", i)
			panic(s)
		}
		// Dial bounded from 0 to 99
		// I don't know why this solution works, it actually bounds from -99 to 99...
		dial = (dial + amount) % 100
		fmt.Println("dial", dial)

		if dial == 0 {
			zero_count++
			fmt.Println("zero", zero_count)
		}
	}

	if err := scanner.Err(); err != nil {
		checkErr(err)
	}

	fmt.Printf("Solution: %d\n", zero_count)

}

func checkErr(e error) {
	if e != nil {
		panic(e)
	}
}
