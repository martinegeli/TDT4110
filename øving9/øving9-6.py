def number_of_lines(filename):
	f = open(filename, 'r')
	i = 0
	while True:
		for linje in f:
			i += 1
		break
	f.close()
	return i

print("Filen 'numbers.txt' har", number_of_lines('numbers.txt'), 'linjer i filen')

def number_frequency(filename):
	numbers = {}
	tall = []
	f = open(filename, 'r')
	for line in f.read().splitlines():
		tall.append(int(line))
	f.close()
	tall = sorted(tall)
	for i in range(len(tall)):
		numbers[tall[i]] = tall.count(tall[i])
	return numbers

print('Dictionarien kan skrives ut på måten: ', number_frequency('numbers.txt'))



for key, value in number_frequency('numbers.txt').items():
	print(key, ":", value)
