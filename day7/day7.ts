import fs from 'fs';

const calculateFuelNeeded = (locations: number[], useLinearFuelIncrease: boolean = false) => {
	let lowestFuel = Number.MAX_SAFE_INTEGER;
	for (let i = 0; i <= Math.max(...locations); i++) {
		const usedFuelToCurrentPoint = locations
			.map(location => {
				let positionDifference = Math.abs(location - i);
				if (useLinearFuelIncrease) {
					// compute 1 + 2 + 3 + 4 ... (linear sum)
					positionDifference = positionDifference * (positionDifference + 1) / 2
				}
				return positionDifference;
			})
			.reduce((accumulator, currentValue) => {
				return accumulator + currentValue
			}, 0)

		if (usedFuelToCurrentPoint < lowestFuel) {
			lowestFuel = usedFuelToCurrentPoint;
		}
	}

	return lowestFuel
}

const input = fs.readFileSync('../inputs/day7/1.txt', 'utf8');
const lines = input.split(/\n/);
const locations = lines[0].split(",").map(num => parseInt(num));

console.log(calculateFuelNeeded(locations));
console.log(calculateFuelNeeded(locations, true));
