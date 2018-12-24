hemmelig_ord=input('Skriv inn ditt hemmelige ord: ')
antall_liv=int(input('Skriv inn antall liv: '))
løsning="*"*len(hemmelig_ord)
while True:
	bokstav=input('Gjett en bokstav: ')
	if bokstav in hemmelig_ord:
		print('Stemmer, bokstaven', bokstav, 'er i ordet')
	elif bokstav not in hemmelig_ord:
		print('Feil, bokstaven', bokstav, 'er ikke i ordet')
		antall_liv-=1
		print('Du har', antall_liv, 'liv igjen')
		if antall_liv==0:
			print("Du tapte")
			break
	for i in range(len(løsning)):
		if bokstav==hemmelig_ord[i]:
			løsning[i]=hemmelig_ord[i]
			print(løsning)
	if løsning==hemmelig_ord:
		print('Gratulerer, du vant')
		break