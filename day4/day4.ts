import fs from 'fs'

const sum = (array: number[]) => {
	return array.reduce((accumulator, currentValue) => {
	  return accumulator + currentValue
	}, 0)
}

const parseGame = (input: string) => {
	const lines = input.split(/\n/)
	const draws = lines[0].split(",").map(num => parseInt(num))
	
	let boards: number[][][] = []
	let currentBoard: number[][] = []
	
	for (const line of lines.slice(2)) {
		if (line.length < 1) {
			boards.push(currentBoard)
			currentBoard = []
			continue;
		}
	
		const splitLine = line.split(" ")
	
		const currentLineNumberArray = splitLine
			.filter(numString => numString.length > 0)
			.map(numString => parseInt(numString))
	
		currentBoard.push(currentLineNumberArray)
	}

	return {
		draws,
		boards
	}
}

const initializeEmptyBoardHits = (numberOfBoards: number, boardDimensionX: number, boardDimensionY: number): number[][][] => {
	let emptyBoardHits: number[][][] = []

	for (let i = 0; i < numberOfBoards; i++) {
		let emptyBoard: number[][] = [];
		for (let j = 0; j < boardDimensionY; j++) {
			let emptyBoardLine: number[] = []
			for (let k = 0; k < boardDimensionX; k++) {
				emptyBoardLine.push(0)
			}
			emptyBoard.push(emptyBoardLine)
		}
		emptyBoardHits.push(emptyBoard)
	}

	return emptyBoardHits
}

const transpose = (a: any[][]): any[][] => {
	return a[0].map((_, c) => a.map(r => r[c]));
}

const boardHasWin = (boardHitsForBoard: number[][]) => {
	for (const line of boardHitsForBoard) {
		if (line.every(number => number === 1)) {
			return true
		}
	}

	const transposedBoardHitsForBoard = transpose(boardHitsForBoard)

	for (const line of transposedBoardHitsForBoard) {
		if (line.every(number => number === 1)) {
			return true
		}
	}

	return false;
}

const getUnmarkedNumbersFromBoard = (board: number[][], boardHitsForBoard: number[][]): number[] => {
	let result: number[] = []
	for (let i = 0; i < board.length; i++) {
		for (let j = 0; j < board[i].length; j++) {
			if (boardHitsForBoard[i][j] === 0) {
				result.push(board[i][j])
			}
		}	
	}

	return result
}

const setBoardHitsFromDraw = (draw: number, boards: number[][][], boardHits: number[][][]): number[][][] => {
	let newBoardHits = boardHits

	for (let i = 0; i < boardHits.length; i++) {
		for (let j = 0; j < boardHits[i].length; j++) {
			for (let k = 0; k < boardHits[i][j].length; k++) {
				if (boards[i][j][k] === draw) {
					newBoardHits[i][j][k] = 1
				}
			}
		}
	}

	return newBoardHits
}

function shuffleArray(array: unknown[]) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

const input = fs.readFileSync('../inputs/day4/1.txt', 'utf8')

let { draws, boards } = parseGame(input)
shuffleArray(boards)

let boardHits = initializeEmptyBoardHits(boards.length, boards[0][0].length, boards[0].length)

const runGameLoop = () => {
	/**
	 * Game loop
	 */
	for (let round = 0; round < draws.length; round++) {
		// Read a draw
		let currentDraw: number = draws[round]

		// Set hits from current draw
		boardHits = setBoardHitsFromDraw(currentDraw, boards, boardHits)

		// Check for wins
		for (let i = 0; i < boards.length; i++) {
			if (boardHasWin(boardHits[i])) {
				const unmarkedNumbersFromBoard = getUnmarkedNumbersFromBoard(boards[i], boardHits[i])
				const sumOfUnmarkedNumbers = sum(unmarkedNumbersFromBoard)
				const result = sumOfUnmarkedNumbers * currentDraw;
				console.log("Result:", result)
				return;
			}
		}
	}
}

runGameLoop();
