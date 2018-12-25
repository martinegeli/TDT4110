cheeses = {
'cheddar':
('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
'mozarella':
('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
'gombost':
('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
'geitost':
('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
'port salut':
('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
'camembert':
('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
'ridder':
('GOMBOS-4', 'B16-3'),
}

#print(cheeses.keys())
def finn_hylleplasser(ost):
	return cheeses[ost]

print(finn_hylleplasser('port salut'))


def infected_cheeses(cheeses, smittetHyller):
	result = []
	for key, value in cheeses.items():
		for v in value:
			for elem in smittetHyller:
				if v.startswith(elem) and key not in result:
					result.append(key)
	return result

print("B15-1".startswith("B15"))

smittetHyller=['B13', 'B14', 'B15', 'A234', 'A235', 'C31']
infected_cheeses=infected_cheeses(cheeses, smittetHyller)

print('Mulig infiserte oster: ', infected_cheeses)

def find_not_infected(cheeses, infected_cheeses):
	result = []
	for key, value in cheeses.items():
		if key not in infected_cheeses:
			for v in value:
				result.append(str(v).ljust(10) + " " + str(key).ljust(12))
	return result

not_infected = find_not_infected(cheeses, infected_cheeses)
for elem in not_infected:
	print(elem)


l = [1,2,3,1,2]
print(list(set(l)))
