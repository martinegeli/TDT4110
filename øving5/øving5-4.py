tol = float(input('Skriv inn en toleransegrense: ')) #tol som en global variabel
def multi():
	count=1
	prod=1
	while True:
		prod1=prod #setter nye prod til å være gamle prod for hver iterasjon
		r=(1+1/(count)**2) #funksjonen
		count+=1
		prod*=r
		if prod-prod1<tol: #prod1 vil være den gamle prod, fordi den blir endret før prod får sin nye verdi, da ved =*r, og på den måten vil endringen være prod-prod1. 
			break
	return prod, (count-1) #fordi count må begynne på 1 fordi vi ikke ønsker zeroDivisionError. 
		
p, c = multi() #p får verdien prod som returneres etter funksjonen multi, og c får verdien (count-1)
		
print('Produktet ble', p, 'og den kjørte', c, 'ganger')