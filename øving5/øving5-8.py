def gcd(a,b):
	while b!=0:
		gammel_b=b #i løkken setter vi gammel_b til å være b
		b=a%b #finner b ved å ta a modulo b, som gir rest etter at a er delt på b
		a=gammel_b #setter a til å være gammel_b, slik at fra øverst så vil nå resten fra a%b bli til a, som vil brukes til å finne ny rest i neste runde hvor løkken kjører. Dette kjører helt til b blir 0, som da har funnet minste felles divisor. Løkken returnerer a som blir minste felles divisor. 
	return a

print(gcd(100, 8))

def reduce_fraction(a,b):
	d = gcd(a, b) #setter variabelen d til å være gcd mellom a og b fra gcd-funksjonen. 
	a2=int(a/d) #d som er et heltall fra gcd mellom a og b, vil gi et heltall når a deles med d. Dette settes til variabelen a2 som returneres.
	b2=int(b/d)
	return [a2,b2]
	
a=int(input('a: '))
b=int(input('b: '))
	
ab=reduce_fraction(a, b) #fordi jeg returnerte som en liste så vil ab[0] høre til a2
print('brøken a = ', a, '; b = ', b, 'skriver programmet ut "',ab[0], '/',ab[1], '"')