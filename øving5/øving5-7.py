from math import *

def f(x):
	return (x-12)*e**(5*x)-8*((x+2)**2)

def g(x):
	return -x-2*(x**2)-5*(x**3)+6*(x**4)

print(g(1))
print(f(0))

def derivate(h, x, func):
	return (func(x+h/2)-func(x-h/2))/h

print('Derivate: ', derivate(0.000001, -2, f))

def newtons_method(h, x, func, tol):
	xold=x+2*tol 
	while fabs(x-xold) > tol: #fabs returnerer absoluttverdien
		xnew = x - func(x)/derivate(h, x, func)
		xold=x
		x=xnew
	print("Argumentets verdi: ",x)
	print("Funksjonens verdi: ",func(x))
	return x
			 
#tol=float(input('Velg en toleransegrense: '))
newtons_method(0.00000001, -2, f, 0.0000000001)
