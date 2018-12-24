def pris():
	if alder<5:
		print('Turen er gratis')
	elif alder>=5 and alder<=20:
		print('Prisen blir 20kr')
		summer=20
	elif alder>=21 and alder<=25:
		print('Turen blir 50kr')
		summer=50
	elif alder>=26 and alder<=60:
		summer=80
		print('Turen blir', summer, 'kr')
	else: 
		print('Turen er gratis')
		summer=0
	sykkel=input('Har du med deg sykkel (j/n) ?')
	if sykkel=='j':
		summer=summer+50
	elif sykkel=='n':
		summer=summer
	else:
		print('Du må svare enten "j" eller "n"')
	return summer


alder=int(input('Hvor gammel er du? '))
print('Prisen blir', pris(), 'kr')
