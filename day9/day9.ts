import fs from 'fs'

const input = fs.readFileSync('../inputs/day9/1.txt', 'utf8');
const lines = input.trim().split(/\n/);
const numbers = lines.map(line => line.split("").map(numberAsString => parseInt(numberAsString)));

const smallerThanAll = (observedNumber: number, targetNumbers: number[]) => {
	return targetNumbers.every(number => number > observedNumber)
}

const localMinima = []

for (let i = 0; i < numbers.length; i++) {
	for (let j = 0; j < numbers[0].length; j++) {
		const observedNumber = numbers[i][j];
		
		const numberAbove = (i > 0) ? numbers[i-1][j] : 9999999999999;
		const numberToTheLeft = (j > 0) ? numbers[i][j-1] : 9999999999999;
		const numberToTheRight = (j < numbers[0].length - 1) ? numbers[i][j+1] : 9999999999999;
		const numberBelow = (i < numbers.length - 1) ? numbers[i+1][j] : 9999999999999;

		if (smallerThanAll(observedNumber, [numberAbove, numberToTheLeft, numberToTheRight, numberBelow])) {
			localMinima.push(observedNumber)
		}
	}
}

const sumOfRiskLevels = localMinima.reduce((accumulator, currentValue) => {
	return accumulator + currentValue + 1
}, 0)

console.log(sumOfRiskLevels)
