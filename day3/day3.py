import numpy as np

f = open('../inputs/day3/1.txt')

def transform_into_binary_matrix(string_list):
	result = []
	for s in string_list:
		number_list = [int(c) for c in s]
		result.append(number_list)

	return result

matrix = transform_into_binary_matrix(f.read().splitlines())
m = np.array(matrix)

def return_number_with_most_and_least_occurences(array):
	counts = np.bincount(array)
	return np.argmax(counts), np.argmin(counts)

gamma_array = [return_number_with_most_and_least_occurences(bits)[0] for bits in m.T]
gamma_rate_string = ''.join(str(bit) for bit in gamma_array)
gamma_decimal_rate = int(gamma_rate_string, 2)

epsilon_array = [return_number_with_most_and_least_occurences(bits)[1] for bits in m.T]
epsilon_rate_string = ''.join(str(bit) for bit in epsilon_array)
epsilon_decimal_rate = int(epsilon_rate_string, 2)

power_consumption = gamma_decimal_rate * epsilon_decimal_rate

print(power_consumption)
