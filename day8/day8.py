'''
# PART 2 IDEA:
	if length 2 -> save the characters for the 1

	if length 3 -> it's a 7

	if length 4 -> it's a 4

	if length 7 -> it's an 8

	if length 5 ->
		-> if has character for the 1 -> its a 3

	if length 6 ->
		-> doesnt have characters for the 1 -> its a 6
		-> else if doesnt have characters for the 3 -> it's a 0
		-> else -> it's a 9
		-> save the letter that isn't in 9 but is in 6 for later use
	
	if length 5 ->
		-> if has letter from 6 and not 9 -> it's a 2
		-> otherwise it's a 5
	
# TEST:
	input:
		be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb

		be -> length 2 -> 1
		edb -> length 3 -> 7
		cgeb -> length 4 -> 4
		cfbegad -> length 7 -> 8

		fecdb -> has character for 1 -> 3

		fgaecd -> doesnt have characters for the 1 -> 6
		agebfd -> doesnt have characters for the 3 -> 0
		cbdgef -> remaining -> 9

		letter that is in 6 but not in 9 -> a

		fdcge -> doesnt have a letter that is in 6 and not in 9 -> 5
		fabcd -> remaining -> 2

		right side output:
		fdgacbe cefdb cefbgd gcbe
		8		3	  9		 4
'''

def has_all_characters_from_word(observed_word, target_word):
	return len(set(observed_word).intersection(target_word)) == len(target_word)

def find_character_that_is_not_in_target_word(observed_word, target_word):
	'''
	Works for this case:
		character is in: fgaecd
		but not in: cbdgef 

		f is
		g is
		a is NOT -> we should return this one
		e is
		c is
		d is
	'''
	target_word_characters = [c for c in target_word]
	for c in observed_word:
		if c not in target_word_characters:
			return c
	assert("Couldn't find the character, something went wrong, you're an idiot 🤔")

def sort_characters_in_word(word):
	return "".join(sorted(word))

def infer_encoding(signal_inputs):
	encoding = {}

	# find the word with length 2
	encoding[1] = next(word for word in signal_inputs if len(word) == 2)

	# find the word with length 3
	encoding[7] = next(word for word in signal_inputs if len(word) == 3)

	# find the word with length 4
	encoding[4] = next(word for word in signal_inputs if len(word) == 4)

	# find the word with length 7
	encoding[8] = next(word for word in signal_inputs if len(word) == 7)

	# find the words with length 5
	words_with_length_5 = [word for word in signal_inputs if len(word) == 5]

	# word with length 5 and has characters for the 1
	encoding[3] = next(word for word in words_with_length_5 if has_all_characters_from_word(word, encoding[1]))

	# delete the three from the pool of words with length 5 to yet decode
	words_with_length_5 = [word for word in words_with_length_5 if word != encoding[3]]

	# find the words with length 6
	words_with_length_6 = [word for word in signal_inputs if len(word) == 6]

	# find the word with length 6 that doesn't have the characters for the 1
	encoding[6] = next(word for word in words_with_length_6 if not has_all_characters_from_word(word, encoding[1]))

	# delete the six from the pool of words with length 6 to yet decode
	words_with_length_6 = [word for word in words_with_length_6 if word != encoding[6]]	

	# find the word with length 6 that doesn't have the characters for the 3
	encoding[0] = next(word for word in words_with_length_6 if not has_all_characters_from_word(word, encoding[3]))

	# the remaining word of length 6 is a 9
	encoding[9] = next(word for word in words_with_length_6 if word != encoding[0])

	# find the word with length 5 that has the letter missing from 9, which is in 6
	letter_missing_from_9_which_is_in_6 = find_character_that_is_not_in_target_word(encoding[6], encoding[9])
	encoding[2] = next(word for word in words_with_length_5 if has_all_characters_from_word(word, letter_missing_from_9_which_is_in_6))

	# the remaining word of length 5 is a 5
	encoding[5] = next(word for word in words_with_length_5 if word != encoding[2])

	# sort the characters in the encoded signals and invert keys and values
	encoding_with_sorted_characters = {sort_characters_in_word(v): k for k, v in encoding.items()}

	return encoding_with_sorted_characters

def decode_number(encoded_number_signals, encoding_lookup_table):
	# sort the characters in the encoded signals
	sorted_encoded_number_signals = [sort_characters_in_word(signal) for signal in encoded_number_signals]

	# decode each digit
	decoded_digits = []
	for signal in sorted_encoded_number_signals:
		decoded_digits.append(encoding_lookup_table[signal])

	# turn digits into strings
	decoded_digit_strings = [str(d) for d in decoded_digits]

	# join them into one digit string
	number_result_as_string = "".join(decoded_digit_strings)

	# make an integer out of the string and return it
	return int(number_result_as_string)

# open file
f = open('../inputs/day8/1.txt')

# for part one, just count the occurrences of the word lengths in the output signals
print("Part 1:", len([word for line in [line.split("|")[1].strip() for line in open('../inputs/day8/1.txt').read().splitlines()] for word in line.split(" ") if len(word) in [7, 4, 3, 2]]))

# read input
lines = f.read().splitlines()

# initialize decoded number storage
decoded_numbers = []

result = 0

for line in lines:
	split_line = line.split(" | ")
	input_signals = split_line[0].split(" ")
	encoded_number_signals = split_line[1].split(" ")
	encoding = infer_encoding(input_signals)
	decoded_number = decode_number(encoded_number_signals, encoding)
	result += decoded_number

print("Part 2:", result)
