total=0
for x in range(1,101):
	total += x
print('Summen av de', x, 'første tallene er', total)

number = 1
teller=1
count=0
while number < 1000:
	number *= teller
	teller+=1
	count+=1
	print(number)
print('Løkken kjørte', count, 'ganger, produktet ble', number)

tall= ''
while tall!=12:
	tall=int(input('Hva er 3*4? '))
	if tall==12:
		print('Stemmer, svaret var 12')
	else:
		print('Prøv igjen!')