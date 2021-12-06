import numpy as np

DAYS = 256

def generate_empty_window(length):
	return np.array([0 for _ in range(length)])	

f = open('../inputs/day6/1.txt')

fish = np.array([int(f) for f in f.read().rstrip().split(",")])

# Invert instances and numbers to indices and values (as amount of instances)
window = generate_empty_window(9)
for f in fish:
	window[f] += 1

def process_day(window):
	copy = generate_empty_window(9)

	fish_that_reproduce_today = window[0]

	for i in range(1, len(window)):
		copy[i-1] += window[i]
		
	copy[6] += fish_that_reproduce_today
	copy[8] = fish_that_reproduce_today

	return copy

for day in range(DAYS):
	window = process_day(window)

print(sum(window))
