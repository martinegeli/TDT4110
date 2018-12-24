k= int(input('Skriv inn et heltall k som rekken ikke skal overgå: '))
summen = 0
liste=[]

for i in range(100):
	tall = (-1)**i * (i + 1)**2
	summen += tall
	liste.append(summen)
	if k<=summen:
		break
	
print('n =', i)
print('Summen av tallserien er', summen)
print(liste)
print('Resultatet med k =', k, ':', summen)
print('Antall ledd: ', len(liste))
