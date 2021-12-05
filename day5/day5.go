package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {

	content, err := ioutil.ReadFile("../inputs/day5/1.txt")
	if err != nil {
		panic(err)
	}

	inputLines := strings.Split(string(content), "\n")

	matrix := make([][]int, 1000)
	for i := range matrix {
		matrix[i] = make([]int, 1000)
	}

	for _, line := range inputLines[:len(inputLines)-1] {
		coordinatePairs := strings.Split(line, "->")

		for i := 0; i < len(coordinatePairs); i++ {
			coordinatePairs[i] = strings.ReplaceAll(coordinatePairs[i], " ", "")
		}

		firstPair := strings.Split(coordinatePairs[0], ",")
		secondPair := strings.Split(coordinatePairs[1], ",")

		x1, _ := strconv.Atoi(firstPair[0])
		y1, _ := strconv.Atoi(firstPair[1])
		x2, _ := strconv.Atoi(secondPair[0])
		y2, _ := strconv.Atoi(secondPair[1])

		if x1 == x2 {
			var startingY int
			var endingY int

			if y1 < y2 {
				startingY = y1
				endingY = y2
			} else {
				startingY = y2
				endingY = y1
			}

			for i := startingY; i <= endingY; i++ {
				matrix[i][x1]++
			}

		}

		if y1 == y2 {
			var startingX int
			var endingX int

			if x1 < x2 {
				startingX = x1
				endingX = x2
			} else {
				startingX = x2
				endingX = x1
			}

			for i := startingX; i <= endingX; i++ {
				matrix[y1][i]++
			}
		}
	}

	result := 0
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			if matrix[i][j] > 1 {
				result++
			}
		}
	}

	fmt.Println(result)
}
