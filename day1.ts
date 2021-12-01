import fs from 'fs'

let input: string;
try {
	const input = fs.readFileSync('./inputs/day1/1.txt', 'utf8')
	let measurements: number[] = input.split(/\n/).map((measurement: string) => parseInt(measurement))

	let previous = measurements[0]

	measurements = measurements.slice(1)

	let timesIncreased = 0
	for (const measurement of measurements) {
		if (measurement > previous) {
			timesIncreased++;
		}

		previous = measurement
	}

	console.log(timesIncreased)
} catch (err) {
  console.error(err)
}
