#2a) lage en funksjon chess_match() som lar brukeren skrive inn antall kamper og hvem som får poeng hver runde

def chess_match():
	total_score1=0
	total_score2=0
	num_games=int(input('Skriv inn antall partier: '))
	if num_games<1:
		print('Så kjedelig, da blir det ingen kamp!')
	else:
		parti=0
		while num_games>parti:
			score1=float(input('Skriv inn poeng til spiller 1: '))
			score2=float(input('Skriv inn poeng til spiller 2: '))
			total_score1+=score1
			total_score2+=score2
			parti+=1
	print('Kampen er slutt!')
	print('Spiller 1 fikk ', total_score1, ' poeng')
	print('Spiller 2 fikk ', total_score2, ' poeng')
	
#chess_match()

def end_of_match(num_games, game, total_score1, total_score2):
	if num_games>game and total_score1<(num_games/2+0.5) and total_score2<(num_games/2+0.5):
		return 0
	elif total_score1>(num_games/2):
		return 1
	elif total_score2>(num_games/2):
		return 2
	else:
		return 3

print(end_of_match(5, 3, 3, 0))
	
def chess_score():
	swap=True
	while swap:
		score1=eval(input('Skriv inn en score for spiller 1: '))
		if score1==0 or score1==0.5 or score1==1:
			score2=1-score1
			swap=False
		else:
			print('Umulig resultat')
	return score1, score2

#score1, score2 = chess_score()	
#print('Spiller 1 fikk', score1, 'poeng, og spiller 2 fikk', score2, 'poeng')

def player_score(results):
	total=0
	for i in range(len(results)):	
		if results[i] is not None:
			total+=results[i]
	return total
	
score=[1,1,1,0.5,0.5,0,0,None,None,1]
print(player_score(score))


#kodeforeståelse, del 3
def secret2(m):   
	r = len(m)   
	c = len(m[0])
	if r==c:
		for i in range(0,r-1):
			for j in range(i+1,c):
				temp = m[i][j]               
				m[i][j] = m[j][i]               
				m[j][i] = temp
		return m
	else:
		return -1	

m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(secret2(m))

#Oppgave 4: Mer programmering
#4a, en funksjon som tar inn pris og antall billetter. Om antallet er mer enn 3 skal de få 10% rabatt.
def payment(pris, antall):
	if antall>3:
		return pris*antall*0.90
	return pris*antall
	
def get_price(konsertnavn):
	pris=-1
	f=open('prices.txt', 'r')
	konsertline=f.readline()
	while konsertline!='' and pris==-1:
		konsert=konsertline.strip(';')
		if konsert[0]==konsertnavn:
			pris=float(konsert[1].rstrip('\n'))
		else:
			konsertline=f.readline()
	f.close()
	return pris

print(get_price('Gloshaugkameratene'))

def ticket(navn, konsertnavn, antall):
	kol1=18
	kol2=20
	number_stars=kol1 + kol2 + 2
	pris=get_price(konsertnavn)
	total=payment(pris, antall)
	stars='*'
	print(stars*number_stars)
	print('Uka 2015')
	print(stars * number_stars)
	print('Navn: '.rjust(kol1), navn.rjust(kol2))
	print('Konsert: '.rjust(kol1), konsertnavn.rjust(kol2))
	print('Antall billetter: '.rjust(kol1), str(antall).rjust(kol2))
	print('Totalpris: '.rjust(kol1), str(total).rjust(kol2))
	print(stars*number_stars)

ticket('Martin Egeli', 'The Rectorats', 3)

def write_to_file(filename, navn, konsertnavn, antall):
	pris=get_price(konsertnavn)
	total=int(payment(pris, antall))
	f=open(filename, 'a')
	enter='\n'
	data=konsertnavn+';'+str(antall)+';'+str(total)+';'+navn
	f.write(data+enter)
	f.close()

write_to_file('concerts.txt', 'Martin Egeli', 'The Rectorats', 8)



