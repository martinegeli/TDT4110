from turtle import *

for i in range(4):
	forward(100)
	left(90)

for h in range(19, 1, -3):
	forward(100)
	left(60)
	pensize(h)

#oppgave 2
for i in range(35):
	forward(250 - 7 * i)
	left(90)

#oppgave 3
kanter = int(input("Velg antall kanter: "))
omkrets = int(input("Velg omkrets på polygonet: "))

for i in range(kanter):
	pensize(7)
	forward(omkrets / kanter)
	left(360 / kanter)
