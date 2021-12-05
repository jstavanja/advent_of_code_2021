import numpy as np

f = open('../inputs/day3/1.txt')

def transform_array_to_int(array):
	string_val = ''.join(str(bit) for bit in array)
	return int(string_val, 2)

def transform_into_binary_matrix(string_list):
	result = []
	for s in string_list:
		number_list = [int(c) for c in s]
		result.append(number_list)

	return result

matrix = transform_into_binary_matrix(f.read().splitlines())
m = np.array(matrix)

def return_number_with_most_and_least_occurences(array, arg_fallback=1):
	counts = np.bincount(array)
	all_values_same_amount_of_occurrences = np.all(counts == counts[0])

	if all_values_same_amount_of_occurrences:
		return arg_fallback, arg_fallback
	else:
		return np.argmax(counts), np.argmin(counts)

def return_number_with_most_and_least_occurences_in_position(position, matrix, arg_fallback=1):
	return return_number_with_most_and_least_occurences(matrix.T[position], arg_fallback)

gamma_array = [return_number_with_most_and_least_occurences(bits)[0] for bits in m.T]
gamma_rate_string = ''.join(str(bit) for bit in gamma_array)
gamma_decimal_rate = int(gamma_rate_string, 2)

epsilon_array = [return_number_with_most_and_least_occurences(bits)[1] for bits in m.T]
epsilon_rate_string = ''.join(str(bit) for bit in epsilon_array)
epsilon_decimal_rate = int(epsilon_rate_string, 2)

power_consumption = gamma_decimal_rate * epsilon_decimal_rate

print("Power consumption:", power_consumption)

OXYGEN_GENERATOR_RATING_TYPE = 'oxygen'
CO2_SCRUBBER_RATING_TYPE = 'co2'

def filter_bit_function(current_bit, most_common_bit, least_common_bit, rating_type):
	if rating_type == OXYGEN_GENERATOR_RATING_TYPE:
		return current_bit == most_common_bit
	else:
		return current_bit == least_common_bit

def get_rating(matrix, rating_type = OXYGEN_GENERATOR_RATING_TYPE):
	arg_fallback = 1 if rating_type == OXYGEN_GENERATOR_RATING_TYPE else 0
	valid_numbers = matrix

	i = 0

	while len(valid_numbers) > 1:
		most_common_bit, least_common_bit = return_number_with_most_and_least_occurences_in_position(i, valid_numbers, arg_fallback)

		valid_numbers = np.array(
			list(
				filter(
					lambda x: filter_bit_function(x[i], most_common_bit, least_common_bit, rating_type),
					valid_numbers
				)
			)
		)

		i += 1
	
	return valid_numbers[0]

oxygen_generator_array = get_rating(m, OXYGEN_GENERATOR_RATING_TYPE)
co2_scrubber_array = get_rating(m, CO2_SCRUBBER_RATING_TYPE)

oxygen_generator_rating = transform_array_to_int(oxygen_generator_array)
co2_scrubber_rating = transform_array_to_int(co2_scrubber_array)
print("Life support rating:", oxygen_generator_rating * co2_scrubber_rating)
