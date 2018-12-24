
import random

random_number= random.randint(1,100)

while True:
	gjett=int(input('Skriv et tall mellom 1 og 100: '))
	assert 0 <= gjett <=100
	if gjett > random_number:
		print('Det riktige tallet er lavere')
	elif random_number> gjett:
		print('Det riktige tallet er høyere')
	else:
		print("Du gjettet riktig")
		break
		