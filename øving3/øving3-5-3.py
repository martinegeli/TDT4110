from turtle import *

kanter= int(input("Velg antall kanter: "))
omkrets= int(input("Velg omkrets på polygonet: "))

for i in range(kanter):
	pensize(7)
	forward(omkrets/kanter)
	left(360/kanter)