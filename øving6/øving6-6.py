from random import *

numbers=[i+1 for i in range(34)]

myGuess=[2,5,8,12,17,23,33]

def random():
	i=0
	løsning=[]
	numbers=[i+1 for i in range(34)]
	while i<7:
		random=randint(1,34-i)
		løsning.append(numbers[random-1])
		numbers.pop(random-1)
		i+=1
	return numbers, løsning

nyeTall, løsning=random()

def compList(liste1, liste2):
	result=[]
	for item in liste1:
		if item in liste2:
			result.append(item)
	return result

def premie():
	if result==7:
		premie=2749455
	elif result==6 and tillegstall==1:
		premie=102110
	elif result==6:
		premie=3385
	elif result==5:
		premie=95
	elif result==4 and tileggstall==1:
		premie=45
	else:
		premie=0
	return premie
	
def main():
	lottotall=[]
	i=0
	while i<10:
		random=randint(1,34-i)
		lottotall.append(numbers[random-1])
		numbers.pop(random-1)
		i+=1
	sju_første=lottotall[:7]
	tillegg=lottotall[7:10]
	result=compList(myGuess, sju_første)
	tilleggstall=compList(myGuess, tillegg)
	if len(result)==7:
		premie=2749455
	elif len(result)==6 and len(tillegstall)==1:
		premie=102110
	elif len(result)==6:
		premie=3385
	elif len(result)==5:
		premie=95
	elif len(result)==4 and len(tilleggstall)==1:
		premie=45
	else:
		premie=0
	return lottotall, result, tilleggstall, premie
	
print(main())

"""sum_1=0
kostnad=0
antall=0
while antall<1000000:
	main()
	kostnad+=5
	antall+=1
	print(premie)
print(sum_1)
print(kostnad)"""