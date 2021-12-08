print(len([word for line in [line.split("|")[1].strip() for line in open('../inputs/day8/1.txt').read().splitlines()] for word in line.split(" ") if len(word) in [7, 4, 3, 2]]))
