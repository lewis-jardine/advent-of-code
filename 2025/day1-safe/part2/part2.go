// TODO: Complete this challenge (2443 was too low)

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
			dial -= amount

			if dial == 0 {
				zero_count += 1
			} else if dial < 0 {
				// '/' rounds up so always need to add one
				// 50 L225 = -175
				zero_count += (dial / 100) + 1
				dial %= 100
				// Need to bound to 99
				if dial != 0 {
					dial += 100
				}
			}
		case 'R':
			dial += amount
			zero_count += dial / 100
			dial %= 100
		default:
			s := fmt.Sprintf("'L' or 'R' not found as first character of line %d", i)
			panic(s)
		}

		fmt.Printf("Dial rotated %q%d pointing at %d. Zero count: %d\n", direction, amount, dial, zero_count)
		// Bound to 0 - 99, only required if not 0
		if dial > 99 || dial < 0 {
			panic("dial out of bounds")
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
