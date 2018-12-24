from random import *

def randList(size, lower_bound, upper_bound):
	random=[]
	for i in range(size):
		tall=randint(lower_bound, upper_bound)
		random.append(tall)
	return random
		
print(randList(8, 2, 10))

def compareLists(list1, list2):
	sammenligning=[]
	for i in range(len(list1)):
		if list1[i] in list2 and list1[i] not in sammenligning:
			sammenligning.append(list1[i])
	return sammenligning

a=[2,4,6,5,3,9,6,4,6,4]
b=[5,1,6,4,9,6]
print(compareLists(a, b))
print('__________________________')

def multiCompList(lists):
	liste_0=list(set(lists[0]))
	for i in lists[0]:
		for j in range(1, len(lists)):
			if i not in lists[j] and i in liste_0:
				liste_0.remove(i)	
	return liste_0

c=[4,2,6,4,7,6]
d=[a, b, c]

print(multiCompList(d))

print('_______________________________')

def longestEven(liste):
	storst=0
	start=0
	antall=0
	for element in liste:
		if element % 2==0:
			antall+=1
			if antall > storst:
				storst=antall
				start= liste.index(element) - antall + 1
		else:
			antall=0
	return start, storst
			
print(longestEven(a))	
print(longestEven(c))	

def main():
	print(randList(10,2,7))
	a = [1,2,3]
	b = [4,3,1]
	print(compareLists(a,b))
	c = [7,2,1]
	d = [a,b,c]
	print(multiCompList(d))
	list = [4,3,3,6,2,6,8,3,4,3,3]
	print(longestEven(list))
 
main()
	
	