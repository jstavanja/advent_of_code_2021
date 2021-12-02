import fs from 'fs'

const sum = (array: number[]) => {
  return array.reduce((accumulator, currentValue) => {
    return accumulator + currentValue
  }, 0)
}

const getEarliestWindowSumAndRemainingMeasurements = (
  windowSize: number,
  remainingMeasurements: number[]
) => {
  return {
    sum: sum(remainingMeasurements.slice(0, windowSize)),
    remainingMeasurements: remainingMeasurements.slice(1),
  }
}

const getNumberOfIncreasesForWindowSize = (
  measurements: number[],
  windowSize: number
) => {
  let { sum: previousWindowSum, remainingMeasurements } =
    getEarliestWindowSumAndRemainingMeasurements(windowSize, measurements)
  let timesIncreased = 0

  for (let i = 0; i < measurements.length - windowSize; i++) {
    const {
      sum: currentWindowSum,
      remainingMeasurements: currentRemainingMeasurements,
    } = getEarliestWindowSumAndRemainingMeasurements(
      windowSize,
      remainingMeasurements
    )

    if (currentWindowSum > previousWindowSum) {
      timesIncreased++
    }
    previousWindowSum = currentWindowSum
    remainingMeasurements = currentRemainingMeasurements
  }
  return timesIncreased
}

const part1 = (measurements: number[]) => {
  console.log(getNumberOfIncreasesForWindowSize(measurements, 1))
}

const part2 = (measurements: number[], windowSize: number) => {
  console.log(getNumberOfIncreasesForWindowSize(measurements, windowSize))
}

const input = fs.readFileSync('../inputs/day1/1.txt', 'utf8')
let measurements: number[] = input
  .split(/\n/)
  .map((measurement: string) => parseInt(measurement))

part1(measurements)
part2(measurements, 3)
