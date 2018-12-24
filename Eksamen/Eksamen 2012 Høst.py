#EKSAMEN 2012 Høst

#Oppgave 2 - grunnleggende programmering

#2a)
def summer(first, last):
	years=[]
	for i in range(first, last+1):
		if i%4==0:
			years.append(i)
	return years
	
print(summer(1948, 2012))

import datetime 

def findAge(bYear, bMonth, bDay):
	(yyyy, mm, dd)=currentDate()
	
#Oppgave 4 - Programmering
	
#Lager en funksjon som tar inn en liste av temperaturer, og returnerer variabelen days som viser antall døgn det var under 0 grader
def cold_days(tempList):
	days=0
	for i in range(len(tempList)):
		if tempList[i]<0:
			days+=1
	return days

tempList=[-2,3,-4,2,6,8,-1,-4,-6]
print(cold_days(tempList))

#Lager en funksjon cap_data som skal returnere en ny liste hvor tall skal holde seg innenfor en min_value og max_value. Er de over i listen som funksjonen tar inn så settes de like grenseverdiene.
def cap_data(array, min_value, max_value):
	result=[]
	for i in range(len(array)):
		if array[i]<min_value:
			result.append(min_value)
		elif array[i]>max_value:
			result.append(max_value)
		else:
			result.append(array[i])
	return result
A=[-55,25,90,15,-80]
print(cap_data(A, -50, 50))

#lager en funksjon generate_testdata som returnerer en liste med N unike tall, som er random skapt mellom en max og min verdi.
import random
def generate_testdata(N,min_value,max_value):
	result=[]
	n=0
	while n<N:
		tilfeldig=random.randint(min_value,max_value)
		if tilfeldig not in result:
			result.append(tilfeldig)
			n+=1
	return result
#Denne skapte problemer når jeg kalte tilfeldig for random
print(generate_testdata(10, -10, 10))

#lage en funksjon create_db som setter opp en dictionary med verdier
def create_db(temp, rain, humidity, wind):
	my_dict={}
	for i in range(len(temp)):
		my_dict[i+1]=[temp[i],rain[i],humidity[i],wind[i]]
	return my_dict

temp=[1,5,3]
rain=[0,30,120]
humidity=[30,50,65]
wind=[3,5,7]
weather=create_db(temp, rain, humidity, wind)
print(weather)

#Skal lage en funksjon som printer slik at det ser pent ut
"""def print_db(weather):
	print('Day | Temp | Rain | Humidity | Wind |')
	print('====+======+======+==========+======')
	for x in weather:
		liste=weather[x]
		s=str(liste[0]).rjust(4)
		s+=str(liste[1]).rjust(6)
		s+=str(liste[2]).rjust(6)
		s+=str(liste[3]).ljust(10)
		s+=str(liste[4]).ljust(6)
		print(s)
print_db(weather)"""

#lage en funksjon strange_weather som skal finne startdag og sluttdag for det lengste intervallet hvor det er minusgrader, samt at temperaturen falles samtidig som nedbørsmengden stiger i etterfølgende dager.
def strange_weather(temp, rain):
	start=0
	stopp=0
	antall=1
	størst=0
	for i in range(len(temp[1:])):
		if temp[i]<0 and temp[i+1]<temp[i] and rain[i]<rain[i+1]:
			antall+=1
			if antall>størst:
				størst=antall
	return antall

temperatur=[1,3,4,-5,-6,-7,-8,-9,3,0]
regn=[0,20,30,0,10,30,50,0,5,2]
print(strange_weather(temperatur, regn))

