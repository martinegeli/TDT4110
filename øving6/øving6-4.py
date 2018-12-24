from math import *

def vektor():
	x=int(input('Skriv et tall: '))
	y=int(input('Skriv et tall: '))
	z=int(input('Skriv et tall: '))
	return [x,y,z]

vec1=vektor()
print('vec1 = ', vec1)

def skalar(v, c):
	return [c * item for item in v]
#ganger c med item for hver item i v. Når v har 3 elementer vil c gange inn hvert element og returnere det som en liste.

vec2=[3,4,5]
print(vec2)
print(skalar(vec2, 3))

def lengde(v):
	total=0
	for i in v:
		total+=i**2
	return sqrt(total)
#for hver i som finnes i v, så blir i**2 lagt til i total. return på slutten returnerer roten av total, som gir vektorens lengde.
	
print(lengde(vec2))
print(lengde(vec1))

def produkt(v, u):
	total=0
	for i in range(len(v)):
		total+=v[i]*u[i]
	return total
#produktet skal gange det første elementet i v med det første elementet i u, osv. Dette fungerer bare om vektorene er like lange. Returnerer total som da blir skalarproduktet.

print(produkt(vec1, vec2))

