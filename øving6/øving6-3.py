

def is_six_at_edge(liste):
	if liste[0] == 6 or liste[len(liste)-1] == 6: #kan også bruke liste[-1] for å finne siste
		return True
	return False
#listen returnerer True om det første eller siste elementet er i listen. len begynner å telle på 1, men indeksen til listen begynner på 0. Derfor må man trekke fra en for indeks til listen for å finne det siste tallet.

def average(liste):
	f = float(sum(liste) / len(liste))
	return f
#deler summen av listen på lengden av listen

def median(liste):
	liste.sort()
	mid = int((len(liste)/2-0.5))
	return liste[mid]
#funker best om det er en oddetallsliste. Sorterer listen, deretter finner det midterste ved lengden/2. Om listen er av partallslengde vil den, fordi jeg trakk fra 0.5, returnere den minste verdien av de to i midten.

k=[1,2,3,4,5,6,7]
l=[1,2,3,4,5,6]
h=[6,1,5,2,7,3]

print(is_six_at_edge(k))
print(average(h))
print(median(k))
print(median(h))
