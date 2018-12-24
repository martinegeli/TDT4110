a=int(input('Skriv inn et tall: '))
b=int(input('Skriv inn et tall til: '))
c=int(input('Skriv inn et siste tall: '))

d=b**2-(4*a*c)
if d<0:
    print('Andregradslikningen', a,'*x^2 +', b,'*x +', c, 'har to imaginære løsninger')
elif d>0:
    print('Andregradslikningen', a,'*x^2 +', b,'*x +', c, 'har to reelle løsninger')
else:
    print('Andregradslikningen', a,'*x^2 +', b,'*x +', c, 'har en reell løsning')
