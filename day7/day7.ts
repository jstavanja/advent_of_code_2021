import fs from 'fs';

// read and parse input
const input = fs.readFileSync('../inputs/day7/1.txt', 'utf8');
const lines = input.split(/\n/);
const locations = lines[0].split(",").map(num => parseInt(num));

// find a median
const calculateMedian = (array: number[]) => {
	array = array.sort((a: number, b: number) => {
		return a - b;
	});
	if (array.length % 2 === 0) {
		return (array[(array.length / 2) - 1] + array[array.length / 2]) / 2;
	}
	else {
		return array[(array.length - 1) / 2];
	}
};

const median = calculateMedian(locations);

// find the amount of spent fuel
const spentFuel = locations.reduce((accumulator, currentLocation) => {
	return accumulator + Math.abs(currentLocation - median);
}, 0)

console.log(spentFuel);
